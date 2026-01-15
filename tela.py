import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        [sg.change_look_and_feel('DarkBrown2')]
        # Layout
        layout = [
            [sg.Text('Nome', size=(5, 1)), sg.Input(size=(15, 1), key='nome')],
            [sg.Text('Idade', size=(5, 1)), sg.Input(size=(15, 1), key='idade')],
            [sg.Text('Quais provedores de e-mail são aceitos?')],
            [sg.Checkbox('Gmail', key='gmail'), sg.Checkbox('Outlook', key='outlook'),
             sg.Checkbox('Yahoo', key='yahoo')],
            [sg.Text('Aceita cartão')],
            [sg.Radio('Sim','cartoes', key='AceitaCartao'),
             sg.Radio('Não','cartoes', key='naoAceitaCartao')],
            [sg.Slider(range=(0, 225), default_value=0, orientation='h', size=(15, 20), key='sliderVelocidade')],
            [sg.Button('Enviar Dados')],
            [sg.Output(size=(20, 20))]

        ]
        # Janela
        self.janela = sg.Window("Dados do Usuário", layout)

    def Iniciar(self):
        while True:
            # Extrair Dados
            self.button, self.values = self.janela.read()
            nome = self.values['nome']
            idade = self.values['idade']
            aceita_gmail = self.values['gmail']
            aceita_outlook = self.values['outlook']
            aceita_yahoo = self.values['yahoo']
            aceita_cartao = self.values['AceitaCartao']
            nao_aceita_cartao = self.values['naoAceitaCartao']
            slider_script = self.values['sliderVelocidade']
            print(f'Nome: {nome}')
            print(f'Idade: {idade}')
            print(f'Aceita Gmail: {aceita_gmail}')
            print(f'Aceita Outlook: {aceita_outlook}')
            print(f'Aceita Yahoo: {aceita_yahoo}')
            print(f'Aceita Cartao: {aceita_cartao}')
            print(f'Não aceita cartao: {nao_aceita_cartao}')
            print(f'Slider script: {slider_script}')

tela = TelaPython()
tela.Iniciar()