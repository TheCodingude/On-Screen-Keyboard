import tkinter as tk

class FullSizedKeyboardGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Full-Sized Virtual Keyboard")
        self.keys = {}

        # Entry widget to display typed text
        self.text_entry = tk.Entry(root, width=50)
        self.text_entry.grid(row=0, column=0, columnspan=15)

        # Define the keyboard layout
        keyboard_layout = [
            ['Esc', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12'],
            ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'Backspace'],
            ['tab','q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\'],
            ['caps lock','a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'"],
            ['Shift' ,'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', 'Shift'],
            ['Ctrl','win','Alt', 'Space', 'Ctrl', 'Alt', 'Fn']
        ]

        # Create and place buttons based on the layout
        for i, row in enumerate(keyboard_layout):
            for j, key in enumerate(row):
                self.keys[key] = tk.Button(root, text=key, width=4, height=2, command=lambda key=key: self.key_press(key))
                self.keys[key].grid(row=i+1, column=j)

    def key_press(self, key):
        current_text = self.text_entry.get()

        if key == 'Backspace':
            self.text_entry.delete(tk.END, tk.END)
        elif key == 'Enter':
            # Handle Enter key press
            print("Entered:", current_text)
            # You can perform additional actions here
            self.text_entry.delete(0, tk.END)
        elif key == 'Space':
            # Handle Space key press
            self.text_entry.insert(tk.END, ' ')
        elif key == 'Shift':
            pass
        else:
            # Handle other key presses
            self.text_entry.insert(tk.END, key)

if __name__ == "__main__":
    root = tk.Tk()
    app = FullSizedKeyboardGUI(root)
    root.mainloop()
