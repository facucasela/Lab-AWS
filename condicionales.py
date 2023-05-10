edad = int(input("Ingrese su edad: "))

if edad < 4:
    print("Usted puede ingresar gratis.")
elif 18 > edad >= 4:
    print("Usted debe pagar 5 euros.")
elif edad > 18:
    print("Usted debe pagar 10 euros.")