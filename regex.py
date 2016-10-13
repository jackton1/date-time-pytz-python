import re

names_file = open("names.txt", encoding='utf-8')
data = names_file.read()
names_file.close()

president =  r'Obama'
teacher = r'Love'
teacher2 = r'Kenneth'

# print(re.search(president, data))
# print(re.search(teacher2, data))
# print(re.findall(r'\(?\d{3}\)?-?\s?\d{3}-\d{4}', data))
# print(re.findall(r'\w*, \w+', data))
# print(re.findall(r'[-\w\d+.]+@[-\w\d.]+', data))
# print(re.findall(r'\b[trehous]{8,9}\b', data, re.I))
#print(re.findall(r'''
#    \b@[-\w\d.]+   # Find a word boundary an @ and any number of characters
#    [^gov\t]+  # Ignore 1+ Instances of the letter 'g', 'o', or 'v' and a tab.
#    \b  #Match another word boundary
#''', data, re.VERBOSE|re.I))
#print(re.findall(r'''
#    \b[-\w]*, # Find a word boundary, 1+ hyphens or characters, and a comma
#    \s #Find 1 whitespace
#    [-\w ]+ # 1+ hyphens and character and explicit spaces
#    [^\t\n] #ignore tabs or new line
#  ''', data, re.X))

line = re.compile(r'''
      ^(?P<name>(?P<last>[-\w ]*),\s(?P<first>[-\w ]+))?\t  #Last and First Name
      (?P<email>[-\w\d+.]+@+[-\w\d.]+)\t  #Email
      (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t # Phone
      (?P<job>[\w\s]+,\s[\w\s.]+)\t?  #Job and Company
      (?P<twitter>@[\w\d]+)?$  #Twitter Account
      ''', re.X|re.M)

#print(line.search(data).groupdict())
#print(re.search(line, data).groupdict())

for match in line.finditer(data):
  print('{first} {last} <{email}>'.format(**match.groupdict()))

