from board import Board
from player import Player


class Tictactoe:

    def start(self):
        print("************************")
        print(" Welcome to Tic¬Tac¬Toe ")
        print("************************")

        board = Board()
        player = Player()
        computer = Player(False)

        board.print_board()

        while True:

            while True:
                player_move = player.get_move()
                board.make_move(player, player_move)
                board.print_board()

                if board.check_tie():
                    print("It's a tie! Play again? ")
                    break
                elif board.check_game_over(player, player_move):
                    print(" You won!")
                    break
                else:
                    computer_move = computer.get_move()
                    board.make_move(computer, computer_move)
                    board.print_board()

                    if board.check_game_over(computer, computer_move):
                        print("Computer won!")
                        break
            play_again = input("Would you like to play again? Enter X for YES or O for No: ").upper()

            if play_again == "O":
                print("Bye")
                break
            elif play_again == "X":
                self.start_new_round(board)
            else:
                print("Invalid input")
                self.start_new_round(board)

    def start_new_round(self, board):
        print("************************")
        print(" New round ")
        print("************************")
        board.reset_board()
        board.print_board()

game = Tictactoe()
game.start()