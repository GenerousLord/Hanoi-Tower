import time

# Tower of Hanoi (n-disk) algorithm in Python with ASCII art display of Pole/rod
# Contents the 3 poles representation
poles = [[], [], []]

def TOH(n, A="A", B="B", C="C"):
    if n > 0:
        TOH(n-1, A, C, B)
        print(f"Move disk from rod {A} to rod {C}")
        move(A, C)
        displayPoles()  # Display the state of the poles
        time.sleep(1)  # Introduce a 1-second delay
        TOH(n-1, B, A, C)

def initPoles(n):
    global poles
    poles = [[i for i in range(n, 0, -1)], [], []]

def move(source, destination):
    global poles
    # get source and destination pointers
    ptr1 = ord(source) - ord('A')
    ptr2 = ord(destination) - ord('A')
    top = poles[ptr1].pop()
    poles[ptr2].append(top)

def displayPoles():
    global poles
    max_height = max(len(pole) for pole in poles)
    for level in range(max_height - 1, -1, -1):
        for pole in poles:
            if level < len(pole):
                # Displaying the disks and spaces
                print("|", " " * (max_height - pole[level]), "*" * (2 * pole[level] - 1), " " * (max_height - pole[level]), "|", sep="", end="\t")
            else:
                print("|", " " * (2 * max_height - 1), "|", sep="", end="\t")
        print()

N = 3
initPoles(N)
print(f"Initial state of the poles with {N} disks:\n")
displayPoles()
print(f"\nTower of Hanoi Solution for {N} disks:\n")
TOH(N)