def multi(x):
    return x*x  
    def abc(x):
        return x
def add(x):
    return x+x
fun=[multi,add]
for i in range(10):
    print list(map(lambda x: x(i), fun))