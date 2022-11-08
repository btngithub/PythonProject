def ab(a):
    return 10//a


try:
    print(ab(int(input())))
except ZeroDivisionError:
    print('Ne vvodi o')
except ValueError:
    print('Vvedite chisla')





