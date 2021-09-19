class employee:
    no_of_employee=0
    raise_amount=1.04
    def __init__(self,first,second,pay):
        self.first=first
        self.second=second
        self.pay=pay
        self.email=first+'.'+second+'@gmail.com'
        employee.no_of_employee += 1
    def fullname(self):
        return '{} {}'.format(self.first,self.second)
    def raise_apply(self):
        self.pay=int(self.pay * employee.raise_amount)
#class developer(employee):
#   def __init__(self,first,second,pay):
@classmethod
def set_raise_amount(cls,amount):
    cls.raise_amount=amount
emp1=employee('Rishabh','soni',5000000)
emp2=employee('UMANG','BHALLA',6000000)
emp_str_1='john-doe-70000'
emp_str_2='steve-smith-30000'
emp_str_3='virat-kohli-50000'

first, last,pay=emp_str_1.split('-')
new_emp1=employee(first,last,pay)
print(new_emp1.email)
print(new_emp1.pay)
#print(emp1.email)
#print(emp2.email)
#emp1.raise_apply()
#print(emp1.raise_amount)
#employee.raise_amount=1.05
#emp1.raise_amount=2
#emp2.raise_apply()
#print(employee.__dict__)
#employee.set_raise_amount(3)
#print(employee.raise_amount)
#print(emp1.raise_amount)
#print(emp2.raise_amount)
#print(employee.no_of_employee)