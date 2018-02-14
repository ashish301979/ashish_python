import sys

"""
* Complete the function below.
* DO NOT MODIFY CODE OUTSIDE THIS FUNCTION!
"""
def rearrange(elements):
    a=[(bin(x).count('1'),x) for x in elements]
    b=sorted(a)
    final,temp=[],[]
    for i in range(b[-1][0]+1):
        for j in b:
            if i == j[0]:
                temp.append(j[1])
        final.extend(sorted(temp))
        temp=[]
    return final    

"""
* DO NOT MODIFY CODE BELOW THIS POINT!
"""
def main():
    data = sys.stdin.readlines()
    
    elements = []

    for i in range(1, int(data[0]) + 1):
        elements.append(int(data[i]))

    result = rearrange(elements)
    
    for val in result:
        print(val)

main()
