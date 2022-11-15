#args = take as many arguements as posssible 
def sum (*args): 
  total = 0 
  for arg in args:
    total += arg
  return total

print(sum(1,117))

#kwargs = key values for arguements, limitless like args 