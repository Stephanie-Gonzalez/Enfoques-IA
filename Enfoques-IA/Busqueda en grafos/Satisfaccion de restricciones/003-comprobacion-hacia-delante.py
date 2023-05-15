# -*- coding: utf-8 -*-
"""

@author: sttep
"""

class ForwardChecking:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

    def forward_checking(self):
        assignment = {}
        return self.forward_check(assignment)

    def forward_check(self, assignment):
        if len(assignment) == len(self.variables):
            return assignment

        var = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(var, assignment):
            if self.is_assignment_consistent(var, value, assignment):
                assignment[var] = value
                pruned_domains = self.forward_check_update_domains(var, value, assignment)
                if pruned_domains:
                    result = self.forward_check(assignment)
                    if result is not None:
                        return result
                del assignment[var]
                self.restore_pruned_domains(pruned_domains)
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

    def forward_check_update_domains(self, var, value, assignment):
        pruned_domains = {}
        for constraint in self.constraints:
            if var in constraint:
                y = constraint[1]
                if y not in assignment:
                    if y not in pruned_domains:
                        pruned_domains[y] = []
                    pruned_values = []
                    for val in self.domains[y]:
                        if not self.is_consistent_assignment(var, value, y, val):
                            pruned_values.append(val)
                    pruned_domains[y] += pruned_values
                    self.domains[y] = [val for val in self.domains[y] if val not in pruned_values]
        return pruned_domains

    def is_consistent_assignment(self, var1, value1, var2, value2):
        for constraint in self.constraints:
            if (var1, var2) == constraint or (var2, var1) == constraint:
                if (value1, value2) not in constraint and (value2, value1) not in constraint:
                    return False
        return True

    def restore_pruned_domains(self, pruned_domains):
        for var, pruned_values in pruned_domains.items():
            self.domains[var] += pruned_values
