"""
@Author George Shen
@Title employee
@Version 1
"""

class Employee():
    def __init__(self, name, leader=None, salary=0):
        """
        Establish new employee
        :param name: Str - Name of new employee
        :param leader: Str - Name of new employee's leader
        :param salary: Float - Amount earned per year
        """
        self.name = name
        self.leader = leader
        self.salary = salary


class Manager():
    def __init__(self, name, leader=None, salary=0):
        """
        Establish new manager
        :param name: Str - Name of new manager
        :param leader: Str - Name of new manager's leader
        :param salary: Float - Amount earned per year
        """
        self.name = name
        self.leader = leader
        self.salary = salary
        self.subordinate = []

    def add_subordinate(self, name):
        """
        Add new subordinate to manager
        :param name: Name of employee
        :return: Boolean
        """
        self.subordinate.append(name)
        self.subordinate = sorted(self.subordinate)
        return True

    def remove_subordinate(self, name):
        """
        Remove subordinate from manager
        :param name:
        :return: Boolean
        """
        pass

