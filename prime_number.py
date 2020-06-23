lower=int(input("Enter starting number"))
higher=int(input("Enter ending number"))
for number in range(lower,higher+1):
    if number>1:
        for i in range(2,number):
            if(number%i==0):
                break;
        else:
            print(number, "is a prime number")
else:
    print(number,"is not a prime number")
    
