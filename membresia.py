import skfuzzy as fuzz

def definir_membresia(acidez, dulzura, calidad):
    # Funciones de membresía para la acidez
    acidez['baja'] = fuzz.trimf(acidez.universe, [0, 2.5, 5])
    acidez['media'] = fuzz.trimf(acidez.universe, [2.5, 5, 7.5])
    acidez['alta'] = fuzz.trimf(acidez.universe, [5, 7.5, 10])

    # Funciones de membresía para la dulzura
    dulzura['baja'] = fuzz.trimf(dulzura.universe, [0, 2.5, 5])
    dulzura['media'] = fuzz.trimf(dulzura.universe, [2.5, 5, 7.5])
    dulzura['alta'] = fuzz.trimf(dulzura.universe, [5, 7.5, 10])

    # Funciones de membresía para la calidad
    calidad['mala'] = fuzz.trimf(calidad.universe, [0, 2.5, 5])
    calidad['regular'] = fuzz.trimf(calidad.universe, [2.5, 5, 7.5])
    calidad['buena'] = fuzz.trimf(calidad.universe, [5, 7.5, 10])

    return acidez, dulzura, calidad