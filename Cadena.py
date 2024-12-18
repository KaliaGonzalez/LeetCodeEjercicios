def multiply( num1: str, num2: str) -> str: 
    numero1 = int (num1) 
    numero2 = int (num2) 
    multiplicacion = numero2*numero1 
    cadena = str(multiplicacion) 
    return cadena

if __name__ == "__main__":
    num1= "123" 
    num2= "456" 
    
    print(multiply(num1,num2))     
    