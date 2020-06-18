'''
Generate all permutations of a set
Permutation is an arrangement of objects in a specific order. Order of arrangement of object is very important. 
The number of permutations on a set of n elements is given by  n!.  
Example
2! = 2*1 = 2 permutations of {1, 2}, namely {1, 2} and {2, 1}
3! = 3*2*1 = 6 permutations of {1, 2, 3}, namely {1, 2, 3}, {1, 3, 2}, {2, 1, 3}, {2, 3, 1}, {3, 1, 2} and {3, 2, 1}.
'''

# one by one extract all elements, place them at first position and them recur on the remaining list
def permutation(lst):
    
    # base cases
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return lst
    
    # permutations for 1st if there are more than 1 characters
    l = []  #list to hold permutations

    for i in range(len(lst)):
        m = lst[i]

        #extract m from the list, and permute with the remaining list
        remList = lst[:i] + lst[i+1:]

        #generate all permutations where m is the first element
        for p in permutation(remList):
            l.append([m] + p)
    
    return l
