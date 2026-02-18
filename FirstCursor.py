import tkinter as tk
import sys
root = tk.Tk()
root.title("User Box Example")
root.geometry("300x200")
user_label = tk.Label(root, text="User ID:")
user_label.pack(pady=10)
user_entry = tk.Entry(root)
user_entry.pack(pady=5)
submit_button = tk.Button(root, text="Submit", command=lambda: print(f"User ID: {user_entry.get()}"))
submit_button.pack(pady=10)
root.mainloop()