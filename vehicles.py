class ve:
	c=0
	def __int__(self, value):
		self.v=value
		ve.c+=1
	def getval(self):
		return self.value
	def getcount(cls):
		return ve.c
	counter = classmethod(getcount)
v1=('car')
v2=('bus')
v3=('bike')
type1=ve(v1)
type1=ve(v2)
type1=ve(v3)

print type1.getval(), type2.getval(), ve.counter(), type2.getcount()


