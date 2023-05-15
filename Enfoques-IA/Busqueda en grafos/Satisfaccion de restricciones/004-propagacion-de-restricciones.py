# -*- coding: utf-8 -*-
"""

@author: sttep
"""

class ConstraintPropagation:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

    def constraint_propagation(self):
        queue = self.initialize_queue()

        while queue:
            (xi, xj) = queue.pop(0)

            if self.revise(xi, xj):
                if len(self.domains[xi]) == 0:
                    return None

                for xk in self.get_neighbors(xi):
                    if xk != xi:
                        queue.append((xk, xi))

        return self.domains

    def revise(self, xi, xj):
        revised = False

        for x in self.domains[xi]:
            if not self.has_support(x, xi, xj):
                self.domains[xi].remove(x)
                revised = True

        return revised

    def has_support(self, x, xi, xj):
        for y in self.domains[xj]:
            if self.is_consistent_assignment(x, xi, y, xj):
                return True

        return False

    def get_neighbors(self, var):
        neighbors = []
        for constraint in self.constraints:
            if var in constraint:
                for neighbor in constraint:
                    if neighbor != var:
                        neighbors.append(neighbor)
        return list(set(neighbors))

    def initialize_queue(self):
        queue = []
        for constraint in self.constraints:
            xi, xj = constraint
            queue.append((xi, xj))
            queue.append((xj, xi))
        return queue

    def is_consistent_assignment(self, value1, var1, value2, var2):
        for constraint in self.constraints:
            if (var1, var2) == constraint or (var2, var1) == constraint:
                if (value1, value2) not in constraint and (value2, value1) not in constraint:
                    return False
        return True
