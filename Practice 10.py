import customtkinter as c

app = c.CTk()
app.title('Day 5 Practice')
app.geometry('300x500')

page_home = c.CTkFrame(master=app)
page_image3 = c.CTkFrame(master=app)
page_image2 = c.CTkFrame(master=app)

def show_page(page_to_show):
    page_home.pack_forget()
    page_image3.pack_forget()
    page_image2.pack_forget()
    page_to_show.pack(fill='both', expand=True)


login_button = c.CTkButton (master=page_home, text='Click Me Loser', 
                            font=('Bold', 20), text_color='white',
                            width=120, height=40, fg_color='black',
                            corner_radius=10, border_width=3, hover_color='purple',
                            border_color='green',
                            command=lambda: show_page(page_image2))
login_button.place(x=79, y=40)

sign_buton = c.CTkButton (master=page_home, text='Click Me Solus', 
                            font=('Bold', 25), text_color='gold',
                            width=40, height=120, fg_color='white',
                            corner_radius=20, border_width=2, hover_color='purple',
                            border_color='blue',
                            command=lambda: show_page(page_image3))
sign_buton.place(x=55, y=150)

page_home.pack(fill='both', expand=True)
app.mainloop()
