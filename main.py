dna_sequence = "ATGCTAGCTAGCTAGCTAGGCTAA"
Guanine = dna_sequence.count('G')
print('The number of Guanine in the DNA sequence is', Guanine)
Cytosine = dna_sequence.count('C')
print('The number of Cytosine in the DNA sequence is', Cytosine)
total_length = len(dna_sequence)
print('The total length of the DNA sequence is', total_length)
gc_percentage = ((Guanine + Cytosine) / total_length) * 100
print("The GC percentage of the DNA sequence is", gc_percentage)
Part 2: 
rna_sequence = dna_sequence.replace('T', 'U')
print('The RNA sequence is', rna_sequence)
start_codon_position = dna_sequence.find('ATG')
print('The position of the start codon is', start_codon_position)
