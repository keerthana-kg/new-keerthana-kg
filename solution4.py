def union_set(set1,set2):
    return set1.union(set2)

def intersection(set1,set2):
    return set1.intersection(set2)

def diff_set(set1,set2):
    return set1-set2

def symmetric_diff(set1,set2):
    return set1.symmetric_diference(set2)

def subset(set1,set2):
    return set1.issubset(set2)

def superset(set1,set2):
    return set1.superset(set2)

def remove(set1,set2):
    result=set1.remove(set2)
    return result

def disjoint(set1,set2):
    return set1.isdisjoint(set2)

def clear_set(set1):
    return set1.clear()
