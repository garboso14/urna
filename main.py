from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
import sqlite3

conexao = sqlite3.connect('urna.db')
cursor = conexao.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS eleicao(idcandidato INTEGER PRIMARY KEY AUTOINCREMENT,nome TEXT,idade INTEGER,descricao TEXT,votos INTEGER);")

class Gereciadordetelas(ScreenManager):
    def switch_theme_style(self):
        self.theme_cls.primary_palette = (
            "Orange" if self.theme_cls.primary_palette == "Red" else "Red"
        )
        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )
class MenuScreen(MDScreen):
    pass
class Votacao(MDScreen):
    pass
class Cadastro(MDScreen):
    def cadastro(self):
        nome = str(self.ids.nome.text)
        idade = int(self.ids.idade.text)
        descricao = str(self.ids.descricao.text)
        params = (nome,idade,descricao,0)
        self.ids.cadastrar.text = cursor.execute("INSERT INTO eleicao VALUES(NULL,?,?,?,?)",params)
class Resultado(MDScreen):
    pass
class MainApp(MDApp):

    def build(self):
        self.theme_cls.theme_style="Dark"
        self.title="Urna Eletronica"
        return Builder.load_file('main.kv')




MainApp().run()