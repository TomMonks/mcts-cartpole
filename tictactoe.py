from abc import ABC, abstractmethod

import numpy as np


class GameEnvironment(ABC): 
    @abstractmethod()
    def step(self, action):
        '''
        Returns:
        --------
        Tuple
            new_state, reward, done, info
        '''
        pass

class TicTacToe(GameEnvironment):
    def __init__(self, size=3):
        self.rows = size
        self.cols = size

        self.NAUGHTS = 0
        self.CROSSES = 1

        #naughts go first.
        self.turn = 0

        self.board = np.full((self.rows, self.cols), -1, dtype=np.int)
        self.actions = {}
        
        #init action dict
        action = 0
        for row in range(self.rows):
            for col in cols(self.cols):
                self.actions[action] = (row, col)
                actions += 1

    def reset(self):
        return self.board

    def step(self, action):
        if self.legal_move(action):
            coord = self.action[action]
            self.play_piece(coord)

        else:
            raise ValueError('Illegal Move')

    def play_piece(self, cood):
        if self.turn == 0:
            self.board[coord[0]][coord[1]] = self.NAUGHTS
            self.turn = 1
        else:
            self.board[coord[0]][coord[1]] = self.CROSS
            self.turn = 0

    def legal_move(self, action):    
        if not action in self.actions:
            return False

        coords = self.actions[action]
        if self.board[coords[0]][coords[1]] != -1
            return False
        return True

    def terminal_state(self, action):
        coord = self.action[action]
        return self.board[self.row:, :]
        
        
    
