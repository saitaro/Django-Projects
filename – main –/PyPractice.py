
class sim:
    a = 1
    b = 2

    def ok(self):
        a = 1
        b = 2   
        return '{} is not {}'.format(a, b)

class bim(sim):
    c = 3
    def m(self, k):
        print(k)


cord = bim()

print(cord.ok())