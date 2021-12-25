# p4wnparse

P4wnparse is an OSINT tool to parse info from Public information directories.

![Usage screenshot](/images/p4wnparse-usage.PNG "Usage screenshot")

![Example screenshot](/images/p4wnparse-example.PNG "Example screenshot")

Currently, p4wnparse uses several scripts to perform specific lookup tasks.

Here are the scripts currently in p4wnparse (as of Dec 8, 2021):

1. ☎️ p4wnparse-phone-callprotect.py --- Give it a Phone Number, it'll give you their Name

2. 🧑 p4wnparse-name-clustrmaps.py --- Give it a Name, it'll give you their Info (Age, etc)

3. 🧑 p4wnparse-name-radaris.py --- Give it a Name, it'll give you their Info (Age, etc)

## How it Works:

- Give the corresponding script a Name / Phone number

- The script fetches and scrapes a website

- The results are displayed

## Install:

First, clone the p4wnparse Github repository:

`git clone https://github.com/p4wnsolo/p4wnsolo-pawnparse.git`

Then change directories into /p4wnsolo-pawnparse:

`cd p4wnsolo-pawnparse`

Finally, run one of the example commands below:

## Usage:

### ☎️ p4wnparse-phone-callprotect.py --- Phone to Name Lookup (Reverse Lookup)

`python3 p4wnparse-phone-callprotect.py 10digitNumberGoesHere`

*For example:*

To look up a phone number 666-420-6969, use this command:

`python3 p4wnparse-phone-callprotect.py 6664206969`

Default phone number lookup points to "John Doe" (if no name is provided via Command Line, this name will be used)

### 🧑 p4wnparse-name-clustrmaps.py --- Name Lookup

`python3 p4wnparse-name-clustrmaps.py Firstname Lastname`

*Example:*

`python3 p4wnparse-name-clustrmaps.py John Doe`

### 🧑 p4wnparse-name-radaris.py --- Name Lookup

`python3 p4wnparse-name-radaris.py Firstname Lastname`

*Example:*

To look up a person named "John Doe", use this command:

`python3 p4wnparse-name-radaris.py John Doe`

Default name lookup is "Carole Baskin" (if no name is provided via Command Line, this name will be used) 
