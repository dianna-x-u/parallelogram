# Dianna Xu
# 110-A - Hw10.1
# This outputs any character in a parallelogram shape

def main():
  print("This program will output a parallelogram.")
  side = int(input("How long do you want each side to be? "))
  character = input("Please enter the character you want it to be made of: ")
  shape = repeatChar(side, character)
  
def repeatChar(numRepeats, outputChar):
  #output the outputChar numRepeats times
  space = " "
  for i in range(numRepeats,-1,-1):
    print(outputChar * (numRepeats-i))
  for i in range(numRepeats):
    print((space*(i+1)) + outputChar * (numRepeats-i-1))

if __name__ == "__main__":
  main()



'''
---PRACTICE SPACE---
numRepeats = 5
outputChar = "@"
space = " "
for i in range(numRepeats,-1,-1):
  print(outputChar * (numRepeats-i))
for i in range(numRepeats):
  print((space*(i+1)) + outputChar * (numRepeats-i-1))

---SAMPLE OUTPUT 1---
This program will output a parallelogram.
How long do you want each side to be? 8
Please enter the character you want it to be made of: *

*
**
***
****
*****
******
*******
********
 *******
  ******
   *****
    ****
     ***
      **
       *

---SAMPLE OUTPUT 1---
This program will output a parallelogram.
How long do you want each side to be? 3
Please enter the character you want it to be made of: $

$
$$
$$$
 $$
  $
'''




        