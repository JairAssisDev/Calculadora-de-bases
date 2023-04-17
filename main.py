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
    x=str(input("coloque um numero: "))
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

#decimal para octal
def decPoctal():
    x=int(input("coloque um numero:"))

    lista=[]
    while x>0:
        a=x%8
        x=x//8
        lista.append(a)
    lista.reverse()
    resutado = ''.join(str(elemento) for elemento in lista)
    return resutado

#octal para decimal
def octalPdec():
    x=str(input("coloque um numero :"))
    lista=[]
    resutado=[]
    for caractere in x:
            lista.append(int(caractere))
    a=0
    for g in reversed(range(len(lista))):
        item=lista[a]
        a+=1
        y=8**g
        x=item*y
        resutado.append(x)
        
    resutado.reverse()
    return sum(resutado)

#decimal para binario
def decPbinario():
    x = int(input("Coloque um número :"))
    lista = []
    while x > 0:
        a = x % 2
        x = x // 2
        lista.append(a)
    lista.reverse()
    resultado = ''.join(str(elemento) for elemento in lista)
    resultado = '{:0>4}'.format(resultado) 
    return resultado

#binário para decimal
def binarioPdec():
    x=str(input("coloque um numero: "))
    lista=[]
    resutado=[]
    for caractere in x:
        if caractere.isdigit():
            lista.append(int(caractere))
    a=0
    for g in reversed(range(len(lista))):
        item=lista[a]
        a+=1
        y=2**g
        x=item*y
        resutado.append(x)
    
    resutado.reverse()
    return sum(resutado)
#decimal2 para octal
def decPoctal2(x):
    lista=[]
    while x>0:
        a=x%8
        x=x//8
        lista.append(a)
    lista.reverse()
    resutado = ''.join(str(elemento) for elemento in lista)
    return resutado
#Decimal para hexadecimal2
def decPhexa2(x):
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
#binario fraçao decimal
def binarioPdec2(x):
    lista=[]
    resutado=[]
    for caractere in x:
        if caractere.isdigit():
            lista.append(int(caractere))
    a=0
    for g in reversed(range(len(lista))):
        item=lista[a]
        a+=1
        y=2**g
        x=item*y
        resutado.append(x)
    
    resutado.reverse()
    return sum(resutado)
#decimal fração 
def decPbinario2(x):
    lista = []
    while x >0:
        a = x % 2
        x = x // 2
        lista.append(a)
    lista.reverse()
    resultado = ''.join(str(elemento) for elemento in lista)
    resultado = '{:0>4}'.format(resultado) 
    return resultado

while True:
    print("Escolha uma opção:")
    print("1. Decimal para binário")
    print("2. Decimal para octal")
    print("3. Decimal para hexadecimal")
    print("4. Binário para decimal")
    print("5. Octal para decimal")
    print("6. Hexadecimal para decimal")
    print("7. Binário para octal")
    print("8. Binário para hexadecimal")
    print("9. binario transformar para hexadecimal em fração")
    print("10. decimal fração transformar para binario fração")
    print("Sair")
    inputUser=str(input("Digite sua opção: "))
    if inputUser == "1":
        print("base 10 para transformar em binário")
        x=decPbinario()
        print("Seu resutado é ",x)
    elif inputUser=="2":
        print("base 10 para transformar base 8")
        x=decPoctal()
        print("Seu resutado é ",x)
    elif inputUser=="3":
        print("na base 10 para transformar em hexadecimal")
        x=decPhexa()
        print("Seu resutado é ",x)
    elif inputUser=="4":
        print("binário transformar para base 10")
        x=binarioPdec()
        print("Seu resutado é ",x)
    elif inputUser=="5":
        print("base 8 para transformar base 10")
        x=octalPdec()
        print("Seu resutado é ",x)
        
    elif inputUser=="6":
        print("hexadecimal transformar para base 10")
        resutado=hexaPdec()
        print("Seu resutado é ",x)
    elif inputUser=="7":
        print("binario transformar para base 8")
        x=binarioPdec()
        print("dasd",x)
        print("Seu resutado é ",decPoctal2(x))
    elif inputUser=="8":
        print("binario transformar para hexadecimal")
        x=binarioPdec()
        print("Seu resutado é ",decPhexa2(x))
    elif inputUser=="8":
        print("binario transformar para hexadecimal")
        x=binarioPdec()
        print("Seu resutado é ",decPhexa2(x))
    elif inputUser=="9":
        print("binario transformar para hexadecimal em fração")
        g=str(input("coloque um numero: "))
        separados = g.split(',')
        x=binarioPdec2(separados[0])
        y=binarioPdec2(separados[1])
        lista=[x,",",y]
        resutado = ''.join(str(elemento) for elemento in lista)
        print("Seu resutado é ",resutado)
    elif inputUser=="10":
        print("decimal fração transformar para binario fração")
        g=str(input("coloque um numero: "))
        separados = g.split(',')
        x=decPbinario2(int(separados[0]))
        y=decPbinario2(int(separados[1]))
        lista=[x,",",y]
        resutado = ''.join(str(elemento) for elemento in lista)
        print("Seu resutado é ",resutado)
    elif inputUser=="sair":
        print("Obrigado por participar S2 ")
        print('   _/﹋\_   ')
        print('   (҂`_´)   ')
        print('   <,︻╦╤─  ')
        print('  _/﹋\_    ')
        print(' SR.JAIR.ASSIS.DEV ')
        break