#!/usr/bin/env python3

from game import Game
import sys
from ai import minimax

if __name__ == "__main__":
  ai = len(sys.argv) > 1 and sys.argv[1] == 'ai'
  g = Game()
  print(g)
  while g.end <= 0:
    if ai and g.next == 2:
      print("ai is thinking...")
      g.drop(minimax(g, 5, True))
    else:
      try:
        t = int(input('col: '))
        g.drop(t)
      except Exception as e:
        print('invalid input:', e)
        continue
    print(g)

