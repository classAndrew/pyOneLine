"""
ONE LINER AT THE BOTTOM, here's my explanation.
This code will compute the definite n-tuple (triple, quadruple, quintuple... n-tuple) integral of some function
over some bounded region.
As you can see here, it's a bit short and simple. (Took me FOREVER to debug).
Basically recursively adds the previous dimension's integral and returns to be added... and so on.
The demo I have below (in the outermost function's parameters), can be thought of as the 
"hyper-mass" of a tesseract with edge length 1 whose density is proportional to the distance from the origin.
The trickiest part is to pass the arguments into the function in the right order (which is why there's
an awkward unpacking operation going on in the call to f).
Variable bound can be added, but I just wanted to demo the basic integration over regions with equal sides (1 in this case)
Slight warning though: THIS DOES NOT SCALE WELL... AT ALL
In fact, I can't run the below code in under 15 minutes (it will run in O(n^k) time for k is the number of
variables, and n is the digits of precision, here it is 2 or -log(dx), ON TOP of all the overhead from recursive calls).
In the one liner, I've swapped out the function to a 3-variable function for my computer's sake.

Update: The 4-variable function surprisingly works when ran with pypy (still don't use it though, your computer will fry itself). 

(lambda f, dx, a, b: 
  (lambda n:
    (lambda itself, i, v:
      dx**n*sum(f(*[x*dx for x in [*v[:-1], r]]) for r in range(int(a/dx), int(b/dx))) if i == n-1 else 
      sum(itself(itself, i+1, [*v[:i],r,*v[i+1:]]) for r in range(int(a/dx), int(b/dx)))
    )((lambda itself, i, v:
      dx**n*sum(f(*[x*dx for x in [*v[:-1], r]]) for r in range(int(a/dx), int(b/dx))) if i == n-1 else 
      sum(itself(itself, i+1, [*v[:i],r,*v[i+1:]]) for r in range(int(a/dx), int(b/dx)))
    ), 0, [0]*n)
  )(f.__code__.co_argcount)
)(lambda x, y, z, w: x**2+y**2+z**2+w**2, 0.01, 0, 1)
"""

# And the one liner
(lambda f, dx, a, b: (lambda n: (lambda itself, i, v: dx**n*sum(f(*[x*dx for x in [*v[:-1], r]]) for r in range(int(a/dx), int(b/dx))) if i == n-1 else sum(itself(itself, i+1, [*v[:i],r,*v[i+1:]]) for r in range(int(a/dx), int(b/dx))))((lambda itself, i, v: dx**n*sum(f(*[x*dx for x in [*v[:-1], r]]) for r in range(int(a/dx), int(b/dx))) if i == n-1 else sum(itself(itself, i+1, [*v[:i],r,*v[i+1:]]) for r in range(int(a/dx), int(b/dx)))), 0, [0]*n))(f.__code__.co_argcount))(lambda x, y, z: x**2+y**2+z**2, 0.01, 0, 1)
