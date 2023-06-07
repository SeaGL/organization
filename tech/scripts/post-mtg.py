import urllib.request
import re

# grab the file from github
url = 'https://raw.githubusercontent.com/SeaGL/organization/shared-script-for-tech-meeting-todos/meetings/2023/20230512-15-all-staff.md'
response = urllib.request.urlopen(url)
data = response.read()  
# with open(data, 'r') as file:
content = data.decode('utf-8')
for line in [line for line in content.split('\n') if re.match(r'.*\[ \].', line)]:
    print(line)
