def _conj(x):
    try:
        return x.conj
    except:
        return x

class Complex:
    def __init__(self,re=0, im=0) -> None:
        self.re = re
        self.im = im

    def __repr__(self) -> str:
        return 'Complex({}, {})'.format(self.re,self.im)

    def __add__(self,other):
        try:
            return Complex(self.re+other.re,self.im+other.im)
        except:
            return NotImplemented

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
