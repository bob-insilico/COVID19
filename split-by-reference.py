from common import read_fasta, fasta_entry, sid_splitter
from argparse import ArgumentParser

def split_sids(sids):
    for sid in sids:
        m = sid_splitter.match(sid)
        if m:
            yield m.group(0,1,2,3)

parser = ArgumentParser()
parser.add_argument('input')
args = parser.parse_args()

with open(args.input) as f:
    seqs = read_fasta(f)

yp_genes = {acc: gene 
            for _, acc, gene, _ in split_sids(seqs) 
            if acc.startswith('YP_')
            }

for yp_acc, yp_gene in yp_genes.items():
    fn = yp_gene.replace('\'','')+'.fa'
    with open(f'gene-fastas/{fn}','w') as wf:
        data_entries = []
        for sid, acc, gene, _ in split_sids(seqs):
            if acc == yp_acc:
                wf.write(fasta_entry(yp_acc, seqs[sid]))
                continue
            if gene == yp_gene:
                data_entries.append(fasta_entry(acc, seqs[sid]))
        for entry in data_entries:
            wf.write(entry)
        print(yp_acc, len(data_entries))