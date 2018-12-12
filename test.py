import time

from timeit import Timer

li1 = [1, 2]

li2 = [23, 5]

li = li1 + li2

li = [i for i in range(10000)]


def test1():
    li = []
    for i in range(10000):
        li.append(i)


def test2():
    li = []
    for i in range(10000):
        li += [i]


def test3():
    li = [i for i in range(10000)]


def test4():
    li = list(range(100000))


def test5():
    li = []
    for i in range(10000):
        li.insert(0, i)


def test6():
    li = []

    for i in range(10000):
        li.append(i)


time1 = Timer("test1()", "from __main__ import test1")
print("append:", time1.timeit(1000))

time2 = Timer("test2()", "from __main__ import test2")
print("+:", time2.timeit(1000))

time3 = Timer("test3()", "from __main__ import test3")
print("[i for i in range]:", time3.timeit(1000))

time4 = Timer("test4()", "from __main__ import test4")
print("list(range()):", time4.timeit(1000))

time5 = Timer("test5()", "from __main__ import test5")
print("test 5 insert 0 ", time5.timeit(1000))

time6 = Timer("test6()", "from __main__ import test6")
print("test 6 append:", time6.timeit(1000))
