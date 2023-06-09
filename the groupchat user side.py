
import tkinter
import tkinter.messagebox
import customtkinter
import subprocess
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread




customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("green")  

class App(customtkinter.CTk):
    

   
    def __init__(self):
        def send(): 
            """Handles sending of messages."""
            msg = self.entry.get()
            client_socket.send(bytes(msg, "utf8"))
            if msg == "{quit}":
                client_socket.close()
        
        super().__init__()
        self.title("Your Chat Room!")
        self.geometry(f"{1100}x{580}")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="The ChatRoom", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 5))
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                                       values=["System", "Dark", "Light"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                               values=["100%", "80%", "90%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Chat", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=1, column=0, padx=20, pady=(5, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text='Take me to AYCI',command=self.sidebar_button_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        
        self.entry = customtkinter.CTkEntry(self, placeholder_text="How Can I Help You?")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
        
        self.main_button_1 = customtkinter.CTkButton(master=self,text="Send", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),command=send)
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")


        

     
      
        self.radiobutton_frame = customtkinter.CTkFrame(self)
        self.radiobutton_frame.grid(row=0, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.radio_var = tkinter.IntVar(value=0)
        self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="Mode of convo")
        self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="Text to Text", variable=self.radio_var, value=0)
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
       
 
        
        
        
        def change_appearance_mode_event(self, new_appearance_mode: str):
            customtkinter.set_appearance_mode(new_appearance_mode)
        def change_scaling_event(self, new_scaling: str):
            new_scaling_float = int(new_scaling.replace("%", "")) / 100
            customtkinter.set_widget_scaling(new_scaling_float)
        def sidebar_button_event(self):
            print("sidebar_button click")
        def receive():
            """Handles receiving of messages."""
            while True:
                try:
                    msg = client_socket.recv(BUFSIZ).decode("utf8")
                    switch = customtkinter.CTkLabel(master=self.scrollable_frame, text=msg)
                    switch.grid( column=0, padx=10)
                    self.scrollable_frame_switches.append(msg)                    
                except OSError:
                        break
        
       
        
            customtkinter.set_widget_scaling(new_scaling_float)
        def sidebar_button_event(self):
            print("sidebar_button click")
            
        

        self.scrollable_frame = customtkinter.CTkScrollableFrame(self,width=250, label_text="The conversation")
        self.scrollable_frame.grid(row=1, column=1,columnspan=3, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame_switches = []
        


        HOST = '127.0.0.1'
        PORT = 3000
        BUFSIZ = 1024
        ADDR = (HOST, PORT)

        client_socket = socket(AF_INET, SOCK_STREAM)
        client_socket.connect(ADDR)

        receive_thread = Thread(target=receive)
        receive_thread.start()
    def sidebar_button_event(self):
       subprocess.call(["python", "chatbot.py"])
    def change_appearance_mode_event(self, new_appearance_mode: str):
            customtkinter.set_appearance_mode(new_appearance_mode)
    def change_scaling_event(self, new_scaling: str):
            new_scaling_float = int(new_scaling.replace("%", "")) / 100
            customtkinter.set_widget_scaling(new_scaling_float)
if __name__ == "__main__":
    app = App()
    app.mainloop()












