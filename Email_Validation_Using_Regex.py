# a-z
# 1-9
# . _ time 1
# @ time 1
# . 2 or 3 pos from last
import re
email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email= input(' Enter Your Email : ')

if re.search(email_condition,user_email):
  print("Right Email")
else:
  print("Wrong Email")
  
  
  # Your code uses the re (regular expression) module to validate an email address. It defines a regular expression pattern stored in the variable email_condition. Let's break down the regular expression and understand the validation criteria:

# ^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$
# ^[a-z]+: The string must start with one or more lowercase letters.
# [\._]?: There may be an optional dot (.) or underscore (_) after the initial lowercase letters.
# [a-z 0-9]+: This part allows one or more lowercase letters, digits, or spaces.
# [@]: There must be an "@" symbol.
# \w+: This allows one or more word characters (letters, digits, or underscores) for the domain name.
# [.]: There must be a dot (.) before the top-level domain.
# \w{2,3}$: The top-level domain should consist of 2 or 3 word characters, and the string must end with it.
# Your code then uses re.search() to check if the user-provided email (user_email) matches the specified pattern (email_condition). If it does, the code prints "Right Email"; otherwise, it prints "Wrong Email."

# This approach is a more concise and readable way to validate email addresses using regular expressions. Just make sure the regular expression meets your specific requirements for email validation.





