cloud_env = ["aws","azure","gcp"]

try:
    print(cloud_env[2])
    raise Exception("This is a new Exception")
except:
    print("exception handled")
finally:
    print("i will execute anyways")


print("This code should run")

try:
    print(cloud_env[4])
    a=10
    b=0
    c=a/b
except ZeroDivisionError as e:
    print("1",e)
except IndexError as e:
    print("2",e)
