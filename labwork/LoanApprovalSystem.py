Credit_Score = float(input("Enter Credit Score:"))
Annual_Income = float(input("Enter Annual Income:"))
Existinng_Loan_Amount = float(input("Enter Existing Loan Amount:"))
#conditions
cond1 =Credit_Score >=750
cond2=Annual_Income >= 800000
cond3= Existinng_Loan_Amount <=200000
#Count how many conditions failed
failed_conditions= []
if not cond1:
    failed_conditions.append("credit Score criteria not satisfied.")
if not cond2:
     failed_conditions.append("Income criteria not satisfied.")
if not cond3:
      failed_conditions.append(" Existing Loan criteria not satisfied.")

#Decision
if len(failed_conditions)==0:
     print("Loan Status: Approved")
elif len(failed_conditions)==1:
     print("Loan Status:Manual Review")
     print("Reason:",failed_conditions[0])
else:
     print("Loan Status: Rejected")
     print("Reasons:")
     for reason in failed_conditions:
          print("-",reason)


