def sort_by_age(list_of_tuples):
    return sorted(list_of_tuples, key=lambda x: x[1])


people = [("Ali", 20), ("abdalla", 19), ("jama", 18)]
sorted_people = sort_by_age(people)
print(sorted_people)   
