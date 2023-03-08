import tkinter as tk
import pyrebase

firebaseConfig = {
    # Aqui você deve inserir as informações de configuração do seu projeto Firebase
    "apiKey": "AIzaSyCVOOkET2KeMR-ItSpwCYcmNj4HSE4pV1M",
    "authDomain": "projetest-d454c.firebaseapp.com",
    "databaseURL": "https://projetest-d454c-default-rtdb.firebaseio.com",
    "projectId": "projetest-d454c",
    "storageBucket": "projetest-d454c.appspot.com",
    "messagingSenderId": "136511753958",
    "appId": "1:136511753958:web:307d0b68618f6e0f58f527"
}

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()


class FirebaseScreen:
    def _init_(self, master):
        self.master = master
        master.title('user')

        self.label = tk.Label(master, text='user')
        self.label.pack()

        self.listbox = tk.Listbox(master)
        self.listbox.pack()

        self.load_data()

    def load_data(self):
        data = db.child('user').get()
        for item in data.each():
            self.listbox.insert(tk.END, item.val())

            

if __name__ == '_main_':
    root = tk.Tk()
    app = FirebaseScreen(root)
    root.mainloop()

