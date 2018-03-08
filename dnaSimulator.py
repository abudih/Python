"""
This is code that reads simulated dna from 3 people simulated in 3 different text files.
The code reads in the text files, parses it to different dna codons(string of length 3).
Then tries to match it to the codons in the sample list and shows which profile matches
the most of the sample.

"""
sample = ['GTA','GGG','CAC']
#reads dna file from text file
def read_dna(dna_file):
  dna_data="";
  with open(dna_file,"r") as f:
    for line in f:
      dna_data+=line;
  return dna_data;
#separates the string into codons and add it to the list
def dna_codons(dna):
  codons=[];
  
  for i in range(0,len(dna),3):
    codons.append(dna[i:i+3]);
  
  return codons;
#match the codons with the sample dna
def match_dna(dna):
  matches=0;
  
  for codon in dna:
    if codon in sample:
      matches+=1;
    
  return matches;
#shows if the profile is matched
def is_criminal(dna_sample):
  dna_data=read_dna(dna_sample);
  codons=dna_codons(dna_data);
  
  num_matches=match_dna(codons);
  if(num_matches>=3):
    print("Investigation should continue, number of matches is %d"%num_matches);
  else:
    print("Investigation should be postponed, number of matches is %d"%num_matches);
    
is_criminal("suspect1.txt"); 
is_criminal("suspect2.txt"); 
is_criminal("suspect3.txt"); 
