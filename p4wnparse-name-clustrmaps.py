# importing re module
import re
import urllib
import requests
import sys

class bcolors:
    HEADER = '\033[95m'  # Pink
    OKBLUE = '\033[94m'  # Blue
    OKCYAN = '\033[96m'  # Cyan
    OKGREEN = '\033[92m' # Green
    WARNING = '\033[93m' # Yellow
    FAIL = '\033[91m'    # Red
    ENDC = '\033[0m'     # Gray
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Set phone number
try:
    first = sys.argv[1]  # Get input from command line
    last = sys.argv[2]  # Get input from command line
    theinput = first + '-' + last
except:
    theinput = 'Carole-Baskin'  # Set a random phone number if none is given

print('Reverse Lookup starting..')

# Set lookup URL
url = 'https://clustrmaps.com/persons/'
url = url + str(theinput)

# Initialize tags to get Name
tag1 = '<h1 class="mb-3'
tag1 = '<div class="hh1">Found <strong>'
tag2 = '</h1>'
tag2 = '</strong>&nbsp;results'

# Initialize tags to get All other data
tag3 = '<div class="mb-5"'
#tag4 = '</div>'
tag4 = '<div class="text-center mt-3 d-md-none">'

# Initialize tags to get Name
tag5 = '<span itemprop="telephone"'
tag6 = '</span'

# Initialize tags to get Name
tag7 = 'Associated persons'
tag8 = '</span></a></div>'

# Initialize tags to get Name
tag9 = '<span itemprop=\'name\'>'
tag10 = '</span><span itemprop=\'sameAs\''

print(bcolors.ENDC + 'Setting generic user agent..')
useragent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14A403 Safari/602.1'
headers = {'User-Agent': useragent}

print(bcolors.ENDC + 'Getting the web page..')
response = requests.get(url, headers=headers)
#response2 = urllib.request.urlopen(url)

# regex to extract required strings
reg_str = tag1 + '(.*?)' + tag2
res = re.findall(reg_str, str(response.content))

reg_str2 = tag3 + '(.*?)' + tag4
res2 = re.findall(reg_str2, str(response.content))

reg_str3 = tag5 + '(.*?)' + tag6
res3 = re.findall(reg_str3, str(response.content))

reg_str4 = tag7 + '(.*?)' + tag8
res4 = re.findall(reg_str4, str(response.content))

reg_str5 = tag9 + '(.*?)' + tag10
res5 = re.findall(reg_str5, str(response.content))


# Print the results
try:
    print(bcolors.HEADER + "\n\nName:" + bcolors.WARNING + theinput)
    print(bcolors.HEADER + "# Results:  " + bcolors.WARNING + str(res[0]))
    #print(response2.read())

    num = 0

    # Print results line by line
    for i in res2:
        ### Assign row colors
        if (num % 2) == 0:
            color = bcolors.OKGREEN
        else:
            color = bcolors.OKCYAN
        isplit = i.split('>')  # Split the string
        ########## Name
        name = isplit[5]  # Get the rough name string
        name = name.split('<')  # Split the name string
        name = name[0]  # Get just the name
        print(color + '\n#' + str(num) + ':  ' + name)  # Print the item number
        #print('Name:  ' + name + '')
        ########## Age
        try:
            age = isplit[8]  # Get the rough age string
            age = age.split('<')  # Split the age string
            age = age[0]  # Get the age string
            age = age.split(' ')  # Split the age string
            age = age[2]  # Get just the age
            print('Age:  ' + age + '')
        except:
            print('Age:  Unknown')
        ########## Phone
        phonenumber = res3[num]
        phonenumber = phonenumber.split('>')
        phonenumber = phonenumber[1]
        try:
            print('Phone Number: ' + phonenumber)
        except:
            print('Phone Number:  Unavailable')
        ########## Associates
        associates = res4[num]
        associates = associates.split('>')
        try:
            print('Associate #1: ' + associates[3])
        except:
            nothing = 0
        try:
            print('Associate #2: ' + associates[11])
        except:
            nothing = 0
        try:
            print('Associate #3: ' + associates[19])
        except:
            nothing = 0
        try:
            print('Associate #4: ' + associates[27])
        except:
            nothing = 0
        try:
            print('Associate #5: ' + associates[35])
        except:
            nothing = 0
        try:
            print('Associate #6: ' + associates[43])
        except:
            nothing = 0
       ########## Address
        try:
            address = isplit[20]
            print('Address:  ' + address + '')
        except:
            print('Address:  Unknown')
        ########## City
        try:  #replace with a different result set
            city = isplit[16]
            city = city.split('<')  # Split the city string
            city = city[0]  # Get the city string
            print('City:  ' + city + '')
        except:
            print('City:  Unknown')
        #print(res5)
        #associates = associates.split('<')
        #associates = associates.split('>')
        #print(associates)
        ##### Iteration
        num = num + 1

except:
    print('Unable to find info from the selected website.')
    print("\nHTTP Response:")
    #print(str(response.status_code) + ' - ' + str(response2))
    # Print results all in one block
    print("\nRaw Data for Results 2:\n" + str(res2))
    print("\nRaw Data for Results 3:\n" + str(res3))
    print("\nRaw Data for Results 4:\n" + str(res4))
    print("\nRaw Data for Results 5:\n" + str(res5))
