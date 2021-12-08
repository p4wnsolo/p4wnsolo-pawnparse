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

print('Reverse Lookup starting for:')
print(bcolors.WARNING + str(theinput) + '\n')

# Set lookup URL
url = 'https://clustrmaps.com/persons/'
url = url + str(theinput)

# Initialize tags to get Name
tag1 = '<h1 class="mb-3'
tag2 = '</h1>'

# Initialize tags to get All other data
tag3 = '<div class="mb-5"'
tag4 = '</div>'

print(bcolors.ENDC + 'Setting generic user agent..')
useragent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14A403 Safari/602.1'
headers = {'User-Agent': useragent}

print(bcolors.ENDC + 'Getting the web page..')
response = requests.get(url, headers=headers)
#response2 = urllib.request.urlopen(url)

# regex to extract required strings
reg_str = tag1 + '(.*?)' + tag2
reg_str2 = tag3 + '(.*?)' + tag4
res = re.findall(reg_str, str(response.content))
res2 = re.findall(reg_str2, str(response.content))

# Print the results
try:
    print(bcolors.HEADER + "\n\nName:\n" + bcolors.WARNING + str(res[0]) + '\n')
    #print(response2.read())

    num = 0

    # Print results line by line
    for i in res2:
        if (num % 2) == 0:
            print(bcolors.OKGREEN + i)
        else:
            print(bcolors.OKCYAN + i + '\n')
        num = num + 1

except:
    print('Unable to find info from the selected website.')
    print("\nHTTP Response:")
    #print(str(response.status_code) + ' - ' + str(response2))
    # Print results all in one block
    print("\nRaw Data:\n" + str(res2))
