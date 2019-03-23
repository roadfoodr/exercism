def proteins(strand):
    '''
    Returns a list of proteins found in a DNA strand, in order
    of their appearance in the strand.
    '''
    codons = {}
    proteins_list = []
    codon_text = '''
        Codon	Protein
        AUG	Methionine
        UUU, UUC	Phenylalanine
        UUA, UUG	Leucine
        UCU, UCC, UCA, UCG	Serine
        UAU, UAC	Tyrosine
        UGU, UGC	Cysteine
        UGG	Tryptophan
        UAA, UAG, UGA	STOP
        '''

    for line in codon_text.splitlines():
        words = line.replace(',','').split()
        if len(words) < 2 or words[0] == 'Codon':
            continue
        for word in words[0:-1]:
            codons[word] = words[-1]

    for i in range(0, len(strand), 3):
        protein = codons.get(strand[i:i+3])
        if protein == 'STOP':
            return proteins_list
        if protein:
            proteins_list.append(protein)

    return proteins_list