import skfuzzy as fuzz
from skfuzzy import control as ctrl

def definir_reglas(acidez, dulzura, calidad):
    reglas = []

    # Reglas difusas
    regla1 = ctrl.Rule(acidez['baja'] & dulzura['alta'], calidad['buena'])
    regla2 = ctrl.Rule(acidez['media'] & dulzura['media'], calidad['regular'])
    regla3 = ctrl.Rule(acidez['alta'] & dulzura['baja'], calidad['mala'])
    
    regla4 = ctrl.Rule(acidez['baja'] & dulzura['media'], calidad['regular'])
    regla5 = ctrl.Rule(acidez['media'] & dulzura['alta'], calidad['buena'])
    regla6 = ctrl.Rule(acidez['alta'] & dulzura['alta'], calidad['buena'])
    
    regla7 = ctrl.Rule(acidez['baja'] & dulzura['baja'], calidad['mala'])
    regla8 = ctrl.Rule(acidez['media'] & dulzura['baja'], calidad['mala'])
    regla9 = ctrl.Rule(acidez['alta'] & dulzura['media'], calidad['regular'])
    
    regla10 = ctrl.Rule(acidez['baja'] & dulzura['alta'], calidad['buena'])
    regla11 = ctrl.Rule(acidez['media'] & dulzura['baja'], calidad['mala'])
    regla12 = ctrl.Rule(acidez['alta'] & dulzura['media'], calidad['regular'])

    reglas.extend([regla1, regla2, regla3, regla4, regla5, regla6, regla7, regla8, regla9, regla10, regla11, regla12])

    return reglas
