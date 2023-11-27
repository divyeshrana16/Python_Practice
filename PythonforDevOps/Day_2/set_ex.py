set_1 = {1,11,1,2,3,4,34}
set_2 = {1,34,43,11,1,2,3,4}


print(set_1.intersection(set_2))

print(set_1.union(set_2))

list_of_env = ["dev","stg","prd","tst","qa","qa","dev"]
print(list_of_env)
list_of_env = list(set(list_of_env))
print(list_of_env)