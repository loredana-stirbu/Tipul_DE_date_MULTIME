A=set(input("dati un sir A: "))
B=set(input("dati un sir B: "))
for i in A:
      if not (i.isalpha()):
        A=set(input("dati sirul A din nou deoarece nu sunt doar cifre: "))
for x in B:
      if not(x.isalpha):
        B=set(input("dati sirul B din nou deoarece nu sunt doar cifre: "))
print("Intersectia multimilor A si B:", A.intersection(B))
print("Reuniunia multimilor A si B:", A.union(B))
print("Diferenta multimilor A si B:", A.difference(B))
print("Diferenta multimilor B si A:", B.difference(A))