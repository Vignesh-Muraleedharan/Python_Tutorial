has_high_income = True
has_good_credit = False
#AND : Both conditions must be true
#OR : Atleast one condition must be true
#NOT : Inverts the boolean value
if has_high_income and has_good_credit:
    print("Eligible for loan")
elif has_high_income or has_good_credit:
    print("Eligible for loan but high interest rate")
else:
    print("Not eligible for loan")