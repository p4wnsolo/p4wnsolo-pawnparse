# importing re module
import re
import urllib
import requests

# initializing string
#test_str = '<b>Gfg</b> is <b>Best</b>. I love <b>Reading CS</b> from it.'

phonenumber = 'Carole-Baskin'
url = 'https://clustrmaps.com/persons/'
url = url + str(phonenumber)

# initializing tags to get Name
tag1 = '<span itemprop="name"'
tag2 = '</h3>'

# initializing tags to get All other data
tag3 = '<div class="mb-5"'
tag4 = '</div>'


response = requests.get(url)
print("Response 1:\n")
print(response.content)
print(response.status_code)
#response2 = urllib.request.urlopen(url)
#print("Response 2:\n")
#print(response2)

# printing original string
#print("The original string is : " + str(test_str))


# regex to extract required strings
reg_str = tag1 + '(.*?)' + tag2
reg_str2 = tag3 + '(.*?)' + tag4
res = re.findall(reg_str, str(response.content))
res2 = re.findall(reg_str2, str(response.content))

# printing result
print("The first Strings extracted : " + str(res))
print("The first Strings extracted : " + str(res2))

#print(response.status_code)
