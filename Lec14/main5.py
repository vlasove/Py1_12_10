# СЕКРЕТНЫЕ АРГУМЕНТЫ: континуальные аргументы (*args, **kwargs)
def add(*args):
    """
    *args означает что все переданные параметры будут собраны в кортеж args
    """
    res = 0
    for item in args:
        res += item **2 
    return res

print(add(2))
print(add(2,3))
print(add(2,2,2,2,2,2,2,2,2,222222,2,2,2,2,2))

def strange(**kwargs):
    """
    **kwargs( KeyWords Arguments) означает, что все переданные именованные параметры будут собраны словарь kwargs
    """
    print(type(kwargs))
    print(kwargs)


strange(bob=20, alex=30, kek=40, lol=50)



# А можно ли их смешать?
def ccccombo( *args, **kwargs):
    print(args)
    print(kwargs)

ccccombo(1,2, 3,4, c =30, e=10, w=20)