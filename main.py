import webbrowser
import requests
from customtkinter import *
from tkinter import *
from tkinter import messagebox
import random as r
import json
from datetime import datetime


class Pixela:
    def __init__(self):
        # ---------- Variables-----------------
        self.users_dic = None
        self.token_list = []
        self.USERNAMES_LIST = []
        self.GRAPH_NAMES_LIST = []
        self.PIXELA_API_LINK = "https://pixe.la/"
        self.is_new_file = False
        self.today = datetime.today().strftime("%Y%m%d")

        # -------------------UI-Setup---------------------------------

        self.window = CTk()
        self.window.title("Habit Tracker")
        self.window.geometry("620x650")
        self.window.config(padx=20, pady=20)

        # -----------All-Buttons-----------------------
        self.token_generate_button = CTkButton(self.window, text="Generate Token", width=200,
                                               command=self.generate_token)
        self.save_button_graph_edit = CTkButton(self.window, text="Save", width=550, command=self.create_new_graph)
        self.get_graph_button = CTkButton(self.window, text="Get Graphs", width=200, command=self.get_graph_names)
        self.date_button = CTkButton(self.window, text="Today's Date", width=190, command=self.update_date_today)
        self.create_user_button = CTkButton(self.window, text="Create User", width=550,
                                            command=self.create_user)
        self.save_graph_button = CTkButton(self.window, text="Save Changes", width=550, command=self.update_graph)
        self.view_graph_button = CTkButton(self.window, text="View Graph", width=550, command=self.callback,
                                           state="disabled")

        # ------------All-Entries------------
        self.token_entry = CTkEntry(self.window,
                                    placeholder_text="Enter your own token or press the button to generate.",
                                    width=330)
        self.username_entry = CTkEntry(self.window, placeholder_text="Enter your unique username.", width=330)
        self.graph_name_entry = CTkEntry(self.window, placeholder_text="Name your Graph.", width=550)
        self.habit_name_entry = CTkEntry(self.window, placeholder_text="Habit Name", width=320)
        self.unit_entry = CTkEntry(self.window, placeholder_text="Unit of measurement.", width=205)
        self.date_entry = CTkEntry(self.window, placeholder_text="YYYYMMDD (Without Spaces)", width=350)
        self.quantity_entry = CTkEntry(self.window, placeholder_text="Duration/Quantity", width=350)

        # ------------All-Labels---------------------
        self.graph_label = CTkLabel(self.window, text="New Graph Details", font=("Ariel", 20, "bold"))
        self.color_label = CTkLabel(self.window, text="Choose Color", font=("Ariel", 20, "bold"))
        self.unit_label = CTkLabel(self.window, text="Unit", font=("Ariel", 15, "bold"))

        # ----------Color Selection RadioButtons-----------------
        self.color_selected = StringVar(value="")
        self.green_radio_button = CTkRadioButton(self.window, text="Green", variable=self.color_selected,
                                                 value="shibafu")
        self.red_radio_button = CTkRadioButton(self.window, text="Red", variable=self.color_selected, value="momiji")
        self.blue_radio_button = CTkRadioButton(self.window, text="Blue", variable=self.color_selected, value="sora")
        self.yellow_radio_button = CTkRadioButton(self.window, text="Yellow", variable=self.color_selected,
                                                  value="ichou")
        self.purple_radio_button = CTkRadioButton(self.window, text="Purple", variable=self.color_selected,
                                                  value="ajisai")
        self.black_radio_button = CTkRadioButton(self.window, text="Black", variable=self.color_selected, value="kuro")

        # ----------Dropdown-Menus-------------------
        self.username_dropdown = CTkOptionMenu(self.window, values=self.USERNAMES_LIST, anchor="center")
        self.username_dropdown.set("Select Username")
        self.graph_dropdown = CTkOptionMenu(self.window, values=self.USERNAMES_LIST, command=self.update_unit)
        self.graph_dropdown.set("Select Graph to make changes")

        # Header Radio Buttons------------------------------------------------------------------------------------
        self.radio_var = IntVar(value=0)
        self.new_user_selection = CTkRadioButton(self.window, text="Create New User", variable=self.radio_var, value=1,
                                                 command=self.start_process)
        self.new_user_selection.grid(row=0, column=0, padx=25)
        self.old_user_selection = CTkRadioButton(self.window, text="Add to Graphs", variable=self.radio_var, value=3,
                                                 command=self.start_process)
        self.old_user_selection.grid(row=0, column=2, padx=45)
        self.new_graph_selection = CTkRadioButton(self.window, text="New Graph", variable=self.radio_var, value=2,
                                                  command=self.start_process)
        self.new_graph_selection.grid(row=0, column=1, padx=45)

        self.all_ui_names = [self.token_generate_button, self.save_button_graph_edit, self.get_graph_button,
                             self.date_button, self.create_user_button, self.token_entry, self.username_entry,
                             self.graph_name_entry, self.habit_name_entry, self.unit_entry, self.date_entry,
                             self.quantity_entry, self.graph_label, self.color_label, self.unit_label,
                             self.green_radio_button, self.red_radio_button, self.blue_radio_button,
                             self.yellow_radio_button, self.purple_radio_button, self.black_radio_button,
                             self.username_dropdown, self.graph_dropdown, self.save_graph_button,
                             ]
        self.start_process()
        self.window.mainloop()

    def remove_all_widgets(self):
        for name in self.all_ui_names:
            name.grid_forget()

    def graph_ui(self):
        self.username_dropdown.configure(width=550)
        self.username_dropdown.grid(row=5, column=0, columnspan=3, sticky="e", pady=20)
        self.graph_label.grid(row=4, column=1, pady=20, sticky="e")
        self.graph_name_entry.grid(row=6, column=0, columnspan=3, pady=10, sticky="e")
        self.habit_name_entry.grid(row=7, column=0, columnspan=2, pady=10)
        self.unit_entry.grid(row=7, column=2)
        self.color_label.grid(row=8, column=1, pady=20, sticky="e")
        self.green_radio_button.grid(row=9, column=0)
        self.red_radio_button.grid(row=9, column=1)
        self.blue_radio_button.grid(row=9, column=2)
        self.yellow_radio_button.grid(row=10, column=0, pady=20)
        self.purple_radio_button.grid(row=10, column=1, pady=20)
        self.black_radio_button.grid(row=10, column=2, pady=20)
        self.save_button_graph_edit.grid(row=11, column=0, columnspan=3, pady=10, sticky="e")

    def new_user_ui(self):
        self.token_entry.grid(row=1, column=0, pady=20, columnspan=2)
        self.token_generate_button.grid(row=1, column=2, pady=20, sticky="w")
        self.username_entry.grid(row=2, column=0, columnspan=2)
        self.create_user_button.grid(row=3, column=0, columnspan=3, pady=10, sticky="e")

    def start_process(self):
        if self.radio_var.get() == 1:
            self.remove_all_widgets()
            self.new_user_ui()
            self.graph_ui()
            self.update_usernames()

        elif self.radio_var.get() == 2:
            self.remove_all_widgets()
            self.graph_ui()
            self.update_usernames()
        else:
            self.remove_all_widgets()
            self.add_to_graph_ui()
            self.update_usernames()

    def add_to_graph_ui(self):
        self.username_dropdown.configure(width=330)
        self.username_dropdown.grid(row=1, column=0, columnspan=2, pady=20)
        self.graph_dropdown.configure(width=550, anchor="center")
        self.graph_dropdown.grid(row=2, column=0, columnspan=3, pady=20, sticky="e")
        self.get_graph_button.grid(row=1, column=2, pady=20, sticky="w")
        self.date_entry.grid(row=3, column=0, columnspan=2, pady=20, sticky="e")
        self.date_button.grid(row=3, column=2)
        self.quantity_entry.grid(row=4, column=0, columnspan=2, pady=20, sticky="e")
        self.unit_label.grid(row=4, column=2, sticky="w", padx=20)
        self.save_graph_button.grid(row=5, column=0, columnspan=3, sticky="e")
        self.view_graph_button.grid(row=6, column=0, columnspan=3, sticky="e", pady=20)

    def generate_token(self):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u',
                   'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                   'P',
                   'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        self.token_list += [r.choice(letters) for n in range(0, 15)]

        r.shuffle(self.token_list)

        token = "".join(self.token_list)
        self.token_entry.insert(0, token)

    def create_user(self):
        user_create_api = f"{self.PIXELA_API_LINK}v1/users"
        pixela_token = self.token_entry.get()
        pixela_username = self.username_entry.get()
        if len(pixela_username) != 0 and len(pixela_token) != 0:
            create_user_parameters = {
                "token": pixela_token,
                "username": pixela_username,
                "agreeTermsOfService": "yes",
                "notMinor": "yes"
            }
            response = requests.post(url=user_create_api, json=create_user_parameters)
            if check_response(response, task="User", action="created"):
                data_to_save = {
                    pixela_username: {
                        "token": pixela_token,
                        "graphs": {}
                    }
                }

                if not self.is_new_file:
                    with open("users.json", "r") as old_file:
                        self.users_dic = json.load(old_file)
                        self.users_dic.update(data_to_save)
                    with open("users.json", "w") as updated_file:
                        json.dump(self.users_dic, updated_file, indent=4)
                else:
                    with open("users.json", "w") as new_file_created:
                        json.dump(data_to_save, new_file_created, indent=4)
                    self.is_new_file = False

                self.update_usernames()
        else:
            messagebox.showerror(message="Please fill all boxes.", title="Error")

    def update_usernames(self):
        try:
            updated_data = open("users.json", "r")
            try:
                data_to_load = json.load(updated_data)
                self.USERNAMES_LIST = list(data_to_load.keys())
                self.username_dropdown.configure(values=self.USERNAMES_LIST)
            except json.JSONDecodeError:
                pass
            updated_data.close()
        except FileNotFoundError:
            new_file = open("users.json", "w")
            new_file.close()
            self.is_new_file = True

    def create_new_graph(self):
        try:
            dict_data = get_data()
            graph_unit = self.unit_entry.get()
            graph_id = self.graph_name_entry.get()
            username = self.username_dropdown.get()
            api_link = f"{self.PIXELA_API_LINK}v1/users/{username}/graphs"
            header = {
                "X-USER-TOKEN": dict_data[username]["token"]
            }
            parameters = {
                "id": graph_id,
                "name": self.habit_name_entry.get(),
                "unit": graph_unit,
                "type": "float",
                "color": self.color_selected.get()
            }
            response = requests.post(url=api_link, json=parameters, headers=header)
            if check_response(response, task="Graph", action="created"):
                dict_data[username]["graphs"][graph_id] = graph_unit
                with open("users.json", "r") as old_file:
                    self.users_dic = json.load(old_file)
                    self.users_dic.update(dict_data)
                with open("users.json", "w") as updated_file:
                    json.dump(self.users_dic, updated_file, indent=4)
        except KeyError:
            messagebox.showerror(message="Please fill all boxes and select username if not selected.", title="Error")

    def get_graph_names(self):
        username = self.username_dropdown.get()
        try:
            data_dict = get_data()
            self.GRAPH_NAMES_LIST = []
            self.GRAPH_NAMES_LIST = data_dict[username]["graphs"]
            self.graph_dropdown.configure(values=self.GRAPH_NAMES_LIST)
        except KeyError:
            messagebox.showerror(message="Please select username.", title="Error")

    def update_graph(self):
        try:
            username = self.username_dropdown.get()
            graph_name = self.graph_dropdown.get()
            graph_update_api = f"{self.PIXELA_API_LINK}v1/users/{username}/graphs/{graph_name}"
            dict_data = get_data()
            quantity = self.quantity_entry.get()
            header = {
                "X-USER-TOKEN": dict_data[username]["token"]
            }
            parameters = {
                "date": self.date_entry.get(),
                "quantity": quantity
            }
            response = requests.post(url=graph_update_api, json=parameters, headers=header)
            if not check_response(response, task="Changes", action="made"):
                messagebox.showerror(message="Please select Graph Name.", title="Error")
        except KeyError:
            messagebox.showerror(message="Please select username.", title="Error")

    def update_unit(self, value):
        username = self.username_dropdown.get()
        graph_name = self.graph_dropdown.get()
        data_dict = get_data()
        unit = data_dict[username]["graphs"][graph_name]
        self.unit_label.configure(text=f"{unit}")
        self.view_graph_button.configure(state="normal")

    def update_date_today(self):
        self.date_entry.insert(0, self.today)

    def callback(self):
        username = self.username_dropdown.get()
        graph_name = self.graph_dropdown.get()
        url_to_open = f"https://pixe.la/v1/users/{username}/graphs/{graph_name}.html"
        webbrowser.open_new(url_to_open)


def get_data() -> dict:
    with open("users.json", "r") as data:
        return json.load(data)


def check_response(response, task, action):
    if not response.ok:
        response.raise_for_status()
        messagebox.showerror(message=f"Some error occurred while performing, please check your internet"
                                     "connection and try again.", title="Error")
        return False
    else:
        messagebox.showinfo(message=f"{task} successfully {action}!", title="Successful!")
        return True


window = Pixela()
