#!/usr/in/env python3.9

class KTer:
    def __init__(self, para_ho, para_ten):
        self.ho = para_ho
        self.ten = para_ten

    @property
    def email(self):
        return self.ho + '-' + self.ten + '@example.com'
    
    @property
    def ho_va_ten(self):
        return '{}{}'.format(self.ho, self.ten)
    
    @ho_va_ten.setter
    def ho_va_ten(self, tenmoi):
        ten_moi, ho_moi = tenmoi.split(' ')
        self.ten = ten_moi
        self.ho = ho_moi

    @ho_va_ten.deleter
    def ho_va_ten(self):
        self.ho = None
        self.ten = None
        print("da xoa")
    
kter_A = KTer("tran", "long")

kter_A.ho_va_ten = "Nguyen Kinh"

print(kter_A.ho_va_ten)
del kter_A.ho_va_ten
print(kter_A.ho)
print(kter_A.ten)
