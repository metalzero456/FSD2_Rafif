#1 Membandingkan integer
x = 3
y = 5

if x < y:
    print('x less than y')
else:
    print('x is greater than y')

#2 Membandingkan apakah string ada di dalam string lainnya
if 'aul' in 'grault':
    print('aul found!')

#3 Membandingkan apakah ada elemen di dalam list
a = 'qux'
b = ['bar', 'qux', 'gamer']

if a in b:
    print("element a of", a, "is in", b)
else:
    print("element not found!")

x = range(5)
for n in x:
    print(n)
