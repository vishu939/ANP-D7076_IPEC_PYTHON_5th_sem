'''problem password Strength'''
while True:
#--- input from the user--- 
 password = input("Enter the password:")
 if len(password) <8:
     print("password short")
 else:
     print("password Accepted:")