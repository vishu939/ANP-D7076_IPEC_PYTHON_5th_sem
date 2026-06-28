# problem statement
# A goverment tax portal calculates tax based on the following condition:
income = int(input("Enter Annual Income:"))
Age = int(input("Enter Age: "))
Gender =input("Enter Gender(M/F): ").strip().upper()

# step 1: calculate base tax
if income <=500000:
    tax =0
elif income <=1000000:
    tax =(income-500000)*0.10
elif income <=2000000:
    tax =(500000*0.10)+(income-1000000)*0.20
else: 
    tax =(500000*0.10)+(1000000*0.20)+(income-2000000)*0.30
    
print("Tax before rebate: ₹",tax)
    # step 2: Aplly rebates
if Age >=60:
     rebate =tax*0.05 #5% rebate           
     tax -=rebate
     print("Senior Citizen Rebate: ₹", rebate)

if Gender ==  "F":
            rebate =tax*0.02 # 2% rebate
            tax -=rebate
            print("Women rebate: ₹",rebate)

print("Final tax Payable:₹",tax+rebate)

"""
 Sample Input
 Enter Annual Income: 1200000
 Enter Age:65
 Enter Gender(M/F):F

 Sample output
 Tax before rebate:₹ 2400000
"""
