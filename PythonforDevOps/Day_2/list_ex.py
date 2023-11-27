list_of_cloud_serv = list(["AWS","Azure","gcp"])

list_of_envs = ["dev","stg","prd","testing","qa"]
list_of_envs.append("client")
for i in list_of_envs:
    print("Deploying to")
    print(i)

#print(dir(list_of_envs))

a = 2
list_of_envs.insert(1,"testing")
print(list_of_envs)


print(a.denominator.__doc__)