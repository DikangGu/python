import os, sys

def main():
  filename = sys.argv[1]
  total = 0
  with open(filename) as f:
    for line in f:
      total += long(float(line))
  print total

if __name__ == "__main__":
  main()
