#!/usr/bin/env python3.8

class SieuNhan:
    suc_manh = 50

# this class inherit from SieuNhan class
class SieuNhan_Gao(SieuNhan):
    pass

# this class inherit from SieuNhan class with attribute suc_manh having other value
class SieuNhan_Gao2(SieuNhan):
    suc_manh = 60

sieu_nhan_A = SieuNhan_Gao()
sieu_nhan_B = SieuNhan_Gao2()

print(sieu_nhan_A.suc_manh)
print(sieu_nhan_B.suc_manh)
print("sieu_nhan_A.suc_manh")
