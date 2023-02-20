# print("Hello World")
# print("Xin chao the gioi ", end = "DoanDuyHoan")

# n = input("Nhap so n = ")
# print("So vua nhap n = ", n)

# name = "Doan Duy Hoan"
# print(name)

# _int = 5
# _float = 10.5
# _bool = True
# _string = "Xin chao the gioi"

# print(_int ,  type(_int))
# print(_float ,  type(_float))
# print(_bool ,  type(_bool))
# print(_string ,  type(_string))

# _first = int (input("Nhap so thu nhat = "))
# _second = int (input("Nhap so thu hai = "))
# print("Sum = ",_first + _second)
# print("Sub = ", _first - _second)
# print("Mul = ", _first * _second)
# print("Div = ", _first / _second)
# print("Rem = ", _first % _second)

# so_thu_nhat = int (input("Nhap so thu nhat "))
# so_thu_hai = int (input("Nhap so thu hai "))
# print("Phep chia ", so_thu_nhat, "/", so_thu_hai, "=", so_thu_nhat / so_thu_hai)
# print("Phan nguyen =", so_thu_nhat // so_thu_hai)
# print("Phan thap phan =", so_thu_nhat / so_thu_hai - so_thu_nhat // so_thu_hai)
# print("Chia lay du =", so_thu_nhat % so_thu_hai)

# a = int (input("Nhap a = "))
# b = int (input("Nhap b = "))
# a = a + b
# b = a - b
# a = a - b
# print("a = ",a)
# print("b = ",b)

# _str = "This is my string!"
# print(_str)
# print(_str[:])
# print(_str[3:])
# print(_str[:4])
# print(_str[-7:-1])

# name = "  Doan Duy Hoan  "  
# print(len(name))
# print(name.strip())
# print(name.lower())
# print(name.upper())
# print(name.replace("o","<~>"))
# print(name.split())
# Hoan = name.split()
# print(Hoan[2])

# f_name = "Doan"
# l_name =  "Hoan"
# name = f_name + l_name
# print(name)
# print(f_name in name)
# print("Doan {} Hoan".format("Duy"))

# name = "I am learning Computer Vision!"
# print(name.upper())
# if name.find("ng"):
#       print("YES")
# else:
#       print("NO")
# print(name[:10])

t = int (input("So nam can kiem tra "))
while t!=0:
      month = int (input("Nhap thang: "))
      year = int (input("Nhap nam: "))
      if str(month) in "1 3 5 7 8 10 12" and month != 2:
            print("31 days\n")
      elif str(month) in "4 6 9 11":
            print("30 days\n")
      else:
            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                  print("29 days\n")
            else:
                  print("28 days\n")
      t = t - 1

