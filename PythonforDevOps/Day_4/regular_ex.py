"""

Regular expression for extracting email ids

"""

import re

text = """
This alert service notifies divyeshrana16@gmail.com
and div@gmail.com and ankita@gmail.com
"""

list_of_emails = re.findall("[a-z0-9\.\-+_]+@+[a-z0-9\.\-+_]+.[a-z]+",text)

print(list_of_emails)