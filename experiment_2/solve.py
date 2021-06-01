seq = {}
def SequenceLoader():
    pass

with open(r'seq.fasta') as f:
    for line in f:
        if line.startswith('>'):
            name = line.replace('\n', '')
            seq[name] = ''
        else:
            seq[name] += line

def get_GC_content(seq : dict):
    base_common = ['A', 'T', 'G', 'C', 'a', 't', 'g', 'c']

    for k, v in seq.items():
        print("sequence name : " + str(k).replace('>', ''))
        seq_len = len(v)
        base = {'A':0, 'T':0, 'G':0, 'C':0}
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

def dect_num_in_line(seq_str: str):
    cnt = 0
    for i in seq_str:
        if i is not '/n':
            cnt += 1
    return cnt


def get_reverse_seq(seq : dict, line_num = 0 ):
    for k, v in seq.items():
        print(k)  #todo
        print(split_to_num(v, dect_num_in_line(v))[::-1])

def get_complementary_seq(seq : dict):
    comp_dic = {'A':'T', 'T':"A", 'G':'C', 'C':'G', 'a':'t', 't':"a", 'g':'c', 'c':'g'}
    for k, v in seq.items():
        print(k) #todo
        split_num = dect_num_in_line(v)
        cnt = 0
        for i in v:
            if i is not '\n':
                print(comp_dic[i], end='')
            else:
                print(i, end='')
# print(seq)

get_GC_content(seq)
# get_reverse_seq(seq)
get_complementary_seq(seq)