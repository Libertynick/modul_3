
data_structure =[

[1, 2, 3],

{'a': 4, 'b': 5},

(6, {'cube': 7, 'drum': 8}),

"Hello",

((), [{(2, 'Urban', ('Urban2', 35))}])

]


def calculate_structure_sum(data_structure):
    total_length = 0
    if isinstance(data_structure, str):
        total_length += len(data_structure)
    elif isinstance(data_structure, (list, tuple, set)):
        for i in data_structure:
            total_length += calculate_structure_sum(i)
    elif isinstance(data_structure, dict):
        for key, value in data_structure.items():
            total_length += calculate_structure_sum(key)
            total_length += calculate_structure_sum(value)
    elif isinstance(data_structure, (int, float)):
        total_length += data_structure
    return total_length

print(calculate_structure_sum(data_structure))



#dict = {'555': 'fdgdg', 'c': 6}
#for key in dict:
    #print(len(key))

#for values in dict.values():
    #print(len(str(values)))