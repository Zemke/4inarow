#!/usr/bin/env python3

from game import Game
import sys

if __name__ == "__main__":
  ai = len(sys.argv) > 1 and sys.argv[1] == 'ai'
  g = Game()
  while g.end <= 0:
    try:
      t = int(input('col: '))
      g.drop(t)
    except Exception as e:
      print('invalid input:', e)
      continue
    print(g)

