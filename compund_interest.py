# Coding Challenge 1, compund_interest.py
#Name:Niraj Lamichhane
#Student No:NP03CS4S210145

#Compound Interest Calculator

"""
Requirements:
    You will develop a program to calculate compound interest.

    • Print a welcome message explaining the purpose of the program.
    • Prompt the user for the necessary inputs (see formulae and brief)
    • Convert input values to suitable data types.
    • Perform compound interest calculation using the forumlae provided.
    • Print the result to the terminal using appropriate formatting.
    
    • Your program should be as close as possible to the example shown in the assessment brief.

Constraints:
    • Ensure that the interest rate is entered as a percentage and not a decimal.
    • Ensure that all monetary values are formatted to two decimal places.

Hints:
    • Think about what data types are the most appropriate for each input value.
    • Order of operations will be important, make sure you use parenthesis.
    • Review lecture two for more information on string formatting.
    • Your programs output should be as close as possible to the example in the assessment brief.
"""

# TODO: Write your code here!
print("Welcome to the wolving compound interest.")
print("This program calculates your potential returns when you invest with us")

#code
P = int(input("Enter the principal amount:"))
r = float(input("Enter the annual rate of interest:"))
t = int(input("Enter the amount of years the amount is invested:"))
n = int(input("Enter the amount of times the interest is compounded per year:"))
print("Year     Period      Old Balance        Interest      New Balance")                                                          
# We can also use something like this print(f"{'Year'}{'Period':>14}{'Old Balance':>14}{'Interest':>14}{'New Balance':>15}") 
print("-"*70)
per=int(t*(n))                                       # total period
j=1                                                  # variable for the loop
nb=float                                             # defined new balance variable 
ob=float(P)                                          # defined old balance variable
i=r                                                  # current interest(changes inside the loop)
y=1                                                  # current year(changes inside the loop)
while (j <= per):                                    
    i=(((1/n)*r)*ob)/100
    nb=ob+i
    print(f"{y}{j:>14}{ob:>14.2f}{i:>14.2f}{nb:>15.2f}") #print function to display the data with proper spacing and formatting
    if(j%n == 0):                                    # 
        y=int(y+1)                                   # current year is counted based on the total years and the current period every 4 period(1/4 years) year increases
    ob=nb                                            
    j=j+1
A=nb                                                 # final amount
print("\n",P,"invested at %.2f"%r,"% for ",t," years, compounded ",n," times per year is: %.2f"%A)










