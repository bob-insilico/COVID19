from common import read_fasta
from argparse import ArgumentParser
import re

parser = ArgumentParser(description='Find accessions which match gene name regex')
parser.add_argument('fasta')
parser.add_argument('regex')
parser.add_argument('--full',action='store_true')
parser.add_argument('--partial',action='store_true',help='Include |partial sequences')
args = parser.parse_args()

with open(args.fasta) as f:
    fasta = read_fasta(f)
for sid in fasta:
    m = re.match(r'>(.*) \|(.*) \[(.*)\]', sid)
    if not m:
        continue
    gene = m.group(2)
    gene_match = re.match(args.regex, gene, flags=re.IGNORECASE)
    if gene_match:
        if '| partial' in gene and not(args.partial):
            continue
        if args.full:
            print(sid)
        else:
            print(m.group(1))
            

