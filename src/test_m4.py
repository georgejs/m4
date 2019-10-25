"""
@Author George Shen
@Title test_m4
@Version 1
"""

"""
I did not cover all cases this I only wrote enough to show case that I know how to use unittest
"""


import unittest
import m4
import employee

class Test_M4(unittest.TestCase):
    """
    Unit Test for M4
    """

    def test_m4_add_new_employee(self):
        """
        Test case for method add_new_employee
        :return:
        """
        """
        Test proper Employee and Manager
        """
        self.assertIsInstance(m4.add_new_employee('name_new', leader=None, salary=0, type='e'), employee.Employee)
        self.assertIsInstance(m4.add_new_employee('name_new_manager', leader=None, salary=0, type='m'), employee.Manager)

        """
        Test Name case where Name is not defined
        """
        self.assertFalse(m4.add_new_employee(leader=None, salary=0, type='e'))
        self.assertFalse(m4.add_new_employee(leader=None, salary=0, type='m'))

        """
        Test Type is not e/m
        """
        self.assertFalse(m4.add_new_employee(leader=None, salary=0, type='x'))
        """
        
        Test if Salary is not not a float
        """
        self.assertFalse(m4.add_new_employee('name_new', salary='x'))

    def test_m4_Org_add_employee(self):
        """
        Test Org Class and Add Employee Function
        :return:
        """
        self.test_org = m4.Org()
        self.employee_type_e = employee.Employee('name_new', leader=None, salary=0)
        self.employee_type_m = employee.Manager('name_new', leader=None, salary=0)
        """
        Test if added to array correctly.
        """
        self.assertIsInstance(self.test_org.add_employee(self.employee_type_e), list)
        self.assertIsInstance(self.test_org.add_employee(self.employee_type_m), list)

        """
        Test to see if add employee only accepts type Employee or Manager
        """
        self.assertFalse(self.test_org.add_employee(None))
        self.assertFalse(self.test_org.add_employee(list()))
        self.assertFalse(self.test_org.add_employee(tuple()))
        self.assertFalse(self.test_org.add_employee(dict()))
        self.assertFalse(self.test_org.add_employee(str()))

if __name__ == '__main__':
    unittest.main()
