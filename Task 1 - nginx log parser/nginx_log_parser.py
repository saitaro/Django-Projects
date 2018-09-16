from os.path import join, dirname, abspath
import re

# 'www.trendybelly.com.log'
# 'nginx.log'

log = 'nginx.log'

log_path = join(dirname(abspath(__file__)), log)
parsed_path = join(dirname(abspath(__file__)), log + ' HTTP 500.txt')

uniques = set()
get_200_count = 0

with open(log_path, 'r') as log, open(parsed_path, 'w') as results:
    for line in log:
        if 'GET ' in line and ' 200 ' in line:
            get_200_count += 1
        if ' 500 ' in line:
            results.write(line)

        search = re.match(r'(?P<ip>(\d{1,3}\.){3}\d{1,3})', line)
        if search:
            uniques.add(search.group('ip'))

uniques_string = str(uniques).replace("'", "").strip('{}')

print(get_200_count)
print(uniques_string)


