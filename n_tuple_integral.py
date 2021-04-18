"""
Compute Riemann sums of Riemann sums to approximate an iterated integral.
Bottom line: get ready for you computer fan to explode.

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
