#/usr/bin/python

import numpy as np

class Map:
    
    def __init__(self, N=10, M=None, dtype=int):
        self.N = N
        self.M = N if M is None else M
        self.data = np.zeros((self.N, self.M), dtype=dtype)
    
    def isValid(self, pos):
        pos = np.asarray(pos)
        assert pos.shape == (2,)
        return all(pos >= (0,0)) and all(pos < (self.N,self.M))
    
    def __getitem__(self, pos):
        if self.isValid(pos):
            return self.data[pos]
        else:
            return None
    
    def __setitem__(self, pos, val):
        if self.isValid(pos):
            self.data[pos] = val
    
    def isA(self, pos, pred):
        if type(pred) == self.data.dtype:
            _pred = lambda x: x == pred
        else:
            _pred = pred
        return self.isValid(pos) and _pred(self[pos[0],pos[1]])
    
    def nbrs(self, pos, pred=lambda x:True, withDiags=False, probs=None):
        if probs is None:
            probs = np.array(((withDiags,1,withDiags),
                           (1,0,1),
                           (withDiags,1,withDiags)))
        assert probs.shape == (3,3)
        
        indices = np.array(np.unravel_index(np.arange(probs.size), probs.shape)).T
        nbrPos = indices[(np.random.rand(*probs.shape) < probs).flatten()] \
            + [-1,-1] + pos
        return list(filter(lambda p: self.isA(p, pred), nbrPos))

def genMaze(N=10, M=None):
    maze = Map(N, M, dtype=bool)
    space = True
    wall = False
    
    start = np.random.randint(maze.N), np.random.randint(maze.M)
    maze[start] = True
    walls = maze.nbrs(start, wall)
    
    while len(walls) != 0:
        i = np.random.randint(len(walls))
        pos = walls[i]
        if len(maze.nbrs(pos, space)) == 1:
            maze[pos[0],pos[1]] = space # clear the wall
            newSpace = 2*pos-maze.nbrs(pos, space)[0]
            maze[newSpace[0],newSpace[1]] = space # clear the next room
            walls.extend(maze.nbrs(newSpace, wall))
        walls.pop(i)
    return maze
