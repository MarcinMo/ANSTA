from decimal import Decimal

string1 = "79-900"
string2 = "80-155"

def generator(arg1,arg2):

    generator_list = []
    start = None
    start = arg1[0:2]
    start +=arg1[3:7]
    start = int(start)
    start += 1
    end = None
    end = arg2[0:2]
    end +=arg2[3:7]
    end = int(end)

    for i in range(start,end,1):
        i = str(i)
        new = i[0:2] + "-" + i[2:5]
        generator_list.append(new)
    print(generator_list)
generator(string1,string2)

def request2(ns, n):
    return list(set(range(n)) - set(ns))

def request3():
    return [Decimal(20 + x * 5) / 10 for x in range(8)]


print(request2([1, 3, 4, 5, 6, 7, 8], 10))
print(request3())
