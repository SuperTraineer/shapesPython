import turtle
import math
import time

def draw_ellipse(t, center_x, center_y, radius_x, radius_y, angle=0, steps=100):
    """
    Draws an approximate ellipse using turtle graphics.
    """
    t.penup()

    angle_rad = math.radians(angle)
    step_angle = 2 * math.pi / steps

    # Calculate the initial position
    theta = 0
    x_local = radius_x * math.cos(theta)
    y_local = radius_y * math.sin(theta)

    x_rot = x_local * math.cos(angle_rad) - y_local * math.sin(angle_rad)
    y_rot = x_local * math.sin(angle_rad) + y_local * math.cos(angle_rad)

    t.goto(center_x + x_rot, center_y + y_rot)
    t.pendown()

    for i in range(1, steps + 1):
        theta = i * step_angle
        x_local = radius_x * math.cos(theta)
        y_local = radius_y * math.sin(theta)

        x_rot = x_local * math.cos(angle_rad) - y_local * math.sin(angle_rad)
        y_rot = x_local * math.sin(angle_rad) + y_local * math.cos(angle_rad)
        
        t.goto(center_x + x_rot, center_y + y_rot)

def draw_react_logo(t, rotation_angle):
    """
    Draws the React logo, rotated by 'rotation_angle' degrees.
    """
    # React’s primary color
    react_color = "#61DAFB"
    t.color(react_color)

    # For convenience, define ellipse radii
    radius_x = 100
    radius_y = 40

    # We’ll rotate each ellipse by (rotation_angle + base_offset)
    # so the whole shape spins together
    base_offsets = [0, 120, 240]

    for offset in base_offsets:
        draw_ellipse(t, 0, 0, radius_x, radius_y, rotation_angle + offset)

    # Draw the small center circle (also rotated by rotation_angle, 
    # but a circle looks the same at any rotation, so it's optional).
    t.penup()
    # Put the center circle slightly “down” from the center
    # so that the circle encloses the center properly
    t.goto(0, -10)
    t.pendown()
    t.circle(10)

def main():
    # Setup screen
    screen = turtle.Screen()
    screen.title("Spinning React Logo")
    screen.bgcolor("white")

    # Turn off automatic updates for smoother animation
    screen.tracer(0)

    # Create our turtle
    t = turtle.Turtle()
    t.speed(0)
    t.pensize(2)

    # Animation loop
    angle = 0
    while True:
        # Clear previous drawing
        t.clear()

        # Draw the React logo at the current angle
        draw_react_logo(t, angle)

        # Update the screen (because tracer(0) means manual updates)
        screen.update()

        # Increment the angle for next frame
        angle -= 3   # increase or decrease to speed up / slow down the spin

        # Optional short sleep so it doesn't spin too fast
        time.sleep(0.02)

if __name__ == "__main__":
    main()
