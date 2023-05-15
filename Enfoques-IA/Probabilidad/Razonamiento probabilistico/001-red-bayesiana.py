# -*- coding: utf-8 -*-
"""

@author: sttep
"""

from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD

# Crear la estructura de la red bayesiana
modelo = BayesianModel([('A', 'C'), ('B', 'C'), ('B', 'D'), ('C', 'E')])

# Definir las tablas de distribución de probabilidad condicional (CPDs)
cpd_A = TabularCPD(variable='A', variable_card=2, values=[[0.6, 0.4]])
cpd_B = TabularCPD(variable='B', variable_card=2, values=[[0.7, 0.3]])
cpd_C = TabularCPD(variable='C', variable_card=2, values=[[0.3, 0.9, 0.2, 0.8], [0.7, 0.1, 0.8, 0.2]],
                   evidence=['A', 'B'], evidence_card=[2, 2])
cpd_D = TabularCPD(variable='D', variable_card=2, values=[[0.8, 0.4], [0.2, 0.6]], evidence=['B'], evidence_card=[2])
cpd_E = TabularCPD(variable='E', variable_card=2, values=[[0.9, 0.3], [0.1, 0.7]], evidence=['C'], evidence_card=[2])

# Agregar los CPDs al modelo
modelo.add_cpds(cpd_A, cpd_B, cpd_C, cpd_D, cpd_E)

# Verificar si el modelo es válido
print("¿El modelo es válido?", modelo.check_model())

# Obtener la probabilidad conjunta de las variables
probabilidad_conjunta = modelo.get_independencies()

# Imprimir la probabilidad conjunta
print("Probabilidad conjunta:")
for independencia in probabilidad_conjunta:
    print(independencia)
