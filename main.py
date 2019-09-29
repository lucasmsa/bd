# -*- Coding: UTF-8 -*-
#coding: utf-8

import  mysql.connector
import datetime
import base64
import string
from datetime import date
today = date.today()

#----------------------------------------------------------------------------      
    
#----------------------------------------------------------------------------  

def NotificarSeguir(usuario, user):
    quer = ("INSERT INTO NotificarSeguir (data_ns, usernamenotfollow, usernamenotfollowed) VALUES (%s, %s, %s)")
    argose = (today, usuario, user)
    cursor = db.cursor()
    cursor.execute(quer, argose)
    db.commit()


#----------------------------------------------------------------------------      
    
#----------------------------------------------------------------------------    
# Solicitar_Seguir(usuario, user):
#     print('Solici')
    
    
    
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------  

def Ver_Comentarios(idpub):
    plo = "SELECT conteudo, usernamecom FROM Comentario WHERE idpublicacaocom = %s"
    argii = (idpub,)
    cursor = db.cursor()
    cursor.execute(plo, argii)
    test2 = cursor.fetchall()
    if test2:
        for coms in test2:
            print("\tUser: {0} - {1}".format(coms[1], coms[0]))
            
#----------------------------------------------------------------------------      
    
#----------------------------------------------------------------------------  

def existencia(usuario, user):
    B = "SELECT Username FROM Usuario WHERE Username = %s"
    adr = (user,)
    cursor = db.cursor()
    cursor.execute(B, adr)
    test2 = cursor.fetchall()
    if (not test2):
        return 0
    else:
        return 1
    
#----------------------------------------------------------------------------    

def Ver_Posts_Perfil(user):
    B = "SELECT texto, IDPublicacao FROM Publicacao WHERE usernamepub = %s"
    adr = (user,)
    cursor = db.cursor()
    cursor.execute(B, adr)
    test = cursor.fetchall()
    if (not test):
        print('\nUsuario inexiste :v')
        print('-'*30)
        return 0
    else:
        #print(test2)
        for uf in test:
            if uf != None:
                # blabo = "SELECT Descricao, Nome, Username FROM Usuario WHERE Username = %s"
                # plapco = (user,)
                # cursor = db.cursor()
                # cursor.execute(blabo, plapco)
                # testipa = cursor.fetchall()
                # print('\nNome: {0}, \nDescricao: {2}'.format(test[0][1], test[0][0]))             
                print('o'*30)
                print('\n')
                qe = "SELECT texto, IDPublicacao, usernamepub FROM Publicacao WHERE usernamepub = %s"
                argh = (user,)
                curso = db.cursor()
                cursor.execute(qe, argh)
                test2 = cursor.fetchall()
                print("Username: {0} --- ID: {1}\nPost: {2}\nComentarios:  ".format(test2[0][2], test2[0][1], test2[0][0]))
                Ver_Comentarios(test2[0][1])

#----------------------------------------------------------------------------      
    
    
#----------------------------------------------------------------------------  
    
def Visita_perfil(usuario):
    
    user = input("Digite o username do usuario que desejas visitar: ")
    papot = "SELECT usernameblocked, usernameblock FROM Bloquear WHERE usernameblocked = %s AND usernameblock = %s"
    papito = (user, usuario)
    cursor = db.cursor()
    cursor.execute(papot, papito)
    Block_test = cursor.fetchall()
    
    if not Block_test:
    
        pap = "SELECT Username, Privacidade FROM Usuario WHERE Username = %s"
        pop = (user,)
        cursor = db.cursor()
        cursor.execute(pap, pop)
        test = cursor.fetchall()

        if existencia(usuario, user) == 1:
            if (test[0][1] == 0):
                Ver_Posts_Perfil(user)
                print('-'*30)
                Menu_Rede(usuario)

            else:
                d = "SELECT usernamefollowed, usernamefollow FROM Seguir WHERE usernamefollowed = %s AND usernamefollow = %s"
                adr = (user, usuario)
                cursor = db.cursor()
                cursor.execute(d, adr)
                test2 = cursor.fetchall()

                if not test2:
                    print('\nEste usuario eh privado e voce ainda nao o segue :( /n')
                    print('-'*30)
                    Menu_Rede(usuario)
                    
                else:
                    Ver_Posts_Perfil(user)
                    print('-'*30)
                    Menu_Rede(usuario)
        else:
            print('\nUsuario inexiste :o')
            print('-'*30)
            Menu_Rede(usuario)

    else:
        print('Usuario bloqueado :o')
        print('-'*30)
        Menu_Rede(usuario)
        
#----------------------------------------------------------------------------  
                            
                            
#----------------------------------------------------------------------------  
def Comentar(usuario):
    idpub = input('Digite o ID da publicacao na qual deseja comentar: ')
    plip = "SELECT usernamepub FROM Publicacao WHERE IDPublicacao = %s"
    plap = (idpub,)
    cursor =  db.cursor()
    cursor.execute(plip, plap)
    testaburger = cursor.fetchall()
    if not testaburger:
        print('Um post com esse ID nao existe :c')
        print('-'*30)
        Menu_Rede(usuario)
    else:  
        user_check = testaburger[0][0]
        papoto = "SELECT usernameblocked, usernameblock FROM Bloquear WHERE (usernameblocked = %s AND usernameblock = %s) OR (usernameblocked = %s AND usernameblock = %s)"
        papitoks = (user_check, usuario, usuario, user_check)
        cursor = db.cursor()
        cursor.execute(papoto, papitoks)
        Block_test = cursor.fetchall()
        
        if not Block_test:
            comment = input('Digite seu comentario\n\n')
            que = ("INSERT INTO Comentario (conteudo, data_c, usernamecom, idpublicacaocom) VALUES (%s, %s, %s, %s)")
            argos = (comment, today, usuario, idpub)
            cursor = db.cursor()
            cursor.execute(que, argos)
            db.commit()
            print('Comentario concluido :)')
            print('-'*30)
            Menu_Rede(usuario)
        else: 
            print('Usuario bloqueado :o')
            print('-'*30)
            Menu_Rede(usuario)
#----------------------------------------------------------------------------
                            
#----------------------------------------------------------------------------                            
def Bloquear(usuario):
    userblock = input("Digite o username do usuario que desejas bloquear: ")
    lap = "SELECT usernameblocked, usernameblock FROM Bloquear WHERE usernameblocked = %s AND usernameblock = %s"
    lop = (userblock, usuario)
    cursor = db.cursor()
    cursor.execute(lap, lop)
    test = cursor.fetchall()
    
    if (not test):
        B = "SELECT Username FROM Usuario WHERE Username = %s"
        adr = (userblock,)
        cursor = db.cursor()
        cursor.execute(B, adr)
        test2 = cursor.fetchall()
        if (not test2):
            print('Usuario nao existe :v')
            print('-'*30)
            Menu_Rede(usuario)
            
        else:
            d = ("INSERT INTO Bloquear (usernameblock, usernameblocked) VALUES (%s, %s)")
            args = (usuario, userblock)
            cursor = db.cursor()
            cursor.execute(d, args)
            db.commit()
            print('Voce bloqueou: {}'.format(userblock))
            Ver_Bloqueados(usuario)
            print('-'*30)
            Menu_Rede(usuario)
            
    else: 
        print('Voce ja bloqueou esse usuario :D')
        print('-'*30)
        Menu_Rede(usuario)
#----------------------------------------------------------------------------                            

#----------------------------------------------------------------------------                            
def Ver_Bloqueados(usuario):
    q = "SELECT usernameblocked FROM Bloquear WHERE usernameblock = %s"
    arg = (usuario,)
    cursor = db.cursor()
    cursor.execute(q, arg)
    test = cursor.fetchall()
    if not test:
        print('Voce nao tem usuarios bloqueados :(')
        print('-'*30)
        Menu_Rede(usuario)
    else:
        for row in test:
            print(row)
        print('-'*30)
        Menu_Rede(usuario)
#----------------------------------------------------------------------------
                            
#----------------------------------------------------------------------------                            
def Postar(usuario):
    conteudo = input('O que voce esta pensando?\n\n')
    tipo = input('Seu post se encaixa em que?\n\n')
    que = ("INSERT INTO Publicacao (usernamepub, texto, topico) VALUES (%s, %s, %s)")
    argos = (usuario, conteudo, tipo)
    cursor = db.cursor()
    cursor.execute(que, argos)
    db.commit()
    print('Post concluido :)')
    print('-'*30)
    Menu_Rede(usuario)
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
# Vou_Solicitar_Seguir(usuario, userseguir):
#     # B = "SELECT Username, Senha FROM Usuario WHERE Username = %s AND Senha = %s"
#     # adr = (username, senha)
#     # cursor.execute(B, adr)
#     # test = cursor.fetchall()
#     return 1
#----------------------------------------------------------------------------  



#----------------------------------------------------------------------------                            
def Seguir_Alguem(usuario):
    userseguir = input("Digite o username do usuario que desejas seguir: ")
    pap = "SELECT usernamefollowed FROM Seguir WHERE usernamefollowed = %s AND usernamefollow = %s"
    pop = (userseguir, usuario)
    cursor = db.cursor()
    cursor.execute(pap, pop)
    test = cursor.fetchall()
    
    if (not test):
        if existencia(usuario, userseguir) == 0:
            print('Usuario nao existe :v')
            print('-'*30)
            Menu_Rede(usuario)
            
        else:
            papi = "SELECT Privacidade FROM Usuario WHERE Username = %s"
            dadi = (userseguir,)
            cursor = db.cursor()
            cursor.execute(papi, dadi)
            checa_priv = cursor.fetchall()
            if(checa_priv[0][0] == 0):
                d = ("INSERT INTO Seguir (usernamefollow, usernamefollowed) VALUES (%s, %s)")
                args = (usuario, userseguir)
                cursor = db.cursor()
                cursor.execute(d, args)
                db.commit()
                #NotificarSeguir(usuario, userseguir)
                print('Voce agora esta seguindo: ')
                Ver_Seguindo(usuario)
                #Notificar_seguir()
                print('-'*30)
                Menu_Rede(usuario)
            else:
                print('Solicitacao de seguir enviada')
                d = ("INSERT INTO Seguir (usernamefollow, usernamefollowed) VALUES (%s, %s)")
                args = (usuario, userseguir)
                cursor = db.cursor()
                cursor.execute(d, args)
                db.commit()
                print('-'*30)
                Menu_Rede(usuario)
                #Vou_Solicitar_Seguir(usuario, userseguir)
                # Solicitar_Seguir(usuario, userseguir)

    else: 
        print('Voce ja segue esse usuario :D')
        print('-'*30)
        Menu_Rede(usuario)
#----------------------------------------------------------------------------
   
#----------------------------------------------------------------------------
def Ver_Seguidores(usuario):
    #C = "SELECT * FROM Seguir WHERE usernamefollowed = %s"
    q = "SELECT usernamefollow FROM Seguir WHERE usernamefollowed = %s"
    arg = (usuario,)
    cursor = db.cursor()
    cursor.execute(q, arg)
    test = cursor.fetchall()
    if not test:
        print('Voce nao tem seguidores :(')
        print('-'*30)
        Menu_Rede(usuario)
    else:
        for row in test:
            print(row)
        print('-'*30)
        Menu_Rede(usuario)
#----------------------------------------------------------------------------
  
#----------------------------------------------------------------------------                            
def Ver_Seguindo(usuario):
    
    q = "SELECT usernamefollowed FROM Seguir WHERE usernamefollow = %s"
    arg = (usuario,)
    cursor = db.cursor()
    cursor.execute(q, arg)
    test = cursor.fetchall()
    if not test:
        print('Voce nao segue ninguem :(')
        print('-'*30)
        Menu_Rede(usuario)
    else:
        for row in test:
            print(row)
            
        print('-'*30)
        Menu_Rede(usuario)
#----------------------------------------------------------------------------
    
def Ver_Posts(usuario):
    
    q = "SELECT usernamefollowed, usernamefollow, usernameblock, usernameblocked FROM Seguir LEFT JOIN Bloquear ON usernamefollow = usernameblock WHERE usernamefollow = %s"
    argu = (usuario,)
    cursor = db.cursor()
    cursor.execute(q, argu)
    test = cursor.fetchall()
    
    for uf in test:
        if uf != None:
            if (uf[0] != uf[3]):
                
                qe = "SELECT texto, IDPublicacao, usernamepub FROM Publicacao WHERE usernamepub = %s"
                argh = (uf[0],)
                cursor = db.cursor()
                cursor.execute(qe, argh)
                test2 = cursor.fetchall()
                print('='*30)
                print("\nUsername: {0} --- ID: {1}\nPost: {2}\nComentarios:  ".format(test2[0][2], test2[0][1], test2[0][0]))
                print('-'*30)
                Ver_Comentarios(test2[0][1])
            
    print('-'*30)
    Menu_Rede(usuario)
    
#-----------------------------------------------------------------------------------------
                            
#-----------------------------------------------------------------------------------------   


#-----------------------------------------------------------------------------------------

def VerNotificacoes(usuario):
    qi = "SELECT usernamefollow FROM Seguir WHERE usernamefollowed = %s"
    argen = (usuario,)
    cursor = db.cursor()
    cursor.execute(qi, argen)
    test = cursor.fetchall()
    print('-'*30)
    for usu in test:
        print('O usuario {} comecou a lhe seguir\n'.format(usu[0]))
    print('-'*30)
    
    qo = "SELECT usernamecom, idpublicacaocom FROM Comentario INNER JOIN Publicacao ON idpublicacaocom = IDPublicacao WHERE usernamepub = %s"
    cursor = db.cursor()
    cursor.execute(qo, argen)
    test2 = cursor.fetchall()
    for elements in test2:
        print('Usuario {0} comentou no seu post de ID: {1}\n'.format(elements[0], elements[1]))
    
    print('-'*30)
    Menu_Rede(usuario)
    

#-----------------------------------------------------------------------------------------  

def Unfollow(usuario):
    userseguir = input("Digite o username do usuario que desejas dar unfollow: ")
    papw = "SELECT usernamefollowed FROM Seguir WHERE usernamefollowed = %s AND usernamefollow = %s"
    popa = (userseguir, usuario)
    cursor = db.cursor()
    cursor.execute(papw, popa)
    test = cursor.fetchall()
    
    if (not test):
        print('Voce nao segue este usuario! :o')

    else: 
        d = ("DELETE FROM Seguir WHERE usernamefollow = %s AND usernamefollowed = %s")
        args = (usuario, userseguir)
        cursor = db.cursor()
        cursor.execute(d, args)
        db.commit()
        print('Apos o unfollow, seus seguidores agora sao: ')
        Ver_Seguindo(usuario)
        print('-'*30)
        Menu_Rede(usuario)


#-----------------------------------------------------------------------------------------
def Menu_Rede(usuario):
    print('Ver posts - 1')
    print('Seguir Alguem - 2')
    print('Ver Seguidores - 3')
    print('Ver Seguindo - 4')
    print('Bloquear Alguem - 5')
    print('Ver Bloqueados - 6')
    print('Postar - 7')
    print('Fazer comentario em post - 8')
    print('Ver notificacoes - 9')
    print('Buscar um perfil - 10')
    print('Dar unfollow alguem - 11')
    print('Desbloquear alguem - 12')
    print('Buscar posts - 13')
    print('Sair - 14')
    
    escolha = int(input('\n'))
    
    if escolha == 1:
        Ver_Posts(usuario)
        
    if escolha == 2:
        Seguir_Alguem(usuario)
        
    if escolha == 3:
        Ver_Seguidores(usuario)
        
    if escolha == 4:
        Ver_Seguindo(usuario)
        
    if escolha == 5:
        Bloquear(usuario)
        
    if escolha == 6:
        Ver_Bloqueados(usuario)
        
    if escolha == 7:
        Postar(usuario)
        
    if escolha == 8:
        Comentar(usuario)
        
    if escolha == 9:
        VerNotificacoes(usuario)
        
    if escolha == 10:
        Visita_perfil(usuario)
        
    if escolha == 11:
        Unfollow(usuario)
        
    if escolha == 12:
        Unblock(usuario)    
        
    if escolha == 13:
        Buscar(usuario)
        
    if escolha == 14:
        exit(2)
#-----------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------
def Buscar(usuario):
    tema = input('Digite o topico de posts que voce deseja pesquisar: ')
    osiu = "SELECT texto, IDPublicacao, usernamepub FROM Publicacao WHERE topico = %s"
    ihu = (tema,)
    cursor = db.cursor()
    cursor.execute(osiu, ihu)
    testipo = cursor.fetchall()
    if not testipo:
        print('Nao tem nenhum post com esse tema ;(')
    else:
        for items in testipo:
            print("Post: {0}, ID: {1}, User: {2}" .format(items[0], items[1], items[2]))
            id = items[1]
            oise = "SELECT conteudo FROM Comentario WHERE idpublicacaocom = %s"
            oiapa = (id,)
            cursor = db.cursor()
            cursor.execute(oise, oiapa)
            testapo = cursor.fetchall()
            for itams in testapo:
                print("\tComent: {0} ".format(itams[0]))
            
    print('-'*30)
    Menu_Rede(usuario)
    

#-----------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------                            
def Unblock(usuario):
    userblock = input("Digite o username do usuario que desejas dar unblock: ")
    lap = "SELECT usernameblocked FROM Bloquear WHERE usernameblocked = %s"
    lop = (userblock,)
    cursor = db.cursor()
    cursor.execute(lap, lop)
    test = cursor.fetchall()
    
    if (not test):
        print('Voce nao bloqueou esse usuario :3 ')
       
    else:
        d = ("DELETE FROM Bloquear WHERE usernameblock = %s AND usernameblocked = %s")
        args = (usuario, userblock)
        cursor = db.cursor()
        cursor.execute(d, args)
        db.commit()
        print('Voce desbloqueou: {}\nOs usuarios que permanecem bloqueados sao:\n'.format(userblock))
        Ver_Bloqueados(usuario)
        print('-'*30)
        Menu_Rede(usuario)

#-----------------------------------------------------------------------------------------                            
                            
#-----------------------------------------------------------------------------------------
def Login():
    username = input('Username: ')
    senha = input('Password: ')
    print(username)
    B = "SELECT Username, Senha FROM Usuario WHERE Username = %s AND Senha = %s"
    adr = (username, senha)
    cursor.execute(B, adr)
    test = cursor.fetchall()
    print(test)
    if (not test):
        print('Username/senha incorreto(s)')  
    
    else:
        print('Welcome')
        Menu_Rede(username)
#-----------------------------------------------------------------------------------------                            
 
#-----------------------------------------------------------------------------------------                            
def Cadastro():
    nome = input('Digite seu nome: ')
    username_cadastro = input('Digite o seu username: ')
    senha_cadastro = input('Digite sua senha: ')
    privacidade_cadastro = input('Privacidade do perfil (0 - Publico, 1 - Privado):  ')
    descricao_cadastro = input('Descricao pessoal: ')
    q = ("INSERT INTO Usuario (Nome, Senha, Username, Descricao, Privacidade) VALUES (%s, %s, %s, %s, %s)")
    arguments = (nome, senha_cadastro, username_cadastro, descricao_cadastro, privacidade_cadastro)
    cursor = db.cursor()
    cursor.execute(q, arguments)
    db.commit()
    print('-'*20)
    print("Criacao feita com sucesso")
    print('-'*20)
    Menu_Rede(username_cadastro)
#-----------------------------------------------------------------------------------------    
    

db = mysql.connector.connect(
	host ='localhost',
	user ='root',
	password='',
	database ='Instagram2')

cursor = db.cursor()
cursor.execute("SELECT Username, Senha FROM Usuario")
for Username, Senha in cursor:
    print(Username, Senha)

print('\n')

First_Question = int(input('Voce deseja criar um novo usuario ou fazer login? (0 - criar, 1 - login, Outro numero - Sair): '))

print('-'*50)

if(First_Question != 0 and First_Question != 1):
    exit(1)

if(First_Question == 1):
    Login()
        
    
if(First_Question == 0):
    Cadastro()
    
    
    
print('-'*50)

db.close()