#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):
        self.score = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        index = random.randint(0, len(moves) - 1)
        return moves[index]


class HumanPlayer(Player):
    def move(self):
        while True:
            try:
                print("\tChoose: \n\tRock, Paper, Scissors-->", end='')
                choice = input()
                if choice.lower() in moves:
                    break
                else:
                    raise Exception
            except Exception as e:
                print("Invalid Choice!!")
                print("Please Choice From Rock, Paper, Scissors.")

        return choice.lower()


class ReflectPlayer(Player):
    def __init__(self):
        super().__init__()
        self.previousmove = ''

    def move(self):
        if self.previousmove == '':
            index = random.randint(0, len(moves) - 1)
            return moves[index]
        else:
            return self.previousmove

    def learn(self, my_move, their_move):
        self.previousmove = their_move


class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.cyclemove = ''

    def move(self):
        if self.cyclemove == '':
            index = random.randint(0, len(moves) - 1)
            return moves[index]
        else:
            return self.cyclemove

    def learn(self, my_move, their_move):
        if my_move == moves[0]:
            self.cyclemove = moves[1]
        elif my_move == moves[1]:
            self.cyclemove = moves[2]
        else:
            self.cyclemove = moves[0]


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
        print(f"\tPlayer 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2):
            print("\tPlayer 1 Won!!")
            self.p1.score += 1
        elif move1 == move2:
            print("\tTie Between Players!!")
        else:
            print("\tPlayer 2 Won!!")
            self.p2.score += 1

    def play_game(self):
        print("Game Start")
        round = 0
        while True:
            print("\nRock Paper Scissors, Go!")
            print(f"Round {round} --")
            round += 1
            self.play_round()
            player1_score = self.p1.score >= self.p2.score + 3
            player2_score = self.p2.score >= self.p1.score + 3
            if player1_score or player2_score:
                break

        print("\n")
        print("*" * 40)
        print("{:<20} {:<20}".format("Player 1 Score", "Player 2 Score"))
        print("*" * 40)
        print("{:<20} {:<20}".format(self.p1.score, self.p2.score))
        print("*" * 40)

        if self.p1.score > self.p2.score:
            print("Player 1 Won.")
        else:
            print("Player 2 Won.")

        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
