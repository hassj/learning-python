#!/usr/bin/env python3.8

class SieuNhan:
    suc_manh = 50
    def __init__(self, para_ten, para_vu_khi, para_mau_sac):
        self.ten = para_ten
        self.vu_khi = para_vu_khi
        self.mau_sac = para_mau_sac

class SieuNhanGao(SieuNhan):
    suc_manh = 60

sieu_nhan_A = SieuNhanGao("gao do", "kiem", "do")

print(sieu_nhan_A.__dict__)
print(sieu_nhan_A.suc_manh)