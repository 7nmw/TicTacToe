#cran – решетка игры
#proverka – принимает и проверяет ввод пользователя
#pobeda – проверяет выиграл ли игрок
#zapusk –  запускает функции
print("""
Крестики-нолики
Игроки X и O вводят по очереди цифры от 1 до 9
Начало игры
""")

cran = list(range(1, 10))

def create_tabl(cran):
   print("#" * 13)
   for i in range(3):
      print("#", cran[0+i*3], "#", cran[1+i*3], "#", cran[2+i*3], "#")
      print("#" * 13)

def proverka(chislo):
   valid = False
   while not valid:
      otvet = input("Введите целое число от 1 до 9. Игрок" + chislo + "?")
      try:
         otvet = int(otvet)
      except:
         print("Error. Введите целое число от 1 до 9?")
         continue
      if 1 <= otvet <= 9:
          if(str(cran[otvet-1]) not in "XO"):
              cran[otvet-1] = chislo
              valid = True
          else:
              print("Такой ход уже был. Сделайте другой ход")
      else:
          print("Error. Введите целое число от 1 до 9.")

def pobeda(cran):
   pobeda_cod = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in pobeda_cod:
       if cran[each[0]] == cran[each[1]] == cran[each[2]]:
          return cran[each[0]]
   return False

def zapusk(cran):
    counter = 0
    win = False
    while not win:
        create_tabl(cran)
        if counter % 2 == 0:
           proverka("X")
        else:
           proverka("O")
        counter += 1
        if counter > 4:
           fin = pobeda(cran)
           if fin:
              print(fin, "игрок победил")
              win = True
              break
        if counter == 9:
            print("ничья")
            break
    create_tabl(cran)
zapusk(cran)