import random
b=random.randint(0,100)
print("Guess a number Between 0 to 100")
while True:
    n=int(input("Enter a Number:"))
    if (n < b):
        print( "Guess Higher")
    elif (n > b):
        print ("Guess Lower")
    else:
        print( f"You have guessed it correctly:{n}={b}") 
