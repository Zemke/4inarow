#!/usr/bin/env python3

class Game:
  def __init__(self):
    # 7x6
    self.C = [[0 for _ in range( 7)] for _ in range(6)]

  def __repr__(self):
    for c in self.C:
      print(c)

g = Game()
print(g)

