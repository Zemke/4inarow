#!/usr/bin/env python3

class Game:

  def __init__(self):
    # 7x6
    self.C = [[0 for _ in range(6)] for _ in range(7)]
    self.next = 1


  def drop(self, target_c):
    if self.C[target_c][0] != 0:
      raise Exception("out of space in col " + target_c);
    for r in range(len(self.C[target_c])):
      if self.C[target_c][r] != 0:
        self.C[target_c][r-1] = self.next
        break
      if r == 5:
        self.C[target_c][r] = self.next
        break
    self.next = 1 if self.next == 2 else 2


  def __repr__(self):
    s = ''
    for r in range(len(self.C[0])):
      for c in range(len(self.C)):
        s += str(self.C[c][r])
      s += "\n"
    s += str(self.next) + "\n"
    return s


g = Game()
print(g)

tt = [2,2,2,4]
for t in tt:
  g.drop(t)
  print(g)

