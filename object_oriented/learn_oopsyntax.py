class employee:
    raise_amount=1.04
    def __init__(self,first,second,pay):
        self.first=first
        self.second=second
        self.pay=pay
        self.email=first+'.'+second+'@gmail.com'
    def fullname(self):
        return '{} {}'.format(self.first,self.second)
emp1=employee('Rishabh','soni',5000000)
emp2=employee('UMANG','BHA LLA',6000000)

print(emp1.email)
print(emp2.email)
