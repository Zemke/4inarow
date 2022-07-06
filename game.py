#!/usr/bin/env python3

# num of cols, num of rows
NC, NR = 7, 6

class Game:

  def __init__(self):
    self.C = [[0 for _ in range(NR)] for _ in range(NC)]
    self.next = 1
    self.end = self._end()
    self.last = None


  def drop(self, target_c):
    if self.end > 0:
      raise Exception("game has ended")
    if self.C[target_c][0] != 0:
      raise Exception("out of space in col " + str(target_c));
    for r in range(len(self.C[target_c])):
      if self.C[target_c][r] != 0:
        self.C[target_c][r-1] = self.next
        self.last = target_c,r-1
        break
      if r == 5:
        self.C[target_c][r] = self.next
        self.last = target_c,r
        break
    self.next = 1 if self.next == 2 else 2
    self.end = self._end()


  def _end(self):
    # horizontally
    on_count, count = None, 0
    for r in range(NR):
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
    for c in range(NC):
      for r in range(NR):
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

    # diagonally
    for c in range(NC):
      for r in range(NR):
        if self.C[c][r] != 0:
          for diag in self._diags(c, r):
            if diag.count(self.C[c][r]) == 4:
              return self.C[c][r]

    return 0


  def _safe(self, c, r):
    if c < 0 or r < 0:
      return None
    if c >= NC or r >= NR:
      return None
    return self.C[c][r]


  def _diags(self, c, r):
    return [
      [self._safe(c+i, r+i) for i in range(4)],
      [self._safe(c-i, r-i) for i in range(4)],
      [self._safe(c-i, r+i) for i in range(4)],
      [self._safe(c+i, r-i) for i in range(4)]
    ]


  def __repr__(self):
    s = ''
    for r in range(NR):
      for c in range(NC):
        last = self.last == (c,r)
        if last:
          s += '\033[1m'
        s += str(self.C[c][r])
        if last:
          s += '\033[0m'
      s += "\n"
    s += f"next:{self.next} end:{self.end}\n"
    return s


  def copy(self, ):
    g = Game()
    g.next = self.next
    g.end = self.end
    g.C = [[self.C[c][r] for r in range(NR)] for c in range(NC)]
    return g

