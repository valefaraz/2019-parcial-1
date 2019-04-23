class Notnumberexeption(Exception):
   pass

def interfaz_decimal_hexa(decimal):
    from parcial import decimal_a_hexa

    try:
        numero1=int(decimal)
        return decimal_a_hexa(numero1)

    except:
        return 'Disculpe, solo acepto numeros'   

    if not isinstance (decimal,int):
        return 'Disculpe, solo acepto numeros'

def main():
    decimal=input('Ingrese un numero decimal')
    print('su numero hexadecimal es')
    result=interfaz_decimal_hexa(decimal)
    print(result)
main()