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


  def end(self):
    # horizontally
    on_count, count = None, 0
    for r in range(len(self.C[0])):
      for c in range(len(self.C)):
        if self.C[c][r] == 0:
          on_count = None
          count = 0
        else:
          if self.C[c][r] == on_count:
            count += 1
          else:
            on_count = self.C[c][r]
            count = 1
          if count == 4:
            return on_count

    # vertically
    on_count, count = None, 0
    for c in range(len(self.C)):
      for r in range(len(self.C[c])):
        if self.C[c][r] == 0:
          on_count = None
          count = 0
        else:
          if self.C[c][r] == on_count:
            count += 1
          else:
            on_count = self.C[c][r]
            count = 1
          if count == 4:
            return on_count
        


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

tt = [1,3,1,3,1,3,1]
for t in tt:
  g.drop(t)
  print('end', g.end())
  print(g)

