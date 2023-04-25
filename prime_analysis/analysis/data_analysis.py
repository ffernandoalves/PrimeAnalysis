import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import estatistica_descritiva as ed



# x = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863]
# y = [2, 3, 2, 1, 2, 1, 2, 1, 2, 5, 4, 7, 8, 7, 8, 11, 14, 13, 16, 17, 16, 19, 20, 23, 28, 29, 28, 29, 28, 29, 40, 41, 44, 43, 50, 49, 52, 55, 56, 59, 62, 61, 68, 67, 68, 67, 76, 85, 86, 85, 86, 89, 88, 95, 98, 101, 104, 103, 106, 107, 106, 113, 124, 125, 124, 125, 136, 139, 146, 145, 146, 149, 154, 157, 160, 161, 164, 169, 170, 175, 182, 181, 188, 187, 190, 191, 194, 199, 200, 199, 200, 209, 214, 215, 220, 221, 224, 233, 232, 247, 250, 257, 260, 263, 262, 265, 272, 275, 278, 277, 280, 283, 284, 283, 292, 299, 298, 299, 302, 305, 304, 313, 314, 317, 322, 329, 334, 341, 346, 349, 352, 353, 358, 361, 362, 367, 368, 379, 386, 395, 394, 401, 400, 401, 400, 407, 418, 419, 418, 419]
# nx = np.array(x)
# ny = np.array(y)
# dados = ny

filedata = "C:\\Users\\UFMA\\Documents\\docs\\Nova pasta (2)\\primes&restos.csv"
dt = pd.read_csv(filedata, sep="&")
dados = dt["resto"]

n, k, c, (part, iterv_p), fj, f_rj, (Fj, h), F_rj = ed.frequencia(dados, k=None, c=None)


def letra_a_tablefreq():
    ed.tabela_frequencia(iterv_p, fj, f_rj, Fj, F_rj, k)

def letra_c_hist():
#        plt.hist(dados, bins=k, density=True)
    x = np.array(part)+2.5
    plt.bar(x, f_rj, width=np.zeros(x.shape)+c, edgecolor=[0., 0., 0])
    plt.plot(x, f_rj, 'r.-')
#        plt.savefig(file_hist_img, dpi=1500)
    plt.show()

def letra_b_diag_barras():
    labels = [r"$F_{0}$".format(i) for i in range(len(Fj))]
    x = np.arange(len(labels))
    fig_acumul, ax_acumul = plt.subplots()
    ax_acumul.bar(x, Fj)
    ax_acumul.set_xticks(x)
    ax_acumul.set_xticklabels(labels)
#        plt.savefig(file_name_diag_barras, dpi=1000)
    plt.show()

def letra_c_describe():
    describe = ed.analise_descritiva(dados)
    print(describe)


if __name__ == "__main__":
    # letra_a_tablefreq()
    letra_c_describe()
    # letra_c_hist()
    # letra_b_diag_barras()