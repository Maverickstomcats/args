#args = take as many arguements as posssible 
def sum (*args): 
  total = 0 
  for arg in args:
    total += arg
  return total

print(sum(1,117))

#kwargs = key values for arguements, limitless like args 
#step above args
def a_sum(**kwargs):
  total = 0 
  for key,value in kwargs.items():
    print(f'{key} = {value}')
    total += value
  return total 
print(a_sum(x=3,y=5, z=22))