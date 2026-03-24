import sys
import os

# Ensure the root of the project is in the PYTHONPATH
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.game import Game

if __name__ == "__main__":
    game = Game()
    game.run()
