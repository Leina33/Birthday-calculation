import datetime

name = input("enter your name:")
age = input("enter your age:")

now = datetime.datetime.now()

diff = 80-int(age)

print("hi" + name + " You will complete 80 year in ",(now.year + diff))