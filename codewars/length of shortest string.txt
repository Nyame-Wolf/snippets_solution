1.)Simple, given a string of words, return the length of the shortest word(s).
String will never be empty and you do not need to account for different data types.
soln
def find_short(s):
    l = min(len(word) for word in s.split())# your code here
    return l # l: shortest word length
def find_short(s):
    s = s.split() # splits the string into a list of individual words
    l = min(s, key = len) # finds the shortest string in the list
    return len(l) # returns shortest word length