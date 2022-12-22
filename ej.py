x=1
while x <21:
  if(x==5):
    x+=1
    continue
  print(x, end=': ')
  a=2
  while a <x:     
    if x%a==0:
      print("no es primo")
      break
    a+=1
  else:
    print("es primo")
  x+=1
else:
  print('fin Algoritmo')



"""
for x in range(1,21):
  print(x, end=': ')
  for a in range(2,x):    
    if x%a==0:
      print("no es primo")
      break
  else:
    print("es primo")

"""