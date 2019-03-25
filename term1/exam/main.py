import curses
import random
import sys

class Game():

    def __init__(self):
        self.scr = curses.initscr()
        self.scr.keypad(1)
        curses.noecho()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        self.dims = self.scr.getmaxyx()
        self.grid = [0] * 9

    def draw_field(self, choosen=-1, stat = ''):
        pad = curses.newpad(9, 6)
        pad.addstr(0, 0, "  {}  ".format(self.round_number))
        for x in range(5):
            pad.addch(2, x, ord(" | | "[x]))
            pad.addch(3, x, ord("-+-+-"[x]))
            pad.addch(4, x, ord(" | | "[x]))
            pad.addch(5, x, ord("-+-+-"[x]))
            pad.addch(6, x, ord(" | | "[x]))
        coord = {0: (2,0), 1: (2,2), 2: (2,4),
                 3: (4,0), 4: (4,2), 5: (4,4),
                 6: (6,0), 7: (6,2), 8: (6,4)}
        for _ in range(9):
            if self.grid[_] == -1:
                pad.addch(*coord[_], ord('X'))
            elif self.grid[_] == 1:
                pad.addch(*coord[_], ord('O'))
        if choosen != -1:
            if self.grid[choosen]:
                pad.addch(*coord[choosen], ord(self.player_ch),
                          curses.color_pair(1) | curses.A_REVERSE)
            else:
                pad.addch(*coord[choosen], ord(self.player_ch),
                          curses.color_pair(0) | curses.A_REVERSE)
        pad.addstr(8, 0, stat)
        posy = self.dims[0] // 2 - 5
        if self.round_number == 1:
            posx = self.dims[1] // 4 - 3
        elif self.round_number == 2:
            posx = self.dims[1] // 2 - 3
        elif self.round_number == 3:
            posx = int(self.dims[1] * 3/4) - 3
        pad.refresh(0, 0, posy, posx, posy + 9, posx + 9)

    def start(self):
        curses.curs_set(0)
        self.scr.addstr(self.dims[0] // 3,
                        self.dims[1] // 2 - 6, 'Tik tak toe!')
        self.scr.refresh()
        control = 0
        reverse = (curses.A_NORMAL, curses.A_REVERSE)
        r_switch = 1
        while control != ord(' ') and control != 10: # 10 -'enter'
            self.scr.addstr(self.dims[0] // 2,
                            self.dims[1] // 4, 'Goofy',
                            curses.A_BOLD | reverse[r_switch])
            self.scr.addstr(self.dims[0] // 2,
                            int(self.dims[1] * 3/4), 'PRO',
                            curses.A_BOLD | reverse[(r_switch + 1) % 2])
            control = self.scr.getch()
            if control == 27:
                curses.endwin()
                sys.exit(0)
            if control == curses.KEY_LEFT or control == curses.KEY_RIGHT:
                r_switch = (r_switch + 1) % 2
            self.scr.refresh()

        self.go(r_switch)
        control = self.scr.getch()

    def is_win(self, grid):
        win = [0] * 8
        for x in range(3):
            win[0] += grid[x]
            win[1] += grid[x + 3]
            win[2] += grid[x + 6]
            win[3] += grid[3 * x]
            win[4] += grid[1 + 3*x]
            win[5] += grid[2 + 3*x]
            win[6] += grid[3*x + x]
            win[7] += grid[2*(x + 1)]
        for w in win:
            if w == -3:
                return 'X'
            elif w == 3:
                return 'O'
        return 0

    def player_step(self, choosen):
        control = 0
        while control != ord(' ') and control != 10:
            control = self.scr.getch()
            if control == curses.KEY_LEFT:
                choosen = (choosen - 1) % 9
            elif control == curses.KEY_RIGHT:
                choosen = (choosen + 1) % 9
            elif control == curses.KEY_UP:
                choosen = (choosen - 3) % 9
            elif control == curses.KEY_DOWN:
                choosen = (choosen + 3) % 9
            elif control == 27:
                curses.endwin()
                sys.exit(0)
            self.draw_field(choosen)
        return choosen

    def goofy_round(self):
        self.free_cells = {0, 1, 2, 3, 4, 5, 6, 7, 8}
        self.grid = [0] * 9
        self.draw_field()
        self.player_ch = random.choice(('X', 'O'))

        if self.player_ch == 'X':
            self.cpu_ch = 'O'
            tik = 0
            while not self.is_win(self.grid) and self.free_cells:
                while True:
                    tik = self.player_step(tik)
                    if tik in self.free_cells:
                        self.grid[tik] = -1
                        self.free_cells.remove(tik)
                        break
                if self.free_cells and not self.is_win(self.grid):
                    tak = random.choice(list(self.free_cells))
                    self.grid[tak] = 1
                    self.free_cells.remove(tak)
                self.draw_field(tik)
            w = self.is_win(self.grid)
            if w == 'X':
                self.draw_field(stat=" WIN ")
                self.pl_scor += 1
            elif w == 'O':
                self.draw_field(stat="LOOSE")
                self.cpu_scor += 1
            elif w == 0:
                self.draw_field(stat="DRAW!")

        if self.player_ch == 'O':
            self.cpu_ch = 'X'
            tik = 0
            while not self.is_win(self.grid) and self.free_cells:
                if self.free_cells:
                    tak = random.choice(list(self.free_cells))
                    self.grid[tak] = -1
                    self.free_cells.remove(tak)
                self.draw_field(tik)
                while self.free_cells and not self.is_win(self.grid):
                    tik = self.player_step(tik)
                    if tik in self.free_cells:
                        self.grid[tik] = 1
                        self.free_cells.remove(tik)
                        break
            w = self.is_win(self.grid)
            if w == 'O':
                self.draw_field(stat=" WIN ")
                self.pl_scor += 1
            elif w == 'X':
                self.draw_field(stat="LOOSE")
                self.cpu_scor += 1
            elif w == 0:
                self.draw_field(stat="DRAW!")

    def pro_cpu(self, free):
        if not free:
            return -1
        elif len(free) == 1:
            return free[0]

        def minmax(free, grid, cpu_turn):
            if len(free) == 1:
                if cpu_turn:
                    grid[free[0]] = -1 if self.cpu_ch == 'X' else 1
                else:
                    grid[free[0]] = 1 if self.cpu_ch == 'X' else -1
                w = self.is_win(grid)
                if w == 'X':
                    return -10
                elif w == 'O':
                    return 10
                elif w == 0:
                    return 0
            else:
                score = 0
                for pos in free:
                    if cpu_turn:
                        new_grid = grid[:]
                        new_grid[pos] = -1 if self.cpu_ch == 'X' else 1
                        new_free = free[:]
                        new_free.remove(pos)
                        new_cpu_turn = not cpu_turn
                        score += minmax(new_free, new_grid, new_cpu_turn)
                    else:
                        new_grid = grid[:]
                        new_grid[pos] = 1 if self.cpu_ch == 'X' else -1
                        new_free = free[:]
                        new_free.remove(pos)
                        new_cpu_turn = not cpu_turn
                        score += minmax(new_free, new_grid, new_cpu_turn)
                return score

        scores = []
        for i in range(len(free)):
            new_grid = self.grid[:]
            new_grid[free[i]] = -1 if self.cpu_ch == 'X' else 1
            new_free = free[:]
            new_free.remove(free[i])
            scores.append(minmax(new_free, new_grid, False))
        if self.cpu_ch == 'X':
            min = 1000000
            for i in range(len(scores)):
                if scores[i] < min:
                    min = scores[i]
                    answ = i
        elif self.cpu_ch == 'O':
            max = -1000000
            for i in range(len(scores)):
                if scores[i] > max:
                    max = scores[i]
                    answ = i
        return free[answ]

    def pro_round(self):
        self.free_cells = {0, 1, 2, 3, 4, 5, 6, 7, 8}
        self.grid = [0] * 9
        self.draw_field()
        self.player_ch = random.choice(('X', 'O'))

        if self.player_ch == 'X':
            self.cpu_ch = 'O'
            tik = 0
            while not self.is_win(self.grid) and self.free_cells:
                while True:
                    tik = self.player_step(tik)
                    if tik in self.free_cells:
                        self.grid[tik] = -1
                        self.free_cells.remove(tik)
                        break
                if self.free_cells and not self.is_win(self.grid):
                    tak = self.pro_cpu(list(self.free_cells))
                    self.grid[tak] = 1
                    self.free_cells.remove(tak)
                self.draw_field(tik)
            w = self.is_win(self.grid)
            if w == 'X':
                self.draw_field(stat=" WIN ")
                self.pl_scor += 1
            elif w == 'O':
                self.draw_field(stat="LOOSE")
                self.cpu_scor += 1
            elif w == 0:
                self.draw_field(stat="DRAW!")

        if self.player_ch == 'O':
            self.cpu_ch = 'X'
            tik = 0
            self.grid[4] = -1
            self.free_cells.remove(4)

            while not self.is_win(self.grid) and self.free_cells:
                while True:
                    tik = self.player_step(tik)
                    if tik in self.free_cells:
                        self.grid[tik] = 1
                        self.free_cells.remove(tik)
                        break
                if self.free_cells and not self.is_win(self.grid):
                    tak = self.pro_cpu(list(self.free_cells))
                    print(tak)
                    self.scr.addstr(0, 0, str(tak))
                    self.grid[tak] = -1
                    self.free_cells.remove(tak)
                self.draw_field(tik)
            w = self.is_win(self.grid)
            if w == 'O':
                self.draw_field(stat=" WIN ")
                self.pl_scor += 1
            elif w == 'X':
                self.draw_field(stat="LOOSE")
                self.cpu_scor += 1
            elif w == 0:
                self.draw_field(stat="DRAW!")

    def go(self, r_switch):
        self.scr.clear()
        self.scr.refresh()
        self.round_number = 0
        self.pl_scor = 0
        self.cpu_scor = 0
        self.scr.addstr(1, self.dims[1]//2 - 6, 'YOU {}:{} CPU'.
                        format(self.pl_scor, self.cpu_scor))
        if r_switch:
            for _ in range(3):
                self.round_number += 1
                self.goofy_round()
                self.scr.addstr(1, self.dims[1]//2 - 6, 'YOU {}:{} CPU'.
                                format(self.pl_scor, self.cpu_scor))
                if self.scr.getch() == 27:
                    sys.exit(0)
        else:
            for _ in range(3):
                self.round_number += 1
                self.pro_round()
                self.scr.addstr(1, self.dims[1]//2 - 6, 'YOU {}:{} CPU'.
                                format(self.pl_scor, self.cpu_scor))
                if self.scr.getch() == 27:
                    sys.exit(0)
        self.scr.clear()
        self.scr.refresh()
        if self.cpu_scor > self.pl_scor:
            self.scr.addstr(self.dims[0]//2, self.dims[1]//2 - 5, 'YOU LOOSE!')
        elif self.cpu_scor == self.pl_scor:
            self.scr.addstr(self.dims[0]//2, self.dims[1]//2 - 3, 'DRAW!')
        elif self.cpu_scor < self.pl_scor:
            self.scr.addstr(self.dims[0]//2, self.dims[1]//2 - 4, 'YOU WIN!')

if __name__ == "__main__":
    game = Game()
    game.start()
    '''
    stdscr.refresh()
    pad = curses.newpad(100, 100)
    for y in range(0, 99):
        for x in range(0, 99):
            pad.addch(y, x, ord('='))

    # Displays a section of the pad in the middle of the screen.
    # (0,0) : coordinate of upper-left corner of pad area to display.
    # (5,5) : coordinate of upper-left corner of window area to be filled
    #         with pad content.
    # (20, 75) : coordinate of lower-right corner of window area to be
    #          : filled with pad content.
    pad.refresh( 0,0, 3,5, 20,75)
    '''
