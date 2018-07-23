

class Employee(object):
    def __init__(self, employee_info, mail):
        self.employee_info = employee_info
        self._mail = mail

    def __len__(self):
        return len(self._mail)

    def __getitem__(self, position):
        return self._mail[position]

    def __str__(self):
        return self.employee_info.name + ' : ' + self.employee_info.address
