from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton, MDRaisedButton
from kivymd.uix.card import MDCard
from kivymd.uix.fitimage import FitImage
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.screen import MDScreen
from kivy_deps import sdl2, glew
from kivy.lang import Builder
from kivy.properties import ObjectProperty,StringProperty
import matplotlib.pyplot as plt
import numpy as np
import sqlite3
import os, sys
from kivy.resources import resource_add_path, resource_find

conexao = sqlite3.connect('urna.db')
cursor = conexao.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS eleicao(idcandidato INTEGER PRIMARY KEY AUTOINCREMENT,nome TEXT,idade TEXT,descricao TEXT,votos INTEGER);")


class MD3Card(MDCard):
    pass
class Gereciadordetelas(ScreenManager):
    pass
class MenuScreen(MDScreen):
    pass
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
    def fetchall(self):
        conexao = sqlite3.connect('urna.db')
        c = conexao.cursor()
        c.execute("SELECT nome FROM eleicao")
        eleicao = c.fetchall()
        #self.ids.label.text = str(eleicao)
        self.candidatos = []
        self.i=0
        styles = {
            "elevated": "#000000"
        }

        for self.candidatos in eleicao:
            for style in styles.keys():
                self.ids.grid.add_widget(
                        MD3Card(
                            MDRelativeLayout(
                                FitImage(
                                    source="img/ícone-do-pic-perfil-isolado-no-fundo-branco-133862807.jpg",
                                    size_hint_y=0.35,
                                    pos_hint={"top": 1},
                                    radius=(36, 36, 0, 0),
                                ),
                                MDLabel(
                                    text=str(self.candidatos[self.i]),
                                    adaptive_size=True,
                                    color="black",
                                    pos=("12dp", "12dp"),
                                    ),

                                ),

                            line_color=(0.2, 0.2, 0.2, 0.8),
                            style=style,
                            padding="4dp",
                            size_hint=(None, None),
                            size=("200dp", "500dp"),
                            md_bg_color=styles[style],
                            shadow_softness=2 if style == "elevated" else 12,
                            shadow_offset=(0, 1) if style == "elevated" else (0, 2),
                            pos_hint={'center_x':.5+self.i,'center_y':.5},
                            spacing= 70,
                            ripple_behavior= True

                        )
                        )
        self.ids.grid.remove_widget(self.ids.btn)
        #self.ids.box.add_widget(MDBoxLayout(MDLabel(text=str(self.candidatos),pos_hint={"center_x": 0.5,"center_y": 0.5}),))


        conexao.commit()
    def eleicao(self):
        print('Votando')
        conexao = sqlite3.connect('urna.db')
        c = conexao.cursor()
        c.execute('update eleicao set votos=votos+1 where idcandidato=1')
        conexao.commit()
        conexao.close()
    def eleicao1(self):
        print('Votando')
        conexao = sqlite3.connect('urna.db')
        c = conexao.cursor()
        c.execute('update eleicao set votos=votos+1 where idcandidato=2')
        conexao.commit()
        conexao.close()
    def eleicao2(self):
        print('Votando')
        conexao = sqlite3.connect('urna.db')
        c = conexao.cursor()
        c.execute('update eleicao set votos=votos+1 where idcandidato=3')
        conexao.commit()
        conexao.close()
    def eleicao3(self):
        print('Votando')
        conexao = sqlite3.connect('urna.db')
        c = conexao.cursor()
        c.execute('update eleicao set votos=votos+1 where idcandidato=4')
        conexao.commit()
        conexao.close()
    def eleicao4(self):
        print('Votando')
        conexao = sqlite3.connect('urna.db')
        c = conexao.cursor()
        c.execute('update eleicao set votos=votos+1 where idcandidato=5')
        conexao.commit()
        conexao.close()
    def eleicao5(self):
        print('Votando')
        conexao = sqlite3.connect('urna.db')
        c = conexao.cursor()
        c.execute('update eleicao set votos=votos+1 where idcandidato=6')
        conexao.commit()
        conexao.close()

class Resultado(MDScreen):
    def resultados(self):
        conexao = sqlite3.connect('urna.db')
        c = conexao.cursor()
        c.execute("SELECT nome,votos FROM eleicao")
        candidatosresultados = c.fetchall()
        c.execute("SELECT nome FROM eleicao")
        nome = c.fetchall()
        c.execute("SELECT votos FROM eleicao")
        votos = c.fetchall()

        print(max(candidatosresultados))
        self.ids.resultado.add_widget(MD3Card(
                            MDRelativeLayout(
                                FitImage(
                                    source="img/ícone-do-pic-perfil-isolado-no-fundo-branco-133862807.jpg",
                                    size_hint_y=0.35,
                                    pos_hint={"top": 1},
                                    radius=(36, 36, 0, 0),
                                ),
                                MDLabel(
                                    text=f"{nome[0]}{str(max(votos))}votos",
                                    adaptive_size=True,
                                    color="black",
                                    pos=("20dp", "20dp"),
                                    ),

                                ),
                            pos_hint={"center_x":.5,"center_y":.5},
                            padding="4dp",
                            size_hint=(None, None),
                            size=("200dp", "400dp"),
                        ))
        #x = [votos[0],votos[1],votos[2],votos[3]]
        #colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(x)))
        # for candidatos in range(len(nome)):
        #     fig, ax = plt.subplots()
        #     ax.pie(x, colors=colors, radius=3, center=(4, 4),
        #           wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)

        #    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
        #          ylim=(0, 8), yticks=np.arange(1, 8))

        #    plt.show()
        #plt.pie(, labels=nome, autopct='%1.1f%%', shadow=True, startangle=140)
        #plt.axis('equal')
        #plt.show()
class MainApp(MDApp):

    def build(self):
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        self.title="Urna Eletronica"
        return Builder.load_file('main.kv')

    def switch_theme_style(self):
        self.theme_cls.primary_palette = (
            "Orange" if self.theme_cls.primary_palette == "Red" else "Red"
        )
        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )


if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    MainApp().run().run()


