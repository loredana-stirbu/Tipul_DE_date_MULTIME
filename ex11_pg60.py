from itertools import combinations

s = {"A", "B", "C", "D"}

def submultimi(n):
    combinatii=[]
    for i in range(len(n)+1):
        combinatii.append(list(combinations(n,i)))
    return combinatii

s_submultimi=submultimi(s)
for i, n in enumerate(s_submultimi):
        print("Toate seturile de lungimea:",i)
        print(n)