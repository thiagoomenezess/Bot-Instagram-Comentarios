import time

def extrair_links_totais(pagina, index):
    links_sem_tratamento = []
    for i in range(index.count()):
        hrefs = pagina.locator('a').nth(i)
        # print(hrefs)
        links_sem_tratamento.append(hrefs.get_attribute('href'))
    return links_sem_tratamento

def extrair_link_tratado(link_sem_tratamento):
    link_com_tratamento = []
    for links in link_sem_tratamento:
        if "/p/" in links and "/liked_by/" in links:
            link_com_tratamento.append(links)
    return link_com_tratamento

def rolar_pagina_para_baixo(pagina, quantidade_vezes_rolar_para_baixo):
    for i in range(quantidade_vezes_rolar_para_baixo):
        pagina.keyboard.down('PageDown')

def pagina_pessoas_curtiram (pagina, quantidade_vezes_rolar_para_baixo, link_com_tratamento):
    pagina.goto("https://www.instagram.com{}".format(link_com_tratamento[0]))
    time.sleep(2)
    pagina.wait_for_selector("text=Seguir")
    rolar_pagina_para_baixo(pagina, quantidade_vezes_rolar_para_baixo)
    time.sleep(1)
    rolar_pagina_para_baixo(pagina, quantidade_vezes_rolar_para_baixo)
    time.sleep(1)
    rolar_pagina_para_baixo(pagina, quantidade_vezes_rolar_para_baixo)
    time.sleep(4)

def extrair_lista_quem_curtiu(pagina, index):
    lista_sem_tratamento = []
    for i in range(index.count()):
        hrefs = pagina.locator('//a[contains(@class, "oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl _a6hd")]').nth(i)
        # print(hrefs)
        lista_sem_tratamento.append(hrefs.get_attribute('href'))
    return lista_sem_tratamento

def extrair_lista_quem_curtiu_com_tratamento(lista_sem_tratamento, conta_pessoal_para_evitar_erro):
    lista_com_tratamento = []
    for links in lista_sem_tratamento:
        if len(links) > 3 and "explore" not in links and conta_pessoal_para_evitar_erro not in links:
            lista_com_tratamento.append(links)
    return lista_com_tratamento

def navegar_pagina_pessoa_comentar(pagina, lista_de_quem_curtiu_com_tratamento, comentario):
    for i, pessoa in enumerate(lista_de_quem_curtiu_com_tratamento):
        pagina.goto("https://www.instagram.com{}".format(pessoa))
        time.sleep(3)

        sem_tratamento = []
        com_tratamento = []

        index = pagina.locator('a')

        for i in range(index.count()):
            hrefs = pagina.locator('a').nth(i)
            sem_tratamento.append(hrefs.get_attribute("href"))

        for pic in (sem_tratamento):
            if "/p/" in pic:
                com_tratamento.append(pic)
        time.sleep(1)
        # print(com_tratamento)
        # pagina.locator('//*[@aria-label="Adicione um comentário..."]').click()

        pagina.goto('https://www.instagram.com{}'.format(com_tratamento[0]))
        time.sleep(1)
        comentar(pagina, comentario)

def comentar(pagina, comentario):
    try:
        pagina.fill('//*[@aria-label="Adicione um comentário..."]', comentario)
        pagina.keyboard.down("Enter")
        time.sleep(1)
    except:
        pass

def login_automatico(tempo):
    # Abrir navegador na página pretendida
    pagina.goto("https://www.instagram.com/")
    # Selecionar o campo de login e clicar
    pagina.locator('//*[@name="username"]').click()
    # Preencher o campo de login com o LOGIN
    pagina.fill('//*[@name="username"]', login)
    # Selecionar o campo de senha e clicar
    pagina.locator('//*[@name="password"]').click()
    # Preencher o campo de senha com o SENHA
    pagina.fill('//*[@name="password"]', senha)
    # clicar em Entrar
    pagina.locator('//*[@type="submit"]').click()
    # Tempo para colocar o login de segunda etapa
    time.sleep(tempo)

def isnumber(valor):
    try:
         int(valor)
    except ValueError:
         return False
    return True