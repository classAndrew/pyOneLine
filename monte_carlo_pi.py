# pretty straight forward.
(lambda r: (lambda x: 4*x/10**6)(sum((r(0, 1e9)/1e9)**2+(r(0, 1e9)/1e9)**2 <= 1 for i in range(10**6))))(__import__("random").randrange)
