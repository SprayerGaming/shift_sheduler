import pyautogui
import time

# Get screen resolution
screen_width, screen_height = pyautogui.size()

print("Move the mouse to the desired position... (3 sec delay)")
time.sleep(5)

# Get absolute position
x, y = pyautogui.position()

# Convert to relative coordinates (0 to 1 range)
rel_x = x / screen_width
rel_y = y / screen_height

print(f"Absolute Position: ({x}, {y})")
print(f"Relative Position: ({rel_x}, {rel_y})")
