"""Will create a class for the board and all things a board is able to do
within the FindTheArrow.py(main).

The formatter class has some tricks: !s calls str(), !r repr(), !a calls ascii()
Example fprint("yatata {name!s}").format(format_strings(positional), *args, **kwargs)
name should go where the positional arg goes.
"""



import random as rm
from string import Formatter

class Board:
    """The game board and all of its glory."""
    def __init__(self, player_move=0):
        """This class was implemented after these functions were made, so if you find an
        unwanted feature(bug), this is most likely why..."""
        self.player_move = player_move
        self.arrow = '##-->>' # Maybe a list of each direction the arrow string can be in on board
        self.game_grid = []
        self.hash = '#'
        self.rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        self.side = ('left', 'right')
        self.cols = [' ']
        self.col1 = [' ']
        self.col2 = [' ']

    def board_concealed(self):
        """Fully concealed from view game board 10x40"""
        for i in range(10):
            i = []
            self.game_grid.append(i)
        [i.append(self.hash*40) for i in self.game_grid]
        return self.game_grid


    def board_half(self):
        """Returns a list of lists containing a single board half of 10x20"""

        for i in self.game_grid:
            i = [str(self.hash*20)]
        self.half = self.game_grid
        return self.half

    # @property <<-- by using @name.setter/getter/delleter* name being the private or property method identifier
    def board_legend(self):
        """Will handle all possible game board positions for a player to pick."""
        if self.game_grid:
            for num in range(0, 41, 5):
                self.cols.append(str(num))
        else:
            for num in range(0, 21, 5):
                self.col1.append(str(num))
            self.col2 = self.col1
        return self.cols, self.col1, self.col2, self.side



    def randomize_arrow(self):
        """Will randomly choose a number between 1 and 400. The arrow tip will go there.
        Random number between 1-4(N,E,S,W)(Direction of arrow)"""
        location = rm.randint(1, 400)
        direction = rm.randint(1, 4)
        new_loc = [location, direction]
        return new_loc



    def perspective(self):
        """What the player is seeing. Updates perspective as the return value."""
        with open("Concealed.txt", "w") as view:
            for e in self.cols:
                line1 = view.write(e + ' ')
            for i in self.rows:
                if i == self.rows[0]:
                    view.write('\n' + i + ' ')
                    cur = view.tell()
                    view.write('\n')
                else:
                    spots = [cur]
                    pos = view.tell()
                    spots.append(pos)
                    view.write(i + '\n')


            for p in spots:
                p = view.seek(pos)
                for i in self.game_grid:
                    view.write(i[0])



# Need to fine tune the seek/tell sequence of events in order to allow for the entire screen to become
# perfect***
n = Board()
n.board_concealed()
n.board_legend()
n.perspective()
