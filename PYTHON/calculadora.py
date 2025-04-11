print('1. Suma')
print('2. Resta')
print('3. Multiplicacion')
print('4. Division')

ope=int(input('Elige una opcion: '))
# if ope>=1 and ope<=4:
#     num1=float(input('Introduce el primer numero: '))
#     num2=float(input('Introduce el segundo numero: '))
#     if ope==1:
#         print('La suma es:',num1+num2)
#     elif ope==2:
#         print('La resta es:',num1-num2)
#     elif ope==3:
#         print('La multiplicacion es:',num1*num2)
#     elif ope==4:
#         if num2!=0:
#             print('La division es:',num1/num2)
#         else:
#             print('No se puede dividir entre 0')
# else:
#     print('Opcion no valida')




if ope<=1 and ope>=4:
    print('Opcion no valida')
else:
    num1=float(input('Introduce el primer numero: '))
    num2=float(input('Introduce el segundo numero: '))
    if ope==1:
        print('La suma es:',num1+num2)
    elif ope==2:
        print('La resta es:',num1-num2)
    elif ope==3:
        print('La multiplicacion es:',num1*num2)
    elif ope==4:
        if num2!=0:
            print('La division es:',num1/num2)
        else:
            print('No se puede dividir entre 0')
