from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression

import scipy.stats

import matplotlib.pyplot as plt

import numpy as np


x = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863]
y = [2, 3, 2, 1, 2, 1, 2, 1, 2, 5, 4, 7, 8, 7, 8, 11, 14, 13, 16, 17, 16, 19, 20, 23, 28, 29, 28, 29, 28, 29, 40, 41, 44, 43, 50, 49, 52, 55, 56, 59, 62, 61, 68, 67, 68, 67, 76, 85, 86, 85, 86, 89, 88, 95, 98, 101, 104, 103, 106, 107, 106, 113, 124, 125, 124, 125, 136, 139, 146, 145, 146, 149, 154, 157, 160, 161, 164, 169, 170, 175, 182, 181, 188, 187, 190, 191, 194, 199, 200, 199, 200, 209, 214, 215, 220, 221, 224, 233, 232, 247, 250, 257, 260, 263, 262, 265, 272, 275, 278, 277, 280, 283, 284, 283, 292, 299, 298, 299, 302, 305, 304, 313, 314, 317, 322, 329, 334, 341, 346, 349, 352, 353, 358, 361, 362, 367, 368, 379, 386, 395, 394, 401, 400, 401, 400, 407, 418, 419, 418, 419]

data_size = 50
# x = x[:data_size]
# y = y[:data_size]

size_train = 5
x_interval = 100

def linear_regression():
    x_plot = np.linspace(min(x), max(x), 100)
    x_train = np.sort(x[:size_train])
    x_test = np.sort(x[size_train:])
    yy = np.sort(y[:size_train])
    y_test = np.sort(y[size_train:])
    X = x_train[:, np.newaxis]
    X_plot = x_plot[:, np.newaxis]
    colors = ["teal", "yellowgreen", "orange", "blue", "green", "red", "black"]
    lw = 2
    degrees = [2, 3, 4, 5, 6, 7]
    for count, degree in enumerate(degrees):
        model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
        model.fit(X, yy)
        y_plot = model.predict(X_plot)
        plt.plot(x_plot,  y_plot, color=colors[count], linewidth=lw, label=f"Grau {degree}")

    plt.scatter(x, y, color="navy", s=30, marker="o")
    plt.ylim([-2, max(y)+10])
    plt.legend(loc="best")
    plt.show()


def PlotPolly(model, independent_variable, dependent_variable, x_name, y_name):
    x_new = np.linspace(min(x), max(x), x_interval)
    y_new = model(x_new)

    plt.plot(independent_variable, dependent_variable, ".", x_new, y_new, "-")
    plt.title(f"Polynomial Fit with Matplotlib for {x_name} ~ {y_name}")
    ax = plt.gca()
    ax.set_facecolor((0.898, 0.898, 0.898))
    fig = plt.gcf()
    plt.xlabel(x_name)
    plt.ylabel(y_name)

    plt.show()
    plt.close()


def plot_normalizate(x, y, model=None):
    if model is not None:
        x_new = np.linspace(min(x), max(x), 1000)
        y_new = model(x_new)
        plt.plot(x, y, ".", x_new, y_new, "-")
    else:
        plt.plot(x, y, ".")

    ax = plt.gca()
    ax.set_facecolor((0.898, 0.898, 0.898))
    fig = plt.gcf()

    plt.show()
    plt.close()



if __name__ == "__main__":
    # xx = scipy.stats.zscore(x)
    # yy = scipy.stats.zscore(y)

    # f = np.polyfit(xx, yy, 50)
    # p = np.poly1d(f)
    # print(p)
    # PlotPolly(p, x, y, "Primos", "Restos")


    plot_normalizate(x, y)