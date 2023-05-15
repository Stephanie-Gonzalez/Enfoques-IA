# -*- coding: utf-8 -*-
"""

@author: sttep
"""

class Backtracking:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

    def backtracking_search(self):
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
        for var in self.variables:
            if var not in assignment:
                return var

    def order_domain_values(self, var, assignment):
        return self.domains[var]

    def is_assignment_consistent(self, var, value, assignment):
        for constraint in self.constraints:
            if var in constraint:
                x, y = constraint
                if x in assignment and y in assignment:
                    if assignment[x] == value and assignment[y] == assignment[x]:
                        return False
        return True
