class Complex:
    def __init__(self,re=0, im=0) -> None:
        self.re = re
        self.im = im

    def __str__(self) -> str:
        return '({}, {})'.format(self.re,self.im)