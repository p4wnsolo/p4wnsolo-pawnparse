# p4wnparse

P4wnparse is an OSINT tool to parse info from Public information directories.

Currently, p4wnparse is multiple Python scripts which each perform a specific lookup task.

Here are the scripts currently in p4wnparse (as of Dec 8, 2021):

1) p4wnparse-phone-callprotect.py --- Give it a Phone Number, it'll give you their Name
2) p4wnparse-name-clustrmaps.py --- Give it a Name, it'll give you their Info (Age, etc)

*How it Works:
- Give the corresponding script a Name / Phone number
- The script gets and scrapes a website
- The info is displayed

Usage:

p4wnparse-phone-callprotect.py --- Give it a Phone Number, it'll give you their Name
<code>python3 p4wnparse-phone-callprotect.py 10digitNumberGoesHere</code>

ex:  
To look up a phone number 666-420-6969, use this command:

<code>python3 p4wnparse-name-clustrmaps.py 6664206969</code>

Default phone number lookup points to "John Doe" (if no name is provided via Command Line, this name will be used)


p4wnparse-name-clustrmaps.py --- Give it a Name, it'll give you their Info (Age, etc)
<code>python3 p4wnparse-name-clustrmaps.py Firstname Lastname</code>

ex:  
To look up a person named "John Doe", use this command:

<code>python3 p4wnparse-name-clustrmaps.py John Doe</code>

Default name lookup is "Carole Baskin" (if no name is provided via Command Line, this name will be used) 
