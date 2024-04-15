#!/usr/bin/env python3.8

class KTer:
    def __init__(self, para_ho, para_ten):
        self.ho = para_ho
        self.ten = para_ten
    
    @property
    def email(self):
        return self.ho + "-" + self.ten + "@example.com"
    
    @property
    def ho_va_ten(self):
        return "{}{}".format(self.ho, self.ten)
    
    @ho_va_ten.setter
    def ho_va_ten(self, tenmoi):
        ho_moi, ten_moi = tenmoi.split(' ')
        self.ho = ho_moi
        self.ten = ten_moi
    
#Initialize an object from KTer class
kter_A = KTer("Tran", "Giau")

kter_A.ho_va_ten = "Nguyen Linh"

print(kter_A.email)
print(kter_A.ho_va_ten)
