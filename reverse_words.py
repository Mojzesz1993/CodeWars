"""
def reverse_words(text):
    textarr = text.split()
    texttmp = ''
    for i in range (0, len(textarr)):
        texttmp = textarr[i][::-1]
        textarr[i] = texttmp
        
    newtextarr = ' '.join(map(str, textarr))
    
    return newtextarr
    

reverse_words ("The quick brown fox jumps over the lazy dog.")

'elbuod decaps sdrow'
'elbuod  decaps  sdrow'
"""

def reverse_words(string):
    # Split the input string into words
    words = string.split()
    
    # Initialize an empty result string
    result = ""
    
    # Iterate through each word in the list
    for word in words:
        # Reverse the word and add it to the result string
        reversed_word = word[::-1]
        result += reversed_word
        
        # Add a space if it's not the last word
        if word != words[-1]:
            result += ' '
    
    return result

print(reverse_words("double  spaces"))