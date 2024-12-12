import string, sys

def is_pangram(s):
    alphabet=string.ascii_lowercase
    alphaset=set(alphabet)
    return alphaset <= set(s.lower())
          


  
    
 
print ( is_pangram('The quick brown fox jumps over the lazy dog')) 
print (is_pangram("The quick, brown fox jumps over the lazy dog!"))