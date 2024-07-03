from motor import crear_motor, ejecutar_motor

# Crear el motor de inferencia y obtener las variables difusas
sistema_calidad, acidez, dulzura, calidad = crear_motor()

# Solicitar datos al usuario
acidez_valor = float(input("Introduce el valor de acidez (entre 0 y 10): "))
dulzura_valor = float(input("Introduce el valor de dulzura (entre 0 y 10): "))

# Ejecutar el motor de inferencia con valores de entrada proporcionados por el usuario
ejecutar_motor(sistema_calidad, acidez, dulzura, calidad, acidez_valor, dulzura_valor)
