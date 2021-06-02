from types import resolve_bases


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


def seq_print(seq : dict) -> None:
    for k, v in seq.items():
        print(k.replace('>', ''))
        print(seq[k])

def get_GC_content(seq : dict) -> None:
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


def dect_num_in_line(seq_str: str) -> int:
    return len(seq_str.split('\n')[0])

def get_reverse_seq(seq : dict) -> dict:
    re_seq = {}
    for k, v in seq.items():
        re_v = split_to_num(v.replace('\n', '')[::-1], dect_num_in_line(v))
        re_seq[k] = re_v
    return re_seq
        # print(k)  #todo
        # print(split_to_num(v, dect_num_in_line(v))[::-1])

def get_complementary_seq(seq : dict):
    re_seq = {}
    comp_dic = {'A':'T', 'T':"A", 'G':'C', 'C':'G', 'a':'t', 't':"a", 'g':'c', 'c':'g'}
    for k, v in seq.items():
        split_num = dect_num_in_line(v)
        co_v = str()
        for i in v.replace('\n', ''):
            co_v += comp_dic[i]
        re_seq[k] = split_to_num(co_v, split_num)
    return re_seq


def get_rev_and_comp_seq(seq : dict):
    re_seq = {}
    for k, v in seq.items():
        re_seq[k] = get_reverse_seq({k : get_complementary_seq({k : v})[k]})[k]
    return re_seq
# print(seq)

get_GC_content(seq)
# seq_print(get_reverse_seq(seq))
# seq_print(get_complementary_seq(seq))
seq_print(get_rev_and_comp_seq(seq))

