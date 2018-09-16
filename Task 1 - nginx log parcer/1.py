import os
import re

# line = '123.22.233.134'
# m = re.match(r'(?P<ip>(\d{1,3}\.){3}\d{1,3})', line)

# if m:
#     print(type(m.group('ip')))

parced = os.path.join(os.getcwd(), '\\result.txt')
filename = 'nginx.log'
print(os.path.join(os.path.dirname(os.path.abspath(__file__)), filename))