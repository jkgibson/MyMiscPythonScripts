def collatz(number):
    
    if number % 2 == 0:
        
        return number // 2
      #  print(str(number))
        
    elif number % 2 == 1:
       
        return 3 * number + 1
     #   print(str(number))
  
    
print('This program explores the Collatz sequence.')

print('Type in any number.')

try:
    newInput=int(input())
except ValueError:
    print('Enter an integer, dipshit.')

newInput=int(input())

while collatz(newInput) > 1:
    newInput = collatz(newInput)    
    print(str(newInput))

   
print(str(collatz(newInput)))
       
    
