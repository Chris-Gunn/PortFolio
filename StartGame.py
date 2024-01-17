# Define a class for a game piece that can move around a board
class GamePiece:
    def __init__(self, position):
        self.current_position = position

    def move(self, new_position):
        self.current_position = new_position + self.current_position
        print("Moved to position", self.current_position)

# Create a game piece object with starting position 0
my_game_piece = GamePiece(0)

# Move the game piece to a new position and store it as the current position
new_position = 5
my_game_piece.move(position)
new_position = 5
my_game_piece.move(position)
