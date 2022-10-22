import tkinter.messagebox
from tkinter import ttk, Tk, StringVar, BooleanVar, IntVar, Scale, W, E, DoubleVar

from config import Config
from voter import Voter


def run():
    progress.set(0)
    progressbar.update()
    config = Config(
        max_votes=int(max_votes.get()),
        vote_interval_seconds=float(vote_interval_seconds.get()),
        round_interval_seconds=float(round_interval_seconds.get()),
        number_of_rounds=number_of_rounds.get(),
        headless=headless.get()
    )
    progressbar.config(maximum=number_of_rounds.get())
    with Voter(config) as voter:
        voter.run(set_progress=set_progress)
    tkinter.messagebox.showinfo("Finished", "Voting Finished")


def set_progress(cur_progress):
    progress.set(cur_progress)
    progressbar.update()


root = Tk()
root.title("Voter")

max_votes = IntVar()
vote_interval_seconds = StringVar()
vote_interval_seconds.set("0.1")
round_interval_seconds = StringVar()
round_interval_seconds.set("2.0")
number_of_rounds = IntVar()
headless = BooleanVar()
headless.set(True)
progress = DoubleVar()

frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text="Max Votes:").grid(column=0, row=1)
scale_max_votes = ttk.LabeledScale(frm, variable=max_votes, from_=1, to=20)
scale_max_votes.grid(column=1, row=1)
max_votes.set(10)
scale_max_votes.update()

ttk.Label(frm, text="Vote Interval (second):").grid(column=0, row=2)
ttk.Entry(frm, textvariable=vote_interval_seconds).grid(column=1, row=2)

ttk.Label(frm, text="Round Interval (second):").grid(column=0, row=3)
ttk.Entry(frm, textvariable=round_interval_seconds).grid(column=1, row=3)

ttk.Label(frm, text="Number of Rounds:").grid(column=0, row=4)
scale_rounds = ttk.LabeledScale(frm, variable=number_of_rounds, from_=1, to=20)
scale_rounds.grid(column=1, row=4)
number_of_rounds.set(5)
scale_rounds.update()

ttk.Label(frm, text="Headless:").grid(column=0, row=5)
ttk.Checkbutton(frm, variable=headless).grid(column=1, row=5)

progressbar = ttk.Progressbar(frm, variable=progress, maximum=1)
progressbar.grid(column=0, columnspan=2, row=6, sticky=W + E)

ttk.Button(frm, text="Run", command=run).grid(column=0, row=7)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=7)

ttk.Label(frm, text="With great power comes great responsibility.").grid(column=0, columnspan=2, row=8, sticky=W + E)

root.mainloop()
