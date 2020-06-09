lista=[]
def corto(collatz):

    while collatz !=1:
        if collatz%2==0:
            #lista[].append(collatz)
            print("%d," % (collatz), end="")
            collatz = collatz/2
        else:
            print("%d," % (collatz), end="") 
            collatz=(collatz*3)+1

        if collatz == 1:
            print("1")
            
for i in range(2,779):
    corto(i)
    #print lista[0]

                    