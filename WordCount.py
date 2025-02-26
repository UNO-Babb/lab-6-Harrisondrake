#WordCount.py
#Name:Harrison Drake
#Date: 2/26/25
#Assignment: Lab 6

def main():
  textFile = open("fish.txt", 'r')
  linecount = 0
  wordcount = 0
  lettercount = 0

  for line in textFile:
    linecount += 1
    words = line.split()
    
    for word in words:
      wordcount += 1
      for letter in word:
        lettercount += 1
        

  print("Lines: ", linecount)
  print("Words: ", wordcount)
  print("Letters: ", lettercount)

if __name__ == '__main__':
  main()
