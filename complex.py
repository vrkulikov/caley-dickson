from itertools import zip_longest

def _conj(x):
    try:
        return x.conj
    except:
        return x

class Complex:
    def __init__(self,*args) -> None:
        if len(args) == 0:
            self.re = 0
            self.im = 0
        elif len(args)== 1:
            self.re = args[0]
            self.im = 0
        elif len(args)==2:
            self.re, self.im = args
        else:
            l = len(args)
            k = 1
            while k<l:
                k*=2
            new_args = args+tuple(0 for _ in range(k-l))
            self.re=Complex(*new_args[:k//2])
            self.im=Complex(*new_args[k//2:])
    

    @property
    def order(self):
        n = 0
        a = self
        while isinstance(a, Complex):
            n += 1
            a = a.re
        return n

    def __repr__(self) -> str:
        return 'Complex({}, {})'.format(self.re,self.im)


    @property
    def pair(self):
        try:
            return self.re.pair+self.im.pair        
        except:
            return self.re,self.im
    

    def __str__(self):
        return 'Complex'+str(self.pair)

    @staticmethod
    def zeros(order):
        if order <= 0:
            return 0
        else:
            return Complex(Complex.zeros(order-1),Complex.zeros(order-1))

    def __add__(self,other):
        try:
            return Complex(self.re+other.re,self.im+other.im)
        except:
            try:
                return Complex(*[a+b for a,b in zip_longest(self.pair,other.pair,fillvalue=0)])
            except:
                return NotImplemented
            

    def __radd__(self,other):
        return self+other

    def __eq__(self,other):
        return self.im == other.im and self.re == other.re

    def __neg__(self):
        return Complex(-self.re,-self.im)

    def __sub__(self,other):
        return Complex(self.re-other.re,self.im-other.im)

    def __mul__(self,other):
        try:
            return Complex(
                self.re * other.re - _conj(other.im) * self.im,
                other.im * self.re + self.im * _conj(other.re)
            )
        except AttributeError:
            try:
                return  Complex(self.re*other,self.im*other)
            except:
                return NotImplemented

    def __rmul__(self,other):
        return self * other
    @property
    def conj(self):
        try:
            re = self.re.conj
        except:
            re = self.re
        
        return Complex(re, -self.im)
