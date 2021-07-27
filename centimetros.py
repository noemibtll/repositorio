valor = int ( input (" ingrese el valor en centimetros " ))
kilometro = 100000
metro = 100
residuok = 0
kilometros = 0
residuom = 0

#int es un tipo de dato numerico entero

#float es un tipo de dato numerico flotante ( con punto decimal )

#input es una funcion que permite la entrada de cualquier cosa por teclado
#una funcion siempre tiene un nombre que la define y unos parentesis, dentro de los parentesis
#se incerta los valores o argumentos con los que va a trabajar esa funcion 
#== este operador compara y verifica si dos variables son iguales 

if valor >= kilometro :
    residuok = valor % kilometro
    kilometros = valor // kilometro

# % este operador te devuelve el sobrante de una division    
    
if residuok >= 100 :
    residuom = residuok % metro 
    metros = residuok // metro

# //significa division entera sin punto decimal

print ( kilometros, " km ", metros, " m ", residuom, " cm " )





