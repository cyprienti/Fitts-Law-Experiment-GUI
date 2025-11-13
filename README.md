 # Fitts’ Law Experiment GUI (Python)

This project implements a graphical user interface (GUI) for conducting a two-dimensional Fitts’ Law experiment.
The goal is to measure the time required to click two circular targets in sequence, with varying widths (W) and distances (D).

# Features

  -  Displays two circles that must be clicked one after another.
  -  Automatically measures the time between the first and second click.
  -  Three different values for:
        Target Width (W)
        Target Distance (D)

    Each width–distance combination (3 × 3) is repeated 3 times, resulting in 27 total trials.
    Circles are placed randomly at different angles while ensuring they:
  -  Do not overlap
  -  Do not extend outside the window

# Calculates the Index of Difficulty (ID) for each trial:

        𝐼𝐷 = log2(𝐷𝑊+1)
        ID = log2(WD+1)

# Automatically saves all data to a CSV file, including:
  -  Width (W)
  -  Distance (D)
  -  Index of Difficulty (ID)
  -  Reaction Time (s)

    RUN main.py
