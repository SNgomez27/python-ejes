""""vas a capturar el de nombre de una y el sueldo bruto que va a cobrar  debes calcular el sueldo neto de dicha persona.
Se le descuenta como irpf un 12% y en concepto de Seguridad Social 5,28 mostrar un mensaje "el sueldo neto de xx es de xx """


nombre = input("introduzca su nombre")
sueldo = int(input("introduzca su sueldo"))
descuentoIrpf = sueldo * 0.12
descuentoSS = sueldo * 0.0528
descuentoTotal= descuentoIrpf + descuentoSS
SueldoNeto = sueldo - descuentoTotal

print("el sueldo neto de", nombre, "es de ", SueldoNeto)




"""Modifica el ejercicio anterior  modificando que el suelo de la persona es positivo . debes indicar el final del proceso,
caunto dinero recauda el estado en concepto de irpfy de ss, por separado. y cuanto paga la empresa en total 
y la lista de suldo netos con los nombres de los trabahadores """

