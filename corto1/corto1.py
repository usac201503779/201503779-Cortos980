#file=open(collatz.txt,w)
#Se crea una lista
lista=[]
#Creo la funcion corto que ejecutara el codigo de collatz
def corto(collatz):

    #El codigo se ejecuta siempre y cuando no sea 1
    while collatz !=1:
        #si es par se divide en dos
        if collatz%2==0:
            lista.append(collatz)
            print("%d," % (collatz), end="")
            collatz = collatz/2
        #Si no es par se multiplica por 3 y se le suma 1
        else:
            print("%d," % (collatz), end="") 
            collatz=(collatz*3)+1
            lista.append(collatz)

        #Si es uno se imprime el uno y se termina 
        if collatz == 1:
            lista.append("1")
            print("1")
            
#Creo un ciclo para que se ejecute desde el 2 hasta mi numero de carnet
#mi numero de carnet es 779 asi que le sumo uno para que llegue hasta 779
for i in range(2,780):
    corto(i)
    #print (lista[35])

                    