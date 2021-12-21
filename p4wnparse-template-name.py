import re  
import urllib
import requests
import sys

class color:
    PINK = '\033[95m'  # Pink
    BLUE = '\033[94m'  # Blue
    CYAN = '\033[96m'  # Cyan
    GREEN = '\033[92m' # Green
    YELLOW = '\033[93m' # Yellow
    RED = '\033[91m'    # Red
    GRAY = '\033[0m'     # Gray
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

try:  # Get command line arg(s)
    first = sys.argv[1]  # Get input from command line
    last = sys.argv[2]  # Get input from command line
    theinput = first + '-' + last + ''
except:  # Set default input if none given
    theinput = 'Carole-Baskin/'  

url = 'https://searchpeoplefree.com/find/'  # Set URL
url = url + str(theinput)  # Add input to URL
print('URL:\n' + url + '\n')

##### Get web page
print(color.RED + 'Getting web page..')
response = requests.get(url)
print(response.content)
##### Get all results
all_start = '<article'
all_end = '</article>'
all_res = re.findall(all_start + '(.*?)' + all_end, str(response.content))

print(all_res)

parsed = []  # Initialize list

##### Scrape the results
# Get NAME
name_tag_start = ''
name_tag_end = ''

# Get AGE
age_tag_start = ''
age_tag_end = ''

# Print the results
try:
    print(color.PINK + "\nName:  " + color.RED + theinput)
    num = 0
    # Print results line by line
    for i in all_res:
        ########## Get Name
        print('\n' + i)
        num = num + 1
except Exception as e: 
    print(e)
    print('Unable to find info from the selected website.')
    print("\nHTTP Response:")
print('\n' + str(len(all_res)))
