# importing re module
import re
import urllib
import requests

# initializing string
#test_str = '<b>Gfg</b> is <b>Best</b>. I love <b>Reading CS</b> from it.'

phonenumber = 4806488420
url = 'https://callprotect.org/reverse-lookup/?number='
url = url + str(phonenumber)

# initializing tag
tag1 = '<tr><th colspan="2">'
tag2 = '</th>'

response = requests.get(url)
print("Response 1:\n")
print(response.content)
print(response.status_code)
response2 = urllib.request.urlopen(url)
print("Response 2:\n")
print(response2)

# printing original string
#print("The original string is : " + str(test_str))


# regex to extract required strings
reg_str = tag1 + '(.*?)' + tag2
res = re.findall(reg_str, str(response.content))

# printing result
print("The Strings extracted : " + str(res))

#print(response.status_code)
