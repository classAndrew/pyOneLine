"""
Change a, b, and f to what you want.
Not very impressive with builtins like sum and range, but still one line!
"""

(lambda f, dx, a, b: dx*sum(f(dx*i) for i in range(int(a/dx), int(b/dx))))(lambda x: x**2, 0.0001, 0, 1)
