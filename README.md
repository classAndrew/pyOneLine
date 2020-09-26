# pyOneLine

Collection of Python one liners written as a joke (this means don't use this for production).

Rules:
</br >
No newlines
</br >
No semicolons
</br >
No replacing code with semicolons or newlines and exec-ing.
</br >
Recursion for the win (Okay, but list comps allowed)

Each of these files will contain one line (there may be multiple, but those are for comments that won't actually affect the program).
They can also be ran directly in the Python interactive shell as they were meant to be.

Most of these were written before the introduction of the walrus operator (:=). This means if I were to rewrite these programs with :=, I won't have to carry in arguments into another frame for to be used without recalculating. It also means I can do something like 
```python3
(a := lambda: a())()
``` 
for the main loop
