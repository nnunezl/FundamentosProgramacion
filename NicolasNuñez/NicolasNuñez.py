#Autor: Nicolas Núñez / Sección: 01
import datetime

reclamadores = []

def registrarReclamos(reclamadores):
    rut = input("Ingrese su rut: ")
    monto = float(input("Ingresa monto: ")) 
    fecha = datetime.date.today() 
    reclamo = input("porfavor, escriba su reclamo: (20 caracteres)")
    reclamador = {'fecha': fecha, 'rut': rut, 'monto': monto, 'reclamo': reclamo}
    reclamadores.append(reclamador)

def listarReclamos():
    for reclamador in reclamadores:
        print(f"Fecha: {reclamador['fecha']}, Rut: {reclamador['rut']}, Monto: {reclamador['monto']}, Reclamo: {reclamador['reclamo']}")

def respaldarReclamos(reclamadores):
    with open('listaDeReclamos.txt', 'a') as f:
        for reclamador in reclamadores:
            f.write(f"Fecha: {reclamador['fecha']}\nRut: {reclamador['rut']}\nMonto: {reclamador['monto']}\nReclamo: {reclamador['reclamo']}\n\n")

def main():
    while True:
        try:
            opcion = int(input("""
            Bienvenido a menú
            1. Registrar Reclamos
            2. Listar Reclamos
            3. Respaldar Reclamos
            4. Salir
            """))
            if opcion == 1:
                registrarReclamos(reclamadores)
            elif opcion == 2:
                listarReclamos()
            elif opcion == 3:
                respaldarReclamos(reclamadores)
            elif opcion == 4:
                break
        except ValueError:
            print("Inválido, intenta nuevamente.")

if __name__ == "__main__":
    main()
