from tkinter import *
from tkinter import filedialog, messagebox

def encrypt_decrypt_image(encrypt=True):
    file1 = filedialog.askopenfile(mode='r', filetype=[('jpg file', '*.jpg')])
    if file1 is not None:
        file_name = file1.name
        key = entry1.get().strip()

        if not key.isdigit():
            messagebox.showerror("Invalid Key", "Key should be a numeric value.")
            return

        key = int(key)
        try:
            with open(file_name, 'rb') as fi:
                image = bytearray(fi.read())
            
            for index, value in enumerate(image):
                image[index] = value ^ key
            
            with open(file_name, 'wb') as fi:
                fi.write(image)
            
            action = "encrypted" if encrypt else "decrypted"
            messagebox.showinfo("Success", f"Image successfully {action}.")
        
        except Exception as e:
            messagebox.showerror("Error", str(e))

root = Tk()
root.geometry("300x150")
root.title("Image Encrypt/Decrypt")

Label(root, text="Enter Key:").place(x=10, y=10)
entry1 = Entry(root, show="*")
entry1.place(x=100, y=10)

Button(root, text="Encrypt", command=lambda: encrypt_decrypt_image(encrypt=True)).place(x=50, y=50)
Button(root, text="Decrypt", command=lambda: encrypt_decrypt_image(encrypt=False)).place(x=150, y=50)

root.mainloop()