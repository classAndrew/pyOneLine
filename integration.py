"""

Update: boring, see n_tuple_integral.py

Change a, b, and f to what you want.
Not very impressive with builtins like sum and range, but still one line!

"""

(lambda f, dx, a, b: dx*sum(f(dx*i) for i in range(int(a/dx), int(b/dx))))(lambda x: x**2, 0.0001, 0, 1)

"""
Double integral here. Computes the volume under a cone in a square region of length 1.
Change x**2+y**2 and the bounds (curry in the new x bounds or y bounds separately if there's a need for
non-rectangular regions.
"""

(lambda f, dx, a, b: dx**2*sum(sum(f(dx*i, dx*j) for j in range(int(a/dx), int(b/dx))) for i in range(int(a/dx), int(b/dx))))(lambda x, y: x**2+y**2, 0.01, 0, 1)
