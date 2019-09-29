/*USUARIO:*/

	INSERT INTO Usuario(Nome, Senha, Privacidade, Descricao, Username)
	VALUES ('Juca', 'cachorrossaofofos', 1, 'Um apreciador do futebol arte', 'jucaCorinthians');

	INSERT INTO Usuario(Nome, Senha, Privacidade, Descricao, Username)
	VALUES ('Enzo', 'brksmonark', 0, 'curto muito lolzinho e minecraf', 'Enzombie_Hunter');

	INSERT INTO Usuario(Nome, Senha, Privacidade, Descricao, Username)
	VALUES ('Richard', 'solemar', 0, 'save nature', 'richardVibzz');
	
	INSERT INTO Usuario(Nome, Senha, Privacidade, Descricao, Username)
	VALUES ('Geraldo Marques', 'familiaehtudo', 0, 'Saudacoes flamenguistas =)', 'rubro_negro_geraldo');
	
	INSERT INTO Usuario(Nome, Senha, Privacidade, Descricao, Username)
	VALUES ('Gabriel Barbosa', 'hojetemgol', 0, 'Blessed', 'Gabigol');
	
	INSERT INTO Usuario(Nome, Senha, Privacidade, Descricao, Username)
	VALUES ('Natasha Stanford', '101dalmatas', 1, 'Lifestyle | Travel | Gratitude', 'Nat_ford');
	
	INSERT INTO Usuario(Nome, Senha, Privacidade, Descricao, Username)
	VALUES ('Perry, o Ornitorrinco', 'Grrrhhhhh', 0, 'Detetive', '_Perry_');
	
	# INSERT INTO Usuario(Nome, Senha, Privacidade, Descricao, Username)
	# VALUES ('Perry,', 'Grrrhhhhh', 0, 'Detetive', '_Perry_');
	
	
/*---------------------------------------------------------------------------------------------------------
SEGUIR:*/
	
	INSERT INTO Seguir(usernamefollow, usernamefollowed)
	VALUES ('rubro_negro_geraldo', 'Gabigol');
	
	INSERT INTO Seguir(usernamefollow, usernamefollowed)
	VALUES ('jucaCorinthians', 'Gabigol');
	
	INSERT INTO Seguir(usernamefollow, usernamefollowed)
	VALUES ('_Perry_', 'Gabigol');
	
	INSERT INTO Seguir(usernamefollow, usernamefollowed)
	VALUES ('Gabigol', '_Perry_');
	
	INSERT INTO Seguir(usernamefollow, usernamefollowed)
	VALUES ('_Perry_', 'rubro_negro_geraldo');
	
	INSERT INTO Seguir(usernamefollow, usernamefollowed)
	VALUES ('Enzombie_Hunter', 'Gabigol');
	
	

/*---------------------------------------------------------------------------------------------------------

BLOQUEAR:*/

	INSERT INTO Bloquear(usernameblock, usernameblocked)
	VALUES ('richardVibzz', 'Nat_ford');

/*---------------------------------------------------------------------------------------------------------

PUBLICAÇÕES:*/

	INSERT INTO Publicacao(IDPublicacao, usernamepub, texto, topico)
	VALUES (1, 'Gabigol', 
	'Muito agradecido com todos que me desejaram bem nessa jornada no flamengo, e gracas a Deus esta dando tudo 	certo, que continuemos assim',
	'Flamengo');
	
	INSERT INTO Publicacao(IDPublicacao, usernamepub, texto, topico)
	VALUES (2, 'jucaCorinthians', 
	'Gabigol jogou muito bem no jogo de hoje e marcou dois gols na vitória do flamengo sobre o belo',
	'analise_esportiva');


/*---------------------------------------------------------------------------------------------------------


COMENTÁRIOS:*/

	INSERT INTO Comentario(IDComentario, conteudo, data_c, usernamecom, idpublicacaocom)
	VALUES (1, 'Te odeio mano', '2019-09-20', 'Enzombie_Hunter', 1);
	
	INSERT INTO Comentario(IDComentario, conteudo, data_c, usernamecom, idpublicacaocom)
	VALUES (2, 'vamos para cima deles mengão!!!', '2019-09-21', 'rubro_negro_geraldo', 1);
	
	