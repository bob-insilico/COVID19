# COVID19
COVID19 


# Getting Data

Download most recent data from [NCBI](https://www.ncbi.nlm.nih.gov/labs/virus/vssi/#/virus?SeqType_s=Protein&VirusLineage_ss=SARS-CoV-2,%20taxid:2697049) into the file data/sequences.fa

# Extracting gene fastas

Create a directory called `gene-fastas`. Run 

```python
python3 split-by-reference.py data/sequences.fa
```
to create a fasta for each reference gene identified in `sequences.fa`. Reference genes are found by the `YP_` prefix to the accession.

# Building identity matrix

The linux binary `clustalo` is in the repo, but it can be downloaded fresh using

```sh
wget http://www.clustal.org/omega/clustalo-1.2.4-Ubuntu-x86_64 -O clustalo
```

Create a directory called idmats, and create identity matrices with `./make-idmats.sh`