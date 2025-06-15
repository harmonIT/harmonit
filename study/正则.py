import re
bd='&nbsp;/&nbsp;大闹天宫 上下集  /  The Monkey King'
director=re.split(r'(&nbsp;)+',bd)
print(director)