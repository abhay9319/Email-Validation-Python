# Email-Validation-Python
The code starts by getting user input for an email address.
It checks if the length of the email is at least 6 characters.
It checks if the first character of the email is alphabetic.
It checks if the email contains exactly one "@" symbol.
It checks if the email's last four characters are ".com" or ".org" but not both.
If any of these conditions are not met, the code prints an error message indicating where the validation failed. The error messages are numbered based on the step where the validation failed:

"Wrong Email 1": If the length of the email is less than 6 characters.
"Wrong Email 2": If the first character is not alphabetic.
"Wrong Email 3": If there is no "@" symbol or if there is more than one "@" symbol.
"Wrong Email 4": If the email's last four characters do not meet the specified condition.
"Wrong email 5": If there are spaces in the email, if there are uppercase letters in the local part of the email, or if there are other invalid characters.
If none of these conditions are met, the code prints "Right Email," indicating that the email passed all the validation checks.
