#Criação das tabelas no mysql, na Database Instagram

        CREATE TABLE IF NOT EXISTS Usuario(
            Senha VARCHAR(100) NOT NULL,
            Nome VARCHAR(100) NOT NULL,
            Privacidade INT NOT NULL,
            Descricao VARCHAR(256),
            Username VARCHAR(50) NOT NULL PRIMARY KEY
        );

        CREATE TABLE IF NOT EXISTS Bloquear(
            usernameblock VARCHAR(50) NOT NULL,
            usernameblocked VARCHAR(50) NOT NULL,
            FOREIGN KEY(usernameblock) REFERENCES Usuario(Username),
            FOREIGN KEY(usernameblocked) REFERENCES Usuario(Username)
        );

        CREATE TABLE IF NOT EXISTS Seguir(
            usernamefollow VARCHAR(50),
            usernamefollowed VARCHAR(50),
            FOREIGN KEY(usernamefollow) REFERENCES Usuario(Username),
            FOREIGN KEY(usernamefollowed) REFERENCES Usuario(Username)
        );
        
        CREATE TABLE IF NOT EXISTS Publicacao (
            IDPublicacao INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
            usernamepub VARCHAR(50) NOT NULL,
            texto VARCHAR(2000) NOT NULL,
            topico VARCHAR(60),
            FOREIGN KEY(usernamepub) REFERENCES Usuario(Username)
        );


        CREATE TABLE IF NOT EXISTS Notificacao (
            IDNotificacao INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
            data_n Date NOT NULL,
            categoria VARCHAR(60) NOT NULL,
            usernamenot VARCHAR(50) NOT NULL,
            idpublicacaonot INT NOT NULL,
            idcometarionot INT NOT NULL,
            FOREIGN KEY(usernamenot) REFERENCES Usuario(Username),
            FOREIGN KEY(idpublicacaonot) REFERENCES Publicacao(IDPublicacao),
            FOREIGN KEY(idcometarionot) REFERENCES Comentario(IDComentario)
        );
        

        CREATE TABLE IF NOT EXISTS Comentario (
            IDComentario INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
            conteudo VARCHAR(1000) NOT NULL,
            data_c Date NOT NULL,
            usernamecom VARCHAR(50) NOT NULL,
            idpublicacaocom INTEGER NOT NULL,
            FOREIGN KEY(usernamecom) REFERENCES Usuario(Username),
            FOREIGN KEY(idpublicacaocom) REFERENCES Publicacao(IDPublicacao)
        );
