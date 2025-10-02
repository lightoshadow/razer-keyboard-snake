from openrazer.client import DeviceManager
from random import randrange
import curses

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(300)
    curses.noecho()

    devman = DeviceManager()

    stdscr.addstr(f"Found {len(devman.devices)} Razer devices\n")

    # Iterate over each device and pretty out some standard information about each
    for device in devman.devices:
        stdscr.addstr(f"{device.name}:")
        stdscr.addstr(f"   type: {device.type}\n")
    
    stdscr.addstr("use ARROWS to mode DELETE to quit")
    stdscr.refresh()

    devman.sync_effects = False
    device = devman.devices[0]

    rows, cols = device.fx.advanced.rows, device.fx.advanced.cols

    device.fx.advanced.matrix.reset()
    device.fx.advanced.draw()

    firstRow = 0
    lastRow = rows - 1
    firstCol = 1
    lastCol = cols - 1
    
    row = randrange(0,lastRow)
    col = randrange(1,lastCol)
    segments = [(row, col)]
    lenght = 1
    foodRow = randrange(0,lastRow)
    foodCol = randrange(1,lastCol)
    
    running = True
    direction = None

    while running:
        keyp = stdscr.getch()
        if keyp == curses.KEY_RIGHT:
            direction = "right"
        elif keyp == curses.KEY_LEFT:
            direction = "left"
        elif keyp == curses.KEY_DOWN:
            direction = "down"
        elif keyp == curses.KEY_UP:
            direction = "up"
        elif keyp == curses.KEY_DC:
            running = False
        
        if direction == "right":
            if col < lastCol:
                col += 1
            else:
                col = firstCol
        elif direction == "left":
            if col > firstCol:
                col -= 1
            else:
                col = lastCol
        elif direction == "down":
            if row < lastRow:
                row += 1
            else:
                row = firstRow
        elif direction == "up":
            if row > firstRow:
                row -= 1
            else:
                row = lastRow
    
        #Player ate itself
        if segments[0] in segments[1:]:
            running = False
            stdscr.clear()
            stdscr.addstr(f"GAME OVER! \nyou ate yourself \nScore {lenght-1}")
            stdscr.refresh()
            stdscr.timeout(-1)
            stdscr.getch()

        #Player ate fruit
        if row == foodRow and col == foodCol:
            lenght += 1
            foodRow = randrange(0,lastRow)
            foodCol = randrange(1,lastCol)
            while [foodRow, foodCol] in segments:
                foodRow = randrange(0,lastRow)
                foodCol = randrange(1,lastCol)

        segments.append((row, col))
        segments = segments[-lenght:]
        
        device.fx.advanced.matrix.reset()
        device.fx.advanced.matrix[foodRow, foodCol] = (255,0,0)
        for segment in segments:
            device.fx.advanced.matrix[segment[0], segment[1]] = (0,255,0)
        device.fx.advanced.draw()    

    device.fx.advanced.restore()


if __name__ == "__main__":
    curses.wrapper(main)
