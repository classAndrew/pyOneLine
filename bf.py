# I make excellent life decisions
# This is a brainf**k interpreter written in one line of Python
# the interpreted bf code (last line) is a "Hello World" found on wikipedia
# '/' isn't actually part of the bf specification, but I added it because I needed to test something

(f := lambda f, stack, prgvals, inmap, ins, *action: 
	f(f, stack, prgvals, inmap, ins, inmap[ins[prgvals[1]]](prgvals, stack, ins), prgvals.__setitem__(1, prgvals[1]+1)) if prgvals[1] < len(ins) else None
)(f, [0]*30000, [0, 0, 0], 
{
	"/": lambda prgvals, stack, ins: None,
	">": lambda prgvals, stack, ins: prgvals.__setitem__(0, prgvals[0]+1),
	"<": lambda prgvals, stack, ins: prgvals.__setitem__(0, prgvals[0]-1),
	"+": lambda prgvals, stack, ins: stack.__setitem__(prgvals[0], stack[prgvals[0]]+1),
	"-": lambda prgvals, stack, ins: stack.__setitem__(prgvals[0], stack[prgvals[0]]-1),
	".": lambda prgvals, stack, ins: print(chr(stack[prgvals[0]]), end=''),
	",": lambda prgvals, stack, ins: stack.__setitem__(prgvals[0], input("Enter byte: ")),
	"[": lambda prgvals, stack, ins: (a := lambda a, *ac: 
				a(a, prgvals.__setitem__(1, prgvals[1]+1),
					prgvals.__setitem__(2, prgvals[2]+(ins[prgvals[1]] == '[')),
					prgvals.__setitem__(2, prgvals[2]-(ins[prgvals[1]] == ']'))
				)
				if prgvals[2] else None
				)(a, prgvals.__setitem__(2, prgvals[2]+1), prgvals.__setitem__(1, prgvals[1]+1)) if not stack[prgvals[0]] else None,
	"]": lambda prgvals, stack, ins: (a := lambda a, *ac: 
				a(a, prgvals.__setitem__(1, prgvals[1]-1),
					prgvals.__setitem__(2, prgvals[2]-(ins[prgvals[1]] == '[')),
					prgvals.__setitem__(2, prgvals[2]+(ins[prgvals[1]] == ']'))
				)
				if prgvals[2] else None
				)(a, prgvals.__setitem__(2, prgvals[2]+1), prgvals.__setitem__(1, prgvals[1]-1)) if stack[prgvals[0]] else None
}, list("++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.")
)

# and as one line
(f := lambda f, stack, prgvals, inmap, ins, *action: f(f, stack, prgvals, inmap, ins, inmap[ins[prgvals[1]]](prgvals, stack, ins), prgvals.__setitem__(1, prgvals[1]+1)) if prgvals[1] < len(ins) else None)(f, [0]*30000, [0, 0, 0], {"/": lambda prgvals, stack, ins: None, ">": lambda prgvals, stack, ins: prgvals.__setitem__(0, prgvals[0]+1), "<": lambda prgvals, stack, ins: prgvals.__setitem__(0, prgvals[0]-1), "+": lambda prgvals, stack, ins: stack.__setitem__(prgvals[0], stack[prgvals[0]]+1), "-": lambda prgvals, stack, ins: stack.__setitem__(prgvals[0], stack[prgvals[0]]-1), ".": lambda prgvals, stack, ins: print(chr(stack[prgvals[0]]), end=''), ",": lambda prgvals, stack, ins: stack.__setitem__(prgvals[0], input("Enter byte: ")), "[": lambda prgvals, stack, ins: (a := lambda a, *ac: a(a, prgvals.__setitem__(1, prgvals[1]+1), prgvals.__setitem__(2, prgvals[2]+(ins[prgvals[1]] == '[')), prgvals.__setitem__(2, prgvals[2]-(ins[prgvals[1]] == ']'))) if prgvals[2] else None)(a, prgvals.__setitem__(2, prgvals[2]+1), prgvals.__setitem__(1, prgvals[1]+1)) if not stack[prgvals[0]] else None, "]": lambda prgvals, stack, ins: (a := lambda a, *ac: a(a, prgvals.__setitem__(1, prgvals[1]-1), prgvals.__setitem__(2, prgvals[2]-(ins[prgvals[1]] == '[')),prgvals.__setitem__(2, prgvals[2]+(ins[prgvals[1]] == ']'))) if prgvals[2] else None)(a, prgvals.__setitem__(2, prgvals[2]+1), prgvals.__setitem__(1, prgvals[1]-1)) if stack[prgvals[0]] else None}, list("++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."))
