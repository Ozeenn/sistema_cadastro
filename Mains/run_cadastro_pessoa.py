"""
@author: patrick_alan
@created_date: 17/09/2022
"""

from tkinter import Label, Entry, Button, Tk, StringVar
from tkinter.messagebox import showwarning, showinfo
from Config.Postgre import PostgreConfig
from Connections.Postgre import PostgreConnection
from datetime import datetime, date
import json

###################
post_conn = PostgreConnection(
    PostgreConfig('db_cadastro')
)
###################


class CadApp:
    def __init__(self):
        self.tkinter = Tk()
        self.tkinter.protocol("WM_DELETE_WINDOW", lambda: CadApp.close_window(self))
        self.tkinter.title('LOGIN DE USUÁRIO')
        self.__screen_width = self.tkinter.winfo_screenwidth()
        self.__screen_height = self.tkinter.winfo_screenheight()
        self.__entry_var_register_1 = StringVar()
        self.__entry_var_register_2 = StringVar()
        self.__entry_var_login_1 = StringVar()
        self.__entry_var_login_2 = StringVar()
        self.__window_width = 400
        self.__window_height = 300
        self.__x_cord = int(
            (self.__screen_width / 2) - (self.__window_width / 2)
        )
        self.__y_cord = int(
            (self.__screen_height / 2) - (self.__window_height / 2)
        )

        self.tkinter.geometry(
            "{}x{}+{}+{}".format(
                self.__window_width, self.__window_height, self.__x_cord, self.__y_cord
            )
        )
        self.tkinter.resizable(False, False)
        self.tkinter.configure(bg='#6ec3f9')

        self.__label_dft_config = {
            'font': ("Mulish bold", 40),
            'background': '#6ec3f9'
        }

        CadApp.menu_screen(self)

    @staticmethod
    def register_screen(self):
        self.__label_register = Label(
            self.tkinter,
            text='CADASTRO',
            **self.__label_dft_config
        )

        self.__label_register.pack(side='top')

        self.__label_register_2 = Label(
            self.tkinter,
            text='User',
            font=("Mulish bold", 20),
            background='#6ec3f9'
        )

        self.__label_register_2.pack(side='top')

        self.__input_box_register_1 = Entry(
            self.tkinter,
            cursor='arrow',
            width=20,
            font='Mulish',
            justify='left',
            takefocus=True,
            textvariable=self.__entry_var_register_1
        )

        self.__input_box_register_1.pack(side='top')

        self.__label_register_3 = Label(
            self.tkinter,
            text='Password',
            font=("Mulish bold", 20),
            background='#6ec3f9'
        )

        self.__label_register_3.pack(side='top')

        self.__input_box_register_2 = Entry(
            self.tkinter,
            cursor='arrow',
            width=20,
            font='Mulish',
            justify='left',
            takefocus=True,
            show="*",
            textvariable=self.__entry_var_register_2
        )

        self.__input_box_register_2.pack(side='top')

        self.__empty_label = Label(
            self.tkinter,
            text='',
            background='#6ec3f9',
            height=0
        )

        self.__empty_label.pack(side='top')

        self.__register_button = Button(
            self.tkinter,
            text='REGISTER',
            command=lambda: CadApp.cad_user(
                user=self.__input_box_register_1.get(),
                pswd=self.__input_box_register_2.get()
            ),
            padx=75, pady=15, state='disabled'
        )

        self.__register_button.pack(side='right')

        self.__trace_id_1 = self.__entry_var_register_1.trace_add("write",
                                                                  lambda *args: CadApp.character_limit(
                                                                      self.__entry_var_register_1.get(),
                                                                      self.__register_button))

        self.__trace_id_2 = self.__entry_var_register_2.trace("w",
                                                              lambda *args: CadApp.character_limit(
                                                                  self.__entry_var_register_2.get(),
                                                                  self.__register_button))

        self.__register_home_button = Button(
            self.tkinter,
            text='MENU',
            command=lambda: (
                self.__label_register.destroy(),
                self.__register_button.destroy(),
                self.__register_home_button.destroy(),
                self.__label_register_2.destroy(),
                self.__label_register_3.destroy(),
                self.__input_box_register_1.destroy(),
                self.__input_box_register_2.destroy(),
                self.__empty_label.destroy(),
                self.__entry_var_register_1.trace_remove('write', self.__trace_id_1),
                self.__entry_var_register_2.trace_remove('write', self.__trace_id_2),
                self.__entry_var_register_1.set(""),
                self.__entry_var_register_2.set(""),
                CadApp.menu_screen(self)
            ),
            padx=76, pady=15
        )

        self.__register_home_button.pack(side='left')

    @staticmethod
    def login_screen(self):
        self.__label_login = Label(
            self.tkinter,
            text='CONECTAR',
            **self.__label_dft_config
        )

        self.__label_login.pack(side='top')

        self.__label_login_2 = Label(
            self.tkinter,
            text='User',
            font=("Mulish bold", 20),
            background='#6ec3f9'
        )

        self.__label_login_2.pack(side='top')

        self.__input_box_login_1 = Entry(
            self.tkinter,
            cursor='arrow',
            width=20,
            font='Mulish',
            justify='left',
            takefocus=True,
            textvariable=self.__entry_var_login_1
        )

        self.__input_box_login_1.pack(side='top')

        self.__label_login_3 = Label(
            self.tkinter,
            text='Password',
            font=("Mulish bold", 20),
            background='#6ec3f9'
        )

        self.__label_login_3.pack(side='top')

        self.__input_box_login_2 = Entry(
            self.tkinter,
            cursor='arrow',
            width=20,
            font='Mulish',
            justify='left',
            takefocus=True,
            show="*",
            textvariable=self.__entry_var_login_2
        )

        self.__input_box_login_2.pack(side='top')

        self.__empty_label = Label(
            self.tkinter,
            text='',
            background='#6ec3f9',
            height=0
        )

        self.__empty_label.pack(side='top')

        self.__login_button = Button(
            self.tkinter,
            text='CONECTAR',
            command=lambda: CadApp.login_user(
                user=self.__input_box_login_1.get(),
                pswd=self.__input_box_login_2.get()
            ),
            padx=75, pady=15, state='disabled'
        )

        self.__login_button.pack(side='right')

        self.__trace_id_3 = self.__entry_var_login_1.trace("w",
                                                           lambda *args: CadApp.character_limit(
                                                               self.__entry_var_login_1.get(),
                                                               self.__login_button))
        self.__trace_id_4 = self.__entry_var_login_2.trace("w",
                                                           lambda *args: CadApp.character_limit(
                                                               self.__entry_var_login_2.get(),
                                                               self.__login_button))

        self.__login_home_button = Button(
            self.tkinter,
            text='MENU',
            command=lambda: (
                self.__label_login.destroy(),
                self.__login_button.destroy(),
                self.__login_home_button.destroy(),
                self.__label_login_2.destroy(),
                self.__label_login_3.destroy(),
                self.__input_box_login_1.destroy(),
                self.__input_box_login_2.destroy(),
                self.__empty_label.destroy(),
                self.__entry_var_login_1.trace_remove('write', self.__trace_id_3),
                self.__entry_var_login_2.trace_remove('write', self.__trace_id_4),
                self.__entry_var_login_1.set(""),
                self.__entry_var_login_2.set(""),
                CadApp.menu_screen(self)
            ),
            padx=76, pady=15
        )

        self.__login_home_button.pack(side='left')

    @staticmethod
    def menu_screen(self):
        self.__label_menu = Label(
            self.tkinter,
            text='MENU INICIAL',
            **self.__label_dft_config
        )

        self.__label_menu.pack(side='top')

        self.__home_register_button = Button(
            self.tkinter,
            text='CADASTRE-SE',
            command=lambda: (
                self.__label_menu.destroy(),
                self.__home_register_button.destroy(),
                self.__home_login_button.destroy(),
                self.__empty_label.destroy(),
                CadApp.register_screen(self)
            ),
            padx=100, pady=30
        )
        self.__home_register_button.pack(side='top')

        self.__empty_label = Label(
            self.tkinter,
            text='',
            background='#6ec3f9',
            height=0
        )

        self.__empty_label.pack(side='top')

        self.__home_login_button = Button(
            self.tkinter,
            text='CONECTE-SE',
            command=lambda: (
                self.__label_menu.destroy(),
                self.__home_register_button.destroy(),
                self.__home_login_button.destroy(),
                self.__empty_label.destroy(),
                CadApp.login_screen(self)
            ),
            padx=103, pady=30
        )
        self.__home_login_button.pack(side='top')

    def run_screen(self):
        self.tkinter.mainloop()

    @staticmethod
    def character_limit(entry_text, button_obj):
        if len(entry_text) > 15 or entry_text is None or entry_text == '':
            button_obj["state"] = "disabled"
        else:
            button_obj["state"] = "normal"

    @staticmethod
    def cad_user(user: str = None, pswd: str = None):
        if CadApp.verifica_user_cadastrado(user):
            showwarning('Atenção', 'Usuário já cadastrado, tente outro')
            CadApp.set_log_user(user=user, log_event='Usuário já cadastrado', event_type='ERRO')
        else:
            post_conn.insert_into(
                table='staging.stg_cadastro',
                data=[
                    [user.upper(), pswd, datetime.today()]
                ],
                flg_trunc_before=False
            )
            post_conn.call_proc('proc_insert_tb_cadastro')

            showinfo('Sucesso', 'Usuário cadastrado com sucesso')
            CadApp.set_log_user(user=user, log_event='Novo usuário cadastrado', event_type='SUCESSO')

    @staticmethod
    def login_user(user: str = None, pswd: str = None):
        if not post_conn.return_query_list(f"""
                select 1 from cadastro_pessoa.tb_cadastro
                where nom_user = '{user.upper()}' and des_password = '{pswd}' """):
            showwarning('Atenção', 'Usuário ou senha incorretos. Verifique seus dados')
            CadApp.set_log_user(user=user, log_event='Erro: Tentativa de login fracassada', event_type='ERRO')

        else:
            showinfo('Sucesso', 'Login feito com sucesso')
            CadApp.set_log_user(user=user, log_event='Login realizado com sucesso', event_type='SUCESSO')

    @staticmethod
    def close_window(self):
        if self.__entry_var_register_1.get() != '':
            CadApp.set_log_user(self.__entry_var_register_1.get(), 'Fechar janelas', event_type='SISTEMA')
        elif self.__entry_var_register_2.get() != '':
            CadApp.set_log_user(self.__entry_var_register_2.get(), 'Fechar janelas', event_type='SISTEMA')
        elif self.__entry_var_login_1.get() != '':
            CadApp.set_log_user(self.__entry_var_login_1.get(), 'Fechar janelas', event_type='SISTEMA')
        elif self.__entry_var_login_2.get() != '':
            CadApp.set_log_user(self.__entry_var_login_2.get(), 'Fechar janelas', event_type='SISTEMA')
        else:
            pass

        self.tkinter.destroy()

    @staticmethod
    def set_log_user(user, log_event, event_type):
        if CadApp.verifica_user_cadastrado(user):
            json_history = CadApp.return_history_json(user=user, dat_event=date.today().strftime('%Y-%m-%d'))
            if json_history:
                json_history['log_history'].append(
                    {
                        "event_timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        "event": log_event,
                        "event_type": event_type
                    }
                )
            else:
                json_history = {
                    "nom_user": user.upper(),
                    "log_history": [
                        {
                            "event_timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                            "event": log_event,
                            "event_type": event_type
                        }
                    ]
                }
            print("     " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " - Criando novo registro de log")
            post_conn.insert_into(
                table='staging.stg_log_user',
                data=[[user.upper(), str(json_history).replace("'", '"'), date.today().strftime('%Y-%m-%d')]],
                flg_trunc_before=True
            )

            post_conn.call_proc('proc_merge_tb_log_user')

    @staticmethod
    def verifica_user_cadastrado(user):
        if post_conn.return_query_list(f"""
                                    select 1 from cadastro_pessoa.tb_cadastro
                                    where nom_user = '{user.upper()}' """):
            return True
        else:
            return False

    @staticmethod
    def return_history_json(user, dat_event):
        query_result = post_conn.return_query_list(f"""select des_history from staging.stg_log_user
        where nom_user = '{user.upper()}' and to_char(dat_event, 'yyyy-mm-dd') = '{dat_event}'""")
        if query_result:
            json_history = json.loads(query_result[0][0])
        else:
            json_history = None
        return json_history


if __name__ == '__main__':
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " - Iniciando script")
    tela = CadApp()
    tela.run_screen()
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " - Finalizando script")
