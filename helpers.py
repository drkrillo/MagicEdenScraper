

def divide_chunks_by_type(l, type=int):
    """
    Makes chunks from list based on type.

    E.g.: 
    input: [1, 'a', 'b','c', 3, '4','6','d']
    output: [[1,'a', 'b','c'], [3,'4','6','d']]
    """
    type_indexes= []
    for i in range(len(l)):
        if isinstance(l[i], int) == True:
            type_indexes.append(i)
    for pos in range(len(type_indexes)):
        if pos == len(type_indexes) - 1:
            yield l[type_indexes[pos]:]
        else:
            yield l[type_indexes[pos]:type_indexes[pos+1]]
        
        
def divide_chunks(l, n):

    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]