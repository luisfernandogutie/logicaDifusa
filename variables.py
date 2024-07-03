import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Definición de las variables difusas
def definir_variables():
    # Variables de entrada
    acidez = ctrl.Antecedent(np.arange(0, 11, 1), 'acidez')
    dulzura = ctrl.Antecedent(np.arange(0, 11, 1), 'dulzura')

    # Variable de salida
    calidad = ctrl.Consequent(np.arange(0, 11, 1), 'calidad')

    return acidez, dulzura, calidad
