import json
import os
from pynput import keyboard, mouse
from PIL import ImageGrab

# File to persist color history
HISTORY_FILE = 'colors_history.json'

# Load color history from file (if exists)
def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r') as f:
            return json.load(f)
    return []

# Save current color list to history file
def save_history(colors):
    with open(HISTORY_FILE, 'w') as f:
        json.dump(colors, f)

# Clear history file
def clear_history():
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)
    return []

# Show total colors in history
def show_history_stats(colors):
    print(f"Total colors stored: {len(colors)}")
    for i, color in enumerate(colors):
        print(f"{i+1}. {color}")

# --------- Main color grabbing code (as in your earlier script) -----------

colorList = load_history()

def printColorList():
    print("Colors detected are:", end=" ")
    for color in colorList:
        print(f"{color}", end=", ")
    print()

def getHex(rgb):
    output = ''.join([hex(v)[2:].upper().zfill(2) for v in rgb])
    return output

def hex_to_rgb(hexcode):
    hexcode = hexcode.lstrip('#')
    return tuple(int(hexcode[i:i+2], 16) for i in (0, 2, 4))

def getColor(x, y):
    coor = x, y
    return ImageGrab.grab().getpixel(coor)

def onClick(x, y, button, press):
    if button == mouse.Button.right and press:
        color = getColor(x, y)
        hex_color = getHex(color)
        colorList.append(hex_color)
        print(f"Color at mouse click: (x={x}, y={y}) = {hex_color}")
        save_history(colorList)

exit_requested = False
def onKey(key):
    global exit_requested
    if key == keyboard.Key.delete:
        print("Exiting color capture...")
        exit_requested = True
        return False

def main():
    while True:
        print("\nColor Capture Tool")
        print("1. Start capturing colors")
        print("2. Export colors to a file")
        print("3. Clear color history")
        print("4. Show color history stats")
        print("5. Exit")
        choice = input("Enter choice (1-5): ")
        if choice == '1':
            print("Right-click to capture colors. Press Delete to exit.")
            with keyboard.Listener(on_press=onKey) as k, mouse.Listener(on_click=onClick) as m:
                k.join()
        elif choice == '2':
            file_path = input("Enter file path to export colors: ")
            with open(file_path, 'w') as f:
                for color in colorList:
                    f.write(f"{color}\n")
            print(f"Colors exported to {file_path}")
        elif choice == '3':
            colorList = clear_history()
            print("Color history cleared.")
        elif choice == '4':
            show_history_stats(colorList)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please choose between 1-5.")

if __name__ == "__main__":
    main()