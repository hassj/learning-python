#!/usr/bin/env python 3.8

class SieuNhan:
    suc_manh = 50
    def __init__(self, para_ten, para_vu_khi, para_mau_sac):
        self.ten = para_ten
        self.vu_khi = para_vu_khi
        self.mau_sac = para_mau_sac
    
    @staticmethod
    def bien_hinh():
        print("1 2 3 bien hinh!")
    

sieu_nhan_A = SieuNhan("sieu nhan do", "kiem", "do")

print(sieu_nhan_A.bien_hinh())
