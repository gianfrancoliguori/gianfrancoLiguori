def Ej1():

    x = 0
    while (x <= 30) :
        x+=1
        if (x == 4 or x== 6 or x == 10):
            print("The value ", x ," of x was skipped")
            continue
        if (x == 15):
            print("The execution of the loop was broken when x was" , x)
            break
        print('The value of the loop is: ' , x)
 
def Ej6():
    listNum = [8, 55, 25, 548, 456, 89, 55, 33, 78]
    
   
        
    numA = int(input("Ingrese un numero de 0 a 1000 para encontrar: "))
    
    for num in listNum :
        if num == numA :
            print(numA, "pertnece a la lista")
            break
    else:
        print(numA,"no pertenece a la lista")
  
def Ej5():
    for num in range(1, 21):
        if num % 2 != 0:
            continue
        else:
            print(num)
   
def Ej4():
    num1 = int(input("INGRESE UN AÑO: ")) 
    num2 = int(input("INGRESE OTRO AÑO: ")) 
    if num1 > num2:
        numHigher = num1
        numLess = num2
    else:
        numHigher = num2
        numLess = num1
        
    
    for year in range(numLess, numHigher):
        biciesto = False
        if year % 400 == 0:
            biciesto = True
        elif (year % 4 == 0 and year % 100 != 0):
            biciesto = True
        if (biciesto and year % 10 == 0 ):
            print(year, " es biciesto y es multiplo de 10")
    
def Ej3():
    num = 1
    primos = []
    while (num > 0):
        num = int(input("Ingrese un numero (Ingrese 0 para finalizar): "))
        for n in range(2,num):                        
            if (num % n == 0):
                    primos.pop(num)
                    break
                    
    print("La cantidad de numero primos fue: ",len(primos))

def Ej2():
    money = 0
    print("D - DEPOSITAR")
    print("R - RETIRAR")
    print("S - SABER SALARIO")
    print("X - FINALIZAR")

    while True :

        answer = input("QUE OPERACION DESEA REALIZAR? (D/R/S/X)")
        

        if answer.upper() == "D" :
            deposit = int(input("Cuanto desea ingresar?"))
            money += deposit
            print(f"Depositò ${deposit} // TOTAL: ${money}")
            deposit = 0

        elif answer.upper() == "R" :
            remove = int(input("Cuanto desea retirar?"))
            if remove>=money :
                remove = money
                money = 0
                print(f"retirò ${remove} // TOTAL: ${money}")
                remove = 0
            else : 
                money -= remove
                print(f"retirò ${remove} // TOTAL: ${money}")
                remove = 0
            

        elif answer.upper() == "S" :
            print(f"// TOTAL: ${money} //")

        elif answer.upper() == "X" :
            break

        else : 
            print("RESPUESTA INVALIDA")

def Ej1_1():

    while True:
        line = input("Ingrese una linea")
        counter = 0
        for letter in line :
            if letter == " ":
                counter += 1
            
        if (counter != len(line)):
            print(line.upper())
        else:
            break

Ej1_1()



    
