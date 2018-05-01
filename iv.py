#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Wen Jiang"

import math
import matplotlib.pylab as plt
import matplotlib.ticker as ticker
import scipy.stats


class f():
    def __init__(self, s, E, r, t, c, si):
        self.s = s
        self.E = E
        self.r = r
        self.t = t
        self.c = c
        self.si = si

    def p(s, E, r, t, c, si):
        d1 = (math.log(s / E) + (r + si ** 2 / 2) * t) / (si * math.sqrt(t))
        d2 = d1 - si * math.sqrt(t)

        return s * scipy.stats.norm.cdf(d1) - E * math.exp(r * t) * scipy.stats.norm.cdf(d2) - c

    def d(s, E, r, t, c, si):
        d1 = (math.log(s / E) + (r + si ** 2 / 2) * t) / (si * math.sqrt(t))
        d2 = d1 - si * math.sqrt(t)
       
        dd1 = (si ** 2 * t * math.sqrt(t) - (math.log(s / E) + (r + si ** 2 / 2) * t) * math.sqrt(t)) / (
            si ** 2 * t)

        dd2 = dd1 - math.sqrt(t)
 
        return s * scipy.stats.norm.pdf(d1) * dd1 - E * math.exp(-r * t) * scipy.stats.norm.pdf(d2) * dd2

class gr(object):
    def __init__(self, name):
        self.name = name

    def type(self):
        print("Plotting", self.name)

class ma(gr):
    def __init__(self, name):
        super(ma, self).__init__(name)

    def type(self):
        print("Plotting", self.name)

    def plot(self, solution):

        print("Close the plot windows if needed to continue")

        ci = (range(1, len(solution) + 1, 1))

        fig, ax = plt.subplots()
        for axis in [ax.xaxis, ax.yaxis]:
            axis.set_major_locator(ticker.MaxNLocator(integer=True))

        plt.plot(ci, solution, color='red', label="Value")
        plt.xlabel('Number of Estimate')
        plt.ylabel('Estimate')
        plt.legend(loc='lower center')
        plt.title('Calculation')

        for i, j in zip(ci, solution):
            if (i == len(ci)):
                ax.annotate('%s' % round(j, 4), xy=(i, j), xytext=(0, 0), textcoords='offset points')

        plt.show()


def e(s, E, r, t, c):
    si = 0.1
    to = 0.00000001

    an = [0] * 10
    an[1] = si

    mi = 100
    i = 2

    while (i <= mi):

        fun = f.p(s, E, r, t, c, si)
        dif = f.d(s, E, r, t, c, si)

        si = si - fun / dif
        an[i] = si

        if (abs(an[i] - an[i - 1]) < to):
            an = an[1:i]
            break
        i = i + 1

    return an


def main():
    solution = (e(34, 34, 0.001, 1, 2.7240 ))
    g = gr("Calculation")
    g.type()
    m = ma('Plot')
    m.plot(solution)


if __name__ == "__main__":
    main()
