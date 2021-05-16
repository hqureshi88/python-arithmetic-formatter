import re

def arithmetic_arranger(problems, display = True):
  arranged_problems = ''
  lineOne = ''
  lineTwo = ''
  lineThree = ''
  lineFour = ''
  if len(problems) > 5:
    return "Error: Too many problems."
  else:
    for i, s in enumerate(problems): 
      
      x = s.split()
      x1 = x[0]
      x2 = x[2]

      if(len(x1)>4 or len(x2)>4):
        return "Error: Numbers cannot be more than four digits."

      if(not x1.isdigit() or not x2.isdigit()):
        return "Error: Numbers must only contain digits."

      char = re.findall('[+/-]', s)

      if(char[0] != '+' and char[0] != '-'):
        return "Error: Operator must be '+' or '-'."
      
      ansr = 0
      if char[0] == '+':
        ansr = int(x1) + int(x2)
      else:
        ansr = int(x1) - int(x2)

      line4 = ''
      line3 = ''
      line2 = ''
      line1 = ''
  
      if len(x1) >= len(x2):
        length = len(x1) + 2
        line1 = x1.rjust(length)
        if i == 0:
          lineOne += line1
        else:
          lineOne += "    " + line1

        length2 = length - len(x2)
        line2 = char[0].ljust(length2) + x2
        if i == 0:
          lineTwo += line2
        else:
          lineTwo += "    " + line2

        n = length
        s = '-'
        line3 = ''.join([char*n for char in s])
        if i == 0:
          lineThree += line3
        else:
          lineThree += "    " + line3

        if(display == True):
          line4 = str(ansr).rjust(length)
          if i == 0:
            lineFour += line4
          else:
            lineFour += "    " + line4
        else:
          lineFour = ''

      else:
        line2 = char[0].ljust(2) + x2
        if i == 0:
          lineTwo += line2
        else:
          lineTwo += "    " + line2
        line1 = x1.rjust(len(line2))
        if i == 0:
          lineOne += line1
        else:
          lineOne += "    " + line1

        n = len(line2)
        s = '-'
        line3 = ''.join([char*n for char in s])
        
        if i == 0:
          lineThree += line3
        else:
          lineThree += "    " + line3
      
        if(display == True):
          line4 = str(ansr).rjust(len(line2))
          if i == 0:
            lineFour += line4
          else:
            lineFour += "    " + line4
        elif(display == False):
          lineFour = ''

      if len(problems)-1 == i:
        lineOne += "\n"
        lineTwo += "\n"
        if(display == True):
          lineThree += "\n"
        #lineFour += "\n"

  arranged_problems += lineOne + lineTwo + lineThree + lineFour
  return arranged_problems