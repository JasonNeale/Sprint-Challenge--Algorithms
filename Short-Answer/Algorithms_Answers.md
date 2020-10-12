#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
Runtime would be O(n) because the function is linear. It will keep going until a = n * n * n

b)
Runtime would be O(n). Runtime is dependent on the size of n but is still a linear function.

c)
Runtime would be O(c^n). This is a recursive function dependent on the input of bunnies.

## Exercise II

to determine if the egg will break from the current floor in the building
loop through the floors in n 
if the current floor is equal to or greater than 'f' then the egg will break (true)
if the current floor is less than 'f' then the egg will not break (false)

def CkeckEggBreakability(n, f):
    if floor => f:
      return true
    elif floor < f:
      return false

Complexity: O(n)