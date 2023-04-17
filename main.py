#Decimal para hexadecimal
def decPhexa():
    x=int(input("coloque um numero na base 10 para transformar em hexadecimal:"))
    lista=[]
    while x>0:
        a=x%16
        x=x//16
        if a<=9:
            lista.append(a)
        elif a==10:
            lista.append("a")
        elif a==11:
            lista.append("b")
        elif a==12:
            lista.append("c")
        elif a==13:
            lista.append("d")
        elif a==14:
            lista.append("e")
        elif a==15:
            lista.append("f")
    lista.reverse()
    resutado = ''.join(str(elemento) for elemento in lista)
    return resutado

#hexa para decimal
def hexaPdec():
    x=str(input("coloque um numero em hexadecimal transformar para base 10:"))
    lista=[]
    resutado=[]
    for caractere in x:
        if caractere.isdigit():
            lista.append(int(caractere))
        else:
            lista.append(caractere)
    for i in range(len(lista)):
        if lista[i] in ["a", "A"]:
            lista[i] = 10
        elif lista[i] in ["b", "B"]:
            lista[i] = 11
        elif lista[i] in ["c", "C"]:
            lista[i] = 12
        elif lista[i] in ["d", "D"]:
            lista[i] = 13
        elif lista[i] in ["e", "E"]:
            lista[i] = 14
        elif lista[i] in ["f", "F"]:
            lista[i] = 15
    a=0
    for g in reversed(range(len(lista))):
        item=lista[a]
        a+=1
        y=16**g
        x=item*y
        resutado.append(x)
    return sum(resutado)