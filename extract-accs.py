from common import read_fasta, fasta_entry
from argparse import ArgumentParser
import sys
import re

parser = ArgumentParser(description='Extract fasta entries by accession')
parser.add_argument('fasta')
parser.add_argument('accs',nargs='*')
args = parser.parse_args()

accs = set(args.accs)
if not accs:
    for l in sys.stdin.readlines():
        accs.add(l.rstrip('\r\n'))
if not accs:
    exit('no accessions provided')

with open(args.fasta) as f:
    fasta = read_fasta(f)

for sid in fasta:
    m = re.match(r'>(.*) \|(.*) \[(.*)\]', sid)
    if not m:
        continue
    acc = m.group(1)
    if acc in accs:
        print(fasta_entry(sid, fasta[sid]), end='')