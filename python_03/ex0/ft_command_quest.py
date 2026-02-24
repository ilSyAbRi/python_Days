import sys

print("=== Command Quest ===")
if len(sys.argv) == 1:
    print("No arguments provided!")
    print("Program name:", sys.argv[0])
    print("Total arguments:", len(sys.argv))
else:
    print("Program name:",sys.argv[0])
    print("Arguments received:", len(sys.argv) -1)

    i = 1
    while i < len(sys.argv):
        print("Argument",i,":",sys.argv[i])
        i += 1
    print("Total arguments:", len(sys.argv))
