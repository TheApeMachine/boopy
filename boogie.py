import sys
import logging
from booloader import BooLoader

class Boogie:

    def __init__(self, filename):
        self.program = BooLoader(filename)

def main(filename):
    print("Boogie v0.0.1")
    print("Running: " + filename)

    Boogie(filename)

if __name__ == "__main__":
    # Get the first command-line argument so we can pass a file
    # to run to our language processing.
    try:
        main(sys.argv[1])
    except IndexError:
        logging.fatal("no input file provided")
