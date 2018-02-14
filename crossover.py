import sys
"""
* Complete the function below.
* DO NOT MODIFY CODE OUTSIDE THIS FUNCTION!
"""
def rearrange(elements):
    new=[]
    value=[]
    for i in elements:
        new.append((i,bin(i)[2:].count('1')))
    for i in sorted(sorted(new), key=lambda x: x[1]):
        value.append(i[0])
    return value


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
