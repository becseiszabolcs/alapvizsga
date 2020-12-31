h = int(input('Hány óra van most? '))
if 7<h<16:
  print('A bolt nyitva van. ')
  print(f'Ennyi órád van még odaérni: {16-h}')
else:
  print('A bolt zárva van.')