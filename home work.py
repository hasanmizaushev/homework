import random
import pandas as pd

class My_scipy:
    def rvs(self, p, size):
        self.sp = []
        g = [0, 1]
        p = str(p)
        p = p[2:]
        if p[:] == p[:1]:
            p = int(str(p) + "0")
        for s in range(size):
            if p == 50:
                head_or_tail = random. choice(g)
                self.sp.append(head_or_tail)
        print(self.sp)

    def pmf(self, k, n, p):
        nk = [[n], [k]]
        b = []
        for i in nk:
            for g in i:
                b.append((g * p**k * (1-p)(n-k)))
        print(sum(b))

    def cdf(self, k, n, p):
        b = []
        for i in range(k):
            nk = [[n], [i]]
            for h in nk:
                for g in h:
                    b.append((g * p**i *  (1 - p)(n-i)))
        print(sum(b))

    def sf(self, k, n, p):
        print(1-self.cdf(k, n, p))

    def mean(self, array_list):
        return sum(array_list) / len(array_list)

    def expected_value(self, p):
        return p*1 + 0*(1-p)

    def variance(self, x):
        my_mean = self. mean(x)
        _sum = 0
        for i in x:
            _sum += (i - my_mean)**2
        print(_sum/(len(x)-1))

    def stats(self, x, p):
        print('expected_value: {}'.format(self.expected_value(p)), "variance:{}".format(self.variance(x)))

df = pd.read_excel('probability_data.xlsx')
df = list(df["number"])
binom = My_scipy()
binom.mean(df)
binom.variance(df)