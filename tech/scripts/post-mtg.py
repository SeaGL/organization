import re

with open('/home/jhustler/play/pyplay/seagl/SeaGL_Tech.txt', 'r') as file:
    content = file.readlines()

for line in [line for line in content if re.match(r'.*\[ \].', line)]:
    print(line)