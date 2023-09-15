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