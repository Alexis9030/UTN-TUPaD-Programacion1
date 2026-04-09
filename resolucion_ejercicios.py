# Ejercicio 1

nombre = input("Ingrese el nombre del cliente: ")

while nombre == "" or not nombre.isalpha():
    print("Error: ingrese solo letras.")
    nombre = input("Ingrese el nombre del cliente: ")

cantidad = input("Ingrese la cantidad de productos a comprar: ")

while not cantidad.isdigit() or int(cantidad) <= 0:
    print("Error: ingrese un número entero mayor a 0.")
    cantidad = input("Ingrese la cantidad de productos a comprar: ")

cantidad = int(cantidad)

total_sin_descuentos = 0
total_con_descuentos = 0

for i in range(cantidad):
    precio = input(f"Ingrese el precio del producto {i + 1}: ")

    while not precio.isdigit():
        print("Error: ingrese un número entero.")
        precio = input(f"Ingrese el precio del producto {i + 1}: ")

    precio = int(precio)

    descuento = input("¿Tiene descuento? (S/N): ")

    while descuento.lower() != "s" and descuento.lower() != "n":
        print("Error: ingrese S o N.")
        descuento = input("¿Tiene descuento? (S/N): ")

    total_sin_descuentos += precio

    if descuento.lower() == "s":
        precio_final = precio - (precio * 0.10)
    else:
        precio_final = precio

    total_con_descuentos += precio_final

ahorro_total = total_sin_descuentos - total_con_descuentos
promedio = total_con_descuentos / cantidad

print()
print(f"Cliente: {nombre}")
print(f"Total sin descuentos: ${total_sin_descuentos}")
print(f"Total con descuentos: ${total_con_descuentos:.2f}")
print(f"Ahorro total: ${ahorro_total:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")


# Ejercicio 2 

usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0
acceso = False

while intentos < 3 and not acceso:
    usuario = input("Usuario: ")
    clave = input("Clave: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        acceso = True
        print("Acceso concedido.")
    else:
        intentos += 1
        print("Error: credenciales inválidas.")

if not acceso:
    print("Cuenta bloqueada.")
else:
    salir = False

    while not salir:
        print()
        print("1) Estado")
        print("2) Cambiar clave")
        print("3) Mensaje")
        print("4) Salir")

        opcion = input("Opción: ")

        while not opcion.isdigit():
            print("Error: ingrese un número válido.")
            opcion = input("Opción: ")

        opcion = int(opcion)

        while opcion < 1 or opcion > 4:
            print("Error: opción fuera de rango.")
            opcion = input("Opción: ")

            while not opcion.isdigit():
                print("Error: ingrese un número válido.")
                opcion = input("Opción: ")

            opcion = int(opcion)

        if opcion == 1:
            print("Inscripto")

        elif opcion == 2:
            nueva_clave = input("Nueva clave: ")

            if len(nueva_clave) < 6:
                print("Error: mínimo 6 caracteres.")
            else:
                confirmar = input("Confirmar clave: ")

                if nueva_clave == confirmar:
                    clave_correcta = nueva_clave
                    print("Clave cambiada correctamente.")
                else:
                    print("Error: las claves no coinciden.")

        elif opcion == 3:
            print("Seguí adelante, vas muy bien.")

        elif opcion == 4:
            print("Sesión finalizada.")
            salir = True

# Ejercicio 3

operador = input("Ingrese el nombre del operador: ")

while operador == "" or not operador.isalpha():
    print("Error: solo se permiten letras.")
    operador = input("Ingrese el nombre del operador: ")

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

cerrar = False

while not cerrar:
    print()
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")

    opcion = input("Seleccione una opción: ")

    while not opcion.isdigit():
        print("Error: ingrese un número.")
        opcion = input("Seleccione una opción: ")

    opcion = int(opcion)

    while opcion < 1 or opcion > 5:
        print("Error: opción inválida.")
        opcion = input("Seleccione una opción: ")

        while not opcion.isdigit():
            print("Error: ingrese un número.")
            opcion = input("Seleccione una opción: ")

        opcion = int(opcion)

    if opcion == 1:
        dia = input("Elegir día (1=Lunes, 2=Martes): ")

        while not dia.isdigit() or (dia != "1" and dia != "2"):
            print("Error: ingrese 1 o 2.")
            dia = input("Elegir día (1=Lunes, 2=Martes): ")

        paciente = input("Ingrese nombre del paciente: ")

        while paciente == "" or not paciente.isalpha():
            print("Error: solo letras.")
            paciente = input("Ingrese nombre del paciente: ")

        if dia == "1":
            if lunes1 == paciente or lunes2 == paciente or lunes3 == paciente or lunes4 == paciente:
                print("Error: paciente repetido en Lunes.")
            elif lunes1 == "":
                lunes1 = paciente
                print("Turno reservado en Lunes.")
            elif lunes2 == "":
                lunes2 = paciente
                print("Turno reservado en Lunes.")
            elif lunes3 == "":
                lunes3 = paciente
                print("Turno reservado en Lunes.")
            elif lunes4 == "":
                lunes4 = paciente
                print("Turno reservado en Lunes.")
            else:
                print("No hay cupos en Lunes.")

        else:
            if martes1 == paciente or martes2 == paciente or martes3 == paciente:
                print("Error: paciente repetido en Martes.")
            elif martes1 == "":
                martes1 = paciente
                print("Turno reservado en Martes.")
            elif martes2 == "":
                martes2 = paciente
                print("Turno reservado en Martes.")
            elif martes3 == "":
                martes3 = paciente
                print("Turno reservado en Martes.")
            else:
                print("No hay cupos en Martes.")

    elif opcion == 2:
        dia = input("Elegir día (1=Lunes, 2=Martes): ")

        while not dia.isdigit() or (dia != "1" and dia != "2"):
            print("Error: ingrese 1 o 2.")
            dia = input("Elegir día (1=Lunes, 2=Martes): ")

        paciente = input("Ingrese nombre del paciente a cancelar: ")

        while paciente == "" or not paciente.isalpha():
            print("Error: solo letras.")
            paciente = input("Ingrese nombre del paciente a cancelar: ")

        if dia == "1":
            if lunes1 == paciente:
                lunes1 = ""
                print("Turno cancelado.")
            elif lunes2 == paciente:
                lunes2 = ""
                print("Turno cancelado.")
            elif lunes3 == paciente:
                lunes3 = ""
                print("Turno cancelado.")
            elif lunes4 == paciente:
                lunes4 = ""
                print("Turno cancelado.")
            else:
                print("Paciente no encontrado en Lunes.")
        else:
            if martes1 == paciente:
                martes1 = ""
                print("Turno cancelado.")
            elif martes2 == paciente:
                martes2 = ""
                print("Turno cancelado.")
            elif martes3 == paciente:
                martes3 = ""
                print("Turno cancelado.")
            else:
                print("Paciente no encontrado en Martes.")

    elif opcion == 3:
        dia = input("Elegir día (1=Lunes, 2=Martes): ")

        while not dia.isdigit() or (dia != "1" and dia != "2"):
            print("Error: ingrese 1 o 2.")
            dia = input("Elegir día (1=Lunes, 2=Martes): ")

        if dia == "1":
            print("Agenda de Lunes:")
            print("Turno 1:", "libre" if lunes1 == "" else lunes1)
            print("Turno 2:", "libre" if lunes2 == "" else lunes2)
            print("Turno 3:", "libre" if lunes3 == "" else lunes3)
            print("Turno 4:", "libre" if lunes4 == "" else lunes4)
        else:
            print("Agenda de Martes:")
            print("Turno 1:", "libre" if martes1 == "" else martes1)
            print("Turno 2:", "libre" if martes2 == "" else martes2)
            print("Turno 3:", "libre" if martes3 == "" else martes3)

    elif opcion == 4:
        ocupados_lunes = 0
        ocupados_martes = 0

        if lunes1 != "":
            ocupados_lunes += 1
        if lunes2 != "":
            ocupados_lunes += 1
        if lunes3 != "":
            ocupados_lunes += 1
        if lunes4 != "":
            ocupados_lunes += 1

        if martes1 != "":
            ocupados_martes += 1
        if martes2 != "":
            ocupados_martes += 1
        if martes3 != "":
            ocupados_martes += 1

        disponibles_lunes = 4 - ocupados_lunes
        disponibles_martes = 3 - ocupados_martes

        print("Resumen general:")
        print(f"Lunes -> Ocupados: {ocupados_lunes} | Disponibles: {disponibles_lunes}")
        print(f"Martes -> Ocupados: {ocupados_martes} | Disponibles: {disponibles_martes}")

        if ocupados_lunes > ocupados_martes:
            print("Día con más turnos: Lunes")
        elif ocupados_martes > ocupados_lunes:
            print("Día con más turnos: Martes")
        else:
            print("Día con más turnos: Empate")

    elif opcion == 5:
        print("Sistema cerrado.")
        cerrar = True

# Ejercicio 4

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

agente = input("Ingrese el nombre del agente: ")

while agente == "" or not agente.isalpha():
    print("Error: solo se permiten letras.")
    agente = input("Ingrese el nombre del agente: ")

racha_forzar = 0
bloqueo = False

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not bloqueo:
    print()
    print("----- ESTADO -----")
    print(f"Agente: {agente}")
    print(f"Energía: {energia}")
    print(f"Tiempo: {tiempo}")
    print(f"Cerraduras abiertas: {cerraduras_abiertas}")
    print(f"Alarma: {alarma}")
    print(f"Código parcial: {codigo_parcial}")
    print("------------------")
    print("1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")

    opcion = input("Elija una opción: ")

    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        print("Error: ingrese 1, 2 o 3.")
        opcion = input("Elija una opción: ")

    opcion = int(opcion)

    if opcion == 1:
        energia -= 20
        tiempo -= 2
        racha_forzar += 1

        if racha_forzar == 3:
            alarma = True
            print("La cerradura se trabó. Se activó la alarma y no se abrió la cerradura.")
        else:
            if energia < 40:
                print("Hay riesgo de alarma.")
                riesgo = input("Elija un número del 1 al 3: ")

                while not riesgo.isdigit() or int(riesgo) < 1 or int(riesgo) > 3:
                    print("Error: ingrese un número del 1 al 3.")
                    riesgo = input("Elija un número del 1 al 3: ")

                if riesgo == "3":
                    alarma = True
                    print("Se activó la alarma.")

            if not alarma and cerraduras_abiertas < 3:
                cerraduras_abiertas += 1
                print("Abriste una cerradura.")

    elif opcion == 2:
        energia -= 10
        tiempo -= 3
        racha_forzar = 0

        print("Hackeando panel...")
        for i in range(4):
            codigo_parcial += "A"
            print(f"Paso {i + 1}/4 - Código parcial: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("Se abrió automáticamente una cerradura por hackeo.")

    elif opcion == 3:
        tiempo -= 1
        energia += 15

        if energia > 100:
            energia = 100

        if alarma:
            energia -= 10

        racha_forzar = 0
        print("Descansaste.")

    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        bloqueo = True

if cerraduras_abiertas == 3:
    print("VICTORIA")
elif bloqueo:
    print("DERROTA (bloqueo por alarma)")
else:
    print("DERROTA")

# Ejercicio 5

print("--- BIENVENIDO A LA ARENA ---")

nombre = input("Nombre del Gladiador: ")

while nombre == "" or not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")

vida_gladiador = 100          
vida_enemigo = 100            
pociones = 3                  
danio_base_pesado = 15        
danio_base_enemigo = 12       
turno_gladiador = True        

print("=== INICIO DEL COMBATE ===")

while vida_gladiador > 0 and vida_enemigo > 0:

    if turno_gladiador:
        print()
        print(f"{nombre} (HP: {vida_gladiador}) Vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
        print("Elige acción:")
        print("1. Ataque Pesado")
        print("2. Ráfaga Veloz")
        print("3. Curar")

        opcion = input("Opción: ")

        while not opcion.isdigit():
            print("Error: Ingrese un número válido.")
            opcion = input("Opción: ")

        while int(opcion) < 1 or int(opcion) > 3:
            print("Error: Ingrese un número válido.")
            opcion = input("Opción: ")
            while not opcion.isdigit():
                print("Error: Ingrese un número válido.")
                opcion = input("Opción: ")

        opcion = int(opcion)

        if opcion == 1:
            danio_final = danio_base_pesado

            if vida_enemigo < 20:
                danio_final = danio_base_pesado * 1.5  

            vida_enemigo = vida_enemigo - danio_final
            print(f"¡Atacaste al enemigo por {danio_final} puntos de daño!")

        elif opcion == 2:
            print(">> ¡Inicias una ráfaga de golpes!")
            for i in range(3):
                vida_enemigo = vida_enemigo - 5
                print(">> Golpe conectado por 5 de daño")

                if vida_enemigo <= 0:
                    break

        elif opcion == 3:
            if pociones > 0:
                vida_gladiador = vida_gladiador + 30
                pociones = pociones - 1

                if vida_gladiador > 100:
                    vida_gladiador = 100

                print(">> Usaste una poción y recuperaste 30 puntos de vida.")
            else:
                print("¡No quedan pociones!")

        if vida_enemigo > 0:
            vida_gladiador = vida_gladiador - danio_base_enemigo
            print(f"¡El enemigo te atacó por {danio_base_enemigo} puntos de daño!")

        print("=== NUEVO TURNO ===")

if vida_gladiador > 0:
    print(f"VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")