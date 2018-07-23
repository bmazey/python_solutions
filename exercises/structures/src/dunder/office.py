

class Office(object):
    def __init__(self, employees, boss=None):
        self.employees = employees
        self.boss = boss

    def __len__(self):
        return len(self.employees)

    def __getitem__(self, position):
        return self.employees[position]

    def __add__(self, employee):
        all_employees = self.employees + tuple(employee)
        return Office(all_employees, self.boss)

    def __repr__(self):
        return 'Office(%r, %r)' % (self.employees, self.boss)

    def __str__(self):
        return 'employees: {}'.format(
            str(self.employees)
        )
