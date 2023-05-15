# -*- coding: utf-8 -*-
"""

@author: sttep
"""

class ConflictDirectedBacktracking:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

    def conflict_directed_backtracking(self):
        assignment = {}
        return self.backtrack(assignment)

    def backtrack(self, assignment):
        if len(assignment) == len(self.variables):
            return assignment

        var = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(var, assignment):
            if self.is_assignment_consistent(var, value, assignment):
                assignment[var] = value
                result = self.backtrack(assignment)
                if result is not None:
                    return result
                del assignment[var]
        return None

    def select_unassigned_variable(self, assignment):
        unassigned_variables = [v for v in self.variables if v not in assignment]
        return max(unassigned_variables, key=lambda v: self.conflict_score(v, assignment))

    def order_domain_values(self, var, assignment):
        return self.domains[var]

    def is_assignment_consistent(self, var, value, assignment):
        for constraint in self.constraints:
            if var in constraint:
                x, y = constraint
                if x in assignment and y in assignment:
                    if not self.constraint_satisfied(x, y, assignment[x], assignment[y]):
                        return False
        return True

    def conflict_score(self, var, assignment):
        score = 0
        for constraint in self.constraints:
            if var in constraint:
                x, y = constraint
                if x in assignment and y in assignment:
                    if not self.constraint_satisfied(x, y, assignment[x], assignment[y]):
                        score += 1
        return score

    def constraint_satisfied(self, x, y, value_x, value_y):
        # Verifica si una restricción se satisface
        # Implementa tu lógica de restricciones aquí
        return True
