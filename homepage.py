import tkinter
import tkinter.messagebox
import customtkinter
import subprocess

# Appearance Settings
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Configure Window
        self.title("D633 Lights/Music Management System")
        
        # Window Size
        self.geometry(f"{1100}x{480}")

        # Configure Grid Layout
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure((1), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)



        # Sidebar Frame (Left)
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        # Logo Label
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="D633 LMMS",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # All Lights ON Button
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="All Lights ON")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)

        # All Lights OFF Button
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="All Lights OFF")
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)

        # Appearance Mode (Light/Dark)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionmenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                                      values=["Light", "Dark", "System"],
                                                                      command=self.change_appearance_mode_event)
        self.appearance_mode_optionmenu.grid(row=6, column=0, padx=20, pady=(10, 10))



        # Sidebar Frame (Right)
        self.sidebar_frame2 = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame2.grid(row=0, column=2, rowspan=4, sticky="nsew")
        self.sidebar_frame2.grid_rowconfigure(4, weight=1)

        # Close Button
        self.main_button_1 = customtkinter.CTkButton(self.sidebar_frame2, text="Close", fg_color="transparent",
                                                     border_width=2, text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=6, column=2, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.main_button_1.configure(command=self.close_window)



        # Main Frame
        self.frame = customtkinter.CTkFrame(self, width=300, corner_radius=5)
        self.frame.grid(row=0, column=1, rowspan=2, sticky="nsew")
        self.frame.grid_rowconfigure(4, weight=1)

        total_rows = self.grid_size()[1]

        middle_row = total_rows // 2

        self.frame.grid(row=1, column=1, padx=20, pady=(10,10))

        # Page Heading
        self.label = customtkinter.CTkLabel(self.frame, text=" Welcome to the D633 Lights and Music Management System",
                                                 font=customtkinter.CTkFont(size=22, weight="bold"))
        self.label.grid(row=0, column=1, padx=20, pady=(40, 40))

        # Main Menu
        # Light Control Button
        self.button_1 = customtkinter.CTkButton(self.frame, text="Light Control", font=customtkinter.CTkFont(size=20),
                                                        command=self.open_lightcontrol, width=350, height=50, fg_color="#44dd45", hover_color="#02c910", text_color="black", border_width=3, border_color="white")
        self.button_1.grid(row=1, column=1, padx=20, pady=(10,15))
        
        # Music Player Button
        self.button_2 = customtkinter.CTkButton(self.frame, text="Music Player", font=customtkinter.CTkFont(size=20),
                                                        command=self.open_musicplayer, width=350, height=50, fg_color="#44dd45", hover_color="#02c910", text_color="black", border_width=3, border_color="white")
        self.button_2.grid(row=2, column=1, padx=20, pady=(10,15))

        # Special Effects Button
        self.button_3 = customtkinter.CTkButton(self.frame, text="Special Effects", font=customtkinter.CTkFont(size=20),
                                                        command=self.open_specialeffects, width=350, height=50, fg_color="#44dd45", hover_color="#02c910", text_color="black", border_width=3, border_color="white")
        self.button_3.grid(row=3, column=1, padx=20, pady=(10,0))

        # Add More Lights Button
        self.button_4 = customtkinter.CTkButton(self.frame, text="Add More Lights", font=customtkinter.CTkFont(size=20),
                                                        command=self.open_addmorelights, width=350, height=50, fg_color="#44dd45", hover_color="#02c910", text_color="black", border_width=3, border_color="white")
        self.button_4.grid(row=4, column=1, padx=20, pady=(0,10))



        # Default Values
        self.appearance_mode_optionmenu.set("Dark")



    # Functions

    # Open Light Control Page
    def open_lightcontrol(self):
        subprocess.Popen(["python", "lightcontrol.py"])
        self.destroy()

    # Open Music Player Page
    def open_musicplayer(self):
        subprocess.Popen(["python", "musicplayer.py"])
        self.destroy()

    # Open Special Effects Page
    def open_specialeffects(self):
        subprocess.Popen(["python", "specialeffects.py"])
        self.destroy()

    # Open Add More Lights Page
    def open_addmorelights(self):
        subprocess.Popen(["python", "addmorelights.py"])
        self.destroy()

    # Change Appearance Mode
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    # Change Scaling Event
    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    # Close Window
    def close_window(self):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
