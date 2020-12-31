a=len(input('adj egy szót! '))
b=len(input('adj egy másik szót! '))
if a==b:
  print('A két szó egyforma hosszú')
elif a<b:
  print(f'A hosszabb szó {b}.')
else:
  print(f'A hosszabb szó {a}')