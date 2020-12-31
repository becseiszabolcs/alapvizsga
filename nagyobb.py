a=int(input('Adj egy számot! '))
b=int(input('Adj egy másik számot! '))
if a==b:
  print('A kétszám engyelő')
elif a<b:
  print(f'A nagyobb érték {b}.')
else:
  print(f'A nagyobb érték {a}')
