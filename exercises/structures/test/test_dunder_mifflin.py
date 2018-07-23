from collections import namedtuple
from exercises.structures.src.dunder.office import Office
from exercises.structures.src.dunder.employee import Employee
from exercises.structures.src.dunder.employee_info import EmployeeInfo


Email = namedtuple('Email', 'sender recipient message replies')


def test_office():
    jim = Employee(EmployeeInfo('Jim Halpert', 'jim.halpert@dundermifflin.com'), generate_jim_mail())
    dwight = Employee(EmployeeInfo('Dwight Shrute', 'dwight.shrute@dundermifflin.com'), generate_dwight_mail())
    michael = Employee(EmployeeInfo('Michael Scott', 'michael.scott@dundermifflin.com'), generate_michael_mail())
    pam = Employee(EmployeeInfo('Pamela Beesly', 'pam.beesly@dundermifflin.com'), generate_pam_mail())

    employees = (jim, dwight)

    office = Office(employees, michael)
    assert len(office) == 2
    assert office[1].employee_info.name == dwight.employee_info.name

    # assert that jim's first mail is sent to pam
    assert office[0][0].recipient == pam.employee_info.address

    office = office + pam
    assert len(office) == 3

    # implement generate_pam_mail() below with a valid tuple!
    assert office[2].sender == 'pam.beesly@dundermifflin.com'

    assert office.boss.employee_info.name == michael.employee_info.name


def generate_pam_mail():

    # TODO - implement this method with a valid tuple!

    mail = (
        Email('pam.beesly@dundermifflin.com', 'dwight.shrute@dundermifflin.com', 'funny interaction', 0),
    )

    return mail


def generate_jim_mail():

    mail = (
        Email('jim.halpert@dundermifflin.com', 'pam.beesly@dundermifflin.com', 'dinner tonight?', 1),
        Email('pam.beesly@dundermifflin.com', 'jim.halpert@dundermifflin.com', 'sure why not', 1),
        Email('jim.halpert@dundermifflin.com', 'pam.beesly@dundermifflin.com', 'it\'s a date!', 0)
    )

    return mail


def generate_dwight_mail():

    mail = (
        Email('dwight.shrute@dundermifflin.com', 'michael.scott@dundermifflin.com', 'funny interaction', 2),
        Email('michael.scott@dundermifflin.com', 'dwight.shrute@dundermifflin.com', 'other interaction', 1)
    )

    return mail


def generate_michael_mail():

    mail = (
        Email('michael.scott@dundermifflin.com', 'jim.halpert@dundermifflin.com', 'funny interaction', 0),
    )

    return mail
