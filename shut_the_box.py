instructions = """

Instructions from: https://www.mastersofgames.com/rules/shut-box-rules.htm

A round of the game consists of each player taking one turn to try to shut the box. 
A turn consists of a player repeatedly throwing the dice until he or she cannot continue. 

Each throw of the dice is taken as follows:
If 7, 8 and 9 are all covered, the player decides whether to throw one die or two.
If any of these 3 numbers are still uncovered, the player must use both dice.
The player throws the die or dice into the box and adds up the pips. 
The player must then cover available numbers that add up to the total thrown. 

So for instance, if the total is 8, the player may choose one of the following options:


8

7, 1

6, 2

5, 3

5, 2, 1

4, 3, 1


Assuming that one of the options is available to be played, the player selects one, 
covers the selected number or numbers and proceeds to throw the dice again.

If none of the options are available because at least one number is already covered in each case, 
then the player's turn finishes and the player scores the sum of the numbers that are still uncovered. 
For example, if numbers 1, 5 and 9 are uncovered and the player throws a 4, options are 4 or 3 & 1, 
neither of which are available - so the turn finishes and the player's score is 15.

If anyone succeeds in shutting the box i.e. closing all the numbers, 
that player wins outright immediately and receives double the stake from all players. 
Otherwise, after each player has taken one turn, the winner of the round is the player with the lowest score.

"""

import random
import time


def shut_the_box(name):
  box = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
  response = ['Y','N','YES','NO']
  question1 = ''
  question4 = ''
  question5 = ''
  question6 = ''
  question7 = ''
  question8 = ''
  question9 = ''

  while question1 not in response:
    question1 = (input('\n\nDo you know how to play Shut the Box? (Y/N)  ')).upper().strip()
  if question1 == 'N' or question1 == 'NO':
    print(instructions)
    time.sleep(2)
    input('\n\nRespond with anything when you are ready to move on  ')
  time.sleep(2)
  print("\n\nIf after any roll, you are unable to make a play, type 'Done' in the response box.")
  time.sleep(4)
  print("\n\n{}, my friend. Let's begin..".format(name))
  time.sleep(2)
  print("\n\nHere's your box:", box)
  time.sleep(2)
  print('\n\tFirst roll...')
  time.sleep(2)
  first_roll = str(random.randint(2,12))
  print('\n\t...is a(n):  {}!'.format(first_roll))
  time.sleep(2)
  sum1 = 0
  while sum1 != int(first_roll):
    first_move = list(set((input('\nHow will you play? (ex: 1, 3, 4)  ')).upper().strip().split(',')))
    for item in first_move:
      if item == 'DONE':
        score = 0
        for num in box:
          score += int(num)
        return print('\n\nYour final score: {}'.format(score))
      else:
        break
    sum1_1 = 0
    for num in first_move:
      sum1_1 += int(num.strip())
    # need to verify that the numbers chosen are still in box
    for num in first_move:
      if num.strip() in box:
        continue
      else:
        sum1 = 0
    sum1 = sum1_1
  # need to remove decision from box
  for num in first_move:
    box.remove(num.strip())
  time.sleep(2)
  print('\n\nYour updated box:', box)

  # Second round
  time.sleep(2)
  print('\n\tSecond roll...')
  time.sleep(2)
  second_roll = str(random.randint(2,12))
  print('\n\t...is a(n):  {}!'.format(second_roll))
  time.sleep(2)
  sum2 = 0
  while sum2 != int(second_roll):
    second_move = list(set((input('\nHow will you play? (ex: 1, 3, 4)  ')).upper().strip().split(',')))
    for item in second_move:
      if item == 'DONE':
        score = 0
        for num in box:
          score += int(num)
        return print('\n\nYour final score: {}'.format(score))
      else:
        break
    sum2_2 = 0
    for num in second_move:
      sum2_2 += int(num.strip())
    # need to verify that the numbers chosen are still in box
    for num in second_move:
      if num.strip() in box:
        continue
      else:
        sum2 = 0
    sum2 = sum2_2
  # need to remove decision from box
  for num in second_move:
    box.remove(num.strip())
  time.sleep(2)
  print('\n\nYour updated box:', box)

  # Third round
  time.sleep(2)
  print('\n\tThird roll...')
  time.sleep(2)
  third_roll = str(random.randint(2,12))
  print('\n\t...is a(n):  {}!'.format(third_roll))
  time.sleep(2)
  sum3 = 0
  while sum3 != int(third_roll):
    third_move = list(set((input('\nHow will you play? (ex: 1, 3, 4)  ')).upper().strip().split(',')))
    for item in third_move:
      if item == 'DONE':
        score = 0
        for num in box:
          score += int(num)
        return print('\n\nYour final score: {}'.format(score))
      else:
        break
    sum3_3 = 0
    for num in third_move:
      sum3_3 += int(num.strip())
    # need to verify that the numbers chosen are still in box
    for num in third_move:
      if num.strip() in box:
        continue
      else:
        sum3 = 0
    sum3 = sum3_3
  # need to remove decision from box
  for num in third_move:
    box.remove(num.strip())
  time.sleep(2)
  print('\n\nYour updated box:', box)

  #Fourth round (7, 8, 9, could be gone, so must check first!)
  if ('7' in box) or ('8' in box) or ('9' in box):
    time.sleep(2)
    print('\n\tFourth roll...')
    time.sleep(2)
    fourth_roll = str(random.randint(2,12))
    print('\n\t...is a(n):  {}!'.format(fourth_roll))
    time.sleep(2)
    sum4 = 0
    while sum4 != int(fourth_roll):
      fourth_move = list(set((input('\nHow will you play? (ex: 1, 3, 4)  ')).upper().strip().split(',')))
      for item in fourth_move:
        if item == 'DONE':
          score = 0
          for num in box:
            score += int(num)
          return print('\n\nYour final score: {}'.format(score))
        else:
          break
      sum4_4 = 0
      for num in fourth_move:
        sum4_4 += int(num.strip())
    # need to verify that the numbers chosen are still in box
      for num in fourth_move:
        if num.strip() in box:
          continue
        else:
          sum4 = 0
      sum4 = sum4_4
    # need to remove decision from box
    for num in fourth_move:
      box.remove(num.strip())
    time.sleep(2)
    print('\n\nYour updated box:', box)
  # if 7, 8, 9 are all gone, player may use one dice
  else:
    while question4 not in response:
      question4 = (input('\n\nWith 7, 8, and 9 gone, you may now choose to only roll one die. Roll one die? (Y/N)  ')).upper().strip()
    if question4 == 'Y' or question4 == 'YES':
      #one die move:
      time.sleep(2)
      print('\n\tFourth roll...')
      time.sleep(2)
      fourth_roll = str(random.randint(1,6))
      print('\n\t...is a(n):  {}!'.format(fourth_roll))
      time.sleep(2)
      sum4 = 0
      while sum4 != int(fourth_roll):
        fourth_move = list(set((input('\nHow will you play? (ex: 1, 3, 4)  ')).upper().strip().split(',')))
        for item in fourth_move:
          if item == 'DONE':
            score = 0
            for num in box:
              score += int(num)
            return print('\n\nYour final score: {}'.format(score))
          else:
            break
        sum4_4 = 0
        for num in fourth_move:
          sum4_4 += int(num.strip())
      # need to verify that the numbers chosen are still in box
        for num in fourth_move:
          if num.strip() in box:
            continue
          else:
            sum4 = 0
        sum4 = sum4_4
      # need to remove decision from box
      for num in fourth_move:
        box.remove(num.strip())
      time.sleep(2)
      print('\n\nYour updated box:', box)
    else:
      time.sleep(2)
      print('\n\tFourth roll...')
      time.sleep(2)
      fourth_roll = str(random.randint(2,12))
      print('\n\t...is a(n):  {}!'.format(fourth_roll))
      time.sleep(2)
      sum4 = 0
      while sum4 != int(fourth_roll):
        fourth_move = list(set((input('\nHow will you play? (ex: 1, 3, 4)  ')).upper().strip().split(',')))
        for item in fourth_move:
          if item == 'DONE':
            score = 0
            for num in box:
              score += int(num)
            return print('\n\nYour final score: {}'.format(score))
          else:
            break
        sum4_4 = 0
        for num in fourth_move:
          sum4_4 += int(num.strip())
      # need to verify that the numbers chosen are still in box
        for num in fourth_move:
          if num.strip() in box:
            continue
          else:
            sum4 = 0
        sum4 = sum4_4
      # need to remove decision from box
      for num in fourth_move:
        box.remove(num.strip())
      time.sleep(2)
      print('\n\nYour updated box:', box)

  #Fifth round (7, 8, 9, could be gone, so must check first!)
  if len(box) == 0:
    return print('\n\nCongratulations! You won!')
  if ('7' in box) or ('8' in box) or ('9' in box):
    time.sleep(2)
    print('\n\tFifth roll...')
    time.sleep(2)
    fifth_roll = str(random.randint(2,12))
    print('\n\t...is a(n):  {}!'.format(fifth_roll))
    time.sleep(2)
    sum5 = 0
    while sum5 != int(fifth_roll):
      fifth_move = list(set((input('\nHow will you play? (ex: 1, 3, 4)  ')).upper().strip().split(',')))
      for item in fifth_move:
        if item == 'DONE':
          score = 0
          for num in box:
            score += int(num)
          return print('\n\nYour final score: {}'.format(score))
        else:
          break
      sum5_5 = 0
      for num in fifth_move:
        sum5_5 += int(num.strip())
    # need to verify that the numbers chosen are still in box
      for num in fifth_move:
        if num.strip() in box:
          continue
        else:
          sum5 = 0
      sum5 = sum5_5
    # need to remove decision from box
    for num in fifth_move:
      box.remove(num.strip())
    time.sleep(2)
    print('\n\nYour updated box:', box)
  # if 7, 8, 9 are all gone, player may use one dice
  else:
    while question5 not in response:
      question5 = (input('\n\nWith 7, 8, and 9 gone, you may now choose to only roll one die. Roll one die? (Y/N)  ')).upper().strip()
    if question5 == 'Y' or question5 == 'YES':
      #one die move:
      time.sleep(2)
      print('\n\tFifth roll...')
      time.sleep(2)
      fifth_roll = str(random.randint(1,6))
      print('\n\t...is a(n):  {}!'.format(fifth_roll))
      time.sleep(2)
      sum5 = 0
      while sum5 != int(fifth_roll):
        fifth_move = list(set((input('\nHow will you play? (ex: 1, 3, 4)  ')).upper().strip().split(',')))
        for item in fifth_move:
          if item == 'DONE':
            score = 0
            for num in box:
              score += int(num)
            return print('\n\nYour final score: {}'.format(score))
          else:
            break
        sum5_5 = 0
        for num in fifth_move:
          sum5_5 += int(num.strip())
      # need to verify that the numbers chosen are still in box
        for num in fifth_move:
          if num.strip() in box:
            continue
          else:
            sum5 = 0
        sum5 = sum5_5
      # need to remove decision from box
      for num in fifth_move:
        box.remove(num.strip())
      time.sleep(2)
      print('\n\nYour updated box:', box)
    else:
      time.sleep(2)
      print('\n\tFifth roll...')
      time.sleep(2)
      fifth_roll = str(random.randint(2,12))
      print('\n\t...is a(n):  {}!'.format(fifth_roll))
      time.sleep(2)
      sum5 = 0
      while sum5 != int(fifth_roll):
        fifth_move = list(set((input('\nHow will you play? (ex: 1, 3, 4)  ')).upper().strip().split(',')))
        for item in fifth_move:
          if item == 'DONE':
            score = 0
            for num in box:
              score += int(num)
            return print('\n\nYour final score: {}'.format(score))
          else:
            break
        sum5_5 = 0
        for num in fifth_move:
          sum5_5 += int(num.strip())
      # need to verify that the numbers chosen are still in box
        for num in fifth_move:
          if num.strip() in box:
            continue
          else:
            sum5 = 0
        sum5 = sum5_5
      # need to remove decision from box
      for num in fifth_move:
        box.remove(num.strip())
      time.sleep(2)
      print('\n\nYour updated box:', box)

  # Sixth round (7, 8, 9, could be gone, so must check first!)
  if len(box) == 0:
    return print('\n\nCongratulations! You won!')
  if ('7' in box) or ('8' in box) or ('9' in box):
    time.sleep(2)
    print('\n\tSixth roll...')
    time.sleep(2)
    sixth_roll = str(random.randint(2,12))
    print('\n\t...is a(n):  {}!'.format(sixth_roll))
    time.sleep(2)
    sum6 = 0
    while sum6 != int(sixth_roll):
      sixth_move = list(set((input('\nHow will you play? (ex: 1, 3, 4)  ')).upper().strip().split(',')))
      for item in sixth_move:
        if item == 'DONE':
          score = 0
          for num in box:
            score += int(num)
          return print('\n\nYour final score: {}'.format(score))
        else:
          break
      sum6_6 = 0
      for num in sixth_move:
        sum6_6 += int(num.strip())
    # need to verify that the numbers chosen are still in box
      for num in sixth_move:
        if num.strip() in box:
          continue
        else:
          sum6 = 0
      sum6 = sum6_6
    # need to remove decision from box
    for num in sixth_move:
      box.remove(num.strip())
    time.sleep(2)
    print('\n\nYour updated box:', box)
  # if 7, 8, 9 are all gone, player may use one dice
  else:
    while question6 not in response:
      question6 = (input('\n\nWith 7, 8, and 9 gone, you may now choose to only roll one die. Roll one die? (Y/N)  ')).upper().strip()
    if question6 == 'Y' or question6 == 'YES':
      #one die move:
      time.sleep(2)
      print('\n\tSixth roll...')
      time.sleep(2)
      sixth_roll = str(random.randint(1,6))
      print('\n\t...is a(n):  {}!'.format(sixth_roll))
      time.sleep(2)
      sum6 = 0
      while sum6 != int(sixth_roll):
        sixth_move = list(set((input('\nHow will you play? (ex: 1, 3, 4)  ')).upper().strip().split(',')))
        for item in sixth_move:
          if item == 'DONE':
            score = 0
            for num in box:
              score += int(num)
            return print('\n\nYour final score: {}'.format(score))
          else:
            break
        sum6_6 = 0
        for num in sixth_move:
          sum6_6 += int(num.strip())
      # need to verify that the numbers chosen are still in box
        for num in sixth_move:
          if num.strip() in box:
            continue
          else:
            sum6 = 0
        sum6 = sum6_6
      # need to remove decision from box
      for num in sixth_move:
        box.remove(num.strip())
      time.sleep(2)
      print('\n\nYour updated box:', box)
    else:
      time.sleep(2)
      print('\n\tSixth roll...')
      time.sleep(2)
      sixth_roll = str(random.randint(2,12))
      print('\n\t...is a(n):  {}!'.format(sixth_roll))
      time.sleep(2)
      sum6 = 0
      while sum6 != int(sixth_roll):
        sixth_move = list(set((input('\nHow will you play? (ex: 1, 3, 4)  ')).upper().strip().split(',')))
        for item in sixth_move:
          if item == 'DONE':
            score = 0
            for num in box:
              score += int(num)
            return print('\n\nYour final score: {}'.format(score))
          else:
            break
        sum6_6 = 0
        for num in sixth_move:
          sum6_6 += int(num.strip())
      # need to verify that the numbers chosen are still in box
        for num in sixth_move:
          if num.strip() in box:
            continue
          else:
            sum6 = 0
        sum6 = sum6_6
      # need to remove decision from box
      for num in sixth_move:
        box.remove(num.strip())
      time.sleep(2)
      print('\n\nYour updated box:', box)

  # Seventh round (7, 8, 9, could be gone, so must check first!)
  if len(box) == 0:
    return print('\n\nCongratulations! You won!')
  if ('7' in box) or ('8' in box) or ('9' in box):
    time.sleep(2)
    print('\n\tSeventh roll...')
    time.sleep(2)
    seventh_roll = str(random.randint(2,12))
    print('\n\t...is a(n):  {}!'.format(seventh_roll))
    time.sleep(2)
    sum7 = 0
    while sum7 != int(seventh_roll):
      seventh_move = list(set((input('\nHow will you play? (ex: 1, 3, 4)  ')).upper().strip().split(',')))
      for item in seventh_move:
        if item == 'DONE':
          score = 0
          for num in box:
            score += int(num)
          return print('\n\nYour final score: {}'.format(score))
        else:
          break
      sum7_7 = 0
      for num in seventh_move:
        sum7_7 += int(num.strip())
    # need to verify that the numbers chosen are still in box
      for num in seventh_move:
        if num.strip() in box:
          continue
        else:
          sum7 = 0
      sum7 = sum7_7
    # need to remove decision from box
    for num in seventh_move:
      box.remove(num.strip())
    time.sleep(2)
    print('\n\nYour updated box:', box)
  # if 7, 8, 9 are all gone, player may use one dice
  else:
    while question7 not in response:
      question7 = (input('\n\nWith 7, 8, and 9 gone, you may now choose to only roll one die. Roll one die? (Y/N)  ')).upper().strip()
    if question7 == 'Y' or question7 == 'YES':
      #one die move:
      time.sleep(2)
      print('\n\tSeventh roll...')
      time.sleep(2)
      seventh_roll = str(random.randint(1,6))
      print('\n\t...is a(n):  {}!'.format(seventh_roll))
      time.sleep(2)
      sum7 = 0
      while sum7 != int(seventh_roll):
        seventh_move = list(set((input('\nHow will you play? (ex: 1, 3, 4)  ')).upper().strip().split(',')))
        for item in seventh_move:
          if item == 'DONE':
            score = 0
            for num in box:
              score += int(num)
            return print('\n\nYour final score: {}'.format(score))
          else:
            break
        sum7_7 = 0
        for num in seventh_move:
          sum7_7 += int(num.strip())
      # need to verify that the numbers chosen are still in box
        for num in seventh_move:
          if num.strip() in box:
            continue
          else:
            sum7 = 0
        sum7 = sum7_7
      # need to remove decision from box
      for num in seventh_move:
        box.remove(num.strip())
      time.sleep(2)
      print('\n\nYour updated box:', box)
    else:
      time.sleep(2)
      print('\n\tSeventh roll...')
      time.sleep(2)
      seventh_roll = str(random.randint(2,12))
      print('\n\t...is a(n):  {}!'.format(seventh_roll))
      time.sleep(2)
      sum7 = 0
      while sum7 != int(seventh_roll):
        seventh_move = list(set((input('\nHow will you play? (ex: 1, 3, 4)  ')).upper().strip().split(',')))
        for item in seventh_move:
          if item == 'DONE':
            score = 0
            for num in box:
              score += int(num)
            return print('\n\nYour final score: {}'.format(score))
          else:
            break
        sum7_7 = 0
        for num in seventh_move:
          sum7_7 += int(num.strip())
      # need to verify that the numbers chosen are still in box
        for num in seventh_move:
          if num.strip() in box:
            continue
          else:
            sum7 = 0
        sum7 = sum7_7
      # need to remove decision from box
      for num in seventh_move:
        box.remove(num.strip())
      time.sleep(2)
      print('\n\nYour updated box:', box)

  # Eighth round (7, 8, 9, could be gone, so must check first!)
  if len(box) == 0:
    return print('\n\nCongratulations! You won!')
  if ('7' in box) or ('8' in box) or ('9' in box):
    time.sleep(2)
    print('\n\tEighth roll...')
    time.sleep(2)
    eighth_roll = str(random.randint(2,12))
    print('\n\t...is a(n):  {}!'.format(eighth_roll))
    time.sleep(2)
    sum8 = 0
    while sum8 != int(eighth_roll):
      eighth_move = list(set((input('\nHow will you play? (ex: 1, 3, 4)  ')).upper().strip().split(',')))
      for item in eighth_move:
        if item == 'DONE':
          score = 0
          for num in box:
            score += int(num)
          return print('\n\nYour final score: {}'.format(score))
        else:
          break
      sum8_8 = 0
      for num in eighth_move:
        sum8_8 += int(num.strip())
    # need to verify that the numbers chosen are still in box
      for num in eighth_move:
        if num.strip() in box:
          continue
        else:
          sum8 = 0
      sum8 = sum8_8
    # need to remove decision from box
    for num in eighth_move:
      box.remove(num.strip())
    time.sleep(2)
    print('\n\nYour updated box:', box)
  # if 7, 8, 9 are all gone, player may use one dice
  else:
    while question8 not in response:
      question8 = (input('\n\nWith 7, 8, and 9 gone, you may now choose to only roll one die. Roll one die? (Y/N)  ')).upper().strip()
    if question8 == 'Y' or question8 == 'YES':
      #one die move:
      time.sleep(2)
      print('\n\tEighth roll...')
      time.sleep(2)
      eighth_roll = str(random.randint(1,6))
      print('\n\t...is a(n):  {}!'.format(eighth_roll))
      time.sleep(2)
      sum8 = 0
      while sum8 != int(eighth_roll):
        eighth_move = list(set((input('\nHow will you play? (ex: 1, 3, 4)  ')).upper().strip().split(',')))
        for item in eighth_move:
          if item == 'DONE':
            score = 0
            for num in box:
              score += int(num)
            return print('\n\nYour final score: {}'.format(score))
          else:
            break
        sum8_8 = 0
        for num in eighth_move:
          sum8_8 += int(num.strip())
      # need to verify that the numbers chosen are still in box
        for num in eighth_move:
          if num.strip() in box:
            continue
          else:
            sum8 = 0
        sum8 = sum8_8
      # need to remove decision from box
      for num in eighth_move:
        box.remove(num.strip())
      time.sleep(2)
      print('\n\nYour updated box:', box)
    else:
      time.sleep(2)
      print('\n\tEighth roll...')
      time.sleep(2)
      eighth_roll = str(random.randint(2,12))
      print('\n\t...is a(n):  {}!'.format(eighth_roll))
      time.sleep(2)
      sum8 = 0
      while sum8 != int(eighth_roll):
        eighth_move = list(set((input('\nHow will you play? (ex: 1, 3, 4)  ')).upper().strip().split(',')))
        for item in eighth_move:
          if item == 'DONE':
            score = 0
            for num in box:
              score += int(num)
            return print('\n\nYour final score: {}'.format(score))
          else:
            break
        sum8_8 = 0
        for num in eighth_move:
          sum8_8 += int(num.strip())
      # need to verify that the numbers chosen are still in box
        for num in eighth_move:
          if num.strip() in box:
            continue
          else:
            sum8 = 0
        sum8 = sum8_8
      # need to remove decision from box
      for num in eighth_move:
        box.remove(num.strip())
      time.sleep(2)
      print('\n\nYour updated box:', box)

  # Ninth round (7, 8, 9, could be gone, so must check first!)
  if len(box) == 0:
    return print('\n\nCongratulations! You won!')
  if ('7' in box) or ('8' in box) or ('9' in box):
    time.sleep(2)
    print('\n\tNinth roll...')
    time.sleep(2)
    ninth_roll = str(random.randint(2,12))
    print('\n\t...is a(n):  {}!'.format(ninth_roll))
    time.sleep(2)
    sum9 = 0
    while sum9 != int(ninth_roll):
      ninth_move = list(set((input('\nHow will you play? (ex: 1, 3, 4)  ')).upper().strip().split(',')))
      for item in ninth_move:
        if item == 'DONE':
          score = 0
          for num in box:
            score += int(num)
          return print('\n\nYour final score: {}'.format(score))
        else:
          break
      sum9_9 = 0
      for num in ninth_move:
        sum9_9 += int(num.strip())
    # need to verify that the numbers chosen are still in box
      for num in ninth_move:
        if num.strip() in box:
          continue
        else:
          sum9 = 0
      sum9 = sum9_9
    # need to remove decision from box
    for num in ninth_move:
      box.remove(num.strip())
    time.sleep(2)
    print('\n\nYour updated box:', box)
  # if 7, 8, 9 are all gone, player may use one dice
  else:
    while question9 not in response:
      question9 = (input('\n\nWith 7, 8, and 9 gone, you may now choose to only roll one die. Roll one die? (Y/N)  ')).upper().strip()
    if question9 == 'Y' or question9 == 'YES':
      #one die move:
      time.sleep(2)
      print('\n\tNinth roll...')
      time.sleep(2)
      ninth_roll = str(random.randint(1,6))
      print('\n\t...is a(n):  {}!'.format(ninth_roll))
      time.sleep(2)
      sum9 = 0
      while sum9 != int(ninth_roll):
        ninth_move = list(set((input('\nHow will you play? (ex: 1, 3, 4)  ')).upper().strip().split(',')))
        for item in ninth_move:
          if item == 'DONE':
            score = 0
            for num in box:
              score += int(num)
            return print('\n\nYour final score: {}'.format(score))
          else:
            break
        sum9_9 = 0
        for num in ninth_move:
          sum9_9 += int(num.strip())
      # need to verify that the numbers chosen are still in box
        for num in ninth_move:
          if num.strip() in box:
            continue
          else:
            sum9 = 0
        sum9 = sum9_9
      # need to remove decision from box
      for num in ninth_move:
        box.remove(num.strip())
      time.sleep(2)
      print('\n\nYour updated box:', box)
    else:
      time.sleep(2)
      print('\n\tNinth roll...')
      time.sleep(2)
      ninth_roll = str(random.randint(2,12))
      print('\n\t...is a(n):  {}!'.format(ninth_roll))
      time.sleep(2)
      sum9 = 0
      while sum9 != int(ninth_roll):
        ninth_move = list(set((input('\nHow will you play? (ex: 1, 3, 4)  ')).upper().strip().split(',')))
        for item in ninth_move:
          if item == 'DONE':
            score = 0
            for num in box:
              score += int(num)
            return print('\n\nYour final score: {}'.format(score))
          else:
            break
        sum9_9 = 0
        for num in ninth_move:
          sum9_9 += int(num.strip())
      # need to verify that the numbers chosen are still in box
        for num in ninth_move:
          if num.strip() in box:
            continue
          else:
            sum9 = 0
        sum9 = sum9_9
      # need to remove decision from box
      for num in ninth_move:
        box.remove(num.strip())
      time.sleep(2)
      print('\n\nYour updated box:', box)
      
  if len(box) == 0:
    return print('\n\nCongratulations! You won!')



if __name__ == '__main__':
  shut_the_box(input("\n\nWelcome to the Pub, what shall ye be called?  "))
