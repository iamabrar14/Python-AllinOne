"""
We can not slice set directly. If we want to slice a set, we have to convert the set into
a list. Cause set is unodered,unindexed data structure of python
"""
a={1,2,3,4,5,6,7,8,9}
a_list=list(a)
print(a_list[:4])