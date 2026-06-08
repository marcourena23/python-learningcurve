'''
recursion = a function that calls itself from within
            helps to visualiza a complex problem into basic steps,
            wich can be solved more easily iteratively or recursively.
'''

# ITERATIVE

def walk(steps):
    for step in range(steps):
        print('taking a step')
        
walk(10)


# RECURSIVE
def walk(steps):
    if steps > 0:
        print('taking a step')
        walk(steps - 1)
walk(10)