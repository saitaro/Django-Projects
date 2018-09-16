from os.path import join, dirname, abspath
import re

# 'www.trendybelly.com.log'
# 'nginx.log'

log = 'www.trendybelly.com.log'

log_path = join(dirname(abspath(__file__)), log)
parsed_path = join(dirname(abspath(__file__)), log + ' 500 requests.txt')

with open(log_path, 'r') as log, open(parsed_path, 'w') as results:
    uniques = set()
    get_200_count = 0

    for line in log:
        if 'GET ' in line and ' 200 ' in line:
            get_200_count += 1
        if ' 500 ' in line:
            results.write(line)

        search = re.match(r'(?P<ip>(\d{1,3}\.){3}\d{1,3})', line)
        if search:
            uniques.add(search.group('ip'))

    print(get_200_count)
    string = str(uniques).replace("'", "").strip('{}')
    print(string)


