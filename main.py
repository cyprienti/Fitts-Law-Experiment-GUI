import tkinter as tk
import random
import time
import csv
import math

class FittsLawTask:
    def __init__(self, master):
        self.master = master
        self.master.title("Fitts's Law Task")
        self.master.geometry("400x400")

        self.circle_radius_options = [20, 30, 40]
        self.distances = [100, 150, 200]
        self.passages = [(d, r) for d in self.distances for r in self.circle_radius_options] * 3

        self.current_passage = 0
        self.click_times = []

        self.data = []

        self.canvas = tk.Canvas(self.master, width=400, height=400)
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.click_callback)

        self.start_next_passage()

    def start_next_passage(self):
        if self.current_passage < len(self.passages):
            self.canvas.delete("all")
            distance, radius = self.passages[self.current_passage]
            self.create_circles(distance, radius)
        else:
            self.save_data_to_csv()
            self.display_results()
            self.canvas.delete("all")
            self.canvas.create_text(200, 200, text="YOU ARE DONE!", font=("Helvetica", 24))

    def create_circles(self, distance, radius):
        x1 = random.randint(radius + 10, 390 - distance - radius - 10)
        y = random.randint(radius + 10, 390 - radius - 10)
        x2 = x1 + distance

        self.circle1 = self.canvas.create_oval(x1 - radius, y - radius, x1 + radius, y + radius, fill="blue")
        self.circle2 = self.canvas.create_oval(x2 - radius, y - radius, x2 + radius, y + radius, fill="red")

        self.current_width = radius
        self.current_distance = distance

    def click_callback(self, event):
        self.click_times.append(time.time())
        if len(self.click_times) % 2 == 0:
            id_value = math.log2((self.current_distance / self.current_width) + 1)
            time_interval = self.click_times[-1] - self.click_times[-2]
            self.data.append([self.current_width, self.current_distance, id_value, time_interval])
            self.current_passage += 1
            self.start_next_passage()

    def save_data_to_csv(self):
        with open('fitts_law_data.csv', 'w', newline='') as csvfile:
            fieldnames = ['Width', 'Distance', 'ID', 'Time Interval']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in self.data:
                writer.writerow({'Width': row[0], 'Distance': row[1], 'ID': row[2], 'Time Interval': row[3]})

    def display_results(self):
        click_intervals = [self.click_times[i + 1] - self.click_times[i] for i in range(0, len(self.click_times), 2)]
        mean_time = sum(click_intervals) / len(click_intervals)
        print("Mean time between clicks:", mean_time)

def main():
    root = tk.Tk()
    app = FittsLawTask(root)
    root.mainloop()

if __name__ == "__main__":
    main()
