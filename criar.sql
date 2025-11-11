
CREATE TABLE  PERSONAGEM  (
   ID_Personagem  int PRIMARY KEY,
   Nome  varchar(255),
   Data_Nascimento  date,
   Status  varchar(50),
   Alias  varchar(255)
);

CREATE TABLE  HEROI  (
   ID_Personagem  int PRIMARY KEY,
   Nome_Heroi  varchar(255),
   Ranking  int,
   Num_Casos_Resolvidos  int,
   ID_Agencia  int
);

CREATE TABLE  VILAO  (
   ID_Personagem  int PRIMARY KEY,
   Nome_Vilao  varchar(255),
   Num_Crimes  int
);

CREATE TABLE  ALUNO  (
   ID_Personagem  int PRIMARY KEY,
   Ano_Letivo  int,
   Turma  varchar(10)
);

CREATE TABLE  AGENCIA  (
   ID_Agencia  int PRIMARY KEY,
   Nome  varchar(255),
   Num_Membros  int,
   Localizacao  varchar(255),
   ID_Lider  int
);

CREATE TABLE  ORGANIZACAO_VILOES  (
   ID_Organizacao  int PRIMARY KEY,
   Nome  varchar(255),
   Num_Membros  int,
   Localizacao  varchar(255),
   ID_Lider  int
);

CREATE TABLE  INDIVIDUALIDADE  (
   ID_Individualidade  int PRIMARY KEY,
   Nome  varchar(255),
   Tipo  varchar(50),
   Descricao  text
);

CREATE TABLE  HABILIDADE  (
   ID_Habilidade  int PRIMARY KEY,
   Nome  varchar(255),
   Tipo  varchar(100),
   Vantagem  text,
   Desvantagem  text,
   ID_Individualidade  int
);

CREATE TABLE  BATALHA  (
   ID_Batalha  int PRIMARY KEY,
   Nome  varchar(255),
   Data  date,
   Duracao  varchar(100),
   ID_Lugar  int
);

CREATE TABLE  LUGAR  (
   ID_Lugar  int PRIMARY KEY,
   Nome  varchar(255),
   Cidade  varchar(255),
   Pais  varchar(255),
   Arco_Associado  varchar(255)
);

CREATE TABLE  PERSONAGEM_POSSUI_INDIVIDUALIDADE  (
   ID_Personagem  int,
   ID_Individualidade  int,
  PRIMARY KEY ( ID_Personagem ,  ID_Individualidade )
);

CREATE TABLE  ALUNO_ESTAGIA_AGENCIA  (
   ID_Aluno  int,
   ID_Agencia  int,
   Data_Inicio_Estagio  date,
   Status_Estagio  varchar(100),
  PRIMARY KEY ( ID_Aluno ,  ID_Agencia )
);

CREATE TABLE  VILAO_PERTENCE_ORGANIZACAO  (
   ID_Vilao  int,
   ID_Organizacao  int,
  PRIMARY KEY ( ID_Vilao ,  ID_Organizacao )
);

CREATE TABLE  PARTICIPANTES_BATALHA  (
   ID_Personagem  int,
   ID_Batalha  int,
  PRIMARY KEY ( ID_Personagem ,  ID_Batalha )
);

ALTER TABLE  HEROI  ADD FOREIGN KEY ( ID_Personagem ) REFERENCES  PERSONAGEM  ( ID_Personagem );
ALTER TABLE  HEROI  ADD FOREIGN KEY ( ID_Agencia ) REFERENCES  AGENCIA  ( ID_Agencia );
ALTER TABLE  VILAO  ADD FOREIGN KEY ( ID_Personagem ) REFERENCES  PERSONAGEM  ( ID_Personagem );
ALTER TABLE  ALUNO  ADD FOREIGN KEY ( ID_Personagem ) REFERENCES  PERSONAGEM  ( ID_Personagem );
ALTER TABLE  AGENCIA  ADD FOREIGN KEY ( ID_Lider ) REFERENCES  HEROI  ( ID_Personagem );
ALTER TABLE  ORGANIZACAO_VILOES  ADD FOREIGN KEY ( ID_Lider ) REFERENCES  VILAO  ( ID_Personagem );
ALTER TABLE  HABILIDADE  ADD FOREIGN KEY ( ID_Individualidade ) REFERENCES  INDIVIDUALIDADE  ( ID_Individualidade );
ALTER TABLE  BATALHA  ADD FOREIGN KEY ( ID_Lugar ) REFERENCES  LUGAR  ( ID_Lugar );
ALTER TABLE  PERSONAGEM_POSSUI_INDIVIDUALIDADE  ADD FOREIGN KEY ( ID_Personagem ) REFERENCES  PERSONAGEM  ( ID_Personagem );
ALTER TABLE  PERSONAGEM_POSSUI_INDIVIDUALIDADE  ADD FOREIGN KEY ( ID_Individualidade ) REFERENCES  INDIVIDUALIDADE  ( ID_Individualidade );
ALTER TABLE  ALUNO_ESTAGIA_AGENCIA  ADD FOREIGN KEY ( ID_Aluno ) REFERENCES  ALUNO  ( ID_Personagem );
ALTER TABLE  ALUNO_ESTAGIA_AGENCIA  ADD FOREIGN KEY ( ID_Agencia ) REFERENCES  AGENCIA  ( ID_Agencia );
ALTER TABLE  VILAO_PERTENCE_ORGANIZACAO  ADD FOREIGN KEY ( ID_Vilao ) REFERENCES  VILAO  ( ID_Personagem );
ALTER TABLE  VILAO_PERTENCE_ORGANIZACAO  ADD FOREIGN KEY ( ID_Organizacao ) REFERENCES  ORGANIZACAO_VILOES  ( ID_Organizacao );
ALTER TABLE  PARTICIPANTES_BATALHA  ADD FOREIGN KEY ( ID_Personagem ) REFERENCES  PERSONAGEM  ( ID_Personagem );
ALTER TABLE  PARTICIPANTES_BATALHA  ADD FOREIGN KEY ( ID_Batalha ) REFERENCES  BATALHA  ( ID_Batalha );


ALTER TABLE LUGAR
ADD COLUMN Latitude DECIMAL(9, 6),
ADD COLUMN Longitude DECIMAL(9, 6);