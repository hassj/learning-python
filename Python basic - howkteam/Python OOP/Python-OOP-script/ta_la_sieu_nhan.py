#!/usr/bin/env python3.8

class Sieunhan:
    def __init__(self, para_ten, para_vu_khi, para_mau_sac):
        self.ten = "Sieu nhan" + para_ten
        self.vu_khi = para_vu_khi
        self.mau_sac = para_mau_sac
    def xinchao(self):
        print("Ta la sieu nhan" + self.ten)
sieu_nhan_A = Sieunhan("do", "kiem", "do")
print(sieu_nhan_A.xinchao())
print(Sieunhan.xinchao(sieu_nhan_A))