"""
Okay, I had to write it in Lisp-style first. Otherwise, I would've driven myself insane with these nested, unformatted parenthesis.
Each generation is not a reference to the previous generation. So, everytime a new generation is generated, an entire copy of the previous generation
is pushed onto the call stack. This will quickly consume a ton of memory so beware with larger boards.

(lambda time, neighbors:
  (lambda f, game, sleep, disp, reset:
    f(f, 
      [[(lambda nc, cell:
    1 if (cell and (nc in {2, 3})) or ((not cell) and nc==3) else 0 # These are the rules for Conway's Game of Life.
  )(neighbors(r,c,game), game[r][c])
 if c!=0 and c!=len(game)-1 and r!=0 and r!=len(game)-1 else 0 for c in range(0, len(game))] for r in range(0, len(game))],time.sleep(0.5),
      print("\033c"),print('\n'.join(str(r) for r in game)) # sleeping, and printing the board after clearing is passed as a function into the next iteration. (They return None)
    )
  )(lambda f, game, sleep, disp, reset:
    f(f, 
      [[(lambda nc, cell:
    1 if (cell and (nc in {2, 3})) or ((not cell) and nc==3) else 0
  )(neighbors(r,c,game), game[r][c])
 if c!=0 and c!=len(game)-1 and r!=0 and r!=len(game)-1 else 0 for c in range(0, len(game))] for r in range(0, len(game))],time.sleep(0.5),
      print("\033c"),print('\n'.join(str(r) for r in game)) # \033c is the escape char for returning to the beginning; it's for overwriting terminal output; however, don't run it with python -c (a friend of mine tried this and the escape char wasn't recognized) 
    ),
    [[0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,1,0,0,0,0],
     [0,0,0,1,1,1,0,0,0], # <--- Game board. You *could* eval(open(file).read()) to cut down on chars.
     [0,0,0,0,1,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0]
    ],None,None,None
  )
)(__import__("time"), lambda r, c, game: sum([sum(game[r-1][c-1:c+2]), sum([*game[r][c-1:c],*game[r][c+1:c+2]]), sum(game[r+1][c-1:c+2])])) # Counting the neighbors is passed as function
"""

# Here's the one liner
(lambda time, neighbors: (lambda f, game, sleep, disp, reset: f(f, [[(lambda nc, cell: 1 if (cell and (nc in {2, 3})) or ((not cell) and nc==3) else 0)(neighbors(r,c,game), game[r][c]) if c!=0 and c!=len(game)-1 and r!=0 and r!=len(game)-1 else 0 for c in range(0, len(game))] for r in range(0, len(game))],time.sleep(0.5),print("\033c"),print('\n'.join(str(r) for r in game))))(lambda f, game, sleep, disp, reset: f(f, [[(lambda nc, cell: 1 if (cell and (nc in {2, 3})) or ((not cell) and nc==3) else 0)(neighbors(r,c,game), game[r][c]) if c!=0 and c!=len(game)-1 and r!=0 and r!=len(game)-1 else 0 for c in range(0, len(game))] for r in range(0, len(game))],time.sleep(0.5),print("\033c"),print('\n'.join(str(r) for r in game))),[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0],[0,0,0,1,1,1,0,0,0],[0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]],None,None,None))(__import__("time"), lambda r, c, game: sum([sum(game[r-1][c-1:c+2]), sum([*game[r][c-1:c],*game[r][c+1:c+2]]), sum(game[r+1][c-1:c+2])]))

