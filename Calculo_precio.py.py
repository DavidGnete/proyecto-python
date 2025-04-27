print("Calculando tu precio total de compra")
try:
 dato1=input("\n ingresa nombre del producto:").strip().lower() #pedimos el nombre del producto donde el usuario realizara su compra, utilizamos strip para eliminar espacios antes y despues, y usamos lower para asegurarnos de que todo este en minuscula
 precio=float(input("\n precio unitario:")) #pedimos el precio que figura en la  tienda, usando float para asegurar cualquier numero decimal
 cantidad=int(input("\n cantidad de productos elegido:")) #pedimos su cantidad en froma de int pues sera siempre una cantidad entera
 descuento=(input("\n porcentaje de descuento que se aplicara:"))  #pedimos su descuento
 descuento=descuento.replace("%","")# en caso que el usuario ingrese un "%" en el descuento lo removeremos para que no nos surja error
 descuento=float(descuento)#obtenemos el numero del descuento sin "%" 
 if precio <0 or cantidad <0 or descuento <0 or descuento >100:
     print("Hay un que dato esta mal ingresado por favor revise el enunciado y vuelva a ingresa correctamente los datos") #pondremos una condiciones donde no pueden haber numeros negativos, y el descuento debe estar en rango (0-100)
 precio_total=precio*cantidad #calculamos el precio total multiplicandolo por el numero de cantidad
 precio_descuento= round(precio_total* descuento /100)# calculamos como hacer el descuento
 precio_final=round(precio_total - precio_descuento, 2)# calculamos el final de la compra, con el descuento
 print(f"\nEl costo total de tu compra de {dato1} sin descuento es: {precio_total:.2f}")# mostramos al usuario su precio total sin aplicar descuento
 print(f"\nEl descuento del {descuento} % aplicado a el {dato1} es de: {precio_descuento:.2f}")#mostramos al usuario cuanto es el descuento de su producto en precio
 print(f"El costo final de tu compra es: {precio_final:.2f}")#le mostramos al usuario su precio final con el descuento de su producto.
except ValueError:
  print("Hay un dato que esta mal ingresado por favor revise el enunciado y vuelva a ingresa correctamente los datos")
  