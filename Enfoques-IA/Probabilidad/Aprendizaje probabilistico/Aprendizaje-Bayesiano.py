# -*- coding: utf-8 -*-
"""

@author: sttep
"""

import pymc3 as pm
import numpy as np

# Datos observados
observed_data = np.array([0, 1, 0, 0, 1, 1, 1, 0, 1, 1])

# Modelo bayesiano
with pm.Model() as model:
    # Priori
    p = pm.Beta('p', alpha=1, beta=1)

    # Verosimilitud
    likelihood = pm.Bernoulli('likelihood', p=p, observed=observed_data)

    # Muestreo de la distribución posterior
    trace = pm.sample(2000, tune=1000, cores=1)  # Puedes ajustar los parámetros según tus necesidades

# Análisis de resultados
pm.plot_posterior(trace)

# Estimación de la probabilidad posterior
posterior_probability = np.mean(trace['p'] > 0.5)
print("Probabilidad posterior p > 0.5:", posterior_probability)
