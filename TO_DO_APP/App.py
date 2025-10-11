

import customtkinter as ctk



class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.task_count=0
        self.configure(fg_color='#1A1C22')
        self.geometry('500x500')
        self.title('To Do Means To Do')

        #heading
        self.head=ctk.CTkLabel(self,text='TO DO LIST',
                               font=('Arial', 25,'bold'),
                               text_color='#A7A8B2',
                               fg_color='#1A1C22')
        self.head.pack(pady=(20,10))

        #Frame to hold tasks
        self.tasks_frame = ctk.CTkFrame(self,fg_color='#1A1C22')
        self.tasks_frame.pack(fill='both',expand=True,pady=10)
        self.tasks_frame.columnconfigure(0,weight=1)

        #Entry + Button Container
        bottom_frame=ctk.CTkFrame(self,fg_color='#1A1C22')
        bottom_frame.pack(fill='x',padx=10,pady=10)
        #entry
        self.work = ctk.CTkEntry(bottom_frame,
                                 placeholder_text="What to Do?",
                                 font=('Arial', 15, 'bold'),
                                 border_color='#5A5C6A',
                                 border_width=3
                                 ,fg_color='#1A1C22')
        self.work.pack(side='left',fill='x',expand=True,padx=(0,5),ipady=5)
        #Button
        self.add_button=ctk.CTkButton(bottom_frame,text='+',
                                      font=('Arial',20,'bold'),
                                      fg_color='#A7A8B2',
                                      hover_color='#1A1C22',width=100,
                                      text_color='black',
                                      command=self.add_task)
        self.add_button.pack(side='right',ipady=3)

    def add_task(self):
        task_text = self.work.get().strip()

        # Empty input
        if not task_text:
            self.show_snackbar("⚠️ Please enter a task!")
            return

        # Too many tasks
        if self.task_count == 8:
            self.show_snackbar("❌ Task limit reached (8 max) !")
            return

        # Create task
        checkbox = ctk.CTkCheckBox(
            self.tasks_frame,
            text=task_text,
            font=('Arial', 15, 'bold'),
            text_color='white',
            fg_color='#5A5C6A',
            border_color='white',
            checkbox_width=20,
            checkbox_height=20
        )
        checkbox.pack(anchor='w', pady=5, padx=5, ipady=5)

        self.task_count += 1
        self.work.delete(0, 'end')

        self.show_snackbar("✅ Task added successfully!")

    def show_snackbar(self, message, duration=1000):
        """Animated snackbar above the Entry box."""

        # Create label
        snackbar = ctk.CTkLabel(
            self,
            text=message,
            fg_color="#323438",
            text_color="white",
            corner_radius=10,
            font=("Arial", 14, "bold"),
            padx=20,
            pady=8
        )

        # Calculate x, y for Entry
        x = self.work.winfo_rootx() - self.winfo_rootx() + self.work.winfo_width() / 2
        y_start = self.work.winfo_rooty() - self.winfo_rooty()  # start just hidden below
        y_end = y_start - 30  # final position above Entry

        snackbar.place(x=x, y=y_start, anchor="s")

        # Animate sliding up
        steps = 10
        dy = (y_start - y_end) / steps

        def slide_up(step=0):
            if step < steps:
                new_y = y_start - dy * step
                snackbar.place_configure(y=new_y)
                self.after(15, lambda: slide_up(step + 1))
            else:
                # stay for duration, then fade out
                self.after(duration, snackbar.destroy)

        slide_up()

if __name__ == '__main__':
    app = App()
    app.mainloop()

