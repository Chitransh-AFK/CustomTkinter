import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.iconbitmap('Icon.ico')
        self.title('Greeting App')
        self.geometry('350x200')
        self._set_appearance_mode('system')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        def say_hello():
            name = self.entry.get().strip()
            if name:
                self.print_name.configure(text=f'Hello! {name}')
            else:
                self.print_name.configure(text='Please Enter Your Name!')

        self.label=ctk.CTkLabel(self,text="Enter Your Name:",font=('Arial',20,'bold'))
        self.label.grid(row=0,pady=(10,5))

        self.entry=ctk.CTkEntry(self,placeholder_text='Your name here',font=('Arial',15,'bold'))
        self.entry.grid(row=1,pady=(10,5),sticky='ew')

        self.submit=ctk.CTkButton(self,text="Submit",font=('Arial',15,'bold'),command=say_hello)
        self.submit.grid(row=2,pady=(10,5),sticky='ew')

        self.print_name=ctk.CTkLabel(self,text="",font=('Arial',15,'bold'))
        self.print_name.grid(pady=10)



if __name__ == '__main__':
    app = App()
    app.mainloop()