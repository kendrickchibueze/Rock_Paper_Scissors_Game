#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random
import time
from colorama import Fore

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    win_count = 0
    my_move = ""
    their_move = ""

    def move(self):
        return 'rock'

# inform a player what the other player move is
    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        play_input = input("please insert either paper,"
                           "rock or scissors: ")
        if play_input in moves:
            return play_input
        else:
            print("The choice you make is invalid,"
                  "please enter something again")
            time.sleep(2)
            self.move()


class ReflectPlayer(Player):
    def move(self):
        if self.their_move in moves:
            return self.their_move
        else:
            return random.choice(moves)


class CyclePlayer(Player):
    # Calling the constructor with superpowers
    def __init__(self):
        super().__init__()
        self.moves_size = len(moves)
        self.my_next_move_index = random.randrange(self.moves_size)

    def move(self):
        my_next_move = moves[self.my_next_move_index]
        self.my_next_move_index = (
            self.my_next_move_index + 1) % self.moves_size
        return my_next_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        # assign move of the player to learn.
        # This helps to recognize moves of player/opponent
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        # The beat method shows who wins
        if beats(move1, move2):
            self.p1.win_count += 1
            time.sleep(2)
            print(
                f"\n** PLAYER ONE WINS **"
                f"\nScore: Player one {self.p1.win_count}, "
                f"Player two {self.p2.win_count}"
            )

        elif beats(move2, move1):
            self.p2.win_count += 1
            time.sleep(2)
            print(
                f"\n** PLAYER TWO WINS **"
                f"\nScore: Player one {self.p1.win_count}, "
                f"Player two {self.p2.win_count}"
            )

        else:
            time.sleep(2)
            print(
                f"\n** IT'S A TIE **"
                f"\nScore: Player one {self.p1.win_count}, "
                f"Player two {self.p2.win_count}"
            )

    def play_game(self):
        print("Rock Paper Scissors, Go!")
        for round in range(9):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")
        time.sleep(2)

        # announce the winner
        if self.p1.win_count > self.p2.win_count:
            print(
                f"\n** FINALLY, PLAYER ONE WON THE GAME!! **"
                f"\nScore: Player one {self.p1.win_count}, "
                f"Player two {self.p2.win_count}"
            )

        elif self.p2.win_count > self.p1.win_count:
            print(
                f"\n** FINALLY, PLAYER TWO WON THE GAME!! **"
                f"\nScore: Player one {self.p1.win_count}, "
                f"Player two {self.p2.win_count}"
            )

        else:
            print(
                f"\n** NOBODY WINS **"
                f"\nScore: Player one {self.p1.win_count}, "
                f"Player two {self.p2.win_count}"
            )


if __name__ == '__main__':
    game = Game(HumanPlayer(), ReflectPlayer())
    game.play_game()
