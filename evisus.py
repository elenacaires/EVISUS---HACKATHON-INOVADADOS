from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.treeview import TreeView
from kivy.uix.treeview import TreeViewLabel
from kivy.uix.treeview import TreeViewNode
from kivy.uix.button import Button
from kivy.clock import Clock
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from fpdf import FPDF
from kivy.uix.popup import Popup
from kivy.config import Config
#CONTEUDOS ESTATICOS

modfom = 'A operacionalização do fomento das pesquisas em saúde pelo Decit/SCTIE/MS é categorizada em três modalidades: fomento nacional, contratação direta e fomento descentralizado (PPSUS).'
fomnac = 'Texto fomento nacional'
fomcont = 'Texto contratação direta'
fomppsus = 'Texto fomento PPSUS'
recpesq = 'Abaixo estão elencados alguns materiais chave de apoio à atuação do pesquisador:'
planpesq = 'O Departamento de Ciência e Tecnologia (Decit), da Secretaria de Ciência, Tecnologia, Inovação e Insumos Estratégicos em Saúde (SCTIE) do Ministério da Saúde (MS), em sua missão de coordenar ações de ciência e tecnologia em saúde para subsidiar políticas públicas, fomentar tecnologias que melhorem a saúde da população brasileira e articular a atuação de atores do Sistema de Ciência, Tecnologia e Inovação em Saúde para o desenvolvimento da pesquisa em consonância aos princípios e diretrizes do Sistema Único de Saúde (SUS), elaborou o Plano de Ação de Pesquisa Clínica no Brasil, instituído por meio da Portaria GM/MS Nº 559 de 09 de março de 2018.'
platpesq = 'A Plataforma Brasil é uma base nacional e unificada de registros de pesquisas envolvendo seres humanos para todo o Sistema CEP/Conep. Ela permite que as pesquisas sejam acompanhadas em seus diferentes estágios - desde sua submissão até a aprovação final pelo Comitê de Ética em Pesquisa (CEP) e/ou pela Conep, quando necessário – possibilitando, inclusive, o acompanhamento da fase de campo, o envio de relatórios parciais e dos relatórios finais das pesquisas (quando concluídas). A Plataforma Brasil permite, ainda, a apresentação de documentos também em meio digital, assegurando à sociedade o acesso aos dados públicos de todas as pesquisas aprovadas. '
manual = 'Clique para acessar o Manual do Pesquisador (Ética em Pesquisa)'
agenda = 'Clique para acessar a Agenda de Prioridades de Pesquisa do Ministério da Saúde'
#DADOS
bolanos = ['2022', '2021', '2020']
database = pd.read_csv('evisusdb.csv')
recomendcat = ['Alimentação e Nutrição', 'Ambiente, Trabalho e Saúde', 'Assistência Farmacêutica', 'Avaliação de Tecnologias e Economia da Saúde', 'Bioética e Ética na Pesquisa', 'Complexo Produtivo da Saúde', 'Comunicação e Informação em Saúde', 'Desenvolvimento de Tecnologias e Inovação em Saúde', 'Doenças Crônicas Não Transmissíveis', 'Doenças Transmissíveis', 'Economia e Gestão em Saúde', 'Epidemiologia', 'Gestão do Trabalho e Educação em Saúde', 'Pesquisa Clínica', 'Promoção da Saúde', 'Saúde Bucal', 'Saúde Materno Infantil', 'Saúde Mental', 'Saúde da Criança e do Adolescente', 'Saúde da Mulher', 'Saúde da Pessoa com Deficiência', 'Saúde da População Negra e das Comunidades Tradicionais', 'Saúde do Idoso', 'Saúde dos Povos Indígenas', 'Sistemas, Programas e Políticas em Saúde', 'Violência, Acidentes e Trauma']
rcat1 = database.loc[database['id']==recomendcat[0]].reset_index()
rcat2 = database.loc[database['id']==recomendcat[1]].reset_index()
rcat3 = database.loc[database['id']==recomendcat[2]].reset_index()
rcat4 = database.loc[database['id']==recomendcat[3]].reset_index()
rcat5 = database.loc[database['id']==recomendcat[4]].reset_index()
rcat6 = database.loc[database['id']==recomendcat[5]].reset_index()
rcat7 = database.loc[database['id']==recomendcat[6]].reset_index()
rcat8 = database.loc[database['id']==recomendcat[7]].reset_index()
rcat9 = database.loc[database['id']==recomendcat[8]].reset_index()
rcat10 = database.loc[database['id']==recomendcat[9]].reset_index()
rcat11 = database.loc[database['id']==recomendcat[10]].reset_index()
rcat12 = database.loc[database['id']==recomendcat[11]].reset_index()
rcat13 = database.loc[database['id']==recomendcat[12]].reset_index()
rcat14 = database.loc[database['id']==recomendcat[13]].reset_index()
rcat15 = database.loc[database['id']==recomendcat[14]].reset_index()
rcat16 = database.loc[database['id']==recomendcat[15]].reset_index()
rcat17 = database.loc[database['id']==recomendcat[16]].reset_index()
rcat18 = database.loc[database['id']==recomendcat[17]].reset_index()
rcat19 = database.loc[database['id']==recomendcat[18]].reset_index()
rcat20 = database.loc[database['id']==recomendcat[19]].reset_index()
rcat21 = database.loc[database['id']==recomendcat[20]].reset_index()
rcat22 = database.loc[database['id']==recomendcat[21]].reset_index()
rcat23 = database.loc[database['id']==recomendcat[22]].reset_index()
rcat24 = database.loc[database['id']==recomendcat[23]].reset_index()
rcat25 = database.loc[database['id']==recomendcat[24]].reset_index()
rcat26 = database.loc[database['id']==recomendcat[25]].reset_index()

#EXEMPLO DE FUNÇÃO AUXILIAR - GERAÇÃO DE RELATÓRIOS
def producao():
    N = 1
    apres = 10000
    aprov = 8000
    ind = np.arange(N)
    plt.figure(figsize=(5, 7))
    width = 0.3
    plt.bar(ind, apres, width, label='Apresentado(a)')
    plt.bar(ind + width, aprov, width, label='Aprovado(a)')
    plt.xlabel(' ')
    plt.ylabel('Quantidade (/1000)')
    plt.title('Quantidades de procedimentos ambulatoriais, Brasil 2022.\n')
    plt.xticks(ind + width / 2, (''))
    plt.legend(loc='best')
    plt.savefig('qtd.jpg')
    apres = int(dfex['output'].loc[dfex['id'] == 'valapres'].values[0]) / 1000
    aprov = int(dfex['output'].loc[dfex['id'] == 'valaprov'].values[0]) / 1000
    plt.figure(figsize=(5, 7))
    plt.bar(ind, apres, width, label='Apresentado(a)')
    plt.bar(ind + width, aprov, width, label='Aprovado(a)')
    plt.xlabel(' ')
    plt.ylabel('Quantidade (/1000)')
    plt.title('Valores dos procedimentos ambulatorials, Brasil 2022.\n')
    plt.xticks(ind + width / 2, (''))
    plt.legend(loc='best')
    pathimage = 'val.jpg'
    plt.savefig('val.jpg')
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="PROCEDIMENTOS AMBULATORIAIS, BRASIL 2022", ln=1, align='C')
    pdf.cell(200, 10,
             txt="Total de procedimentos apresentados: ",
             ln=3, align='L')
    pdf.cell(200, 10,
             txt="Total de procedimentos aprovados: " ,
             ln=4, align='L')
    pdf.cell(200, 10, txt="Valor total apresentado: " ,
             ln=5, align='L')
    pdf.cell(200, 10, txt="Valor total aprovado: " , ln=6,
             align='L')
    pdf.image('qtd.jpg', x=20, y=70, w=80, h=120)
    pdf.image('val.jpg', x=110, y=70, w=80, h=120)
    pdf.output("prodambnac.pdf")

class Gerenciador(ScreenManager):
    pass

class Menu(Screen):
    pass

class Gestor(Screen):
    pass

class Pesquisador(Screen):
    pass

class Profsaude(Screen):
    pass


#TELAS GESTOR

class Boletins(Screen):
    def __init__(self, *args, **kwargs):
        super(Boletins, self).__init__(*args, **kwargs)
        Clock.schedule_once(self.bols)
    def bols(self, dt):
        btv = TreeView(root_options=dict(text='Boletins Epidemiológicos',color=(21/255,54/255,89/255)))
        btvn1 = btv.add_node(TreeViewButton(text='Regulares',size =(36,36)))
        btvn2 = btv.add_node(TreeViewButton(text='Especiais',size =(36,36)))
        btvn3 = btv.add_node(TreeViewButton(text='COVID-19', size=(36,36)))
        for i in range(len(bolanos)):
            btv.add_node(TreeViewButton(text=bolanos[i], size =(32, 32)),btvn1)
            btv.add_node(TreeViewButton(text=bolanos[i], size=(32, 32)), btvn2)
            btv.add_node(TreeViewButton(text=bolanos[i], size =(32, 32)),btvn3)
        self.ids.boletinsbox.add_widget(btv)

class Prod(Screen):
    def __init__(self, *args, **kwargs):
        super(Prod, self).__init__(*args, **kwargs)
        Clock.schedule_once(self.prodrep)
    def prodrep(self, dt):
        def producao(self):
            indice = 0
            for i in range(database.shape[0]):
                if database['id'][i] == 'ph21_1_Distrito Federal':
                    indice = i
            dicio = eval(database['atributos'][indice])
            N = 1
            apres = int(dicio['aihel'])
            aprov = int(dicio['aihurg'])
            ind = np.arange(N)
            plt.figure(figsize=(5, 7))
            width = 0.3
            plt.bar(ind, apres, width, label='Eletivo')
            plt.bar(ind + width, aprov, width, label='Urgência')
            plt.xlabel(' ')
            plt.ylabel('Quantidade (/1000)')
            plt.title('Quantidades dos procedimentos, por modalidade.\n')
            plt.xticks(ind + width / 2, (''))
            plt.legend(loc='best')
            plt.savefig('qtd.jpg')
            apres = int(dicio['valorel'])
            aprov = int(dicio['valorcir'])
            plt.figure(figsize=(5, 7))
            plt.bar(ind, apres, width, label='Eletivo')
            plt.bar(ind + width, aprov, width, label='Urgência')
            plt.xlabel(' ')
            plt.ylabel('Quantidade (/1000)')
            plt.title('Valores dos procedimentos, por modalidade.\n')
            plt.xticks(ind + width / 2, (''))
            plt.legend(loc='best')
            pathimage = 'val.jpg'
            plt.savefig('val.jpg')
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt="PROCEDIMENTOS AMBULATORIAIS, DISTRITO FEDERAL, 2022, POR MODALIDADE", ln=1, align='C')
            pdf.cell(200, 10,
                     txt="Total de procedimentos eletivos: "+str(dicio['aihel']),
                     ln=3, align='L')
            pdf.cell(200, 10,
                     txt="Total de procedimentos de urgência: "+str(dicio['aihurg']),
                     ln=4, align='L')
            pdf.cell(200, 10, txt="Valor total em procedimentos eletivos: "+str(dicio['valorel']),
                     ln=5, align='L')
            pdf.cell(200, 10, txt="Valor total em procedimentos de urgência: "+str(dicio['valorcir']), ln=6,
                     align='L')
            pdf.image('qtd.jpg', x=20, y=70, w=80, h=120)
            pdf.image('val.jpg', x=110, y=70, w=80, h=120)
            pdf.output("prodambnac.pdf")
            popup = Popup(title='', content=Label(text='O PDF foi gerado e baixado.'), size_hint=(None, None), size=(400, 400),
                          auto_dismiss=True)
            popup.open()
        self.ids.prodamb.bind(on_release=producao)
class Indicadores(Screen):
    pass

class Recomend(Screen):
    pass

class Recomendcat(Screen):
    pass

class Recomendpc(Screen):
    pass

class Recomendcat1(Screen):
    def __init__(self, *args, **kwargs):
        super(Recomendcat1, self).__init__(*args, **kwargs)
        Clock.schedule_once(self.addrecomend)

    def addrecomend(self, dt):
        btrec = TreeView(root_options=dict(text='Foram encontradas '+str(rcat1.shape[0])+' pesquisas com recomendações para o SUS:', color=(21 / 255, 54 / 255, 89 / 255), markup=True))
        for i in range(rcat1.shape[0]):
            pesq = eval(rcat1['atributos'][i])
            tit = pesq['titulo']
            res = pesq['resultados']
            x = btrec.add_node(TreeViewLabel(text=tit, size =(32, 32), font_size=13, color=(21 / 255, 54 / 255, 89 / 255)))
            btrec.add_node(TreeViewLabel(text=res, size =(32, 32), font_size=12, color=(21 / 255, 54 / 255, 89 / 255)), x)
        self.ids.reccat1.add_widget(btrec)


class Recomendcat2(Screen):
    pass

class Recomendcat3(Screen):
    pass

class Recomendcat4(Screen):
    pass

class Recomendcat5(Screen):
    pass

class Recomendcat6(Screen):
    pass

class Recomendcat7(Screen):
    pass

class Recomendcat8(Screen):
    pass

class Recomendcat9(Screen):
    pass

class Recomendcat10(Screen):
    pass

class Recomendcat11(Screen):
    pass

class Recomendcat12(Screen):
    pass

class Recomendcat13(Screen):
    pass

class Recomendcat14(Screen):
    pass

class Recomendcat15(Screen):
    pass

class Recomendcat16(Screen):
    pass

class Recomendcat17(Screen):
    pass

class Recomendcat18(Screen):
    pass

class Recomendcat19(Screen):
    pass

class Recomendcat20(Screen):
    pass

class Recomendcat21(Screen):
    pass

class Recomendcat22(Screen):
    pass

class Recomendcat23(Screen):
    pass

class Recomendcat24(Screen):
    pass

class Recomendcat25(Screen):
    pass

class Recomendcat26(Screen):
    pass
#TELAS PESQUISADOR


class Orient(Screen):
    def __init__(self, *args, **kwargs):
        super(Orient, self).__init__(*args, **kwargs)
        Clock.schedule_once(self.topicosor)

    def topicosor(self, dt):
        bto1 = TreeView(root_options=dict(text='[b]Modalidades de fomento[/b]', color=(21/255, 54/255, 89/255), markup=True))
        bto1.add_node(TreeViewLabel(text=modfom,size =(32, 32),color=(21/255, 54/255, 89/255)))
        bto1_1 = bto1.add_node(TreeViewLabel(text='[b]Fomento nacional[/b]',size =(32, 32),color=(21/255, 54/255, 89/255), markup=True))
        bto1.add_node(TreeViewLabel(text=fomnac,size =(32, 32), color=(21/255, 54/255, 89/255)), bto1_1)
        bto1_2 = bto1.add_node(TreeViewLabel(text='[b]Contratação direta[/b]', size =(32, 32),color=(21 / 255, 54 / 255, 89 / 255), markup=True))
        bto1.add_node(TreeViewLabel(text=fomcont,size =(32, 32), color=(21 / 255, 54 / 255, 89 / 255)), bto1_2)
        bto1_3 = bto1.add_node(TreeViewLabel(text='[b]Fomento descentralizado (PPSUS)[/b]', size =(32, 32),color=(21 / 255, 54 / 255, 89 / 255), markup=True))
        bto1.add_node(TreeViewLabel(text=fomppsus, size =(32, 32), color=(21 / 255, 54 / 255, 89 / 255)), bto1_3)
        self.ids.orientbox.add_widget(bto1)

class Recursos(Screen):
    def __init__(self, *args, **kwargs):
        super(Recursos, self).__init__(*args, **kwargs)
        Clock.schedule_once(self.topicosor)

    def topicosor(self, dt):
        bto1 = TreeView(
            root_options=dict(text='[b]Materiais complementares para o pesquisador[/b]', color=(21 / 255, 54 / 255, 89 / 255),
                                  markup=True))
        bto1.add_node(TreeViewLabel(text=recpesq, color=(21 / 255, 54 / 255, 89 / 255)))
        bto1_1 = bto1.add_node(
                TreeViewLabel(text='[b]Plano Nacional de Pesquisa Clínica[/b]', color=(21 / 255, 54 / 255, 89 / 255), markup=True))
        bto1.add_node(TreeViewLabel(text=planpesq, color=(21 / 255, 54 / 255, 89 / 255)), bto1_1)
        bto1_2 = bto1.add_node(
                TreeViewLabel(text='[b]Plataforma Brasil[/b]', color=(21 / 255, 54 / 255, 89 / 255), markup=True))
        bto1.add_node(TreeViewLabel(text=platpesq, color=(21 / 255, 54 / 255, 89 / 255)), bto1_2)
        bto1_3 = bto1.add_node(
                TreeViewLabel(text='[b]Manual do pesquisador[/b]', color=(21 / 255, 54 / 255, 89 / 255),
                              markup=True))
        bto1.add_node(TreeViewLabel(text=manual, color=(21 / 255, 54 / 255, 89 / 255)), bto1_3)
        bto1_4 = bto1.add_node(
                TreeViewLabel(text='[b]Prioridades em pesquisa[/b]', color=(21 / 255, 54 / 255, 89 / 255),
                              markup=True))
        bto1.add_node(TreeViewLabel(text=agenda, color=(21 / 255, 54 / 255, 89 / 255)), bto1_4)
        self.ids.recursosbox.add_widget(bto1)

class Lacunas(Screen):
    pass

#TELAS PROFISSIONAL DE SAÚDE

class Protdir(Screen):
    pass

class Mapeamento(Screen):
    pass

class Atualiza(Screen):
    pass

#FUNCIONALIDADES

class TreeViewButton(Button, TreeViewNode):
    pass

#APLICATIVO

class evisus(App):
    Window.size = (1080/3,1920/3)
    def build(self):
        return Gerenciador()

evisus().run()

