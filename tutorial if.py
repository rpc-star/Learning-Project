import math
from functools import wraps
import time
from operator import length_hint
from shutil import ReadError
import sad
import pickle

# if 5 <= x <= 7:
# print("x в диапазоне <5> <7>")
# else:
# print(x)
import os


def aaa():
    x = (input("введите значение Х в диапазоне от 0 до 999:"))
    if float(x) < 0:
        print("х должен быть положительным")
    elif 0 <= float(x) <= 9:
        print("х - просто цифра")
    elif 10 <= float(x) <= 99:
        print("х - двухзначное число")
    elif 100 <= float(x) <= 999:
        print("х - трехзначное число")
    else:
        aaa()
    print(aaa())


# i = [1,5,3,7,1,2,7]
# a = 0
# while a < len(i):
# f = i[a]%2==0
# if f == True:
#   break
# a +=1
# print(f)
# s = 0
# d = 1

# while d !=0:
# d = int(input("введите четное число: "))
# if d %2 == 0:
# continue
# s += d
#   print(s)

# i = int(input("Факториал: "))

# if i < 1 or i > 100:
#  print("Введено неверное значение")
# else:
#  p = 15
#  for r in range(1, i+1):
#     p *= r
#  print ("vo govno, zhry: " + str(p))

# N = int(input())
# line=[[1 for _ in range(N)] for _ in range(N)]
# for i in line:
#  i[N - 1] = 5
# for i in line:
#  print(*i)

# n = 7
# p = []
# for i in range(n):
# row =[1]*(i+1)
#  for j in range(i+1):
#     if j != 0 and j != i:
#        row[j] = p[i-1][j-1] + p[i-1][j]
#   p.append(row)
#
# for r in p:
#  print(r)


n = [1 for x in range(10)]
print(n)

n = 10
a = [x // 4 for x in range(n)]
print(a)
t = ["хуба буба", "хлопья", "паркууур", "твайлайт спаркл"]
a = [d for d in t]
print(a)

n = [d for d in range(-5, 10) if d % 2 == 0 and d > 0]
print(n)

cities = ["Щербинки", "Ростов на дону", "Махачкала", "Тверь"]

n = [d for d in cities if len(d) >= 7]
print(n)

G = [0, -4, 6, -2, 8, 5, 1, -6]

n = ["четное" if x % 2 == 0 else "нечетное" for x in G]
print(n)

a = [(i, j) for i in range(3) if i % 2 == 0 for j in "pupa"]
print(a)

a = [u ** 2 for u in [x + 1 for x in range(8)]]
print(a)

d = {"wheel": "колесо", "book": "книга", "pen": "ручка", "knife": "нож"}
print(d["wheel"])

dict(rwe="100")
print(dict())
G = [[2, "nrere"], [4, "dsadasdd"]]
dict(G)
print(dict(G))
f = {True: 231, False: "абуабуабу", "list": len("python"), "aboba": [[231, "luna"], [5324, ord("d")]]}
print(f.items())
print(len(f))

lst = ["+7", "+5", "+6", "+4"]
a = dict.fromkeys(lst)
print(a)
a["+7"] = "just a number"
print(a)
a = dict.fromkeys(lst, "Код дивуар")
print(a)
f = dict.fromkeys(lst)
print(f.clear())
f = a.copy()
print(f)
a["+7"] = "pupalupa"
print(a)
d = dict(f)
print(d)
print(id(d))
print(id(f))

print(f.get("+5"))
f.setdefault("+9", "черёмуха")
print(f.setdefault("+3", "сас"))
del f["+3"]
print(f)
print(f.pop("+1", False))
print(f)
for x in a.items():
    print(x, end=" ")
for key, value in f.items():
    print(key, value)

# a.setdefault("+8", "черёмуха")

# print(f,"\n",a)

a.setdefault("+8", "черёмуха")

# f.update(a)
# print(f)

# d3 = {**a, **f}
d3 = a | f
print(d3)
h = 1,
h1 = 1, 2, 4, 5
print(h1)
x, y, c, r = 1, 2, 4, 5
print(x, y, c)

a, b = "ra"
print(a, b)

a = (1, 2, 3)
a = (1, 2, 3) + (4, 5)
print(a)
a += ("echkere",)
print(a)
print(a * 3)
d = [[a], [h]]
print(d)
p = tuple([1, 2, 3])
print(p)
k = tuple("hello")
print(k)
t = tuple([[1, 2, 3], [1, 2, 3]], )
print(t)

a = (True, [1, 4, 5], "kefteme", {"1": "pupa", "2": "lupa"})
print(a)

print(a.count("kefteme"))

e = {1, 2, 3, "hello"}
print(e)

set([1, 4, 6, 4, 2, 1, 2, 5, 7])
print(set([1, 4, 6, 4, 2, 1, 2, 5, 7]))

print(set("aboba"))

print(set(range(7)))

cities = ["Алупка", "Гонконг", "Понивилль", "Сергеевка", "Понивилль", "Алупка"]

print(set(cities))
print((list(set(cities))))

q = set(cities)
for x in q:
    if len(x) <= 20:
        print(x)

# it = iter(q)
# print(next(it))
# print(next(it))
print("Алупка" in cities)

r = set()
r.add(3)
r.add(4)
r.add(1)
r.update(["a", "b", (1, 2), 6])
r.add("jughn")
r.update("jughn")
print(r)

setA = {1, 5, 6, 7, 9, 12}
setB = {5, 8, 1, 6, 7, 511, 214}
# setA & setB
print(setA.intersection(setB))
# setA.intersection_update(setB)
# setA |= setB
print(setA)
print(setB.union(setA))
print(setA ^ setB)

a = {x: x ** 2 for x in range(1, 5)}
print(a)
d = [1, 24, 5, -2, 4, '2', '8']
a = {int(x) for x in d}
print(a)
set_d = set()
for x in d:
    set_d.add(int(x))
print(set_d)

m = {"неудовл.": 2, "удовл.": 3, "хорошо": "4", "отлично": "5"}
a = {key.title(): int(value) for key, value in m.items()}
print(a)
f = {}
for key, value in m.items():
    f.update({key.upper(): int(value)})
print(f)

n = {int(x) for x in d if int(x) % 2 == 0}
print(n)

a = {int(value): key for key, value in m.items() if 2 <= int(value) < 5}
print(a)


def send_mail(from_name):
    text = f"""Уважаемый, я ничего не понял. С наилучшими пожеланиями, ваш {from_name}"""
    print(text)


send_mail("Фемистокл")


def get_sqrt(x):
    res = None if x < 0 else x ** 0.5
    return res, x


print(get_sqrt(4))


def get_max(a, b):
    return a if a > b else b


print(get_max(5, get_max(8, 7)))


def get_max2(a, b, c):
    return get_max(a, get_max(b, c))


x, y, z = 4, 2, 3
print(get_max2(x, y, z))

PERIMETR = False
if PERIMETR:
    def get_rect(a, b):
        return 2 * (a + b)
else:
    def get_rect(a, b):
        return a * b

print(get_rect(5, 5))


def even(i):
    return True if i % 2 == 0 else False


print(x in range(100))


def nod(a, b):
    """dsdsdfdksfllsddf
    sld;l;sad;sad"""
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


res = nod(2, 100000)

print(res)


def test(func):
    a = 50
    b = 60
    res = func(a, b)
    if res == 10:
        print("Тест 1 успешный")
    else:
        print("нет")

    a = 1
    b = 100
    res = func(a, b)
    if res == 1:
        print("ок")
    else:
        print("нет")

    # a = 2
    # b = 10000000


# st = time.time()
# res = func(a, b)
# et = time.time()
#  dt = et - st
# if res == 2 and dt < 0.5:
#     print("ок")
# else:
#      print("no")


test(nod)


def cmd(s1, s2, reg=True, trim=True):
    if reg:
        s1 = s1.lower()
        s2 = s2.lower()
    if trim:
        s1 = s1.strip()
        s2 = s2.strip()
    return s1, s2


v = (cmd("Kuka ", " Lupa"))
print(v)


def add_value(value, lst=[]):
    lst.append(value)
    return lst


l = add_value(1)
l = add_value(2)
l = add_value(3)
print(l)


def os_path(*args):
    path = "\\".join(args)
    return path


p = os_path("F:\\~sdasd.sda", "dAdskdlskdlklgf fdsad", "39\\36. asdsd.doc")
print(p)


def os_path1(disk, *args, sep="\\", **kwargs):
    args = (disk,) + args
    if 'trim' in kwargs and kwargs['trim']:
        args = [x.strip() for x in args]
    path = sep.join(args)
    return path


p = os_path1("F:", "\\~sdasd.sda", "dAdskdlskdlklgf fdsad", "    39\\36.asdsd.doc  ", sep="\\", trim=True)
print(p)

x, *y = 1, 2, 3, 4
print(x, y)
*x, y = [True, "pupa", 4, 5]
print(x, y)
a = [1, 2, 3]
print((a,))
print((*a,))
d = -5, 5
# print(range(d))
print(list(range(*d)))
print([*range(*d)])
print([*range(*d), *(True, False), *a])
t = {0: "zero", 1: "trash", 2: "bad", 3: "average", 4: "good", 5: "amazing"}
t2 = {6: "cool", 5: "rampage"}
print(*t)
print({**t})
print({**t, **t2})


def recurcive(value):
    print(value)
    if value < 5:
        recurcive(value + 1)
    print(value)


recurcive(1)


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


print(fact(6))

F = {
    "C:": {
        'python39': ['python.exe', 'python.ini'],
        'Program Files': {
            'java': ['README.txt', 'Welcome.html', 'java.exe'],
            'MATLAB': ['matlab.bat', 'aclui.dll', 'zipfldr.dll']
        }
    }
}


def get_files(path, depth=0):
    for f in path:
        print(" " * depth, f)
        if type(path[f]) == dict:
            get_files(path[f], depth + 1)
        else:
            print(" " * (depth + 1), " ".join(path[f]))


get_files(F)

s = lambda a, b: a + b
print(s(1, 2))
a = [4, 5, lambda: print('lambda'), 6, 7]
print(a[2]())

lst = [5, 6, 12, 6, 2, 6, 8, 1, 4, 5, 6, 8, 112]


def get_filt(a, filtr=None):
    if filtr is None:
        return a
    res = []
    for x in a:
        if filtr(x):
            res.append(x)
    return res


print(get_filt(lst, lambda x: x % 2 == 0))

x = 0


def outer():
    x = 1

    def inner():
        nonlocal x
        x = 2
        print('Inner ', x)

    inner()
    print('Outer ', x)


outer()

print('global', x)


def counter(start=0):
    def step():
        nonlocal start
        start += 1
        return start

    return step


c1 = counter(5)
c2 = counter(1)
print(c1(), c2())
print(c1(), c2())
print(c1(), c2())
print(c1(), c2())
print(c1(), c2())


def strip_string(strip_chars=" "):
    def do_strip(string):
        return string.strip(strip_chars)

    return do_strip


s1 = strip_string(" ")
s2 = strip_string(" !,.?")

print(s1("    hello!,.?   "))
print(s2("    hello!,.?   "))


def get_function(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print("sdsd")
        return res

    return wrapper


def some_func(title):
    print(f'title: {title}')
    return title


some_func = get_function(some_func)
res = some_func("pupa")
print(res)


def get_time(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        res = func(*args, **kwargs)
        ed = time.time()
        dt = ed - st
        return res, dt

    return wrapper


@get_time
def evclid(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


@get_time
def get_evclid(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a


# evclid = get_time(evclid)
# get_evclid = get_time(get_evclid)
res2 = get_evclid(2, 100)
res = evclid(2, 100)
print(res)
print(res2)


def df_decorator(dx=0.0001):
    def func_decorator(func):
        @wraps(func)
        def wrapper(x, *args, **kwars):
            res = (func(x + dx, *args, **kwars) - func(x, *args, **kwars)) / dx
            return res

        # wrapper.__name__ = func.__name__
        # wrapper.__doc__ = func.__doc__
        return wrapper

    return func_decorator


@df_decorator(dx=0.0001)
def sin_df(x):
    '''pupa lupas kayus bonus'''
    return math.sin(x)


print(sin_df.__doc__)
df = sin_df(math.pi / 3)
print(df)

print(sad.NAME)
print(sad.floor(-5.5))

file = open("my_file.txt", encoding="utf-8")
print(file.read(4))
print(file.read(4))
res = file.tell()
print(res)
file.seek(0)
print(file.tell())
print(file.readline())
# for x in file:
#    print(x, end="")
# print(file.readlines())
try:
    file = open("my_file3.txt", encoding="utf-8")
    s = file.readlines()
    print(s)
    file.close()
except FileNotFoundError:
    print("file non found")

try:
    file = open("my_file.txt", encoding="utf-8")
    try:
        s = file.readlines()
        print(s)
    finally:
        file.close()
except FileNotFoundError:
    print("file non found")
except:
    print("ERROR")

try:
    with open("my_file2.txt", encoding="utf-8") as file:
        s = file.readlines()
except FileNotFoundError:
    print("file non found")
except:
    print("ERROR")
finally:
    print(file.closed)

# file = open("my_file.txt","w")
# file.write("Hello")
# file.close()

file = open("my_file.txt", encoding="utf-8")
f = file.readlines()
print(f)

file = open("my_file2.txt", "w")
file.write("pupalupsky")
file.close()

file = open("my_file2.txt", encoding="utf-8")
f = file.readlines()
print(f)

try:
    with open("my_file3.txt", "w") as file:
        file.write("pupalupsky - lupapupsky - \n")
        file.write("pupalupsky - lupapupsky1 - \n")
        file.write("pupalupsky - lupapupsky2")
except:
    print("ERROR")
finally:
    print(file.closed)

try:
    with open("my_file.txt", "a+") as file:
        file.write(" hello chel\n   ")
        file.seek(0)
        s = file.read()
        print(s)
except:
    print("error")
finally:
    print(file.closed)

# file = open("my_file.txt", encoding = "utf-8")
# s = file.read()
# print(s)

try:
    with open("my_file.txt", "a+") as file:
        file.seek(0)
        file.writelines(["hello\n", "kuku\n"])
        s = file.read()
        print(s)
except:
    print("error")
finally:
    print(file.closed)

book = [("sdsdaa", 200), ("sdagf", 300), ("sdewaw", 400)]
book2 = [("sdsdaa", 200), ("sdagf", 300), ("sdewadsw", 400)]
book3 = [("sdsdaa", 200), ("sdagsdf", 300), ("sdewaw", 400)]
book4 = [("sdsdsaa", 200), ("sdagf", 300), ("sdewaw", 400)]

file = open("my_file4.txt", "wb")
pickle.dump(book, file)
file.close()

file = open("my_file4.txt", "rb")
rs = pickle.load(file)
file.close()
print(rs)

try:
    with open("my_file4.txt", "wb+") as file:
        pickle.dump(book2, file)
        pickle.dump(book3, file)
        pickle.dump(book4, file)
        file.seek(0)
        rs = pickle.load(file)
        rs2 = pickle.load(file)
        rs3 = pickle.load(file)
except:
    print("error")
finally:
    print(file.closed)
print(rs, rs2, rs3, sep="\n")

a = (x ** 2 for x in range(6))
print(next(a), type(a))
print(next(a), type(a))

gen = (x ** 2 for x in range(6))
for x in gen:
    print(x)

for x in gen:
    print(x)

print(list(a))
a = (x * 2 for x in range(6))
print(list(a))

b = (x ** 2 for x in range(6))
print(set(b))

print(sum((x ** 2 for x in range(6))))
print(max((x ** 2 for x in range(6))))

lst = (x for x in range(10000000000000000))
print(next(lst))
print(next(lst))
print(next(lst))
print(next(lst))

# for x in lst:
# print(x, end=" ")
# if x > 200:
#     break
# lst2 = list(range(10000000000000000))

x = (x for x in range(10, 20))
f = list(x)
print(len(f))


def get_list():
    for x in [1, 2, 3, 4]:
        yield x


a = get_list()
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

for x in a:
    print(x)


def get_arf():
    for x in range(1, 10):
        a = range(x, 11)
        yield sum(a) / len(a)


i = get_arf()
# for x in i:
# print(x, end=", ")
print(list(i))


# def file_world(f, word):
#  for x in f:
#   if word == "pupa":
#      yield word


def find_world(f, word):
    g_indx = 0
    for line in f:
        indx = 0
        while (indx != -1):
            indx = line.find(word, indx)
            if indx > -1:
                yield g_indx + indx
                indx += 1

        g_indx += len(line)


try:
    with open("fille.txt", encoding="utf-8") as file:
        file.seek(0)
        a = find_world(file, "pupa")
        print(list(a))
except FileNotFoundError:
    print("file non found")
except:
    print("ERROR")
finally:
    print(file.closed)

b = map(int, ["1", 2, "3", 4, 5])
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))

for x in b:
    print(x)

a = (int(x) for x in ["1", "2", "3", "4", "5"])

print(list(a))

cities = ["Moskva", "Nigjni Novgorod", "Saint Peterburg"]

a = map(len, cities)
print(list(a))

a = map(str.upper, cities)
print(list(a))


def symbols(s):
    return list(s.lower())


# a = map(lambda s: list(s.lower()), cities)
# print(list(a))

# a = map(lambda s: s[::-1], cities)
# print(list(a))

# s = map(int, input().split())
# a = list(s)
# print(a)

# s = list(map(int, input().split()))
# print(s)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

b = filter(lambda x: x % 2 != 0, a)
print(list(b))


def is_prost(x):
    d = x - 1
    if d < 0:
        return False
    while d > 1:
        if x % d == 0:
            return False
        d -= 1
    return True


i = filter(is_prost, a)
print(list(i))

cities = ["Moskva", "Nigjn2i Novgorod", "Saint Peterburg"]

a = filter(str.isalpha, cities)
print(list(a))

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

b = filter(is_prost, a)
s = filter(lambda x: x % 2 == 0, b)
print(list(s))

b1 = filter(lambda x: x % 2 != 0, filter(is_prost, a))
print(tuple(b1))


def get_prost(x):
    d = x - 1
    if d < 0 or x % 2 == 0:
        return False
    while d > 1:
        if x % d == 0:
            return False
        d -= 1
    return True


b2 = filter(get_prost, a)
print(tuple(b2))

a = [1, 2, 3, 4]
b = [5, 6, 7, 8, 9, 10]

z = zip(a, b)
print(next(z))
print(next(z))

for x in z:
    print(x)

a = [1, 2, 3, 4]
b = [5, 6, 7, 8, 9, 10]
c = "python"

z = zip(a, b, c)
# for x in z:
# print(x, end=" ")

# for v1,v2,v3 in z:
# print(v1, v2, v3)

# z1,z2,z3,z4 = zip(a,b,c)
# z1,*z2 = zip(a,b,c)
# print(z1, z2)
# a = list(z)
z1, z2, z3 = zip(*z)
print(z1, z2, z3, sep="\n")

a = [1, 5, 2, 76, -123, 35, 23]
a.sort()
print(a)

a1 = ("sdfd", "sd", "sdkdfvc")
print(sorted(a1))

print(sorted("python"))
a2 = [1, 5, 2, 76, -123, 35, 23]
print(sorted(a2, reverse=True))

d = {"river": "река", "mountin": "гора", "cloud": "облако", "butterfly": "бабочка"}

print(sorted(d))
print(sorted(d.values()))
a3 = sorted(d.items())

print(dict(a3))


def get_numb(x):
    return x % 2


a = [4, 3, -10, 1, 7, 12]
#b = sorted(a, key=lambda x: x % 2)
#print(b)
b = [4, 3, -10, 1, 7, 12]
#b.sort(key = lambda x: x % 2)
print(b)


def key_sort(x):
    return x if x % 2 == 0 else 100 + x

b.sort(key = key_sort)
print(b)

cities = ["Moskva","Nigjni Novgorod","Saint Peterburg","Tumen", "Luxenburg"]

#v1 = sorted(cities, key = len)
#print(sorted(cities, key = lambda x: x[-1]))
print(sorted(cities, key = lambda x: x[0]))

books = (("Евгений онегин", "Пушкин А.С.", 200),
         ("Муму", "Тургенев И.С.", 250),
         ("Мастер и Маргарита", "Булгаков м.А.", 500),
         ("мертвые души", "Гоголь Н.В.", 190)
         )

g = sorted(books, key = lambda x: x[-1])
print(g)

a = 5
print(isinstance(a,int))

b = True

print(isinstance(b, bool))

print(isinstance(a, int))

print(type(b) == int)


print(type(b) is int)
print(type(b) is bool)

print(type(b) in (bool, float, str, set))

data = (4.5, 8.7, True, "books", 8, 10, -11, [True,False])

s = 0

for x in data:
    if isinstance(x, float):
        s += x
print(s)

s1 = sum(filter(lambda x: isinstance(x, float), data))
print(s1)


s2 = sum(filter(lambda x: type(x) is int, data))
print(s2)


a4 = 5.5

print(isinstance(a, (int, float)))












