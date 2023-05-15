# -*- coding: utf-8 -*-
"""

@author: sttep
"""

from typing import List, Dict

class CSP:
    def __init__(self, variables: List[str], domains: Dict[str, List[int]], constraints: List[str]):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

    def backtracking_search(self, assignment={}):
        # Si se han asignado todas las variables, se ha alcanzado una solución
        if len(assignment) == len(self.variables):
            return assignment

        # Selecciona la variable sin asignar con el dominio más reducido
        unassigned_vars = [var for var in self.variables if var not in assignment]
        selected_var = min(unassigned_vars, key=lambda var: len(self.domains[var]))

        # Intenta asignar un valor a la variable seleccionada
        for value in self.domains[selected_var]:
            consistent = True

            # Comprueba si la asignación es consistente con las restricciones
            for constraint in self.constraints:
                if selected_var in constraint and constraint not in assignment:
                    continue
                if not constraint_satisfied(constraint, assignment):
                    consistent = False
                    break

            # Si la asignación es consistente, continúa con la siguiente variable
            if consistent:
                assignment[selected_var] = value
                result = self.backtracking_search(assignment)
                if result is not None:
                    return result

            # Si la asignación no es consistente, deshace la asignación y prueba otro valor
            del assignment[selected_var]

        # Si no se puede encontrar una solución, devuelve None
        return None

def constraint_satisfied(constraint, assignment):
    # Comprueba si la asignación satisface una restricción dada
    x, y = constraint.split("<")
    if x not in assignment or y not in assignment:
        return True
    return assignment[x] < assignment[y]
