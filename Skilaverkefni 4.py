

def error_check(shares):
    shares=input("Enter number of shares: ") 
    try: 
        shares = int(shares)
        return (shares)
    except ValueError:
        print("Invalid numbers!") 
        shares=input("Enter number of shares: ") 
        shares = int(shares)
        return (shares)

def error_check_price(dollars, n, d):
    dollars, n, d=input("Enter price (dollars, numerator, denominator): ").split()
    try:
        dollars = int(dollars)
        n=int(n)
        d=int(d)
        return(dollars, n, d)
    except ValueError:
        print("Invalid price!")
        dollars, n, d=input("Enter price (dollars, numerator, denominator): ").split()
        dollars = int(dollars)
        n=int(n)
        d=int(d)
        return(dollars, n, d)



        
shares = 1
dollars=0
n=0
d=0

while shares > 0: 
    shares = error_check(shares)
    dollars, n, d = error_check_price(dollars, n, d)
    fraction=n/d
    whole_price = fraction+dollars
    value_price = whole_price * shares
    print(shares,"shares with market price",dollars,"{}/{}".format(n,d),"have value", "${}".format(value_price))
    Continue = input("Continue: ")
    if Continue != "y":
        break 

             