import tkinter as tk
import math
from datetime import datetime

class AnalogClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Analog Clock")
        self.canvas = tk.Canvas(root, width=400, height=400, bg='lightblue')
        self.canvas.pack()

        # Clock dimensions
        self.center_x = 200
        self.center_y = 200
        self.radius = 160
        self.hour_hand_length = 80
        self.minute_hand_length = 120
        self.second_hand_length = 140

        # Draw the clock face
        self.draw_clock_face()

        # Create clock hands
        self.create_hands()

        # Start the clock update loop
        self.update_clock()

    def draw_clock_face(self):
        # Outer circle
        self.canvas.create_oval(self.center_x - self.radius, self.center_y - self.radius,
                                self.center_x + self.radius, self.center_y + self.radius,
                                outline='black', width=2)

        # Hour markers and labels
        for i in range(1, 13):
            angle = 30 * i  # 30 degrees per hour
            rad = math.radians(angle)
            x = self.center_x + (self.radius - 20) * math.sin(rad)
            y = self.center_y - (self.radius - 20) * math.cos(rad)
            self.canvas.create_text(x, y, text=str(i), font=('Arial', 12, 'bold'))

        # Minute tick marks (every 5 minutes)
        for i in range(0, 60, 5):
            angle = 6 * i  # 6 degrees per minute
            rad = math.radians(angle)
            x1 = self.center_x + (self.radius - 5) * math.sin(rad)
            y1 = self.center_y - (self.radius - 5) * math.cos(rad)
            x2 = self.center_x + self.radius * math.sin(rad)
            y2 = self.center_y - self.radius * math.cos(rad)
            self.canvas.create_line(x1, y1, x2, y2, width=1)

    def create_hands(self):
        # Create clock hands with tags for later updates
        self.canvas.create_line(self.center_x, self.center_y, 0, 0,
                                tags="hour_hand", width=4, fill="darkblue")
        self.canvas.create_line(self.center_x, self.center_y, 0, 0,
                                tags="minute_hand", width=3, fill="navy")
        self.canvas.create_line(self.center_x, self.center_y, 0, 0,
                                tags="second_hand", width=1, fill="red")

        # Central pivot circle
        self.canvas.create_oval(self.center_x - 8, self.center_y - 8,
                                self.center_x + 8, self.center_y + 8,
                                fill="black")

    def update_clock(self):
        now = datetime.now()
        total_seconds = now.second + now.microsecond / 1e6

        # Calculate angles in degrees
        seconds_angle = total_seconds * 6
        minutes_angle = (now.minute + total_seconds / 60) * 6
        hours_angle = (now.hour % 12 + (now.minute + total_seconds / 60) / 60) * 30

        # Convert to radians
        seconds_rad = math.radians(seconds_angle)
        minutes_rad = math.radians(minutes_angle)
        hours_rad = math.radians(hours_angle)

        # Calculate coordinates for each hand
        x_hour = self.center_x + self.hour_hand_length * math.sin(hours_rad)
        y_hour = self.center_y - self.hour_hand_length * math.cos(hours_rad)

        x_minute = self.center_x + self.minute_hand_length * math.sin(minutes_rad)
        y_minute = self.center_y - self.minute_hand_length * math.cos(minutes_rad)

        x_second = self.center_x + self.second_hand_length * math.sin(seconds_rad)
        y_second = self.center_y - self.second_hand_length * math.cos(seconds_rad)

        # Update hand positions on the canvas
        self.canvas.coords("hour_hand", self.center_x, self.center_y, x_hour, y_hour)
        self.canvas.coords("minute_hand", self.center_x, self.center_y, x_minute, y_minute)
        self.canvas.coords("second_hand", self.center_x, self.center_y, x_second, y_second)

        # Schedule next update
        self.root.after(100, self.update_clock)

if __name__ == "__main__":
    root = tk.Tk()
    clock = AnalogClock(root)
    root.mainloop()