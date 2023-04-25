import statistics
import numpy as np
import pandas as pd
from scipy import stats


def F_j(fj, c):
    Fj = [fj[0]]
    for i in range(1,len(fj)-1):
        Fj.append(Fj[i-1] + fj[i])

    Fj = np.array(Fj)
    h = np.array([f/c for f in Fj])

    return Fj, h # frequência acumulada, altura do eixo y

def intervalo_classes(dados, k, c):
    part = [dados.min()]
    for i in range(1, k+1):
        part.append(part[i-1]+c)

    aux = min(part)
    iterv_p = []
    for i in range(1, k+1): 
        iterv_p.append([aux, part[i]])
        aux = part[i]

    return part, iterv_p

def freq_abs(dados, k, c):
    _freq_abs = lambda dados, l, c: np.logical_and(l<=dados, dados<l+c)
    part, iterv_p = intervalo_classes(dados, k, c)
    _fj = [_freq_abs(dados, j, c) for j in part]
    fj = [np.size(dados[j]) for j in _fj]

    return fj, part, iterv_p

def frequencia(dados, k: int = None, c: int = None):
    n = np.size(dados)

    if k is None:
        k = 1+3.322*np.log(np.size(dados))
        k = int(np.ceil(k))

    if c is None:
        c = (dados.max()-dados.min())/k
        c = int(np.ceil(c))

    fj, part, iterv_p = freq_abs(dados, k, c)
    f_rj = np.array([f/n for f in fj])
    Fj, h = F_j(fj, c)
    F_rj = np.array([f/n for f in Fj])

    return [n, k, c, (part, iterv_p), fj, f_rj, (Fj, h), F_rj]

def tabela_frequencia(interbalo_classe, fj, f_rj, Fj, F_rj, k):
    nomes_col = ["$X = $", "$f_{j}$", "$f_{rj}$", "$F_{j}$", "$F_{rj}$"]
    inter = [f'[{l0}, {l1})' for l0, l1 in interbalo_classe]
    print(" & ".join(nomes_col)+" \\\\ \\hline")

    fj_total = 0
    frj_total = 0

    for i in range(k):
        print("{0} & {1} & {2} & {3} & {4} \\\\ \\hline".format(inter[i], fj[i], f_rj[i], Fj[i], F_rj[i]))
        fj_total += fj[i]
        frj_total += f_rj[i]

    print("Total & {0} & {1} & & \\\\ \\hline".format(fj_total, round(frj_total, 3)))

def analise_descritiva(dados, latex_show=False):
    TrMean = stats.trim_mean(dados, 0.1)
    Skewness = stats.skew(dados)
    Maximum = dados.max()
    Minimum = dados.min()
    Mean = dados.mean()
    Median = statistics.median(dados)
    Mode = stats.mode(dados, keepdims=True).mode
    StandardDeviation = dados.std()
    StandardErrorOfTheMean = stats.sem(dados)
    Kurtosis = stats.kurtosis(dados)
    Sum = dados.sum()
    N = np.size(dados)
    Quartile = np.quantile(dados, (0.25, 0.50, 0.75))
    Q1 = Quartile[0]
    Q2 = Quartile[1]
    Q3 = Quartile[2]
    Variance = dados.var()

    describe = {"TrMean": TrMean,
                "Skewness": Skewness,
                "Maximum": Maximum,
                "Minimum": Minimum,
                "Mean": Mean,
                "Median": Median,
                "Mode": Mode,
                "StDev": StandardDeviation,
                "SE Mean": StandardErrorOfTheMean,
                "Kurtosis": Kurtosis,
                "Sum": Sum,
                "N": N,
                "Variance": Variance,
#                    "Quartile": Quartile,
                "1. Quartile": Q1,
                "2. Quartile": Q2,
                "3. Quartile": Q3
    }

    if latex_show:
        for k, v in describe.items():
            print("{0:12} & {1} \\\\ \\hline".format(k, v))

    return describe


#def dispersao(variavel1:list, variavel2:list, varianca_tex=False):
def dispersao(variaveis: list, varianca_tex=False):
    """ Comparação de dispersão de dados relacionando duas variáveis"""

    print(r"AVISO: S^{2} = \frac{1}{n-1} \sum_{i=1}^{n} (x_{i} - \bar{x})^{2}", end="\n\n")

    vars_dict = {}
    for i in variaveis:
        vars_dict[f"v{i}"] = np.array(variaveis[i], dtype=np.float)

#    A = np.array(variavel1, dtype=np.float)
#    B = np.array(variavel2, dtype=np.float)

    tam_vars = 0
    quant_vars = len(list(vars_dict.keys()))
    
    if quant_vars > 1:
        quant_dados = []
        for dados in vars_dict.values():
            quant_dados.append(len(dados))

        if (quant_dados[:-1]==quant_dados[1:]) and (quant_dados[1:]==quant_dados[:-1]):
            tam_vars = quant_dados[0]

        else:
            print("Erro! As variáveis não possuem a mesma quantidade de dados.")
            return
    else:
        tam_vars = len(vars_dict["v0"])

    ###############
    # Media de ambas variáveis
    Am = A.mean()
    Bm = B.mean()
    ###############

    N_1 = tam_vars - 1  # Assim como está no aviso S²=(1/n-1)(sum(x_i - ẍ)^2)

    ###############
    # Variança de A 
    Av_soma_parcela = np.array([(i - Am)**2 for i in A])
    av = 0
    for i in Av_soma_parcela:
        av+=i
    Av = (1/N_1) * (av)
    ###############
    
    ###############
    # Variança de B
    Bv_soma_parcela = np.array([(i - Bm)**2 for i in B])
    bv = 0
    for i in Bv_soma_parcela:
        bv+=i
    Bv = (1/N_1) * (bv)
    ###############

    ###############
    # Desvio Padrão de A
    Astd = np.sqrt(Av)
    ###############

    ###############
    # Desvio Padrão de B
    Bstd = np.sqrt(Bv)
    ###############

    resultado = {"v1_varianca": Av,
                "v2_varianca": Bv,
                "v1_media": Am,
                "v2_media": Bm,
                "v1_desvio_padrao": Astd,
                "v2_desvio_padrao": Bstd,
    }

    if varianca_tex:
        def montar_bloco(variaveis:list, round_default=4):
            for i in range(quant_vars):
                solucao = []
                _key = f"v{i}_varianca"
                _variavel = variaveis[i]
                for k, v in resultado.items():
                    if _key==k:
                        media_amostral = round(resultado[f"v{i}_media"],
                                   round_default)

                        quad_diff = [f"({j} - {media_amostral})"+
                                    "^{2}" for j in _variavel]

                        arma_soma_quad_diff = ""
                        for j in quad_diff:
                            arma_soma_quad_diff += j+" + "

                        monta_exp1 = ("A_{S^{2}} = \\frac{1}{"+str(N_1)+\
                                        "}\\Big[ " +arma_soma_quad_diff+\
                                        " \\Big] = \\\\")

                        
                        if _key.starswith("v1"):
                            var_parcelas = Av_soma_parcela
                        else:
                            var_parcelas = Bv_soma_parcela

                        soma_quad_diff = ""
                        for j in var_parcelas:
                            soma_quad_diff += j+" + "

                        monta_exp2 = ("A_{S^{2}} = \\frac{1}{"+str(N_1)+\
                                        "}\\Big[ " +soma_quad_diff+\
                                        " \\Big] = \\\\")
                        
                        solucao = [monta_exp1, monta_exp2]

                if solucao:
                    print(f"Variável {i}:\n")
                    print(*[f"\r{s}\n" for s in solucao])
                    print("\n")

        montar_bloco([A, B])

        """
        # Variança de A tex
        Av_tex = [f"({int(i)} - {Am})"+"^{2}" for i in A]
        av_tex = ""
        for i in Av_tex:
            av_tex += i+" + "

        av_tex_p1 = "A_{S^{2}} = \\frac{1}{"+str(N_1)+"}\\Big[ " +av_tex+ " \\Big] = "
        av_tex = ""
        for i in Av_soma_parcela:
            av_tex += i+" + "

        av_tex_p1 = "A_{S^{2}} = \\frac{1}{"+str(N_1)+"}\\Big[ " +av_tex+ " \\Big] = "

        # Variança de B tex
        Bv_tex = [f"({int(i)} - {Bm})"+"^{2}" for i in B]
        bv_tex = ""
        for i in Bv_tex:
            bv_tex += i+" + "

        bv_tex = "B_{S^{2}} = \\frac{1}{"+str(N_1)+"}\\Big[ " +bv_tex+ " \\Big] = "

        print("Variável 1:\n")
        print(av_tex)
        print("\n")
        print("Variável 2:\n")
        print(bv_tex)
        print("\n")
        """

    return resultado
