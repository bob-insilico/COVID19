import re

def read_fasta(f):
    seqs = {}
    seqid = None
    seq = None
    for l in f:
        l = l.rstrip('\r\n')
        if l.startswith('>'):
            if seqid:
                seqs[seqid] = seq
            seqid = l
            seq = ''
        else:
            seq += l
    seqs[seqid] = seq
    return seqs

def chunks(s, n):
    for i in range(0, len(s), n):
        yield s[i:i+n]

def fasta_entry(sid, seq):
    s = ''
    if not sid.startswith('>'):
        sid = '>'+sid
    s += sid+'\n'
    s += '\n'.join(chunks(seq, 60))+'\n'
    return s

sid_splitter = re.compile(r'>(.*) \|(.*) \[(.*)\]')