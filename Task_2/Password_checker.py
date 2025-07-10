import string

N=input("Enter you password:").strip()
while True:
    if len(N) >=14:
        print("Your Password has met required length Proceeding⏭️")
        lower = upper = digit = spl = False
        for A in N:
            if A.islower():
                lower=True
            elif A.isupper():
                upper=True
            elif A.isdigit():
                digit=True
            elif A in string.punctuation:
                spl=True
        a=[lower,upper,digit,spl]
        if all(a):
            print("Your Password is Strong")
        elif upper==False:
            print("Upper Case is Missing")
        elif lower==False:
            print("Lower Case is Missing")
        elif digit==False:
            print("Digit Case is Missing")
        elif spl==False:
            print("Special Character is Missing")
        break
    else:
        print("A password must have atleast 14 characters to be good")

