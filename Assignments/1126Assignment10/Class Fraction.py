
def gcd(a, b):
    while b!=0:
        a, b = b, a%b
    return a

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    def __str__(self):
        return (str(self.numerator) + '/' + str(self.denominator))
    def __add__(self,other):
        num=self.numerator*other.denominator+other.numerator*self.denominator
        den=self.denominator*other.denominator
        g=gcd(num,den)
        return Fraction(num//g,den//g) if num%den else num//den
    def __sub__(self,other):
        num=self.numerator*other.denominator-other.numerator*self.denominator
        den=self.denominator*other.denominator
        g=gcd(num,den)
        return Fraction(num//g,den//g) if num%den else num//den
    def __mul__(self,other):
        num=self.numerator*other.numerator
        den=self.denominator*other.denominator
        g=gcd(num,den)
        return Fraction(num//g,den//g) if num%den else num//den
    def __truediv__(self,other):
        num=self.numerator*other.denominator
        den=self.denominator*other.numerator
        return Fraction(num,den)
    def __floordiv__(self,other):
        num=self.numerator*other.denominator
        den=self.denominator*other.numerator
        g=gcd(num,den)
        return Fraction(num//g,den//g) \
            if num%den else num//den
    def simplify(self):
        g=gcd(self.numerator,self.denominator)
        return Fraction(self.numerator//g,self.denominator//g) \
            if self.numerator % self.denominator \
            else self.numerator // self.denominator
a=Fraction(int(input()),int(input()))
b=Fraction(int(input()),int(input()))
print(f'a:{a},b:{b}')
a=a.simplify()
b=b.simplify()
print(f'simplify:a={a},b={b}')
print(f'a+b:{a+b}')
print(f'a-b:{a-b}')
print(f'a*b:{a*b}')
print(f'a/b:{a/b}')
print(f'a//b:{a//b}')