# CHAPTER 1: CLASS AND OBJECT IN PYTHON OOP
## What is CLASS

class like a sample or pattern in which define attribute and methods to create object or instance

## Syntax
```
clas <class_name>:
    code
```
Example

```
class SieuNhan:
    pass 
```
or 

```
class SieuNhan:
    suc_manh = 50
	def __init__(self, para_ten, para_vu_khi, para_mau_sac):
	    self.ten = para_ten
		self.vu_khi = para_vu_khi
		self.mau_sac = para_mau_sac
		
	def xin_chao(self):
	    print("Xin chao, ta la" +  self.ten)
		print("suc manh cua ta la", self.suc_manh)

sieu_nhan_A = SieuNhan("sieu nhan do", "kiem", "do")

sieu_nhan_A.xin_chao()
```
> __init__ by default is constructor initialize method
>
> pass: hodler command
>
> name of class named as CapWords follow by PEP8.

# Chapter 2: Declare attribute in OOP

> - Talking about class need to mention about method (maybe called function but related to class) and attribute (feature used to difference class with each other)
> - Updating attribute via class will change update all the object created by that class at all.
> - Updating attribute via conductor without class, will have a difference value at other objects created by that class.
> - Updating attribute on object directly, just having effectively only on that object

# Chapter 3: Class Methods in OOP PYTHON

- Regular method: having default parameter "self"
- Class method: defined by first parameter is "cls". It always send arguments to class's method or object created by that class which call to class method.
If class method dont change the value of that class's method. it will send all arguments to regular method init. 
To defined class method, always used "@classmethod" keyword on top of block

> class method used to process data then send value to class instead of processing that data outside class.

```
#!/usr/bin/env python3.8

class SieuNhan:
    suc_manh = 50
    def __init__(self, para_ten, para_vu_khi, para_mau_sac):
        self.ten = para_ten
        self.vu_khi = para_vu_khi
        self.mau_sac = para_mau_sac
    @classmethod
    def from_string(cls, s): # thường những phương thức xử lí thế này hay có tên là from…
        lst = s.split('-')
        new_lst = [st.strip() for st in lst]
        ten, vu_khi, mau_sac = new_lst
        return cls(ten, vu_khi, mau_sac)

infor_str = "Sieu nhan do - Kiem - Do"
sieu_nhan_A = SieuNhan.from_string(infor_str)
print(sieu_nhan_A.__dict__)
```
>always named as from_

- Static method: have not any changes, dont send any arguements to anything at all, it may seem as normal method, but put it inide class for some reasons related to class. 
To defined static method always used "@staticmethod" keyword

```
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
```

> when used methods defined above:
>
> When creating class then using object created by that class you will use regular CLASS
>
> when creating class then using that class you will use class method
>
> other cases you will use static method, it means static_method dont use anything vairable/attribute of class, it only do some task for class such as print something...

# Chapter 4: Inherit class in OOP PYTHON

## Syntax
```
class class_name1:
    pass

class class_name2(class_name1):
    pass

```

Every attribute and methods belong class_name1 would have in class_name2 as inherited

## Inherited attribute
```
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
```
Note
> Above example descirbe two inherited class "SieuNhan_Gao" with origin attribute of class "SieuNhan" and "SieuNhan_Gao2" with attribute overwritten 

## Inherit Constructor method

```
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
```

In case you want to add more attribute for new class, do it follows:

```
#!/usr/bin/env python3.8
class SieuNhan:
    suc_manh = 50
    def __init__(self, para_mau_sac, para_vu_khi, para_mau): 
        self.mau_sac = para_mau_sac
        self.vu_khi = para_vu_khi
        self.mau = para_mau

class SieuNhanGao(SieuNhan):
    suc_manh = 60
    def __init__(self, para_mau_sac, para_vu_khi, para_mau, para_su_thu):
        super().__init__(para_mau_sac, para_vu_khi, para_mau)
        self.su_thu = para_su_thu

sieu_nhan_1 = SieuNhanGao("sieu nhan xanh", "dao", "xanh", "cho")
print(sieu_nhan_1.__dict__)
print(sieu_nhan_1.suc_manh)
```

## Inherit method 

similar with inherit init method, just add more method which you want to adding.

```
class SieuNhan:
    suc_manh = 50
    def __init__(self, para_ten, para_vu_khi, para_mau_sac):
        self.ten = para_ten
        self.vu_khi = para_vu_khi
        self.mau_sac = para_mau_sac
    def xin_chao(self):
        print("Xin chao, ta la", self.ten)
    def show_suc_manh(self):
        print("Suc manh cua ta la", self.suc_manh)

class SieuNhanGao(SieuNhan):
    suc_manh = 40
    def __init__(self, para_ten, para_vu_khi, para_mau_sac, para_su_thu):
        super().__init__(para_ten, para_vu_khi, para_mau_sac)
        self.su_thu = para_su_thu
    def show_suc_manh(self):
        print("Suc manh cua ta la", self.suc_manh)
        print("Su dung su thu", self.su_thu)

sieu_nhan_A = SieuNhan("Sieu nhan do", "Kiem", "Do")
gao_do = SieuNhanGao("Gao do", "Cung", "Do", "Su tu")

sieu_nhan_A.xin_chao()
gao_do.xin_chao()

sieu_nhan_A.show_suc_manh()
gao_do.show_suc_manh()
```

# Chapter 5: Special method in OOP PYTHON
there are many sepecial method. Default format of special __name__(self,parax). it will help us show clear the content instead of.
```
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
print(sieu_nhan_1.__dict__)
print(sieu_nhan_1.suc_manh)

# dont use special method
print(sieu_nhan_1)

# Use special method __str__
print(sieu_nhan_1.__str__())
```
> if have both __str__ and __repr__ in one class, by default __str__ take a precedence by print()
>
> reffer [special method](https://howkteam.vn/course/lap-trinh-huong-doi-tuong-voi-python/cac-phuong-thuc-dac-biet-trong-lap-trinh-huong-doi-tuong-python-3885)

# Chapter 6: Setters, Getters, Deleters in OOP PYTHON
It was method but sometimes it is not method 

## Getters
- you have a class belows:

```
#!/usr/bin/env python3.8

class KTer:
    def __init__(self, para_ho, para_ten):
        self.ho = para_ho
        self.ten = para_ten
        self.email = para_ho + '-' + para_ten + '@example.com'

    # defined another regular method
    def ho_va_ten(self):
         return '{} {}'.format(self.ho, self.ten)


# Initialize an object from KTer
kter_A = KTer("Tran", "Linh")

#print
print(kter_A.ho)
print(kter_A.ten)
print(kter_A.email)
print(kter_A.ho_va_ten())	    
```

>Tran
>Linh
>Tran-Linh@example.com
>Tran Linh

- You want to change the the values of "ho" and "ten", the result in as belows:
```
# Initialize an object from KTer
kter_A = KTer("Tran", "Linh")

kter_A.ho = "nguyen"
kter_A.ten = "Hung"

#print
print(kter_A.ho)
print(kter_A.ten)
print(kter_A.email)
print(kter_A.ho_va_ten())
```
>nguyen
>Hung
>Tran-Linh@example.com
>nguyen Hung

- Email dont change at all, so you want to email change as "ho" "ten" as attribute, you should create a method belows:
```
#!/usr/bin/env python3.8

class KTer:
    def __init__(self, para_ho, para_ten):
        self.ho = para_ho
        self.ten = para_ten
       # self.email = para_ho + '-' + para_ten + '@example.com'

    # defined another regular method
    def ho_va_ten(self):
         return '{} {}'.format(self.ho, self.ten)
    
    def email(self):
	    #return self.ho + '-' + self.ten + '@kteam.com'
        return '{}{}@example.com'.format(self.ho, self.ten )

# Initialize an object from KTer
kter_A = KTer("Tran", "Linh")

kter_A.ho = "nguyen"
kter_A.ten = "Hung"

#print
print(kter_A.ho)
print(kter_A.ten)
#print(kter_A.email)
print(kter_A.email())
print(kter_A.ho_va_ten())
```
It's still method instead attribute as you want it to be. Need add @property keyword to get around. this time you ``print(kter_A.email)`` instead of ``print(kter_A.email())``
```
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
```

And now you're already done for it. so, you want to have attribute from method it would place getters play in.

## Setters

You set value for method ho_va_ten as bellows:

```
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
    
#Initialize an object from KTer class
kter_A = KTer("Tran", "Giau")

kter_A.ho_va_ten = "Nguyen Linh"

print(kter_A.email)
print(kter_A.ho_va_ten)
```
it will casue a error, since ho_va_ten this time is ho_va_ten is method natural. so get rid just add setter in here.
```
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
```

## Deleters
If you want to delete after use, it is time for deleters come in. You could assign 0, none value for which you want to delete
```
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
```


