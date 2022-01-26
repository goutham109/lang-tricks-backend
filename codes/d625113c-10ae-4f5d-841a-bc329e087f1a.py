def get_greater_element(a,b):
    if a > b :
        return a
    else :
        return b
    result = get_greater_element(*[4,9])
    print('The greater element in the list is',result)

    # Printing the elements without for loop.
      lst = [1,4,6,9]
      print(*lst)    # Output: 1 4 6 9
    