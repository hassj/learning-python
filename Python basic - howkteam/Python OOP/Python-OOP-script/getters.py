#!/usr/bin/env python3.8

class KTer:
    def __init__(self, para_ho, para_ten):
        self.ho = para_ho
        self.ten = para_ten
       # self.email = para_ho + '-' + para_ten + '@example.com'

    # defined another regular method
    def ho_va_ten(self):
         return '{} {}'.format(self.ho, self.ten)
    @property
    def email(self):
        return self.ho + '-' + self.ten + '@kteam.com'
        #return '{}{}@example.com'.format(self.ho, self.ten )

# Initialize an object from KTer
kter_A = KTer("Tran", "Linh")

kter_A.ho = "nguyen"
kter_A.ten = "Hung"

#print
print(kter_A.ho)
print(kter_A.ten)
#print(kter_A.email)
#print(kter_A.email())
print(kter_A.email)
print(kter_A.ho_va_ten())