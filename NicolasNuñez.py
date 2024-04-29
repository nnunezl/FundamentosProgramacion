#Autor Nicolas Nuñez / Seccion 01

pikachu_roll = 0
otaku_roll = 0
pulpo_venoso = 0
anguila_electrica = 0
descuento_otaku = 0
Descuento = "soyotaku"
total = 0

menu = int(input( "Bienvenido, presione 1 para continuar: " ))

while menu != 5:
    menu = int(input("""
    1) Pikchu Roll = $4500
    2) Otaku Roll = $5000
    3) Pulpo Venoso = $5200
    4) Anguila Electrica = $4800
    5) Para pagar.               
"""))
    
    if menu == 1:
        pikachu_roll = pikachu_roll + 1
    elif menu == 2:
        otaku_roll = otaku_roll +1
    elif menu == 3:
        pulpo_venoso = pulpo_venoso + 1
    elif menu == 4:
        anguila_electrica = anguila_electrica + 1
    
    total_productos = pikachu_roll+otaku_roll+pulpo_venoso+anguila_electrica
    total = (pikachu_roll*4500) + (otaku_roll*5000) + (pulpo_venoso*5200) + (anguila_electrica*4800)


descuento = str(input("Ingrese codigo de descuento: (Si no tiene presione x) ")).lower
if descuento == "soyotaku":
    descuento_otaku = total*0.1
    total = total - descuento_otaku
else:
    print("Pago sin codigo")    

print("total de productos ",total_productos,"\nPikachu roll : ",pikachu_roll,"\nOtaku Roll: ", otaku_roll,"\nPulpo Venoso: ", pulpo_venoso,"\nAnguila Electrica: ",anguila_electrica,"\nDescuento otaku: ",descuento_otaku,"\nTotal a pagar: ",total,)



