def merge_dicts(dict1, dict2):
    
    merged_dict = {}

    
    for key in dict1:
        if key in merged_dict:
            merged_dict[key] += dict1[key]
        else:
            merged_dict[key] = dict1[key]


    for key in dict2:
        if key in merged_dict:
            merged_dict[key] += dict2[key]
        else:
            merged_dict[key] = dict2[key]

    return merged_dict


dict1 = {'a': 11, 'b': 26, 'c': 40}
dict2 = {'b': 65, 'c': 29, 'd': 70}

merged_result = merge_dicts(dict1, dict2)
print(merged_result)  