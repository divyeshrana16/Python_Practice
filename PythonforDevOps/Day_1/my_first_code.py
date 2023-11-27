env=input("Enter the cloud platform: ")

if env == "aws" or env == "AWS":
    print("You are in AWS environment")
else:
    print("You are not in AWS but another Environment")