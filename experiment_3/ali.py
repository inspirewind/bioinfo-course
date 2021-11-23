import numpy as np

# na_identity = np.eye(4)
# pr_identity = np.eye(20)
# print(pr_identity)

match_score = 4
mismatch_score = -3
gap_score = -3
gap_open_score = -3
gap_extend_score = -1

s1 = "AAATGC"
s2 = "AATGC"


def compare(base1: str, base2: str) -> int:
    if base1 == base2:
        return match_score
    else:
        return mismatch_score


def init_matrix(seq1: str, seq2: str) -> np.ndarray:
    col = len(seq1) + 1
    row = len(seq2) + 1
    mat = np.zeros((row, col))

    # TODO: if open is not equal to extend
    mat[:, 0] = [i * gap_score for i in range(row)]
    mat[0, :] = [i * gap_score for i in range(col)]
    # print(mat)
    return mat


def cal_matrix(mat: np.ndarray, seq1: str, seq2: str) -> tuple:
    mat_shape = mat.shape
    trace_mat = np.zeros((mat_shape[0], mat_shape[1]))
    for i in range(1, mat_shape[0]):
        for j in range(1, mat_shape[1]):
            match = (mat[i - 1, j - 1] + compare(seq1[j - 1], seq2[i - 1]), 1)
            # TODO: imp open and extend
            gap_lf = (mat[i, j - 1] + gap_score, 2)
            gal_up = (mat[i - 1, j] + gap_score, 3)
            grid = max(match, gap_lf, gal_up, key=lambda x: x[0])
            mat[i, j] = grid[0]
            trace_mat[i, j] = grid[1]

            # print("i: " + str(i) + " j: " + str(j))
            # print(mat)
    return (mat, trace_mat)


def get_trace_lis(m_tuple) -> list:
    lis = ["end"]
    trace_mat = m_tuple[1]
    print(trace_mat)
    t_mat_shape = trace_mat.shape

    i = t_mat_shape[0]
    j = t_mat_shape[1]

    while trace_mat[i, j] != 0:
        if trace_mat[i, j] == 1:
            lis.append("match")
            i -= 1; j -= 1
        elif trace_mat[i, j] == 2:
            lis.append("lf")
            i -= 1
        else:
            lis.append("up")
            j -= 1
    #
    # for i in range(t_mat_shape[0] - 1, 1, -1):
    #     for j in range(t_mat_shape[1] - 1, 1, -1):
    #         print("i : " + str(i) + " j: " + str(j) + " " + str(trace_mat[i, j]))
    #         if trace_mat[i, j] == 1:
    #             lis.append("match")


    return lis


def trace(lis: list):
    pass


if __name__ == "__main__":
    mat = init_matrix(s1, s2)
    m_tuple = cal_matrix(mat, s1, s2)
    # print(cal_matrix(mat, s1, s2)[1])
    print(get_trace_lis(m_tuple))
# def matchBase(base1, base2):
#     if base1 == base2:
#         return "match"
#     else:
#         return "mismatch"
# # 初始化动态规划矩阵的第一行和第一列
# def matrix(seq1, seq2):
#     input_1 = []
#     input_2 = []
#     for i in range(len(seq1)):
#         input_1.append(i * -4)
#     for i in range(len(seq2)):
#         input_2.append(i * -4)
#     return input_1, input_2

# def getScore(i, j, result_match):
#     num_s1 = "(" + str(j - 1) +"," +str(i - 1) + ")"
#     num_si = "(" + str(j - 1) +"," + str(i) + ")"
#     num_sj = "(" + str(j) + "," + str(i - 1) + ")"

#     if result_match == "match":
#         score1 = score[num_s1] + 4
#     else:
#         score1 = score[num_s1] - 3
#     score_i = score[num_si] - 4
#     score_j = score[num_sj] - 4
#     score_max = max(score1, score_i, score_j)
#     a = "(" + str(j) +"," +str(i) + ")"

#     if score_max == score1:
#         con[a] = score_max
#     elif score_max == score_i:
#         a_i[a] = score_max
#     else:
#         b_j[a] = score_max

#     score[a] = score_max


# def getPath(j, i,seq1, seq2,flag):
#     a = "(" + str(j) + "," + str(i) + ")"
#     score_res1 = con.get(a)
#     score_res2 = a_i.get(a)
#     score_res3 = b_j.get(a)

#     if score_res1 != None:
#         res1.append(seq1[i])
#         res2.append(seq2[j])
#         if j == 0:
#             return res2
#         res_j = getPath(j - 1, i - 1,seq1, seq2,flag)
#     elif score_res2:
#         res1.append("-")
#         res2.append(seq2[j])
#         if j == 0 :
#             return res2
#         res_j = getPath(j - 1, i ,seq1, seq2,flag)
#     else:

#         if score_res3 != None:
#             res2.append("-")
#             res1.append(seq1[i])
#             flag = False
#         else:
#             res2.append(seq2[j])
#             res1.append(seq1[i])
#             flag = True
#         if j == 0:
#             return res2
#         res_j = getPath(j,i- 1,seq1, seq2,flag)
#     return res_j


# def run(seq1, seq2):
#     input_1, input_2 = matrix(seq1, seq2)
#     for i in range(len(input_1)):
#         s = "(0," + str(i) + ")"
#         score[s] = input_1[i]
#     for i in range(len(input_2)):
#         s = "(" + str(i) + ",0)"
#         score[s] = input_2[i]
#     for j in range(len(seq2) - 1):
#         j += 1
#         for i in range(len(seq1) - 1):
#             i += 1
#             result_match = matchBase(seq1[i],seq2[j])
#             getScore(i, j, result_match)
#     flag = True
#     res_j = getPath(len(seq2) - 1, len(seq1) - 1,seq1, seq2,flag)
#     return res_j


# if __name__ == "__main__":
#     flag = True
#     while(flag):
#         # seq1 = input("Please input seq1")
#         # seq2 = input("Please input seq2")

#         seq1 = "AAAATTC"
#         seq2 = "AAAAGGTTC"

#         res1 = []; res2 = []
#         a_i = {}; b_j = {}
#         con = {}; score = {}

#         seq1 = "0" + seq1.upper()
#         seq2 = "0" + seq2.upper()

#         res_j = run(seq1, seq2)
#         res_j.reverse()
#         res1.reverse()
#         print("  ".join(res1))
#         print("  ".join(res_j))

#         tmp = input("是否继续判断：[y/n]")

#         if tmp.strip() == "n":
#             flag = False
#         else:
#             flag = True
