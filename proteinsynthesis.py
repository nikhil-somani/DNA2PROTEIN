#define the function with dna as inout parameter
def protein_synthesis(dna):
    #define the gentic code dictionary for protein from rna
    protein_dict = { 'UUU':'Phe', 'UUC':'Phe','UUA':'Lue', 'UUG': 'Lue', 
    'CUU': 'Leu','CUC':'Leu', 'CUA': 'Leu','CUG':'Lue',
    'AUU': 'Ile', 'AUC':'Ile', 'AUA': 'Ile', 'AUG':'Met',
    'GUU': 'Val','GUC': 'Val', 'GUA': 'Val', 'GUG':'Val', 
    'UCU':'Ser', 'UCC': 'Ser', 'UCA':'Ser',  'UCG':'Ser', 
    'CCU':'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG':'Pro', 
    'ACU': 'Thr','ACC': 'Thr', 'ACA':'Thr','ACG': 'Thr',            
    'GCU': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala','GCG': 'Ala',
    'UAU': 'Tyr','UAC':'Tyr', 'UAA': 'Stop','UAG': 'Stop',
    'CAU': 'His','CAC': 'His', 'CAA': 'Gln','CAG': 'Asn',
    'AAU':'Asn', 'AAC': 'Asn', 'AAA': 'Lys','AAG': 'Lys',        
    'GAU':'Asp', 'GAC': 'Asp', 'GAA':'Glu','GAG':'Glu', 
    'UGU': 'Cys', 'UGC':'Cys', 'UGA':'Stop', 'UGG': 'Trp',
    'CGU':'Arg','CGC':'Arg', 'CGA':'Arg','CGG': 'Arg',
    'AGU':'Ser','AGC':'Ser', 'AGA':'Arg', 'AGG':'Arg', 
    'GGU': 'Gly','GGC':'Gly', 'GGA': 'Gly', 'GGG':'Gly'}

    #make dna as list instead of string to make easier traverse
    dna = list(dna)
    #create a list of protein to be returned at end
    protein = []
    #coden is a transcribed sequence of dna to rna
    coden = ''
    #start is the start sequence to generate protein
    start = 'AUG'
    #stop is the list of stop sequence to stop the protein making
    stop = ['UAA', 'UAG', 'UGA']
    #transcrib is the dictionary to convert dna to rna symbol
    transcrib = {'A':'U', 'T':'A', 'G':'C', 'C':'G'}

    #a loop to convert dna symbol to rna using transcrib dictionary
    for i in range(len(dna)):
        dna[i] = transcrib[dna[i]]
        
    #convert dna list to string again using list comprehension
    dna = ''.join([str(x) for x in dna])

    #a parameter to note the position of index in sequence
    p = 0
    #while loop to start and stop condition
    while coden != start and p != len(dna) - 3:
        p += 1
        coden = dna[p:p + 3]
        #stop is any stop sequence found
        if(coden == [x for x in stop]):
            break
        #Add 'Met' peptide when additional start sequence are found 
        elif(coden == [x for x in start]):
            protein.append('Met')
        #normally append the peptide three alphabet to protein list
        else:
            protein.append(protein_dict[coden])
    #return the protein list
    return protein

#take dna as an example
dna = "TACCCATACCCC"
#run the function with this dna, this returns the list of protein
protein_synthesis(dna)

