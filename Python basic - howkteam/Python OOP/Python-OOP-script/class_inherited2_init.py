#!/usr/bin/env python3.8
class SieuNhan:
    suc_manh = 50
    def __init__(self, para_ten, para_vu_khi, para_mau_sac): 
        self.ten = para_ten
        self.vu_khi = para_vu_khi
        self.mau_sac = para_mau_sac

class SieuNhanGao(SieuNhan):
    suc_manh = 60
    def __init__(self, para_ten, para_vu_khi, para_mau_sac, para_su_thu):
        super().__init__(para_ten, para_vu_khi, para_mau_sac)
        self.su_thu = para_su_thu

    # define special method __str__
    def __str__(self):
        return "Day la {}, su dung {}".format(self.ten, self.vu_khi)
    
    def __repr__(self):
        return 'ten: {} \nvu khi: {}\n mau sac: {}'.format(self.ten, self.vu_khi, self.mau_sac)

sieu_nhan_1 = SieuNhanGao("sieu nhan xanh", "dao", "xanh", "cho")
print(sieu_nhan_1.ten)
print(sieu_nhan_1.__dict__)
print(sieu_nhan_1.suc_manh)

# dont use special method
print(sieu_nhan_1)

# Use special method __str__
print(sieu_nhan_1.__str__())