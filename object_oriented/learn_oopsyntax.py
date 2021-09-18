class employee:
    raise_amount=1.04
    def __init__(self,first,second,pay):
        self.first=first
        self.second=second
        self.pay=pay
        self.email=first+'.'+second+'@gmail.com'
    def fullname(self):
        return '{} {}'.format(self.first,self.second)
    def raise_apply(self):
        self.pay=int(self.pay * 1.04)

#class developer(employee):
#   def.__init__(self,first,second,pay):
emp1=employee('Rishabh','soni',5000000)
emp2=employee('UMANG','BHALLA',6000000)

print(emp1.email)
print(emp2.email)
emp1.raise_apply()
emp2.raise_apply()
print(emp1.pay)
print(emp2.pay)