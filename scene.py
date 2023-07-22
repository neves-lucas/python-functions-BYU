# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing
import random

def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Grid", scene_width, scene_height)

    diameter = 15
    space = 5
    interval = diameter + space

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    draw_ocean(canvas, scene_width, scene_height)
    #draw_grid(canvas, scene_width, scene_height, 50)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.

def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 1.8,
        scene_width, scene_height, width=0, fill="sky blue")

    """Sun"""
    x1 = 650
    y1 = 200
    x0 = 850
    y0 = 400
    draw_oval(canvas, x0, y0, x1, y1,
        width=7, outline="Orange2", fill="orange")


    """Clouds"""
    half_height = round(scene_height / 1.1)
    min_diam = 50
    max_diam = 95

    for i in range(50):
        x = random.randint(0, (scene_width - 120) - max_diam)
        y = random.randint(0, half_height)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y, x + diameter, y + diameter,
				outline="gray90", fill="gray90")


    # x1 = 20
    # y1 = 450
    # x0 = 120
    # y0 = 360
    # draw_oval(canvas, x0, y0, x1, y1,
    #     width=7, outline="gray", fill="gray")
    # draw_oval(canvas, x0 + 20, y0 + 20, x1 + 20 , y1 + 20,
    #     width=7, outline="gray", fill="gray")
    # draw_oval(canvas, x0 - 50, y0 - 80, x1 - 50, y1 - 80,
    #     width=7, outline="gray", fill="gray")


def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="khaki")
    
   # draw_polygon(canvas, 50, 100, 100, 150, 400, 400,
   #     width=1, outline="black", fill="")  --- Unfinished

def draw_ocean(canvas, scene_width, scene_height):
	"""Draw the ocean"""
	draw_rectangle(canvas, 0, scene_height - 331,
    scene_width, scene_height - 220, width=0, fill="blue1")
  
    #Draw little waves   -- Unfinished
    # half_height = round(scene_height / 1.1)
    # min_diam = 50
    # max_diam = 95

    # for i in range(50):
    #     x = random.randint(0, (scene_width - 120) - max_diam)
    #     y = random.randint(0, half_height)
    #     diameter = random.randint(min_diam, max_diam)
    #     draw_arc(canvas, x0, y0, x1, y1, *,
    #     start=0, extent=90, width=1, outline="black", fill=""):
    

    # GRID to help on drawing objects

# def draw_grid(canvas, width, height, interval, color="green"):
#     """ Draw a vertical line at every x interval."""
#     label_y = 15
#     for x in range(interval, width, interval):
#         draw_line(canvas, x, 0, x, height, fill=color)
#         draw_text(canvas, x, label_y, f"{x}", fill=color)

#     """Draw a horizontal line at every y interval."""
#     label_x = 15
#     for y in range(interval, height, interval):
#         draw_line(canvas, 0, y, width, y, fill=color)
#         draw_text(canvas, label_x, y, f"{y}", fill=color)

# Call the main function so that
# this program will start executing.
main()