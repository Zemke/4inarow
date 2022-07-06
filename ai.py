#!/usr/bin/env python3

from math import inf
from game import Game

# 1 is minimizing
def minimax(G, depth, maximizing, ret=True):
  if depth == 0 or G.end > 0:
    if G.end == 2:
      return +inf
    elif G.end == 1:
      return -inf
    else:
      return 0  # TODO heuristic
  v, vmv = -inf, None
  v = -inf if maximizing else +inf
  vmv = None
  for c,g in poss_mvv(G):
    nv = minimax(g, depth-1, not maximizing, False)
    if (maximizing and v < nv) or (not maximizing and v > nv):
      v = nv
      vmv = c,g
  return vmv[0] if ret else v


def poss_mvv(G):
  mvv = []
  for c in range(len(G.C)):
    g = G.copy()
    try:
      g.drop(c)
      mvv.append((c,g))
    except:
      pass
  return mvv


if __name__ == "__main__":
  g = Game()
  tt = [0,0,1,0,2,0]
  for t in tt:
    g.drop(t)
  print(g)

  c = minimax(g, 5, False)
  g.drop(c)
  print(g, c)

