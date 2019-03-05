from tkinter import messagebox, simpledialog, Tk

def get_even_letter(message):
    return "".join([x for i, x in enumerate(message) if i%2==0])

def get_odds_letter(message):
    return "".join([x for i, x in enumerate(message) if i%2==1])

def swap_letters(message):
    if len(message) % 2 != 0:
        message += "*"
    even = get_even_letter(message)
    odds  = get_odds_letter(message)
    letter_list = []
    for index in range(len(message)//2):
        letter_list.append(odds[index])
        letter_list.append(even[index])
    if task == "decrypt" and letter_list[-1] == "*":
        letter_list = letter_list[:-1]
    return ''.join(letter_list)

def get_task():
    task = simpledialog.askstring("Task","Do you want to encrypt or decrypt or quit ?")
    return task

def get_message():
    message = simpledialog.askstring("Message","Enter the secret message." )
    return message

root = Tk()
while True:
    task = get_task()
    if task == 'encrypt':
        message = get_message()
        encrypted = swap_letters(message)
        messagebox.showinfo('Ciphertext of the secret message is:', encrypted)
    elif task == 'decrypt':
        message = get_message()
        decrypted = swap_letters(message)
        messagebox.showinfo('Plaintext of the secret message is:', decrypted)
    else:
        break
#root.mainloop()
