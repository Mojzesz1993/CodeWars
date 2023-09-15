def DNA_strand(dna):
    dnan = ''
    for i in range (0, len(dna)):
        if dna[i] == 'T':
            dnan += 'A'
        elif dna[i] == 'A':
            dnan += 'T'
        elif dna[i] == 'G':
            dnan += 'C'
        elif dna[i] == 'C':
            dnan += 'G'

    return dnan

DNA_strand("ATTGC")