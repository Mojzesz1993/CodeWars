def dna_to_rna(dna):

    for i in range(0, len(dna)):
        dnal = list(dna)

        if dnal[i] == "T":
            dnal[i] = "U"
        dna = "".join(dnal)
        
    return (dna)

dna_to_rna("GCAT")