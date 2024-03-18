#eval() will evaluate an expression
#if the statement is correct it will evaluate the expression
x = "print('hello')"
eval(x)            #hello

y = eval('[3,6,7,8,9]')
print(y)             #[3, 6, 7, 8, 9]
print(type(y))       #<class 'list'>

z = eval('5+hello')
print(z)             #NameError: name 'hello' is not defined. Did you mean: 'help'?