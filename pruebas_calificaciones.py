#semana 2: entrenamiento, pedir calificaciones, resultados, promedio,comparaciones.

# Uso de varibales en ingles como lo especifico el leader

# PARTE 1: Pedir calificaciones 
count = 0                                                                                 #usamos count como conteo para que valla contando las veces que el usuario pone el valor
accumulator = 0                                                                           #creamos una varible vacia llamada acumulator para que mas adelante podamos acumalar la suma de calificaciones y nos sriva para sacar el promedio
grades = []                                                                               #creamos la variable lista, para guardar las notas ingresadas
grades_count = int(input("Ingresa cuántas calificaciones numéricas quieres ingresar: "))  #creamos la varibale conteo de lista, para ingresar cuantas calificaciones va a ingresar el usuario 

for count in range(grades_count):                                                         #bucle for para hacer el ciclo del conteo en las lista de notas ingresadas por el usuario
    while True:                                                                           #el bucle while es necesario para generar condicion dentro del bucle for y poder generar si la condicion cumple con aprobo o reprobo segun el numero especificado
        try:                                                                              #hacemos un try para asegurarnos de que el usuario ingrese el numero dentro del rango 100 o para que no ingrese letras
            numero1 = float(input(f"Ingrese la calificación #{count + 1} si es mayor a 60 aprobo, si es menor o gual a 60, reprobo ")) #pedimos la nota de la calificacion
            if 0 <= numero1 <= 100:                                                      #generamos la condicion de que el numero debe estar dentro del rango 100 
                break                                                                    #si esta dentro del rango terminamos 
            else: 
                print("La calificación debe estar entre 0 y 100.")                       #si no esta dentro del imprimimos el error, y la condicion
        except ValueError:
            print("Entrada inválida.")                                                   #si ingresa un numero invalido o ingresa letras, le indicamos que esta invalido

    if numero1 <=60:                                                                    # generamos la condicion de que si el numero es menor a 60 imprima "Reprobo"
        print("Reprobo")
    else:
        print("Aprobo")                                                                 #generamos la condicion si el numero es mayor a 60 imprima "aprobo"
    grades.append(numero1)                                                              #cada vez que el bucle haga una vuelta, se acumulara 1 valor en la varibale grades, esto para saber cuantos numeros hay

accumulator = sum(grades)                                                               #en la variable acumulator usamos la funcion sum para sumar la lista 
average = accumulator / len(grades)                                      #creamos la variable average para calcular el promedio que es la suma dividido la cantidad de numeros con la funcion len
roun_d=round(average)                                                    #redondeamos el numero del promedio con la funcion round
print(f"La lista de tus calificaciones es: {grades}")                    #imprimimos la variable grades donde esta acumulada la lista de los numeros ingresados
print(f"El promedio de tus calificaciones es: {roun_d}")                               #imprimimos la variable average para mostrar el promedio 
 
# PARTE 2: Ingresar lista separada por comas
list = input("Ahora ingresa una lista de calificaciones separadas por comas: ")        #ahora pedimos lista de numeros separados por "," al usuario
split_value = list.split(",")                                                           #creamos la varible split_value y usamos la funcion split para separar los numeros con comas dentro de la variable
change_number = []                                                                      #cramos variable para acumular la lista de numeros
for i in split_value:                                                                   #usamos un bucle for para recorrer los numeros ingresados
    try:                                                                                #usamos un try dentro del bucle para evitar cualquier error
        num = float(i)                                                                  #creamos la variable num para convertir numeros ingresados a float dentro del bucle
        if 0 <= num <= 100:                                                             #pondremos la condicion de que debe estar en un rango de 0 - 100                                                                                  
            change_number.append(num)                                                   #si esta dentro del rango se agregara a la lista change_number
        else:
            print(f"La calificación {num} está fuera de rango (0-100) y será ignorada.") #de lo contrario se imprimira que no esta dentro del rango 
    except ValueError:
        print(f"'{i}' no es un número válido.")                                        #si imprime una letra o numero invalido mostrara error          

if len(change_number) == 0:                                                            #ya que en nuestra lista change_number deben estar todos los numeros ingresados con la funcion len calculamos la cantidad dentro de la lista
    print("No se ingresaron calificaciones válidas.")                                # si dentro de la lista solo hay 0 imprimimos calificacion invalida
else:
    sum_total = sum(change_number)                                                   #sumamos con la funcion sum los numeros dentro de la lista change_number
    len_total = len(change_number)                                                   #calculamos la cantidad de elementos con la funcion len
    average2 = sum_total / len_total                                                 #calculamos el promedio dividiendo la suma por la cantidad
    round_number = round(average2)                                                   #redondeamos el numero  con un round
    print(f"El promedio total de tu lista de números es: {round_number}")            #imprimimos el promedio total 

    # PARTE 3: Contar calificaciones mayores a un valor
    comparacion_value = float(input("¿Qué valor específico quieres comparar?: "))  #preguntamos al usuario un valor especifico para comparar
    counter = 0                                                                   #iniciamos un contador para hacer el ciclo while
    max_counter = 0                                                             #creamos una variable que lleve el numero mayor
    min_counter = 0                                                             #creamos otra variable que lleve numero menor
    while counter < len(change_number):                                           #creamos ciclo while que haga el ciclo con el contador
        number_now = change_number[counter]                                    #creamos variable que compare los numeros ingresados por la lista que el usuario ingreso antes
        if number_now > comparacion_value:                                      #ponemos la condicion para comparar el valor
            print(f"El número {number_now} es mayor que {comparacion_value}")   #imprimimos la condicion y la comparacion 
            max_counter += 1                                                    #creamos el contador que va contando el numero de vueltas dentro del while si es mayor
        else:
            print(f"El número {number_now} es menor o igual que {comparacion_value}") #hacemos otra comparacion con menor o igual a el numero ingresado
            min_counter += 1                                                    #creamos el contador que va contando el numero de vueltas dentro del while si es menor
        counter += 1                                                              #el contador que hay dentro del ciclo while
    print(f"Cantidad de números mayores: {max_counter}")                      #imprimimos el total de numeros mayores
    print(f"Cantidad de números menores o iguales: {min_counter}")             #imprimimos el total de numeros iguales o menores

    # PARTE 4: Verificar calificación específica
    especific_grade = float(input("Ingresa la calificación específica que quieres buscar: ")) #pedimos los datos de la cantidad especifica al usuario
    total_count = 0                                                                     #creamos un conteo para saber si ecuentra la calificacion ingresada dentro del while
    for score in change_number:                                             #creamos el bucle for y una variable para que haga el recorrido dentro de la lista creada antes
        if score != especific_grade:                               #ponemos la condicion de que si el numero no es igual al numero ingresado antes..
            continue                                                              #que continue con el ciclo hacia abajo
        total_count += 1                                                                # si si es igual generamos un conteo
        break                                                                      #cuando encuentre al menos una coincidencia rompemos el ciclo con break
    if total_count > 0:                                               
        print(f"La calificación {especific_grade} aparece {total_count} veces en la lista.") #si conteo es mayor a 0, si encontro una coincidencia imprime las veces que lo encontro
    else:
        print(f"La calificación {especific_grade} no está en la lista.")                 #si no lo encontro imprimira que no esta en la lista
