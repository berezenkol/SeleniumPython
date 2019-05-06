#Parameters and variables that are assigned in a called function are said to exist in that function’s local scope.
# Variables that are assigned outside all functions are said to exist in the global scope.
# A variable that exists in a local scope is called a local variable,
# while a variable that exists in the global scope is called a global variable.
# A variable must be one or the other; it cannot be both local and global.
def spam():
    global eggs
    eggs = 'spam'
    print(eggs)

spam()

