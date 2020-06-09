collatz= int(input("Ingresa un numero: "))

while collatz !=1:
    if collatz%2==0:
        print("%d," % (collatz), end="")
        collatz = collatz/2
    else:
        print("%d," % (collatz), end="") 
        collatz=(collatz*3)+1

    if collatz == 1:
            print("1")      