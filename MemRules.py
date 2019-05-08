"""Will have all of the rules readily available to print to the terminal
so if the players wish to read the rules before starting they may do so at will."""

### Importing this function works correctly in the main file.
def arrow_rules():
    """Will display the rules of the game in the terminal."""
    with open("Rules.txt", "r") as rule:
        pr = rule.read()
        print(pr)
