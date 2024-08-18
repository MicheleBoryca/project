import tkinter as tk
from vote_logic import VoteLogic
from gui import VotingApp


def main() -> None:
    '''
    Initializes and runs the tkinter GUI for the voting app.
    '''
    root = tk.Tk()
    root.title("Lab 10")
    root.geometry("240x220")
    root.resizable(False, False)

    vote_logic = VoteLogic()
    app = VotingApp(root, vote_logic)

    root.mainloop()


if __name__ == "__main__":
    main()