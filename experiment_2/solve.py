# from types import prepare_class


seq = {}

def SequenceLoader():
    pass
with open(r'seq.fasta') as f:
    for line in f:
        if line.startswith('>'):
            name = line.replace('\n', '')
            seq[name] = ''
        else:
            seq[name] += line.replace('\n', '')

def get_GC_content(seq : dict):
    base_common = ['A', 'T', 'G', 'C', 'a', 't', 'g', 'c']

    for k, v in seq.items():
        print("sequence name : " + str(k).replace('>', ''))
        seq_len = len(v)
        base = {'A':0, 'T':0, 'G':0, 'C':0, 'a':0, 't':0, 'g':0, 'c':0}
        for i in v:
            if i in base_common:
                i = i.upper()
                base[i] += 1
        for base_name, base_cont in sorted(base.items())[:4]:
            print(base_name + " : " + str(base_cont) + "\tcontent : " + str(base_cont/seq_len))
        # mol_wg = base[A] * + base[T] * + base[C] * + base[G] * 
        # print()
        
def split_to_num(cds : str, num : int):
    new = str()
    cnt = 0
    for i in cds:
        if cnt < num:
            new += i
            cnt +=1
        else:
            new += '\n'
            cnt = 0
    new += '\n'
    return new

def get_reverse_seq(seq : dict, line_num : int):
    for k, v in seq.items():
        print(k)
        print(split_to_num(v, line_num)[::-1])



# print(seq)

get_GC_content(seq)
get_reverse_seq(seq, 60)