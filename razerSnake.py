from openrazer.client import DeviceManager
import time
from pynput.keyboard import Key, Listener
from random import randrange

class keyboardHandler:
    def __init__(self):
        self.keyp = None
        self.running = True
        listener = Listener(on_press=self.show)
        listener.start()

    def show(self, key):
        self.keyp = key
        if key == Key.delete:
            self.running = False
        return self.running 

devman = DeviceManager()

print(f"Found {len(devman.devices)} Razer devices")
print()


# Iterate over each device and pretty out some standard information about each
for device in devman.devices:
    print(f"{device.name}:")
    print(f"   type: {device.type}")
    print()

devman.sync_effects = False
device = devman.devices[0]

rows, cols = device.fx.advanced.rows, device.fx.advanced.cols

device.fx.advanced.matrix.reset()
device.fx.advanced.draw()
kbh = keyboardHandler()

firstRow = 0
lastRow = rows - 1
firstCol = 1
lastCol = cols - 1

row = randrange(0,5)
col = randrange(1,21)
segments = [(row, col)]
lenght = 1
foodRow = randrange(0,5)
foodCol = randrange(1,21)

while kbh.running:
    if kbh.keyp == Key.right:
        if col < lastCol:
            col += 1
        else:
            col = firstCol
    elif kbh.keyp == Key.left:
        if col > firstCol:
            col -= 1
        else:
            col = lastCol
    elif kbh.keyp == Key.down:
        if row < lastRow:
            row += 1
        else:
            row = firstRow
    elif kbh.keyp == Key.up:
        if row > firstRow:
            row -= 1
        else:
            row = lastRow
    time.sleep(0.3)
    
    if segments[0] in segments[1:]:
        kbh.running = False

    if row == foodRow and col == foodCol:
        lenght += 1
        foodRow = randrange(0,5)
        foodCol = randrange(1,21)

    segments.append((row, col))
    segments = segments[-lenght:]
    device.fx.advanced.matrix.reset()
    device.fx.advanced.matrix[foodRow, foodCol] = (255,0,0)
    for segment in segments:
        device.fx.advanced.matrix[segment[0], segment[1]] = (0,255,0)
    device.fx.advanced.draw()    

device.fx.advanced.restore()
