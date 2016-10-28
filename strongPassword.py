#! python3
# strongPassword.py

import re

#TO DO: Make a function that asks the user to input a password, then takes
#       that inputted password as a string and tests it against the matched
#       matched objects.  If there are matches, then let the user in. 


def strongPassword(password):
    compliant = 0
    #Create regex for password length (at least 8 characters)
    lengthRegex = re.compile(r'\w{8,}')
    len_o = lengthRegex.search(password)

    #Create regex for contains both upper and lower
    upperRegex = re.compile(r'[A-Z]+')
    upper_o = upperRegex.search(password)
    
    lowerRegex = re.compile(r'[a-z]+')
    lower_o = lowerRegex.search(password)

    #Create regex for the check for at least one digit
    digitRegex = re.compile(r'\d+')
    digit_o = digitRegex.search(password)

    #TO DO: Create test for all of these matches
    if len_o and upper_o and lower_o and digit_o:    
        compliant = 1
        return compliant 
    else:
        compliant = 0
        return compliant
        

print('Password?: ')
input_password = input()
while strongPassword(input_password) != 1:
    print('Not compliant. Please try again.\n')
    input_password = input()            
    
print('Compliant')
    
    




