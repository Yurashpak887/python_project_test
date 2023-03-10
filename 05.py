import sys

print(sys.argv)

if "-p" in sys.argv:
    print(int(sys.argv[2])+int(sys.argv[3]))
elif "-m" in sys.argv:
    print(int(sys.argv[2]) - int(sys.argv[3]))
elif "-d" in sys.argv:
    print(int(sys.argv[2]) / int(sys.argv[3]))
elif "-u" in sys.argv:
    print(int(sys.argv[2]) * int(sys.argv[3]))