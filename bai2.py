# n = int(input())
# count = 1
# while (count <= 10):
#     print("{} * {} = ".format(n, count),n*count)
#     count+=1

# i = 0
# while (i <= 100):
#     print(i, end = " ")
#     i+=1

# n = int(input())
# i = 1
# count = 0
# while (i<=n):
#     if (n%i==0):
#         count+=1
#     i+=1
# print(count)

# s = "Toi dang hoc lap trinh Python"
# for i in s:
#     print(i, end = " ")

# for i in range(1,10,2):
#     print(i, end = " ")

# n = int(input())
# sum = 0
# for i in range(1,n+1):
#     if (i < n):
#         print(i,"+", end = " ")
#     sum += i
# print(n,"=",sum)

# import math
# n = int(input())
# if n < 2:
#     print(n,"khong phai la so nguyen to")
#     exit()
# for i in range(2, int(math.sqrt(n))):
#     if (n % i == 0):
#         print(n,"khong phai la so nguyen to")
#         exit()
# print(n,"la so nguyen to")

# s = "Toi la sinh vien"
# i = 0
# while i < len(s):
#     if (s[i] == 'v'):
#         break
#     i+=1
# for j in range(0,i):
#     print(s[j], end = " ")
    
# s = "a1b2c3d4e5g6h9k1"
# for i in range(0, len(s)-1):
#     if (s[i] >= '0' and s[i] <= '9'):
#         print(s[i], end = " ")

print("Nhap ho va ten: ")
s = input()
while len(s) == 0:
    print("Nhap ho va ten: ")
    s = input()
print(s)