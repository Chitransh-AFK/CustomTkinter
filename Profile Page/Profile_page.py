

import customtkinter as ctk


class Labels(ctk.CTkFrame):

    def __init__(self,master):
        super().__init__(master)

        self.grid_columnconfigure(1,weight=1)

        #Labels
        self.name = ctk.CTkLabel(self, text="Name:", font=('Arial', 15, 'bold'))
        self.name.grid(row=0, column=0, padx=10, pady=(10,5),sticky='e')

        self.Id=ctk.CTkLabel(self, text="ID:", font=('Arial', 15, 'bold'))
        self.Id.grid(row=1, column=0, padx=10, pady=(10,5),sticky='e')

        self.country=ctk.CTkLabel(self, text="Country:", font=('Arial', 15, 'bold'))
        self.country.grid(row=2, column=0, padx=10, pady=(10,5),sticky='e')

        #entry
        self.name_entry=ctk.CTkEntry(self,placeholder_text='Your Name Here', font=('Arial', 12, 'bold'),border_color='white')
        self.name_entry.grid(row=0, column=1, padx=10, pady=(10,5),sticky='ew')

        self.id_entry=ctk.CTkEntry(self,placeholder_text='Your ID Here', font=('Arial', 12, 'bold'),border_color='white')
        self.id_entry.grid(row=1, column=1, padx=10, pady=(10,5),sticky='ew')

        options = ['Select Country',
            "India",
            "United States",
            "United Kingdom",
            "Canada",
            "Australia",
            "Germany",
            "France",
            "Italy",
            "Spain",
            "Japan",
            "China",
            "South Korea",
            "Brazil",
            "Mexico",
            "Russia",
            "South Africa",
            "New Zealand",
            "Singapore",
            "Switzerland",
            "Netherlands",
            "Sweden",
            "Norway",
            "Denmark",
            "Finland",
            "Argentina",
            "Turkey",
            "Indonesia",
            "Saudi Arabia",
            "Thailand",
            "Philippines"
        ]
        self.country_options=ctk.CTkOptionMenu(self, values=options,font=('Arial', 12, 'bold'))
        self.country_options.grid(row=2, column=1, padx=10, pady=(10,5),sticky='ew')

    def get(self):
        name = self.name_entry.get().strip()
        identification=self.id_entry.get().strip()
        country=self.country_options.get().strip()
        if name=='' or identification== '' or country== '':
            return 'Please Enter Full Credentials'
        else:
            return f'{name} {identification} {country}'

class App(ctk.CTk):
    def __init__(self):
        super().__init__()



        self.iconbitmap('Icon.ico')
        self.title('Profile')
        self.geometry('400x290')
        self.resizable(width=False, height=False)
        self._set_appearance_mode('dark')
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0,weight=1)

        #Heading
        self.head=ctk.CTkLabel(self, text="PROFILE", font=('Arial', 25, 'bold'),text_color='Light Blue')
        self.head.grid(row=0, column=0, padx=10, pady=(10,5),sticky='N')

        self.Labels = Labels(self)
        self.Labels.grid(row=0,pady=10,sticky='ew')

        #Button
        self.Submit=ctk.CTkButton(self, text="Submit", font=('Arial', 15, 'bold'),command=self.button_callback)
        self.Submit.grid(padx=10, pady=10,sticky='ew')

    def button_callback(self):
        print('button callback')
        print(self.Labels.get())


if __name__ == '__main__':
    app = App()
    app.mainloop()






