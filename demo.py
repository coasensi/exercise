print("Bonjour Monde!")

def fn(x):
    return x+1

def another_fn(x):
    return x+3

x=fn(another_fn(fn(3)))
print(x)

def some_other_branch(x):
    return x*2