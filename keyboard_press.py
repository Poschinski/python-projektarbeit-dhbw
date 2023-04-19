import keyboard

def on_press(event):
    print(f"You pressed {event.name}")
    
keyboard.on_press(on_press)

# Keep the program running
while True:
    pass
