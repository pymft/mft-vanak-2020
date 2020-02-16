# empty dictionary
me_dic = {}
# dictionary with integer keys
me_dic = {1: 'apple', 2: 'ball'}
# dictionary with mixed keys
me_dic = {'name': 'John', 1: [2, 4, 3]}
# using dict()
me_dic = dict({1: 'apple', 2: 'ball'})
# from sequence having each item as a pair
me_dic = dict([(1, 'apple'), (2, 'ball')])
print(me_dic)


my_dict = {'name':'Jack', 'age': 26}

# update value
my_dict['age'] = 27

#Output: {'age': 27, 'name': 'Jack'}
print(my_dict)

# add item
my_dict['address'] = 'Downtown'

# Output: {'address': 'Downtown', 'age': 27, 'name': 'Jack'}
print(my_dict)