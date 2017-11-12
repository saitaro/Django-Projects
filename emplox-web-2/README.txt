
Django CMS Themes
=================

Django CMS Themes at django-cms-themes.com, Copyright (c) 2017 Nuwa Information
Co., Ltd, All Rights Reserved.

This file is also a valid Markdown format.

Getting Started
---------------

To use this theme, you can simply let setup.py to do it all for you.

Step 1: Activate your virtualenv (if needed).

Step 2: Next Run 
```
python setup.py my_cms_project_path
```
Where my_cms_project_path is the path to the folder the you wants to
create the project at, it can be an existing project. If the folder does
not exist then a new project will be created at that location.

Step 3: You will be prompted to enter a name for your django site, this
will create a subfolder containing your site under my_cms_project_path.

setup.py will copy all required files to your project and load required 
database records (cms pages, plugins..etc.).

Note: if you receive a 
```
ERROR - Please check your environment which
djangocms-installer is installed or upgrade to the latest.
```
you should try upgrading pip to the latest version.
```
python -m pip install --upgrade pip
```

For more details and options see: 
```
python setup.py -h
``` 

The default login for the admin website is 
```
username: admin
password: admin.
```
Simply append ?edit to the url and a toolbar will appear which will allow you
to edit the current page.

### Prerequisites

Django CMS 3.4+ is required. You can install this theme to existing projects, 
a new Django CMS 3.4+ project, or let setup.py create project for you.

Preferred method: Let setup.py do it all for you. Our setup.py will attempt to 
install all the required libraries and create a Django CMS project for you.

If you wish to create a new Django CMS project manually, you can follow the 
Django CMS tutorial at: 
http://docs.django-cms.org/en/release-3.4.x/introduction/index.html#tutorials

Or you can create an environment then install all required libraries:
```
cmsplugin-filer>=1.1
dj-database-url==0.4.1
Django==1.8.18
django-appconf==1.0.2
django-classy-tags==0.7.2
django-cms==3.4.2
django-filer==1.2.4
django-formtools==1.0
django-mptt==0.8.5
django-polymorphic==0.8.1
django-reversion==1.8.7
django-sekizai>=0.9
django-select2<5.0six
django-treebeard>=4.0,<5.0
djangocms-admin-style>=1.2,<1.3
djangocms-attributes-field==0.1.1
djangocms-video>=2.0
djangocms-column>=1.6
djangocms-flash==0.3.0
djangocms-googlemap>=0.5
djangocms-inherit==0.2.1
djangocms-installer==0.8.11
djangocms-link>=1.8
djangocms-style>=1.7
djangocms-text-ckeditor>=3.2.1
djangocms-snippet>=1.9
easy_thumbnails
html5lib>=0.999999,<0.99999999
Pillow>=3.0
pytz==2016.6.1
six==1.10.0
tzlocal==1.2.2
Unidecode==0.4.19
```

Instructions:

* Save the requirements below to requirements.txt.
* Create virtualenv and activate it.

* Run the following commands
```
pip install -r requirements.txt

django-admin startproject mysite
```

* Follow the instructions at http://docs.django-cms.org/en/stable/how_to/install.html

* Finally, install your desired theme.

```
cd theme_path

python setup.py mysite_path
```

Please change [mysite], [theme_path] and [mysite_path].

Programmer and User modes
---------------

There is a -m (mode) option; the default is programmer mode.
In programmer mode, all placeholders have a pre-built plugin which allows a user
to modify its content from pages. If user removes the plugin, the default
content still shows because {% placeholder 'id' or %}. Sometimes this is 
unexpected behavior. 

You can use user mode to change this:
```
python setup.py -m user my_cms_project_path
```
This will install templates which only use {% placeholder %}. All the default 
content will be placed inside plugins, users can remove plugins to remove the 
block of content. This is a very convenient mode to ship pages to users with.
The side effect is the HTML templates will be simplifed to only have the 
required blocks.

Notes:
---------------

The main purpose of theme is to save as much of your time and effort as 
possible. The final goal is to deliver a theme which can be provided to your 
user/client without any modifications. There is still work to do, so you might
need to modify HTML templates manually to suit what you want to do. This is no
different than modifying a normal django template, you can modify it as normal
Django template. You can change background images, JavaScript behaviors and
anything you want. We have just done all tedious work for you, no obscure
practices or changed to Django :).

There are a lot of useful plugins for Django CMS. We have just used default
plugins to minimize dependencies. It would be a good idea to integrate blog,
picture and history plugins, etc... It's up to you.

Known Issues:
---------------

* Under Django CMS edit mode, there might be some difference to normal mode. This is caused by Django CMS and is normal.
* Some templates attach events on HTML elements, this may make you unable to edit it directly on the frontend, you can edit the plugin content under structure mode.
* Menu detection is not supported yet, however, you can simply edit the menu list on the frontend and change link/anchor.
* If template designer uses images within your css style, it may not be editable at the frontend. This depends on templates. You can easily change images directly or change the css depending on your needs.
