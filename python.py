a=16

if a>=18:
    print("You are eligible to vote")#to check if a person can vote 
else:
    print("You are not eligible to vote")

#a menu based program
while True:
    print("1.addition\n")
    print("2.subtraction\n")
    print("3.multiplication\n")
    print("4.division\n")
    print("5.floor division\n")
    print("6.exit\n")
    a=int(input("enter choice:"))
   
    if a==1:
        b=int(input("enter 1st number:"))
        c=int(input("enter 2nd number:"))
        print("addition is:",b+c)
    elif a==2:
        b=int(input("enter 1st number:"))
        c=int(input("enter 2nd number:"))
        print("subtraction is:",b-c)
    elif a==3:
        b=int(input("enter 1st number:"))
        c=int(input("enter 2nd number:"))
        print("multiplication is:",b*c)
    elif a==4:
        b=int(input("enter 1st number:"))
        c=int(input("enter 2nd number:"))
        print("division is:",b/c)
    elif a==5:
        b=int(input("enter 1st number:"))
        c=int(input("enter 2nd number:"))
        print("floor division is:",b//c)
    elif a==6:
        break
    else:
        print("invalid choice")
'''this code works only with integers but if we want to add char or string we can by changing b=int(input("enter 1st number:"))
        c=int(input("enter 2nd number:")) to b=(input("enter 1st number:"))
        c=(input("enter 2nd number:")) and we only add cant subtract multiply or divide'''



for i in range(1, 100):
    if i % 2 == 0:
        continue  # Skip even numbers, go to next iteration
    elif i == 25:
        break     # Exit the loop when i becomes 25
    else:
        pass      # Explicitly do nothing (dummy placeholder)

    # This block runs only for odd numbers before 25
    print(i)
'''this code returns all odd numbers till 100 but skips 25'''

  
