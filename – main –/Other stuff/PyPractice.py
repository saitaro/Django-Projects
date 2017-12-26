import os

# __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# with open(os.path.join(__location__, 'test.txt')) as f:
#     data = f.read()
#     print(data[6])

# print(os.path.dirname(os.path.realpath(__file__)))

f = os.path.abspath('– main –\Other stuff/test.txt')

with open(f, 'r') as file:
    print(file.read())

print(os.getcwd())