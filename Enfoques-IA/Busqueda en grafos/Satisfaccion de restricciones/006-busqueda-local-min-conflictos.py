# -*- coding: utf-8 -*-
"""

@author: sttep
"""

import random

class MinimumConflicts:
    def __init__(self, variables, domains, constraints, max_steps=1000):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints
        self.max_steps = max_steps

    def minimum_conflicts(self, initial_assignment):
        assignment = initial_assignment

        for _ in range(self.max_steps):
            if self.is_solution(assignment):
                return assignment

            var = self.select_conflicted_variable(assignment)
            value = self.select_minimum_conflict_value(var, assignment)
            assignment[var] = value

        return None

    def is_solution(self, assignment):
        for constraint in self.constraints:
            x, y = constraint
            if not self.constraint_satisfied(x, y, assignment[x], assignment[y]):
                return False
        return True

    def select_conflicted_variable(self, assignment):
        conflicted_vars = []
        for constraint in self.constraints:
            x, y = constraint
            if not self.constraint_satisfied(x, y, assignment[x], assignment[y]):
                conflicted_vars.append(x)
                conflicted_vars.append(y)
        return random.choice(conflicted_vars)

    def select_minimum_conflict_value(self, var, assignment):
        min_conflicts = float('inf')
        min_value = None

        for value in self.domains[var]:
            conflicts = self.count_conflicts(var, value, assignment)
            if conflicts < min_conflicts:
                min_conflicts = conflicts
                min_value = value

        return min_value

    def count_conflicts(self, var, value, assignment):
        conflicts = 0
        for constraint in self.constraints:
            if var in constraint:
                x, y = constraint
                if x in assignment and y in assignment:
                    if not self.constraint_satisfied(x, y, assignment[x], assignment[y]):
                        conflicts += 1
                elif x == var:
                    if y in assignment and not self.constraint_satisfied(x, y, value, assignment[y]):
                        conflicts += 1
                elif y == var:
                    if x in assignment and not self.constraint_satisfied(x, y, assignment[x], value):
                        conflicts += 1
        return conflicts

    def constraint_satisfied(self, x, y, value_x, value_y):
        # Verifica si una restricción se satisface
        # Implementa tu lógica de restricciones aquí
        return True
