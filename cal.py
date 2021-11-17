


num1=float(input("Enter your frist value :"))
num2=float(input("Enter your frist value :"))
print("select operator:")

print("1.Add")
print("2.Sub")
print("3.mul")
print("4.div")
   
   


select =input("select operator:")
if select == "1":
    print(num1+num2)
elif select =="2":
    print(num1-num2)
elif select == "3":
    print(num1*num2)  
elif select == "4":
    print(num1/num2) 
else:
    print("invaled input")   

