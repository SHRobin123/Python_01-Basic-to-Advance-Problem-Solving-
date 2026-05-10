#Tower of Hanoi
def hanoi(n, a, b, c):
    if n == 1:
        print("Move disk 1 from", a, "to", c)
        return
    hanoi(n-1, a, c, b)
    print("Move disk", n, "from", a, "to", c)
    hanoi(n-1, b, a, c)

hanoi(3, "A", "B", "C")

'''
output:- 

Move disk 1 from A to C
Move disk 2 from A to B
Move disk 1 from C to B
Move disk 3 from A to C
Move disk 1 from B to A
Move disk 2 from B to C
Move disk 1 from A to C
'''