def func(x):
    def func2(y):
        return x+y
    return func2


new = func('a')
print(new('b'))
