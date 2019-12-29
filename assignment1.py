# 과제 금요일 
# . >>> 구구단 <<< .
# 2*1=2
# 2*2=4
# 2*3=6
# 2*4=8
# 3*1
# 3*2
# 3*3
# 4*1

print ("구구단 2단부터 9단까지")
for num1 in range(2,10):
  print("")
  print(num1,"단")
  print("")
  for num2 in range(1,10):
   print (num1, "*" , num2, "=" , num1*num2) 
   print("")


p = input("Enter a number (2 to 9) :")
q = int(p)
print(q,"단")
for num3 in range(1,10):
  print( q, "*" , num3, "=", q*num3 ) 
print("")



print("multiply two numbers!")
print("")
x = input("Enter a number,put only integer :")
a = int(x)
y = input("Enter a number,put only integer :")
b = int(y)
print(a,"*",b, "=", a*b)
