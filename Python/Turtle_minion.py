# This code uses the turtle module to draw SVG paths, which must be run in a local Python environment.
# Turtle graphics is not supported in environments without GUI (e.g. online IDEs or sandboxed code runners).

try:
    import turtle
    from xml.dom import minidom
    import re

    # --- Setup ---
    turtle.setup(width=800, height=800)
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    SCALE = 0.5  # Adjust this for scaling the drawing

    def svg_to_turtle_coords(x, y):
        return x * SCALE - 250, 250 - y * SCALE

    # --- SVG Path Parser ---
    def commands_list(path):
        return re.findall(r'[MmLlHhVvCcQqZz]|[-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?', path)

    # --- Draw One Path ---
    def draw_svg_path(path_d):
        commands = commands_list(path_d)
        i = 0
        current_pos = (0.0, 0.0)
        start_pos = (0.0, 0.0)
        last_cmd = ''

        def get_value():
            nonlocal i
            if i < len(commands) and re.match(r'^[-+]?[0-9]', commands[i]):
                val = float(commands[i])
                i += 1
                return val
            return 0.0

        def get_point():
            return get_value(), get_value()

        while i < len(commands):
            token = commands[i]
            if re.match(r'[A-Za-z]', token):
                cmd = token
                i += 1
                last_cmd = cmd
            else:
                cmd = last_cmd

            relative = cmd.islower()
            cmd = cmd.upper()

            if cmd == 'M':
                x, y = get_point()
                if relative:
                    x += current_pos[0]
                    y += current_pos[1]
                tx, ty = svg_to_turtle_coords(x, y)
                t.penup()
                t.goto(tx, ty)
                t.pendown()
                current_pos = (x, y)
                start_pos = (x, y)
                while i + 1 < len(commands) and re.match(r'^[-+]?[0-9]', commands[i]) and re.match(r'^[-+]?[0-9]', commands[i+1]):
                    x, y = get_point()
                    if relative:
                        x += current_pos[0]
                        y += current_pos[1]
                    tx, ty = svg_to_turtle_coords(x, y)
                    t.goto(tx, ty)
                    current_pos = (x, y)

            elif cmd == 'L':
                x, y = get_point()
                if relative:
                    x += current_pos[0]
                    y += current_pos[1]
                tx, ty = svg_to_turtle_coords(x, y)
                t.goto(tx, ty)
                current_pos = (x, y)

            elif cmd == 'H':
                x = get_value()
                if relative:
                    x += current_pos[0]
                tx, ty = svg_to_turtle_coords(x, current_pos[1])
                t.goto(tx, ty)
                current_pos = (x, current_pos[1])

            elif cmd == 'V':
                y = get_value()
                if relative:
                    y += current_pos[1]
                tx, ty = svg_to_turtle_coords(current_pos[0], y)
                t.goto(tx, ty)
                current_pos = (current_pos[0], y)

            elif cmd == 'C':
                x1, y1 = get_point()
                x2, y2 = get_point()
                x, y = get_point()
                if relative:
                    x1 += current_pos[0]; y1 += current_pos[1]
                    x2 += current_pos[0]; y2 += current_pos[1]
                    x += current_pos[0]; y += current_pos[1]
                steps = 20
                for j in range(steps + 1):
                    t_ = j / steps
                    xt = ((1 - t_)**3 * current_pos[0] + 3*(1 - t_)**2*t_*x1 +
                          3*(1 - t_)*t_**2*x2 + t_**3*x)
                    yt = ((1 - t_)**3 * current_pos[1] + 3*(1 - t_)**2*t_*y1 +
                          3*(1 - t_)*t_**2*y2 + t_**3*y)
                    tx, ty = svg_to_turtle_coords(xt, yt)
                    if j == 0:
                        t.penup()
                    else:
                        t.pendown()
                    t.goto(tx, ty)
                current_pos = (x, y)

            elif cmd == 'Q':
                x1, y1 = get_point()
                x, y = get_point()
                if relative:
                    x1 += current_pos[0]; y1 += current_pos[1]
                    x += current_pos[0]; y += current_pos[1]
                steps = 20
                for j in range(steps + 1):
                    t_ = j / steps
                    xt = ((1 - t_)**2 * current_pos[0] + 2*(1 - t_)*t_*x1 + t_**2*x)
                    yt = ((1 - t_)**2 * current_pos[1] + 2*(1 - t_)*t_*y1 + t_**2*y)
                    tx, ty = svg_to_turtle_coords(xt, yt)
                    if j == 0:
                        t.penup()
                    else:
                        t.pendown()
                    t.goto(tx, ty)
                current_pos = (x, y)

            elif cmd == 'Z':
                tx, ty = svg_to_turtle_coords(*start_pos)
                t.goto(tx, ty)
                current_pos = start_pos

    # --- Draw Entire SVG File ---
    def draw_svg_file(file_path):
        doc = minidom.parse(file_path)
        paths = doc.getElementsByTagName('path')
        for path in paths:
            d = path.getAttribute('d')
            draw_svg_path(d)
        doc.unlink()

    # --- Main ---
    if __name__ == '__main__':
        draw_svg_file(r"C:\\Users\\PC\\OneDrive\\文档\\VS CODE\\vecteezy_cute-little-minion_60100435 [Converted]-01.svg")
        turtle.exitonclick()

except ModuleNotFoundError as e:
    print("This code requires the 'turtle' module which is not available in this environment.")
    print("Please run it in a local Python environment with GUI support.")
