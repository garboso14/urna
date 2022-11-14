from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.properties import ObjectProperty,StringProperty
import sqlite3

conexao = sqlite3.connect('urna.db')
cursor = conexao.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS eleicao(idcandidato INTEGER PRIMARY KEY AUTOINCREMENT,nome TEXT,idade TEXT,descricao TEXT,votos INTEGER);")


class MD3Card(MDCard):
    pass
class Gereciadordetelas(ScreenManager):
    pass
class MenuScreen(MDScreen):
    def switch_theme_style(self):
        self.theme_cls.primary_palette = (
            "Orange" if self.theme_cls.primary_palette == "Red" else "Red"
        )
        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )
class Cadastro(MDScreen):
    def submit(self):
        conexao = sqlite3.connect('urna.db')
        c = conexao.cursor()
        c.execute("INSERT INTO eleicao VALUES (NULL,:nome,:idade,:descricao,:votos)",
                  {
                      'nome': self.ids.nome.text,
                      'idade': self.ids.idade.text,
                      'descricao': self.ids.descricao.text,
                      'votos': 0,
                  })
        #self.root.ids.word_label.text = f'{self.root.ids.word_input.text} Adicionado'
        self.ids.nome.text = ''
        self.ids.idade.text = ''
        self.ids.descricao.text = ''
        conexao.commit()
        conexao.close()
class Votacao(MDScreen):
    def __int__(self,candidatos,**kwargs):
        super().__init__(**kwargs)
    def fetchall(self):
        conexao = sqlite3.connect('urna.db')
        c = conexao.cursor()
        c.execute("SELECT nome FROM eleicao")
        eleicao = c.fetchall()
        box = MDBoxLayout()
        i = 0
        for self.canidatos in eleicao:
            self.ids.label.text = str(eleicao)

        conexao.commit()
    def eleicao(self):
        conexao = sqlite3.connect('urna.db')
        print(self.fetchall())
        self.ids.label.text = self.fetchall()
        conexao.commit()
        conexao.close()

class Resultado(MDScreen):
    pass
class MainApp(MDApp):

    def build(self):
        self.theme_cls.theme_style="Dark"
        self.title="Urna Eletronica"
        return Builder.load_file('main.kv')





MainApp().run()