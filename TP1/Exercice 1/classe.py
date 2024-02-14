class Algebre :
    def __init__(self, n):
        self.n = n
    def somme_premiers_entiers(self):
        if (self.n < 0):
            return -1
        return self.n * (self.n + 1)//2

    def factorielle(self):
        if self.n < 0:
            return -1
        if self.n == 0:
            return 1
        else:
            res = 1
            for i in range (1, self.n + 1):
                res = res*i
            return res

