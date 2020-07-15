(lambda f, n: 1 if n == 1 else n*f(f,n-1))((lambda f, n: 1 if n == 1 else n*f(f,n-1)), int(input("enter n: ")))
