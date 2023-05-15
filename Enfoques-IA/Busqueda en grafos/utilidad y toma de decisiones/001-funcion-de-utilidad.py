# -*- coding: utf-8 -*-
"""

@author: sttep
"""

class UtilityTheory:
    def __init__(self, variables, domains, utility_function):
        self.variables = variables
        self.domains = domains
        self.utility_function = utility_function

    def maximize_utility(self):
        best_assignment = None
        max_utility = float('-inf')

        for assignment in self.generate_assignments():
            utility = self.calculate_utility(assignment)
            if utility > max_utility:
                max_utility = utility
                best_assignment = assignment

        return best_assignment

    def generate_assignments(self):
        assignments = []
        self.generate_assignments_helper({}, assignments)
        return assignments

    def generate_assignments_helper(self, assignment, assignments):
        if len(assignment) == len(self.variables):
            assignments.append(assignment)
            return

        var = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(var, assignment):
            assignment[var] = value
            self.generate_assignments_helper(assignment, assignments)
            del assignment[var]

    def select_unassigned_variable(self, assignment):
        for var in self.variables:
            if var not in assignment:
                return var

    def order_domain_values(self, var, assignment):
        return self.domains[var]

    def calculate_utility(self, assignment):
        return self.utility_function(assignment)

def utility_function(assignment):
    # Implementa tu función de utilidad aquí
    # Calcula y devuelve la utilidad basada en la asignación
    return 0.0
