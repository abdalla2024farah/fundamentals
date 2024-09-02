def sort_by_age(list_of_tuples):

    return sorted(list_of_tuples, key=lambda x: x[1])


person1 = input('name :')
person2 =input('name :')
sorted_people = sort_by_age(people)
print(sorted_people)  
