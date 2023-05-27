import math
class MyFractal:
    def __init__(self, numerator, denumerator):
        self.numerator=numerator
        self.denumerator=denumerator
    def __str__(self):
        return f"{self.numerator}/{self.denumerator}"
    def __add__(self, other):
        common_den=self.denumerator*other.denumerator
        second_num=other.numerator*self.denumerator
        first_num=self.numerator*other.denumerator
        return MyFractal(first_num+second_num, common_den)
    def __sub__(self, other):
        common_den=self.denumerator*other.denumerator
        second_num=other.numerator*self.denumerator
        first_num=self.numerator*other.denumerator
        return MyFractal(first_num-second_num, common_den)
    def __add__(self, other):
    #    elif isinstance(other, int):
        second=MyFractal(other, 1) #3/1
    def simplity(self):
        common_den=math.gcd(self.numerator, self.denumerator)
        self.numerator//=common_den
        self.denumerator//=common_den
    def __mul__(self, other):
        if isinstance(other, MyFractal):
            result=MyFractal(self.numerator*other.numerator, self.denumerator*other.denumerator)
            result.simplity()
            return result
        elif isinstance(other, int):
                result=MyFractal(self.numerator*other, self.numerator)
                result.simplity()
                return result
    def __truediv__(self, other):
        if isinstance(other, MyFractal):
            result=MyFractal(self.numerator*other.numerator, self.denumerator*other.denumerator)
            result.simplity()
            return result
        elif isinstance(other, int):
                result=MyFractal(self.numerator/other, self.numerator)
                result.simplity()
                return result