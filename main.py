from playwright.sync_api import sync_playwright
import funcoes as f
import time
import PySimpleGUI as sg

versao = 1.1

sg.theme("Reddit")
layout = [
    [sg.Text("Login do Instagram:  "), sg.InputText(key="login", size=(35, 1))],
    [sg.Text("Senha do Instagram: "), sg.InputText(key="senha", password_char="*", size=(35, 1))],
    [sg.Text("Link da página da foto que deseja buscar as curtidas: ")],
    [sg.InputText(key="link", size=(55, 1))],
    [sg.Text("Digite até 3 comentários diferentes que gostaria de fazer nas fotos: ")],
    [sg.Multiline("", key="comentario1", size=(40,3))],
    [sg.Multiline("", key="comentario2", size=(40,3))],
    [sg.Multiline("", key="comentario3", size=(40,3))],
    [sg.Text("Para evitar erros, digite abaixo seu nome de usuário no instagram, sem o @:")],
    [sg.InputText(key="conta_erro", size=(35, 1))],
    [sg.Text("Digite o número de páginas para buscar:")],
    [sg.InputText(key="paginas", size=(10, 1)), sg.Text("", key="alerta")],
    [sg.Text("")],
    [sg.Button("COMEÇAR"), sg.Button("SAIR")],
    [sg.Text("")],
    [sg.Text("Feito por Thiago", font=('Helvetica', 8, 'italic'))]
]

janela = sg.Window(f"Robô Instagram {versao} / Curtidas", layout)

while True:
    evento, valores = janela.read()

    if evento == sg.WIN_CLOSED or evento == "SAIR":
        break

    if evento == "COMEÇAR" and f.isnumber(valores["paginas"]) == True:
        login = valores["login"]
        senha = valores["senha"]
        link = valores["link"]
        conta_pessoal_para_evitar_erro = valores["conta_erro"]
        rolar_para_baixo = int(valores["paginas"])
        comentario1 = valores["comentario1"]
        comentarios = [comentario1]
        if valores["comentario2"] != "":
            comentario2 = valores["comentario2"]
            comentarios.append(comentario2)
        elif valores["comentario3"] != "":
            comentario3 = valores["comentario3"]
            comentarios.append(comentario3)


        tempo = 30
        with sync_playwright() as p:
            navegador = p.chromium.launch(channel="chrome", headless=False)

            pagina = navegador.new_page()

            f.login_automatico(tempo, pagina, login, senha)

            pagina.goto(link)

            pagina.wait_for_selector('a')

            #LOCALIZAR PESSOAS QUE CURTIRAM A FOTO A PARTIR DO LINK SUPRACITADO
            index = pagina.locator('a')

            link_sem_tratamento = f.extrair_links_totais(pagina, index)
            link_com_tratamento = f.extrair_link_tratado(link_sem_tratamento)

            #NAVEGAR ATÉ A PÁGINA DAS PESSOAS QUE CURTIRAM A FOTO:
            f.pagina_pessoas_curtiram(pagina, rolar_para_baixo, link_com_tratamento)

            #LOCALIZAR E CRIAR LISTA SEM E COM TRATAMENTO DAS PESSOAS QUE CURTIRAM A FOTO
            index = pagina.locator('//a[contains(@class, "oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl _a6hd")]')

            lista_de_quem_curtiu_sem_tratamento = f.extrair_lista_quem_curtiu(pagina, index)
            lista_de_quem_curtiu_com_tratamento = f.extrair_lista_quem_curtiu_com_tratamento(lista_de_quem_curtiu_sem_tratamento,
                                                                                             conta_pessoal_para_evitar_erro)


            f.navegar_pagina_pessoa_comentar(pagina, lista_de_quem_curtiu_com_tratamento, comentarios)

    else:
        janela["alerta"].update("Digite apenas números")