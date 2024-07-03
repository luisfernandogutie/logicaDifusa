#Implementación del Sistema de Calidad Vinícola Utilizando Lógica Difusa#

Introducción
Este documento describe la implementación de un sistema de evaluación de calidad vinícola utilizando lógica difusa. El sistema se ha desarrollado utilizando la librería scikit-fuzzy en Python, diseñado para determinar si un vino es de calidad buena, regular o mala en base a sus niveles de acidez y dulzura.

Arquitectura del Sistema
El sistema se estructura bajo una arquitectura de Sistema Experto (SE), que combina reglas de inferencia difusa con un motor de inferencia para determinar la calidad del vino. A continuación se detallan los componentes principales:

    1.	Base de Conocimiento:
      o	Se define una base de conocimiento que consiste en reglas difusas para evaluar la calidad del vino en base a los niveles de acidez y dulzura.
    2.	Motor de Inferencia:
      o	Utiliza el motor de inferencia de scikit-fuzzy para evaluar las reglas y calcular la calidad del vino en términos de "buena", "regular" o "mala".
    3.	Funciones de Membresía:
      o	Se definen funciones de membresía para las variables lingüísticas de acidez, dulzura y calidad del vino, estableciendo rangos difusos que representan los grados de pertenencia a cada categoría.
    4.	Reglas de Inferencia:
      o	Se establecen reglas difusas que especifican cómo las variables lingüísticas de entrada (acidez y dulzura) afectan a la variable de salida (calidad del vino). Ejemplo: "Si la acidez es alta y la dulzura es baja, entonces la calidad del vino es mala."

Implementación en Python con scikit-fuzzy 
 
Conclusión
Este sistema demuestra cómo la lógica difusa puede ser aplicada efectivamente para evaluar la calidad vinícola basada en criterios subjetivos como la acidez y la dulzura.
La implementación utiliza scikit-fuzzy para definir funciones de membresía, reglas de inferencia y calcular la calidad del vino,
reflejando un enfoque robusto basado en sistemas expertos difusos.
