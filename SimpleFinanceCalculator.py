



#EXTRA NOTES!!!!(TESTING FUNCTIONS OF LOOP AND CALCULATIONS DURING FIRST FEW ATTEMPTS)
#for months in range(1,months+1,):
#firstmonthinterestrate=Interestrate/months
#interestvalue=(firstmonthinterestrate/100)*Balance
#interestrate=(interestvalue/Balance)*100
#Balance=((interestrate+100)/100)*Balance
#print("interest rate:",interestrate,"interestvalue:",interestvalue,"Balance:",Balance)
#addtional notes/functions

#firstmonthinterestrate=Interestrate/100/months
#firstmonthinterestvalue=(firstmonthinterestrate/100/months)*Balance
#Balance=((firstmonthinterestrate+100)/100)*Balance
#print("interest rate:",firstmonthinterestrate,"int value:",firstmonthinterestvalue,"final balance:",Balance)

#interestvalue=(firstmonthinterestrate/100)*Balance
#interestrate=(interestvalue/Balance)*100
#Balance=((interestrate+100)/100)*Balance
#print("2nd interest rate:",interestrate,"2nd interest value:",interestvalue,"2nd Balance:",Balance)
#END OF EXTRA NOTES!!!!(TESTING FUNCTIONS OF LOOP AND CALCULATIONS DURING FIRST FEW ATTEMPTS)



#ANDREW BUDIHARDJA
#THIS PROGRAM HELPS TO CALCULATE INTEREST,BALANCE AND RESULTS FOR LOANS AND SAVINGS ACCOUNT PER MONTH

import math

def main():
    
    Choice=str.upper(input("Please enter the account choice. Insert L for Loan. Insert S for Savings : ")) # Get input from user,L for loan,S for Savings
    while (Choice!='S') and (Choice!='L'):                                                              # what happens if the input is not on the options
        print("ERROR MESSAGE!>RE-INSERT WORD")
        Choice=str.upper(input("Please enter the account choice. Insert L for Loan. Insert S for Savings: "))
    if Choice=='S':                                                                                     #the user inputs S
        print("THE CHOICE WAS SAVINGS!")
        Savings()
    else:                                                                                               #the user inputs L
        print("THE CHOICE WAS LOAN!")
        Loan()
    
def Savings():                                                              
    
    months=int(input("Enter the number of months:"))
    while (0>months) or (months>480):                                                           #Input validation
        print("ERROR MESSAGE!>PLEASE RE-INSERT THE BALANCE!")
        months=int(input("Enter the number of months:"))
        
    
    annualinterest=float(input("Enter the interest rate in percentage(%):"))                    #input validation
    while (0>annualinterest) or (annualinterest>200):
        print("ERROR MESSAGE!>PLEASE RE-INSERT THE BALANCE!")
        annualinterest=float(input("Enter the interest rate in percentage(%):"))
        
    Balance=float(input("Enter the balance:$"))                                                 #input validation
    while (Balance<0) or (Balance>1000000000):
        print("ERROR MESSAGE!>PLEASE RE-INSERT THE BALANCE!")
        Balance=float(input("Enter the balance:$"))
    print('SAVINGS SCHEDULE:')    
        
    interestpermonth=annualinterest/months                                                      
                       
    for months in range(1,months+1,):
    
        print("Month:",months)                                                                  #display month per loop
            
        interestvalue=(interestpermonth/100)*Balance
        Balance=Balance+interestvalue
                                                                      
        print("Interest rate in percentage(%):",format(interestpermonth,".2f"),"Interest value:$",format(interestvalue,".2f"),"Balance:$",format(Balance,".2f")) #Display results in 2 decimals



def Loan():
    
    Balance=float(input("Enter the balance:$"))                                                 #INPUT VALIDATION
    while (Balance<0) or (Balance>1000000000):
        print("ERROR MESSAGE!>PLEASE RE-INSERT THE BALANCE!")
        Balance=float(input("Enter the balance:$"))
        
    annualinterest=float(input("Enter the interest rate(%):"))                                  #INPUT VALIDATION
    while (0>annualinterest) or (annualinterest>200):
        print("ERROR MESSAGE!>PLEASE RE-INSERT THE BALANCE!")
        annualinterest=float(input("Enter the interest rate in percentage(%):"))
        
    payment=float(input("Enter the annual payment per month:$"))                                #INPUT VALIDATION
    while (0>payment) or (payment>100000000):
        print("ERROR MESSAGE!>PLEASE RE-INSERT THE BALANCE!")
        payment=float(input("Enter the annual payment per month:$"))
        
    monthv=0                                                                         # NEW VARIABLE TO HELP DISPLAY MONTH PER LOOP
    interest=annualinterest/12

    print("LOAN SCHEDULE:")
    while Balance>0:
            monthv=monthv+1                                                             #DISPLAY MONTH PER LOOP
            print("Month:",monthv)

            Balance=Balance-payment
            interestperpaymentvalue=(interest/100)*Balance
            Balance=Balance+interestperpaymentvalue
            
            print("Interest per month in percentage(%):",format(interest,".2f"),"Interest value:$",format(interestperpaymentvalue,".2f"),"Balance:$",format(Balance,".2f")) #DISPLAY RESULTS IN 2 DECIMALS  
    
main()                                                      #CALLS THE MAIN FUNCTION


