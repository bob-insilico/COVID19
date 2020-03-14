import os

geneAlias = {''}

#load reference sequence of each virus gene.  Return it in a hash keyed by gene.
#Put the sequence in a list becasue we will add more sequences when samples are loaded.
def load_ref():
    ref_file = open("data/refernece_sequence.fasta", "r")
    line = ref_file.readline()
    gene = ""
    seq_dict = {}
    while (line):
        if line.startswith(">"):
            if gene != "":
                seq_dict[gene] = ['Reference|' + sequence]
            gene = line.split()[1].upper()
            sequence = ""
        else:
            sequence += line.strip()
    
        line = ref_file.readline()
    seq_dict[gene] = [sequence]
    return(seq_dict)    

#Load the sequencing samples in the down loaded genbank records.  For now,
#just look for translated protein sequences that identify the gene.  Don't
#worry about the DNA sequences.
def load_samples(sequences):
    samp_file = open("data/genbank_sequences.gb", "r")
    line = samp_file.readline()
    id = ''
    gene = ''
    
    while (line):
        line = line.strip()
        if line.startswith("LOCUS"):
            toks = line.split()
            id = toks[1] + '(' + toks[len(toks)-1] + ')'
        if line.startswith("/country="):
            id += ' ' + line[10:-1]   
        if line.startswith("/gene="):
            gene=line[6:-1]
        if line.startswith("/translation="):     
            sequence = line[14:-1] 
             
    
            
            
        line = samp_file.readline()
        
        
        
    seq_dict[gene] = [sequence] 
    
    
sequences = load_ref()
load_samples(sequences)
print(sequences['ORF7B'])
# = open("data/genbank_sequences.gb", "r")
