#!/usr/bin/env python
# -*- coding: utf-8 -*-
# $Id: setup.py 10347 2017-10-03 09:43:25Z Lavender $
#
# Copyright (c) 2017 Nuwa Information Co., Ltd, All Rights Reserved.
#
# Licensed under the Proprietary License, 
# you may not use this file except in compliance with the License. 
# You may obtain a copy of the License at our web site.
#
# See the License for the specific language governing permissions and 
# limitations under the License.
#
# $Author: Lavender $
# $Date: 2017-10-03 17:43:25 +0800 (週二, 03 十月 2017) $
# $Revision: 10347 $ 

import os
import sys
import logging
import shutil
import argparse

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(
    logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
logger.addHandler(handler)

SETUP_DIR = os.path.dirname(os.path.abspath(__file__))

def copyToPath(baseDir, templateDir, staticDir, mode):
    if not templateDir:
        templateDir = os.path.join(baseDir, 'templates')
    if not staticDir:
        staticDir = os.path.join(baseDir,'static')
        
    logger.info("-----Start copy templates-----")
    if not os.path.exists(staticDir):
        os.mkdir(staticDir)
    if not os.path.exists(templateDir):
        os.mkdir(templateDir)
    for root, dirs, files in os.walk(os.path.join(SETUP_DIR, "static")):
        for d in dirs:
            index = os.path.join(root, d).index("static") + len("static/")
            path = os.path.join(
                staticDir, os.path.join(os.path.join(root, d))[index:])
            if not os.path.exists(path):
                os.mkdir(path)
                
    if not os.path.exists(os.path.join(baseDir, "fixtures")):
        os.mkdir(os.path.join(baseDir, "fixtures"))
    
    for root, dirs, files in os.walk(SETUP_DIR):
        for f in files:
            if f == 'setup.py':
                continue
            origin = os.path.join(root, f)
            
            if os.path.join(SETUP_DIR, "static") in root:
                index = len(os.path.join(SETUP_DIR, "static")) + 1
                dst = os.path.join(staticDir, origin[index:])
            elif os.path.join(SETUP_DIR, "templates") in root:
                result = os.path.splitext(origin)[0]
                if mode == 'programmer':
                    if result.endswith("_user"):
                        continue
                    dst = os.path.join(templateDir, f)
                else:
                    if not result.endswith("_user"):
                        continue
                    dst = os.path.join(
                        templateDir, f.replace('_user.html', '.html'))
            elif os.path.join(SETUP_DIR, "fixtures") in root:
                index = len(os.path.join(SETUP_DIR, "fixtures")) + 1
                dst = os.path.join(baseDir, "fixtures", origin[index:])
            else:
                continue
            
            if os.path.isfile(dst):
                logger.error("%s exists. failed to copy file." % dst)
            else:
                shutil.copyfile(origin, dst)
                logger.info("Succeed to copy file to %s." % dst)
    

def findSettings(path):
    for root, dirs, files in os.walk(path):
        for f in files:
            if f == 'settings.py':
                return os.path.join(root, f)
    return None
                
def writeSettings(settingsPath, templateDir, staticDir, hasCmsTemplate):
    logger.info("-----Start write and backup settings.py-----")
    def getCMSTemplates():
        templates = []
        
        path = os.path.join(SETUP_DIR, 'templates')
        index = None
                
        for template in os.listdir(path):
            if "_user" in template:
                continue
            if template.lower() == 'index.html':
                index = template
                continue
            templates.append((template, template))
        
        if index:
            return [(index, index),] + templates
        else:
            return templates
    
    settingsDir = os.path.dirname(settingsPath)
    bak = os.path.join(settingsDir, 'settings.py.bak')
    if os.path.isfile(bak):
        logger.error("%s exists. failed to backup file." % bak)
        return 
    shutil.copyfile(settingsPath, bak)
    logger.info("Succeed to backup settings.py to %s." % bak)
                
    with open(settingsPath, 'r') as settings:
        content = settings.read()
                
    with open(settingsPath, 'w') as settings:    
        if hasCmsTemplate:
            content += \
'''
CMS_TEMPLATES = list(CMS_TEMPLATES)
CMS_TEMPLATES += %s
''' % str(getCMSTemplates())
        else:
            content += \
'''
CMS_TEMPLATES = %s
''' % str(getCMSTemplates())

        if not templateDir:
            content = content.replace(
                "'DIRS': []", "'DIRS': [os.path.join(BASE_DIR, 'templates'),]")
            
        if not staticDir:
            content += \
'''
if DEBUG:
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
'''
        
        settings.write(content)
    logger.info("Succeed to write settings.py")
                
def loadData(baseDir, language):
    logger.info("-----Start load data-----")
    data = os.path.join(".", 'fixtures', 'initial_data.json')
    result = os.system("%s manage.py loaddata \"%s\"" % (sys.executable, data))
    
    if not result == 0:
        return False
    
    from cms.models.pagemodel import Page
    from cms.models.titlemodels import Title
    from cms.api import copy_plugins_to_language
    from django.db import transaction
    
    @transaction.atomic
    def modifyData():
        for page in Page.objects.all():
            copy_plugins_to_language(page, "zh-hant", language)
        for title in Title.objects.all():
            title.language = language
            title.save()
    modifyData()
        
    return True
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Path to Project')
    parser.add_argument(
        'path', metavar='path', type=str, help='path', nargs='+')
    parser.add_argument(
        '-m', '--mode', 
        default='programmer',
        choices=['programmer', 'user',],
        help='programmer mode or user mode.')
        
    parser.add_argument(
        '-w', '--wizard', 
        action='store_true',
        help="Run the configuration wizard")   

    
    args = parser.parse_args()
    
    wizard = args.wizard

    if args.mode == 'programmer':
        mode = 'programmer'
    else:
        mode = 'user'
        
    path = " ".join(args.path) 
    
    settingsPath = findSettings(path)
    
    if not settingsPath:
        try:
            import djangocms_installer
        except Exception as e:
            os.system("pip install djangocms-installer")
        
        if sys.version_info.major == 3:
            projectName = input(
                "Django project not found. "
                "Auto create one by djangocms-installer. Input a project name:")
        else:
            projectName = raw_input(
                "Django project not found. "
                "Auto create one by djangocms-installer. Input a project name:")
        path = os.path.join(path, projectName)
        
        if wizard:
            result = os.system(
                "djangocms -f -p \"%s\" \"%s\" -w" % (path, projectName))
        else:
            result = os.system(
                "djangocms -f -p \"%s\" \"%s\"" % (path, projectName))
            
        if not result == 0:
            print
            logger.error(
                "Please check your environment "
                "which djangocms-installer is installed or "
                "upgrade to the latest.")
            sys.exit()
            
        settingsPath = findSettings(path)
    else:
        path = os.path.dirname(os.path.dirname(settingsPath))
    
    settingModule = os.path.splitext(settingsPath[len(path) + 1:])[0]
    settingModule = settingModule.replace("/", ".")
    settingModule = settingModule.replace("\\", ".")
    
    sys.path.append(path)
    os.environ['DJANGO_SETTINGS_MODULE'] = settingModule
    
    import django
    
    try:
        import cms
    except Exception as e:
        os.system("pip install django-cms")
        import cms
        
    cmsVersion = cms.__version__.split('.')
    
    cms34 = True
    try:
        if int(cmsVersion[0]) <= 3 and int(cmsVersion[1]) <= 4:
            cms34 = True
        else:
            cms34 = False
    except Exception as e:
        cms34 = False
        
    if cms34:
        if not (django.VERSION[0] == 1 and django.VERSION[1] <= 10):
            logger.error(
                "Your installed Django above 1.10 which is not supported by "
                "Django CMS 3.4 yet, please reinstall Django or you may "
                "encounter some issues while using Django CMS.")
            sys.exit()
    django.setup()
    
    from django.conf import settings
    
    baseDir = settings.BASE_DIR
    
    apps = [
        'cms',
        'menus',
        'sekizai',
        'treebeard',
        'djangocms_text_ckeditor',
        'filer',
        'easy_thumbnails',
        'cmsplugin_filer_file',
        'cmsplugin_filer_folder',
        'cmsplugin_filer_image',
    ]
    
    endSetup = False
    for app in apps:
        if not app in settings.INSTALLED_APPS:
            logger.error("The app doesn't be included in INSTALLED_APPS: %s" % 
                         app)
            endSetup = True
    
    if endSetup:
        print
        logger.error("The project does not support django cms. "
                     "Please follow the instructions at "
                     "http://docs.django-cms.org/en/stable/how_to/install.html")
        sys.exit()
            
    try:
        templateDir = settings.TEMPLATES[0]['DIRS'][0]
    except Exception as e:
        templateDir = None
    
    try:
        staticDir = settings.STATICFILES_DIRS[0]
    except Exception as e:
        staticDir = None
    
    copyToPath(baseDir, templateDir, staticDir, mode)
    
    if hasattr(settings, "CMS_TEMPLATES"):
        hasCmsTemplate = True
    else:
        hasCmsTemplate = False
        
    writeSettings(settingsPath, 
        templateDir, staticDir, hasCmsTemplate)
        
    os.chdir(baseDir)
        
    success = loadData(baseDir, settings.LANGUAGE_CODE)
    if not success:
        print
        logger.error("Please check the project's db was migrated.")
    else:
        print 
        logger.info("Get into \"%s\" directory and type"
                    " \"python manage.py runserver\" to start your project" % 
                    path)
    
    