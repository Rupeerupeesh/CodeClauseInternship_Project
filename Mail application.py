import tkinter as tk
from tkinter import messagebox

class MailApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mail Application")

        # Create labels and entry widgets
        self.label_to = tk.Label(root, text="To:")
        self.entry_to = tk.Entry(root)

        self.label_subject = tk.Label(root, text="Subject:")
        self.entry_subject = tk.Entry(root)

        self.label_body = tk.Label(root, text="Body:")
        self.text_body = tk.Text(root, height=5, width=30)

        # Create send button
        self.send_button = tk.Button(root, text="Send", command=self.send_mail)

        # Grid layout
        self.label_to.grid(row=0, column=0, sticky=tk.E)
        self.entry_to.grid(row=0, column=1, columnspan=2)

        self.label_subject.grid(row=1, column=0, sticky=tk.E)
        self.entry_subject.grid(row=1, column=1, columnspan=2)

        self.label_body.grid(row=2, column=0, sticky=tk.E)
        self.text_body.grid(row=2, column=1, columnspan=2)

        self.send_button.grid(row=3, column=1)

    def send_mail(self):
        to = self.entry_to.get()
        subject = self.entry_subject.get()
        body = self.text_body.get("1.0", tk.END)

        # You can implement the email sending logic here
        # For simplicity, we'll just display a messagebox with the email details
        message = f"To: {to}\nSubject: {subject}\nBody: {body}"
        messagebox.showinfo("Mail Sent", message)

if __name__ == "__main__":
    root = tk.Tk()
    app = MailApp(root)
    root.mainloop()
