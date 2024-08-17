import tkinter as tk
from tkinter import messagebox


class VotingApp:
    def __init__(self, root, vote_logic):
        self.root = root
        self.root.title("VOTING APPLICATION")

        self.vote_logic = vote_logic  # Pass the VoteLogic instance# Create and place the ID entry label and box
        self.label_id = tk.Label(root, text="Enter your 5-digit ID:")
        self.label_id.pack(pady=10)
        self.entry_id = tk.Entry(root)
        self.entry_id.pack(pady=5)
        self.candidate_var = tk.StringVar(value="None")

        # Create and place the candidate selection
        self.label_candidate = tk.Label(root, text="Select your candidate:")
        self.label_candidate.pack(pady=10)
        self.radio_john = tk.Radiobutton(root, text="John", variable=self.candidate_var, value="John")
        self.radio_john.pack(anchor='w', padx=20)
        self.radio_jane = tk.Radiobutton(root, text="Jane", variable=self.candidate_var, value="Jane")
        self.radio_jane.pack(anchor='w', padx=20)

        # Create and place the submit button
        self.button_submit = tk.Button(root, text="SUBMIT VOTE", command=self.submit_vote)
        self.button_submit.pack(pady=20)

    def submit_vote(self):
        voter_id = self.entry_id.get().strip()
        candidate = self.candidate_var.get()

        # Validate ID
        if not voter_id.isdigit():
            messagebox.showerror("Invalid ID", "ID must be numerical.")
            return
        if len(voter_id) != 5:
            messagebox.showerror("Invalid ID", "ID must be 5 digits long.")
            return

        # Validate candidate selection
        if candidate == "":
            messagebox.showerror("No Selection", "Candidate must be selected.")
            return

        # Process the vote
        result = self.vote_logic.record_vote(voter_id, candidate)

        if result:
            messagebox.showinfo("Vote Submitted", f"Voter ID: {voter_id}\nVoted for: {candidate}")

        # Reset the form
        self.entry_id.delete(0, tk.END)
        self.candidate_var.set("None")