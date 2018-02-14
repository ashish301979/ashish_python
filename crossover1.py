import sys

"""
* Complete the function below.
* DO NOT MODIFY CODE OUTSIDE THIS FUNCTION!
"""
def twins(a, b):
    aa =  list(zip(a,b))
    res = []
    for i in aa:
        x1 = i[0] 
        y1 = i[1] 
        x2 = []
        x3 = []
        y2 = []
        y3 = []
        if len(x1) == len(y1):
            for i in range(len(x1)):
                if i % 2 == 0:
                    x2.append(x1[i])
                    y2.append(y1[i])
                else:
                    x3.append(x1[i])
                    y3.append(y1[i])
            z2 = set(x2)
            w2 = set(y2)
            z3 = set(x3)
            w3 = set(y3)
            if z2 == w2 and z3== w3:
              res.append("Yes")
            else:
              res.append("No")
        else:
            res.append("No")
    return res

"""
* DO NOT MODIFY CODE BELOW THIS POINT!
"""
def main():
    data = sys.stdin.readlines()
    
    pos = 0

    a = []
    b = []

    for a_i in range(pos + 1, int(data[pos]) + 1):
        a.append(data[a_i])

    pos = len(a) + 1

    for b_i in range(pos + 1, int(data[pos]) + pos + 1):
        b.append(data[b_i])
    
    result = twins(a, b)
    
    for val in result:
        print(val)

main()
