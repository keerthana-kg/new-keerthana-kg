def find_max(lst):
    return max(lst)

def find_sum(lst):
    return sum(lst)

def average(lst):
    return sum(lst)/len(lst)

def append_element(lst,num):
    lst.append(num)
    return lst

def reverse(lst):
    return lst[::-1]

def sort(lst):
    return sorted(lst)

def remove_element(lst,num):
    if num in lst:
        lst.remove(num)
    return lst    

def count_occurence(lst,element):
    return lst.count(element)

def find_index(lst,element):
    return lst.index(element)
