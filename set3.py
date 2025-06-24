x={1,2}
y={1,2,3,4}
print(x.issubset(y))
print(y.issuperset(x))
print(x.isdisjoint(y))
""" This will generate subset and superset
if elements are common, it will print (true)
in disjoint: Returns True if two sets have no elements in common.
"""