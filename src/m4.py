"""
@George Shen
@Title m4
@Version 1
"""

import employee

class Org():
    """
    Establish Organization Object
    """
    def __init__(self, org_name='M4'):
        self.org_name = org_name
        self.org_tree = []
        self.total_sal = 0

    def add_employee(self, employee_new):
        if isinstance(employee_new, employee.Employee) or isinstance(employee_new, employee.Manager):
            self.org_tree.append(employee_new)
        else:
            return False

        return self.org_tree

    def print_org(self):
        """
        Print Organization Chart and Total Salary of Company.
        :return: None
        """
        self.level = 0
        self.current_leader = [None]

        print(self.org_name+"\n")
        for person in self.org_tree:

            if type(person) is employee.Manager:
                self.current_leader.append(person.name)
                self.level = self.current_leader.index(person.leader)
                print("{space}{name}\n{space}Employees of {name}".format(name=person.name, space= "  "*self.level))
                self.total_sal += person.salary

            elif type(person) is employee.Employee:
                self.level = self.current_leader.index(person.leader)
                print("{space}{name}".format(name=person.name, space="  "*self.level))
                self.total_sal += person.salary

            else:
                pass

        print("Total Salary: {total_salary}".format(total_salary=self.total_sal))

    def sort_org(self):
        """
        Extra Credit Sort
        :return:
        """

        # To return a new list, use the sorted() built-in function.
        self.org_sorted = sorted(self.org_tree, key=lambda x: x.name, reverse=False)
        for person in self.org_sorted:
            print(person.name)
        return self.org_sorted

def add_new_employee(name=None, leader=None, salary=0, type='e'):
    if name == None:
        return False
    elif isinstance(salary, float) or isinstance(salary, int):
        if type == 'e':
            new_emp = employee.Employee(name, leader, salary)
            employee.Manager(new_emp.leader).add_subordinate(new_emp.name)
        elif type == 'm':
            new_emp = employee.Manager(name, leader, salary)
        else:
            return False
    else:
        return False

    return new_emp

def run_test():
    comp = Org('comp')

    test_employees = [
                {'name' : 'Jeff', 'leader' : None, 'salary' : 120000, 'type' : 'm'},
                {'name' : 'Dave', 'leader' : 'Jeff', 'salary' : 125000, 'type' : 'm'},
                {'name' : 'Andy', 'leader' : 'Dave', 'salary' : 130000, 'type' : 'e'},
                {'name' : 'Dan', 'leader' : 'Dave', 'salary' : 115000, 'type' : 'e'},
                {'name' : 'Jason', 'leader' : 'Dave', 'salary' : 111000, 'type' : 'e'},
                {'name' : 'Rick', 'leader' : 'Dave', 'salary' : 125000, 'type' : 'e'},
                {'name' : 'Suzanne', 'leader' : 'Dave', 'salary' : 118000, 'type' : 'e'},
                {'name' : 'George', 'leader' : 'Jeff', 'salary' : 150000, 'type' : 'e'}
                  ]

    for new_person in test_employees:
        new_emp = add_new_employee(name = new_person.get('name'), leader = new_person.get('leader') ,
                                   salary = new_person.get('salary') , type = new_person.get('type'))
        comp.add_employee(new_emp)



    comp.print_org()

    comp.sort_org()
if __name__ == "__main__":
    run_test()