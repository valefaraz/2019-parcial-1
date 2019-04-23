def decimal_a_hexa(numero1):

    if numero1 <= 9:
        resultado = str(numero1)

        return resultado
    

    if numero1 == 10:
        return 'A'
    if numero1 == 11:
        return 'B'
    if numero1 == 12:
        return 'C'
    if numero1 == 13:
        return 'D'
    if numero1 == 14:
        return 'E'
    if numero1 == 15:
        return 'F'

    div = numero1
    listaresto = []
    listadiv=[]
    listresultado=[]
    i=0
    resultado = ''
    while div >=16 :

        div1 = div / 16
        resto = div % 16
        listaresto.append(resto)
        listadiv.append(div1)
        listresultado.append=(listaresto[::-1])

    for number in listresultado:
        if number == 10:
            listresultado[i] = 'A'
        if number == 11:
            listresultado[i] = 'B'
        if number == 12:
            listresultado[i] = 'C'
        if number == 13:
            listresultado[i] = 'D'
        if number == 14:
            listresultado[i] = 'E'
        if number == 15:
            listresultado[i] = 'F'
        
        resultado=resultado+listresultado[i]

        i+=1
    return resultado