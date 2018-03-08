"""
EXTRA NOTES!!!!(TESTING FUNCTIONS OF LOOP AND CALCULATIONS DURING FIRST FEW ATTEMPTS)
#ANDREW BUDIHARDJA
#THIS PROGRAM HELPS TO CALCULATE INTEREST,BALANCE AND RESULTS FOR LOANS AND SAVINGS ACCOUNT PER MONTH
"""

import math

def main():
    # Get input from user,L for loan,S for Savings
    Choice=str.upper(input("Please enter the account choice. Insert L for Loan. Insert S for Savings : "))
    # what happens if the input is not on the options
    while (Choice!='S') and (Choice!='L'):                                                              
        print("ERROR MESSAGE!>RE-INSERT WORD")
        Choice=str.upper(input("Please enter the account choice. Insert L for Loan. Insert S for Savings: "))
    if Choice=='S':                                                                                     
        print("THE CHOICE WAS SAVINGS!")
        Savings()
    else:                                                                                               
        print("THE CHOICE WAS LOAN!")
        Loan()

#calculate savings 
def Savings():                                                              
    months=int(input("Enter the number of months:"))
    #Input validation
    while (0>months) or (months>480):                                                           
        print("ERROR MESSAGE!>PLEASE RE-INSERT THE BALANCE!")
        months=int(input("Enter the number of months:"))
        
    
    annualinterest=float(input("Enter the interest rate in percentage(%):"))
    #input validation
    while (0>annualinterest) or (annualinterest>200):
        print("ERROR MESSAGE!>PLEASE RE-INSERT THE BALANCE!")
        annualinterest=float(input("Enter the interest rate in percentage(%):"))
        
    Balance=float(input("Enter the balance:$"))
    #input validation
    while (Balance<0) or (Balance>1000000000):
        print("ERROR MESSAGE!>PLEASE RE-INSERT THE BALANCE!")
        Balance=float(input("Enter the balance:$"))
    print('SAVINGS SCHEDULE:')    
        
    interestpermonth=annualinterest/months                                                      
                       
    for months in range(1,months+1,):
        print("Month:",months)                                                                  
            
        interestvalue=(interestpermonth/100)*Balance
        Balance=Balance+interestvalue
                                                                      
        print("Interest rate in percentage(%):",format(interestpermonth,".2f"),"Interest value:$",format(interestvalue,".2f"),"Balance:$",format(Balance,".2f")) #Display results in 2 decimals


#calculate loan
def Loan():
    #INPUT VALIDATION
    Balance=float(input("Enter the balance:$"))                                                 
    while (Balance<0) or (Balance>1000000000):
        print("ERROR MESSAGE!>PLEASE RE-INSERT THE BALANCE!")
        Balance=float(input("Enter the balance:$"))
    #INPUT VALIDATION
    annualinterest=float(input("Enter the interest rate(%):"))                                  
    while (0>annualinterest) or (annualinterest>200):
        print("ERROR MESSAGE!>PLEASE RE-INSERT THE BALANCE!")
        annualinterest=float(input("Enter the interest rate in percentage(%):"))
    #INPUT VALIDATION
    payment=float(input("Enter the annual payment per month:$"))                                
    while (0>payment) or (payment>100000000):
        print("ERROR MESSAGE!>PLEASE RE-INSERT THE BALANCE!")
        payment=float(input("Enter the annual payment per month:$"))
        
    monthv=0                                                                        
    interest=annualinterest/12
    print("LOAN SCHEDULE:")
    while Balance>0:
        monthv=monthv+1                                                             
        print("Month:",monthv)
        Balance=Balance-payment
        interestperpaymentvalue=(interest/100)*Balance
        Balance=Balance+interestperpaymentvalue
        #DISPLAY RESULTS IN 2 DECIMALS  
        print("Interest per month in percentage(%):",format(interest,".2f"),"Interest value:$",format(interestperpaymentvalue,".2f"),"Balance:$",format(Balance,".2f"))
    
main()                                                      

