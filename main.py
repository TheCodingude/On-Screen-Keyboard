import tkinter as tk

class FullSizedKeyboardGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Full-Sized Virtual Keyboard")

        # Entry widget to display typed text
        self.text_entry = tk.Entry(root, width=50)
        self.text_entry.grid(row=0, column=0, columnspan=15)

        # Define the keyboard layout
        keyboard_layout = [
            ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
            ['tab','Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '\\'],
            ['caps lock','A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', "'"],
            ['shift' ,'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/'],
            ['Ctrl','win','Alt', 'Space', 'Ctrl', 'Alt', 'Fn']
        ]

        # Create and place buttons based on the layout
        for i, row in enumerate(keyboard_layout):
            for j, key in enumerate(row):
                button = tk.Button(root, text=key, width=4, height=2, command=lambda key=key: self.key_press(key))
                button.grid(row=i+1, column=j)

    def key_press(self, key):
        current_text = self.text_entry.get()

        if key == 'Clear':
            self.text_entry.delete(0, tk.END)
        elif key == 'Enter':
            # Handle Enter key press
            print("Entered:", current_text)
            # You can perform additional actions here
            self.text_entry.delete(0, tk.END)
        elif key == 'Space':
            # Handle Space key press
            self.text_entry.insert(tk.END, ' ')
        elif key == 'Shift':
            # Handle Shift key press
            pass  # You can add your own functionality for Shift key
        else:
            # Handle other key presses
            self.text_entry.insert(tk.END, key)

if __name__ == "__main__":
    root = tk.Tk()
    app = FullSizedKeyboardGUI(root)
    root.mainloop()
