import random
import time
import sys

class Hand:

  def __init__(self,hand=[],display=[],value=0):
    self.hand = []
    self.display = []
    self.value = 0

  def deal_card(self):
    possible_cards = ['A ','2 ','3 ','4 ','5 ','6 ','7 ','8 ','9 ','10','J ','Q ','K ']
    card = random.choice(possible_cards)
    card_display = [' -----','|     |','|  {} |'.format(card),'|     |',' -----']
    card_values = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':1}

    self.hand.append(card)
    self.display.append(card_display)
    self.value += card_values[card.strip()]

  def print_value(self):
    if 'A ' in self.hand and (self.value + 10 < 22):
      print('{} or {}'.format(self.value, self.value+10))
      
    else:
      print('{}'.format(self.value))
  

  def print_hand(self):
    if len(self.display) == 1:
      for a in self.display[0]:
        print(a)

    elif len(self.display) == 2:
      for a,b in zip(*self.display):
        print(a + '\t' + b)

    elif len(self.display) == 3:
      for a,b,c in zip(*self.display):
        print(a + '\t' + b + '\t' + c)

    elif len(self.display) == 4:
      for a,b,c,d in zip(*self.display):
        print(a + '\t' + b + '\t' + c + '\t' + d)

    elif len(self.display) == 5:
      for a,b,c,d,e in zip(*self.display):
        print(a + '\t' + b + '\t' + c + '\t' + d + '\t' + e)

    elif len(self.display) == 6:
      for a,b,c,d,e,f in zip(*self.display):
        print(a + '\t' + b + '\t' + c + '\t' + d + '\t' + e + '\t' + f)

    elif len(self.display) == 7:
      for a,b,c,d,e,f,g in zip(*self.display):
        print(a + '\t' + b + '\t' + c + '\t' + d + '\t' + e + '\t' + f + '\t' + g)
 
    elif len(self.display) == 8:
      for a,b,c,d,e,f,g,h in zip(*self.display):
        print(a + '\t' + b + '\t' + c + '\t' + d + '\t' + e + '\t' + f + '\t' + g + '\t' + h)

    elif len(self.display) == 9:
      for a,b,c,d,e,f,g,h,i in zip(*self.display):
        print(a + '\t' + b + '\t' + c + '\t' + d + '\t' + e + '\t' + f + '\t' + g + '\t' + h + '\t' + i)

    elif len(self.display) == 10:
      for a,b,c,d,e,f,g,h,i,j in zip(*self.display):
        print(a + '\t' + b + '\t' + c + '\t' + d + '\t' + e + '\t' + f + '\t' + g + '\t' + h + '\t' + i + '\t' + j)


def game(name,player_pot,wager):
  name = Hand()
  dealer = Hand()
  name.deal_card()
  name.deal_card()
  dealer.deal_card()
  print("\n\nDealer's up card:")
  dealer.print_hand() 
  dealer.deal_card() # dealer's second card, not showing, but will use to check for blackjack
  time.sleep(2)
  print('\nYour hand:')
  name.print_hand()
  time.sleep(2)
  if 'A ' in name.hand and (name.value + 10) == 21:
    if 'A ' in dealer.hand and (dealer.value + 10) == 21:
      time.sleep(2)
      print("\nDealer's hand:")
      dealer.print_hand()
      time.sleep(2)
      print("\nWow, blackjacks all around..")
      return player_pot
    else:
      time.sleep(2)
      print('\nBlackjack! Congrats, you win the hand!')
      player_pot += (wager + (wager // 2))
      return player_pot
  elif 'A ' in dealer.hand and (dealer.value + 10) == 21:
    time.sleep(2)
    print("\nDealer's hand:")
    dealer.print_hand()
    time.sleep(2)
    print("\nHouse wins with blackjack..")
    player_pot -= wager
    return player_pot
  print('\nYour total:')
  name.print_value()
  time.sleep(2)
  response = ''
  if name.value in [9,10,11] and (player_pot >= wager*2):
    double_down = ''
    while double_down not in ['YES','NO','Y','N']:
      double_down = (input('\nWould you like to double down? (Y/N)  ')).strip().upper()
    if double_down in ['YES','Y']:
      wager += wager
      response = 'HIT'

  # Since dealer's up card has been printed, can finish out dealer's hand on the backend:
  if 'A ' in dealer.hand and (dealer.value + 10) > 16 and (dealer.value + 10) < 22:
    dealer.value += 10
  elif dealer.value < 17:
    dealer.deal_card()
    if 'A ' in dealer.hand and (dealer.value + 10) > 16 and (dealer.value + 10) < 22:
      dealer.value += 10
    elif dealer.value < 17:
      dealer.deal_card()
      if 'A ' in dealer.hand and (dealer.value + 10) > 16 and (dealer.value + 10) < 22:
        dealer.value += 10
      elif dealer.value < 17:
        dealer.deal_card()
        if 'A ' in dealer.hand and (dealer.value + 10) > 16 and (dealer.value + 10) < 22:
          dealer.value += 10
        elif dealer.value < 17:
          dealer.deal_card()
          if 'A ' in dealer.hand and (dealer.value + 10) > 16 and (dealer.value + 10) < 22:
            dealer.value += 10
          elif dealer.value < 17:
            dealer.deal_card()
            if 'A ' in dealer.hand and (dealer.value + 10) > 16 and (dealer.value + 10) < 22:
              dealer.value += 10
            elif dealer.value < 17:
              dealer.deal_card()
              if 'A ' in dealer.hand and (dealer.value + 10) > 16 and (dealer.value + 10) < 22:
                dealer.value += 10
              elif dealer.value < 17:
                dealer.deal_card()
                if 'A ' in dealer.hand and (dealer.value + 10) > 16 and (dealer.value + 10) < 22:
                  dealer.value += 10
                elif dealer.value < 17:
                  dealer.deal_card()
                  if 'A ' in dealer.hand and (dealer.value + 10) > 16 and (dealer.value + 10) < 22:
                    dealer.value += 10

  #dealer.value is dealer's final score
  #dealer.print_hand() is dealer's cards displayed

  time.sleep(2)
  while response not in ['HIT','STAY']:
    response = input('\nHit or Stay?:  ').strip().upper()
  if response == 'STAY':
    if 'A ' in name.hand and (name.value + 10) < 22:
      name.value += 10
    time.sleep(2)
    print("\nDealer's hand:")
    dealer.print_hand()
    time.sleep(2)
    print("\nDealer's total:  {}".format(dealer.value))
    time.sleep(2)
    if dealer.value > 21:
      print('\n\nDealer busted, you won the hand!')
      player_pot += wager
      return player_pot
    elif name.value > dealer.value:
      print('\n\nYou won the hand!')
      player_pot += wager
      return player_pot
    elif name.value == dealer.value:
      print('\n\nWhen push comes to shove..')
      return player_pot
    elif name.value < dealer.value:
      print('\n\nHouse wins.')
      player_pot -= wager
      return player_pot
  
  else:
    time.sleep(2)
    name.deal_card()
    print('\nYour hand:')
    name.print_hand()
    time.sleep(2)
    print('\nYour total:')
    name.print_value()
    time.sleep(2)
    if name.value > 21:
      print('\nBusted!')
      player_pot -= wager
      return player_pot
    response = ''
    while response not in ['HIT','STAY']:
      response = input('\nHit or Stay?:  ').strip().upper()
    if response == 'STAY' or double_down in ['YES','Y']:
      if 'A ' in name.hand and (name.value + 10) < 22:
        name.value += 10
      time.sleep(2)
      print("\nDealer's hand:")
      dealer.print_hand()
      time.sleep(2)
      print("\nDealer's total:  {}".format(dealer.value))
      time.sleep(2)
      if dealer.value > 21:
        print('\n\nDealer busted, you won the hand!')
        player_pot += wager
        return player_pot
      elif name.value > dealer.value:
        print('\n\nYou won the hand!')
        player_pot += wager
        return player_pot
      elif name.value == dealer.value:
        print('\n\nWhen push comes to shove..')
        return player_pot
      elif name.value < dealer.value:
        print('\n\nHouse wins.')
        player_pot -= wager
        return player_pot
    
    else:
      time.sleep(2)
      name.deal_card()
      print('\nYour hand:')
      name.print_hand()
      time.sleep(2)
      print('\nYour total:')
      name.print_value()
      time.sleep(2)
      if name.value > 21:
        print('\nBusted!')
        player_pot -= wager
        return player_pot
      response = ''
      while response not in ['HIT','STAY']:
        response = input('\nHit or Stay?:  ').strip().upper()
      if response == 'STAY':
        if 'A ' in name.hand and (name.value + 10) < 22:
          name.value += 10
        time.sleep(2)
        print("\nDealer's hand:")
        dealer.print_hand()
        time.sleep(2)
        print("\nDealer's total:  {}".format(dealer.value))
        time.sleep(2)
        if dealer.value > 21:
          print('\n\nDealer busted, you won the hand!')
          player_pot += wager
          return player_pot
        elif name.value > dealer.value:
          print('\n\nYou won the hand!')
          player_pot += wager
          return player_pot
        elif name.value == dealer.value:
          print('\n\nWhen push comes to shove..')
          return player_pot
        elif name.value < dealer.value:
          print('\n\nHouse wins.')
          player_pot -= wager
          return player_pot
        
      else:
        time.sleep(2)
        name.deal_card()
        print('\nYour hand:')
        name.print_hand()
        time.sleep(2)
        print('\nYour total:')
        name.print_value()
        time.sleep(2)
        if name.value > 21:
          print('\nBusted!')
          player_pot -= wager
          return player_pot
        response = ''
        while response not in ['HIT','STAY']:
          response = input('\nHit or Stay?:  ').strip().upper()
        if response == 'STAY':
          if 'A ' in name.hand and (name.value + 10) < 22:
            name.value += 10
          time.sleep(2)
          print("\nDealer's hand:")
          dealer.print_hand()
          time.sleep(2)
          print("\nDealer's total:  {}".format(dealer.value))
          time.sleep(2)
          if dealer.value > 21:
            print('\n\nDealer busted, you won the hand!')
            player_pot += wager
            return player_pot
          elif name.value > dealer.value:
            print('\n\nYou won the hand!')
            player_pot += wager
            return player_pot
          elif name.value == dealer.value:
            print('\n\nWhen push comes to shove..')
            return player_pot
          elif name.value < dealer.value:
            print('\n\nHouse wins.')
            player_pot -= wager
            return player_pot

        else:
          time.sleep(2)
          name.deal_card()
          print('\nYour hand:')
          name.print_hand()
          time.sleep(2)
          print('\nYour total:')
          name.print_value()
          time.sleep(2)
          if name.value > 21:
            print('\nBusted!')
            player_pot -= wager
            return player_pot
          response = ''
          while response not in ['HIT','STAY']:
            response = input('\nHit or Stay?:  ').strip().upper()
          if response == 'STAY':
            if 'A ' in name.hand and (name.value + 10) < 22:
              name.value += 10
            time.sleep(2)
            print("\nDealer's hand:")
            dealer.print_hand()
            time.sleep(2)
            print("\nDealer's total:  {}".format(dealer.value))
            time.sleep(2)
            if dealer.value > 21:
              print('\n\nDealer busted, you won the hand!')
              player_pot += wager
              return player_pot
            elif name.value > dealer.value:
              print('\n\nYou won the hand!')
              player_pot += wager
              return player_pot
            elif name.value == dealer.value:
              print('\n\nWhen push comes to shove..')
              return player_pot
            elif name.value < dealer.value:
              print('\n\nHouse wins.')
              player_pot -= wager
              return player_pot

          else:
            time.sleep(2)
            name.deal_card()
            print('\nYour hand:')
            name.print_hand()
            time.sleep(2)
            print('\nYour total:')
            name.print_value()
            time.sleep(2)
            if name.value > 21:
              print('\nBusted!')
              player_pot -= wager
              return player_pot
            response = ''
            while response not in ['HIT','STAY']:
              response = input('\nHit or Stay?:  ').strip().upper()
            if response == 'STAY':
              if 'A ' in name.hand and (name.value + 10) < 22:
                name.value += 10
              time.sleep(2)
              print("\nDealer's hand:")
              dealer.print_hand()
              time.sleep(2)
              print("\nDealer's total:  {}".format(dealer.value))
              time.sleep(2)
              if dealer.value > 21:
                print('\n\nDealer busted, you won the hand!')
                player_pot += wager
                return player_pot
              elif name.value > dealer.value:
                print('\n\nYou won the hand!')
                player_pot += wager
                return player_pot
              elif name.value == dealer.value:
                print('\n\nWhen push comes to shove..')
                return player_pot
              elif name.value < dealer.value:
                print('\n\nHouse wins.')
                player_pot -= wager
                return player_pot

            else:
              time.sleep(2)
              name.deal_card()
              print('\nYour hand:')
              name.print_hand()
              time.sleep(2)
              print('\nYour total:')
              name.print_value()
              time.sleep(2)
              if name.value > 21:
                print('\nBusted!')
                player_pot -= wager
                return player_pot
              response = ''
              while response not in ['HIT','STAY']:
                response = input('\nHit or Stay?:  ').strip().upper()
              if response == 'STAY':
                if 'A ' in name.hand and (name.value + 10) < 22:
                  name.value += 10
                time.sleep(2)
                print("\nDealer's hand:")
                dealer.print_hand()
                time.sleep(2)
                print("\nDealer's total:  {}".format(dealer.value))
                time.sleep(2)
                if dealer.value > 21:
                  print('\n\nDealer busted, you won the hand!')
                  player_pot += wager
                  return player_pot
                elif name.value > dealer.value:
                  print('\n\nYou won the hand!')
                  player_pot += wager
                  return player_pot
                elif name.value == dealer.value:
                  print('\n\nWhen push comes to shove..')
                  return player_pot
                elif name.value < dealer.value:
                  print('\n\nHouse wins.')
                  player_pot -= wager
                  return player_pot

              else:
                time.sleep(2)
                name.deal_card()
                print('\nYour hand:')
                name.print_hand()
                time.sleep(2)
                print('\nYour total:')
                name.print_value()
                time.sleep(2)
                if name.value > 21:
                  print('\nBusted!')
                  player_pot -= wager
                  return player_pot
                response = ''
                while response not in ['HIT','STAY']:
                  response = input('\nHit or Stay?:  ').strip().upper()
                if response == 'STAY':
                  if 'A ' in name.hand and (name.value + 10) < 22:
                    name.value += 10
                  time.sleep(2)
                  print("\nDealer's hand:")
                  dealer.print_hand()
                  time.sleep(2)
                  print("\nDealer's total:  {}".format(dealer.value))
                  time.sleep(2)
                  if dealer.value > 21:
                    print('\n\nDealer busted, you won the hand!')
                    player_pot += wager
                    return player_pot
                  elif name.value > dealer.value:
                    print('\n\nYou won the hand!')
                    player_pot += wager
                    return player_pot
                  elif name.value == dealer.value:
                    print('\n\nWhen push comes to shove..')
                    return player_pot
                  elif name.value < dealer.value:
                    print('\n\nHouse wins.')
                    player_pot -= wager
                    return player_pot

                else:
                  time.sleep(2)
                  name.deal_card()
                  print('\nYour hand:')
                  name.print_hand()
                  time.sleep(2)
                  print('\nYour total:')
                  name.print_value()
                  time.sleep(2)
                  if name.value > 21:
                    print('\nBusted!')
                    player_pot -= wager
                    return player_pot
                  response = ''
                  while response not in ['HIT','STAY']:
                    response = input('\nHit or Stay?:  ').strip().upper()
                  if response == 'STAY':
                    if 'A ' in name.hand and (name.value + 10) < 22:
                      name.value += 10
                    time.sleep(2)
                    print("\nDealer's hand:")
                    dealer.print_hand()
                    time.sleep(2)
                    print("\nDealer's total:  {}".format(dealer.value))
                    time.sleep(2)
                    if dealer.value > 21:
                      print('\n\nDealer busted, you won the hand!')
                      player_pot += wager
                      return player_pot
                    elif name.value > dealer.value:
                      print('\n\nYou won the hand!')
                      player_pot += wager
                      return player_pot
                    elif name.value == dealer.value:
                      print('\n\nWhen push comes to shove..')
                      return player_pot
                    elif name.value < dealer.value:
                      print('\n\nHouse wins.')
                      player_pot -= wager
                      return player_pot
  

if __name__ == '__main__':
  name = input('\nName, pleeease...  ')
  time.sleep(1)
  print('\n\nOK {}, place your bets!'.format(name))
  player_pot = 100
  wager = 0
  while wager <= 0 or wager > player_pot:
    wager = int((input('\nYou currently have {} coins, what will you wager?  '.format(player_pot))).strip())
  time.sleep(3)
  player_pot = game(name,player_pot,wager)
  wager = 0

  leave_table = ''
  while leave_table not in ['YES','Y']:
    time.sleep(3)
    if player_pot == 0:
      sys.exit('\n\nYou ran out of coins... better luck next time.\n\n')
    leave_table = (input('\n\nLeave table? (Y/N)  ')).strip().upper()
    time.sleep(2)
    if leave_table in ['YES','Y']:
      sys.exit('\n\nFinal coin count: {} coins\n\n'.format(player_pot))
    print('\n\nOK {}, place your bets!'.format(name))
    while wager <= 0 or wager > player_pot:
      wager = int((input('\nYou currently have {} coins, what will you wager?  '.format(player_pot))).strip())
    time.sleep(3)
    player_pot = game(name,player_pot,wager)
    wager = 0
