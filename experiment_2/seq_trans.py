class SequenceLoader():
    # TODO: auto dect seqs in dir
    pass

def seq_print(seq : dict, prefix = '') -> None:
    # print(prefix + ': ', end='')
    for k, v in seq.items():
        print(prefix + ': ' + k.replace('>', ''))
        print(seq[k])

def GC_print(gc_dict : dict) -> None:
    for k, v in gc_dict.items():
        print(k)
        seq_len = v['A'] + v['T'] + v['G'] + v['C']
        for base_name, base_cont in gc_dict[k].items():
            print(base_name + " : " + str(base_cont) + "\tcontent : " + str(base_cont/seq_len))
    print()

def mol_weight_print(mol_dict : dict) -> None:
    for k, v in mol_dict.items():
        print(k)
        print('approx: ' + str(mol_dict[k][0]) + '\n' + 'accurate: ' + str(mol_dict[k][1]))
    print()

def get_GC_content(seq : dict) -> dict:
    re_seq = {}
    #return type: {seq1 : {A:1, T:2, G:3, C:4}, seq2 : {},}
    
    base_common = ['A', 'T', 'G', 'C', 'a', 't', 'g', 'c']
    for k, v in seq.items():
        # print("sequence name : " + str(k).replace('>', ''))
        seq_len = len(v.replace('\n', ''))
        base = {'A':0, 'T':0, 'G':0, 'C':0}
        for i in v:
            if i in base_common:
                i = i.upper()
                base[i] += 1
        re_seq[k.replace('\n', '')] = base

        for base_name, base_cont in sorted(base.items())[:4]:
            # print(base_name + " : " + str(base_cont) + "\tcontent : " + str(base_cont/seq_len))
            pass
        # print()
    return re_seq

def get_mol_weight(seq : dict, type = 'DNA') -> list:
    re_dic = {}
    # return type: {seq1 : (acc, app), seq2 : (acc, app)]

    base = get_GC_content(seq)
    for k, v in base.items():
        accurate = v['A']*329.2 + v['T']*304.2 + v['G']*289.2 + v['C']*329.2 +79.0
        approx = (v['A'] + v['T'] + v['G'] + v['C']) * 303.7 + 79.0
        re_dic[k] = (accurate, approx)

    return re_dic

        
def split_to_num(cds : str, num : int):
    new = str()
    cnt = 0
    for i in cds:
        if cnt < num:
            new += i
            cnt += 1
        else:
            new += '\n'
            new += i
            cnt = 1
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

def get_complementary_seq(seq : dict) -> dict:
    re_seq = {}
    comp_dic = {'A':'T', 'T':"A", 'G':'C', 'C':'G', 'a':'t', 't':"a", 'g':'c', 'c':'g'}
    for k, v in seq.items():
        split_num = dect_num_in_line(v)
        co_v = str()
        for i in v.replace('\n', ''):
            co_v += comp_dic[i]
        re_seq[k] = split_to_num(co_v, split_num)
    return re_seq

def get_rev_and_comp_seq(seq : dict) -> dict:
    re_seq = {}
    for k, v in seq.items():
        re_seq[k] = get_reverse_seq({k : get_complementary_seq({k : v})[k]})[k]
    return re_seq
# print(seq)
def get_rna_seq(seq : dict) -> dict:
    re_seq = {}
    for k, v in seq.items():
        rna_v = str()
        for i in v:
            if i == 'T':
                rna_v += 'U'
            elif i == 't':
                rna_v += 'u'
            else:
                rna_v += i
        re_seq[k] = rna_v
    return re_seq

def generate_vert_for_dna(num : int) -> str:
    vert = str()
    for i in range(num):
        vert += '|'
    return vert

def get_dna_seq(seq : dict) -> dict:
    re_seq = {}
    for k, v in seq.items():
        lis = v.split('\n')
        ddna_v = str()
        for i in lis:
            ddna_v += (i + '\n' + generate_vert_for_dna(len(i)) + '\n' + get_complementary_seq({'tmpline' : i})['tmpline'] + '\n')
        re_seq[k] = ddna_v
    return re_seq

def seq_analysis(seq : dict) -> None:
    GC_print(get_GC_content(seq))
    mol_weight_print(get_mol_weight(seq))
    seq_print(get_reverse_seq(seq), prefix="reverse")
    seq_print(get_complementary_seq(seq), prefix="complementary")
    seq_print(get_rev_and_comp_seq(seq), prefix="reverse and complement")
    seq_print(get_rna_seq(seq), prefix="RNA")
    seq_print(get_dna_seq(seq), prefix="Double Strand DNA")
# print(get_GC_content(seq))
# print(get_mol_weight(seq))
def main():
    seq = {} # the main container for read sequences, global

    with open(r'seq.fasta') as f:
        for line in f:
            if line == "\n":
                continue
            if line.startswith('>'):
                name = line.replace('\n', '')
                seq[name] = ''
            else:
                seq[name] += line

    seq_analysis(seq)

if __name__ == '__main__':
    main()