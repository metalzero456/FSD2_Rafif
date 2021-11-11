def my_generator():
    print("Inside my generator")
    yield 'a'
    yield 'b'
    yield 'c'

my_generator()

for char in my_generator():
    print(char)