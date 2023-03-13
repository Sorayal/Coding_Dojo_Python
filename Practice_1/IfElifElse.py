A= 50
B= 60

str = "{} ist die größere Zahl."


if A > B:
    print(str.format(A))
elif A < B:
    print(str.format(B))
else:
    print("Beide Zahlen sind gleich.")