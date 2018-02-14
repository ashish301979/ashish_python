import sys

"""
* Complete the function below.
* DO NOT MODIFY CODE OUTSIDE THIS FUNCTION!
"""
def balancedOrNot(expressions, maxReplacements):
    new_return=[]
    def element(A,B):
        Z=A.replace('<>','')
        for i in Z:
            if (i=='<' or i=='>') and B>0:
                Z=Z.replace(i,'<>',1)
                B-=1
                Z=Z.replace('<>','')
        if len(Z)>0:
            new_return.append(0)
        else:
            new_return.append(1)
    for l,m in enumerate(expressions):
        element(m,maxReplacements[l])
    return new_return
