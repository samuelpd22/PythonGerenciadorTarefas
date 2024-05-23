import PySimpleGUI as sg

def criar_nova_tarefa():
    sg.theme('DarkBlue4')
    linha = [
        [sg.Checkbox(''),sg.Input('')],
        
    ],
    layout = [
        [sg.Frame('Tarefas',layout=linha, key='container')],
        [sg.Button('Nova Tarefa'),sg.Button('Resetar')]
    ]

    return sg.Window('Todo List',layout=layout, finalize=True)
#Criar janela
janela = criar_nova_tarefa()
#Criar regras da janela
while True :
    event,values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Nova Tarefa':
        janela.extend_layout(janela['container'],
       [[sg.Checkbox(''),
         sg.Input('')]])
    elif event == 'Resetar':
        janela.Close(),
        janela = criar_nova_tarefa()