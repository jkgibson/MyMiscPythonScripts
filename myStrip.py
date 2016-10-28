#! python3
# myStrip.py
# A function that will strip whitespace from the beginning and ending of
# a string when passed with no argument. Also, will strip the characters
# specified from the string.

import re

# TO DO: Search for whitespace at the beginning. Count how many whitespaces
#        there are. Remove that amount from beginning of string.  Maybe
#        check out the string sub function for help with this.
wm_beg = re.compile(r'^\s+')
beg_strip = wm_beg.sub('',string)

# TO DO: Search for whitespace at the end. Count how many whitepaces there are.
#        Remove that amount from the end of the string.
wm_end = re.compile(r'\s+$')
end_strip = wm_end.sub('',beg_strip)
# TO DO: Search for the specified characters in the string. Find a way to remove
#        those characters from the string.
spec_strip = re.compile(r'
# TO DO: Build the function wrapper.
