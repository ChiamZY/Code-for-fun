## Standard Chartered Bank Bonus$aver Calculator (Rates are accurate as of 20th August 2020)


## Average Daily Balance
def avg_daily_bal ():
    while True:
        try:
            balance = float(input("Please enter your estimated Bonus$aver average daily balance (Minimum 2000): $"))
            if balance >= 2000:
                break            
            else:
                print("Invalid amount, please enter at least 2000 dollars")
        except:
            print("Invalid entry")
                    
    return balance

## Card expenditure per month
def card_spend ():
    
    while True:
        try:
            spending = float(input("Please enter your estimated monthly card spending: $"))
            if spending < 500:
                card_interest = 0
                break
            elif spending in range(500, 2000):
                card_interest = 0.25
                break
            else:
                card_interest = 0.75
                break
        except:
            print("Invalid entry")
    
    return card_interest

## Salary credit per month
def salary_credit ():
    
    while True:
        try:
            salary = float(input("Please enter your monthly salary credit to the account: $"))
            if salary < 3000:
                sal_interest = 0
                break
            else:
                sal_interest = 0.4
                break
        except:
            print("Invalid entry")
    
    return sal_interest

## Investment
def investment ():
    
    while True:
        try:
            invest = input("Would you invest in eligible products? (Yes or No):")
            if invest.lower().startswith('y'):
                min_invest = input("Is your investment at least $30,000? (Yes or No):")
                if min_invest.lower().startswith('y'):
                    invest_interest = 0.85
                    break
                else:
                    invest_interest = 0
                    break
            elif invest.lower().startswith('n'):
                invest_interest = 0
                break
        except:
            print("Invalid entry")
    
    return invest_interest

## Insurance
def insurance ():
    
    while True:
        try:
            insure = input("Would you insure in eligible products? (Yes or No):")
            if insure.lower().startswith('y'):
                min_insure = input("Is your insurance at least $12,000? (Yes or No):")
                if min_insure.lower().startswith('y'):
                    insure_interest = 0.85
                    break
                else:
                    insure_interest = 0
                    break
            elif insure.lower().startswith('n'):
                insure_interest = 0
                break
        except:
            print("Invalid entry")
    
    return insure_interest

## Bill Payment
def bill_payment ():
    
    while True:
        try:
            bill_count = input("Would you make at least 3 bill payments online? (Yes or No):")
            if bill_count.lower().startswith('y'):
                bill_interest = 0.1
                break
            elif bill_count.lower().startswith('n'):
                bill_interest = 0
                break            
        except:
            print("Invalid entry")
    
    return bill_interest

## Main running code
def main ():
    ## Bonus interest is only for first $80,000
    ## After 80,000, interest is 0.05%
    
    balance = avg_daily_bal()
    card_interest = card_spend()
    sal_interest = salary_credit ()
    invest_interest = investment ()
    insure_interest = insurance()
    bill_interest = bill_payment ()
    
    base_interest = 0.05
    
    if balance <= 80000:
        bonus_interest_rate = card_interest + sal_interest + invest_interest + insure_interest + bill_interest
        annual_interest_rate = base_interest + bonus_interest_rate
        annual_interest = round((annual_interest_rate * balance)/100, None)
    else:
        excess = balance - 80000
        bonus_interest_rate = card_interest + sal_interest + invest_interest + insure_interest + bill_interest
        annual_interest_rate = base_interest + bonus_interest_rate
        annual_interest = round((annual_interest_rate*80000)/100 + (base_interest*excess)/100, None)
    
    print("Your estimated annual interest is ${} @ {}% p.a.".format(annual_interest, annual_interest_rate))
    return

#balance, card_interest, sal_interest, invest_interest, insure_interest, bill_interest





###########################
if __name__ == '__main__':
    main()
    
    
