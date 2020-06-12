'''
Standard binary search algorithm
1. Sort the list
2. Start with a middle number: is it bigger or smaller than our target number?
Since our list is sorted, the target is either on the left or right sides
3. We divided the problem by half
4. Repeat the same approach on the new half-size problem.
'''

def binary_search(target, nums) -> bool:
    floor_index = -1
    ceiling_index = len(nums)

    # if there isn't at least 1 index between floor and ceiling,
    # we ran out of guesses and the number must not be present
    while floor_index + < ceiling_index:
        # find the index halfway between the floor and ceiling
        