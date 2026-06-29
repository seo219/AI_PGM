# vartest.py
a = 1
def vartest(a):
    a = a + 1

vartest(a)
print(a)

# vartest_error.py
def vartest(a):
    a = a + 1

vartest(3)
print(a)

# vartest_return.py
a = 1 
def vartest(a): 
    a = a + 1 
    return a

a = vartest(a) 
print(a)

# vartest_global.py
a = 1 
def vartest(): 
    global a 
    a = a + 1

vartest() 
print(a)

