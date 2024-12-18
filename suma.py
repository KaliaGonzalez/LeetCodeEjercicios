def getSum( a: int, b: int) -> int: 
    lista = [] 
    lista.append(a) 
    lista.append(b) 
    resultado = sum(lista)
    return resultado 

if __name__ == "__main__":
    num1 = 1 
    num2 = 2
    print(getSum(num1,num2))