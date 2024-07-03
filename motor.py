from variables import definir_variables
from membresia import definir_membresia
from reglas import definir_reglas
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

def crear_motor():
    # Definir las variables
    acidez, dulzura, calidad = definir_variables()

    # Definir las funciones de membresía
    acidez, dulzura, calidad = definir_membresia(acidez, dulzura, calidad)

    # Definir las reglas difusas
    reglas = definir_reglas(acidez, dulzura, calidad)

    # Crear el sistema de control difuso
    control_calidad = ctrl.ControlSystem(reglas)
    sistema_calidad = ctrl.ControlSystemSimulation(control_calidad)

    return sistema_calidad, acidez, dulzura, calidad  # Devolver también las variables difusas

def ejecutar_motor(sistema_calidad, acidez, dulzura, calidad, acidez_valor, dulzura_valor):
    # Entrada de datos
    sistema_calidad.input['acidez'] = acidez_valor
    sistema_calidad.input['dulzura'] = dulzura_valor

    # Realizar el cálculo
    sistema_calidad.compute()

    # Salida
    print(f"Calidad del vino: {sistema_calidad.output['calidad']}")

    # Visualización de las funciones de membresía y resultado
    acidez.view(sim=sistema_calidad)
    plt.show()
    
    dulzura.view(sim=sistema_calidad)
    plt.show()
    
    calidad.view(sim=sistema_calidad)
    plt.show()
