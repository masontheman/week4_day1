places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]
list(filter(lambda x: False if x.strip(' ') == '' else x ,places))

author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]
author.sort(key = lambda x: x.lower().split()[len(x.split())-1][0])
print(author)

places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]
list(map(lambda x: (x[0],(9/5)*x[1] + 32),places))

def fibb(num,x,y,z):
  if num == 0:return y
  else:
    z = x+y
    x = y
    y =z
    return fibb(num-1,x,y,z)
fibb(5,0,1,0)

def gen(num):
  while num != 0:
    yield num**2
    num -=1
infinite_gen = gen(5)
next(infinite_gen)
next(infinite_gen)
next(infinite_gen)