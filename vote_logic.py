import csv
import tkinter as tk
from gui import *

class VoteLogic:
    def __init__(self) -> None:
        '''
        Initializes the VoteLogic class - manages vote storage in CSV file
        '''
        self.vote_file = 'votes.csv'

    def record_vote(self, voter_id, candidate) -> None:
        '''
        Records vote in the CSV file
        '''
        if self.has_voted(voter_id):
            print(f"Duplicate detected for ID: {voter_id}")
            messagebox.showerror("Duplicate Vote", "This voter ID has already voted.")
            return False
        else:
            print(f"Recording vote for ID: {voter_id}")
            with open(self.vote_file, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([voter_id, candidate])
            return True

    def has_voted(self, voter_id) -> bool:
        '''
        Checks if the given voter ID has already voted
        '''
        try:
            with open(self.vote_file, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row and row[0] == voter_id:
                        print(f"ID {voter_id} has already voted.")
                        return True
        except FileNotFoundError:
            print(f"File not found. No votes recorded yet.")
            return False

if __name__ == "__main__":
    root = tk.Tk()
    vote_logic = VoteLogic()
    app = VotingApp(root, vote_logic)
    root.mainloop()