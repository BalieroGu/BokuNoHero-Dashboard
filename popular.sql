-- 1. LIMPA TODAS AS TABELAS EM ORDEM
-- A sintaxe TRUNCATE...CASCADE do PostgreSQL substitui
-- o SET FOREIGN_KEY_CHECKS=0 do MySQL.
TRUNCATE TABLE 
  PARTICIPANTES_BATALHA,
  VILAO_PERTENCE_ORGANIZACAO,
  ALUNO_ESTAGIA_AGENCIA,
  PERSONAGEM_POSSUI_INDIVIDUALIDADE,
  HABILIDADE,
  HEROI,
  ALUNO,
  VILAO,
  PERSONAGEM,
  AGENCIA,
  ORGANIZACAO_VILOES,
  INDIVIDUALIDADE,
  BATALHA,
  LUGAR
RESTART IDENTITY CASCADE;

-- 2. INSERE OS DADOS

-- AGENCIAS
INSERT INTO AGENCIA (ID_Agencia, Nome, Num_Membros, Localizacao, ID_Lider) VALUES
(1, 'Agência de Heróis Endeavor', 50, 'Tóquio, Japão', NULL),
(2, 'Agência Ryukyu', 15, 'Hosu, Japão', NULL),
(3, 'Nighteye Agency', 10, 'Tóquio, Japão', NULL),
(4, 'Agência da Mt. Lady', 5, 'Kyoto, Japão', NULL),
(5, 'Agência da Uwabami', 5, 'Osaka, Japão', NULL),
(6, 'Agência de Best Jeanist', 20, 'Tóquio, Japão', NULL),
(7, 'Agência Native', 8, 'Nagoya, Japão', NULL);

-- ORGANIZAÇÕES VILÃS
INSERT INTO ORGANIZACAO_VILOES (ID_Organizacao, Nome, Num_Membros, Localizacao, ID_Lider) VALUES
(1, 'Liga dos Vilões', 10, 'Esconderijo nas montanhas', NULL),
(2, 'Frente de Liberação Paranormal', 100000, 'Deika City', NULL),
(3, 'Exército de Libertação Meta', 100000, 'Japão (em toda parte)', NULL),
(4, 'Shie Hassaikai (Overhaul)', 20, 'Yakuza HQ, Japão', NULL);

-- INDIVIDUALIDADES
INSERT INTO INDIVIDUALIDADE (ID_Individualidade, Nome, Tipo, Descricao) VALUES
(1, 'One For All', 'Emissor', 'Acumula e transmite poder de um usuário para outro.'),
(2, 'Explosion', 'Emissor', 'Detona suor explosivo das mãos.'),
(3, 'Half-Cold Half-Hot', 'Emissor', 'Gelo do lado direito, fogo do lado esquerdo.'),
(4, 'Zero Gravity', 'Emissor', 'Remove gravidade de objetos tocados.'),
(5, 'Engine', 'Mutante', 'Motores nas pernas, supervelocidade.'),
(6, 'Hardening', 'Transformação', 'Endurecimento corporal quase absoluto.'),
(7, 'Frog', 'Mutante', 'Habilidades anfíbias completas.'),
(8, 'Erasure', 'Emissor', 'Apaga individualidades ao manter contato visual.'),
(9, 'Hellflame', 'Emissor', 'Manipulação intensa de chamas.'),
(10, 'Decay', 'Emissor', 'Desintegra tudo que toca com os cinco dedos.'),
(11, 'Cremation', 'Emissor', 'Criação de chamas azuis letais.'),
(12, 'Transform', 'Transformação', 'Transformação física após ingerir sangue.'),
(13, 'All For One', 'Emissor', 'Rouba e acumula individualidades alheias.'),
(14, 'Fiber Master', 'Emissor', 'Controla fibras de tecidos à distância.'),
(15, 'Fierce Wings', 'Mutante', 'Manipula mentalmente cada pena de suas asas individualmente.'),
(16, 'Dragon', 'Transformation', 'Permite que o usuário se torne um dragão.'),
(17, 'Acid', 'Emissor', 'Secreta ácido de seu corpo.'),
(18, 'Navel Laser', 'Emissor', 'Dispara laser do umbigo.'),
(19, 'Electrification', 'Emissor', 'Gera e descarrega eletricidade.'),
(20, 'Creation', 'Emissor', 'Cria qualquer objeto inorgânico do corpo.'),
(21, 'Earphone Jack', 'Mutante', 'Cabelos em forma de plugues sonoros.'),
(22, 'Voice', 'Emissor', 'Amplifica voz com poder de som destrutivo.'),
(23, 'Somnambulist', 'Emissor', 'Coloca inimigos para dormir com aroma.'),
(24, 'Sharpshooter', 'Emissor', 'Mira sobrenatural com armas.'),
(25, 'Clone', 'Emissor', 'Cria múltiplos clones do próprio corpo.'),
(26, 'Cement', 'Emissor', 'Manipula cimento livremente.'),
(27, 'Double', 'Emissor', 'Cria cópias perfeitas de pessoas.'),
(28, 'Gecko', 'Mutante', 'Fisiologia e aderência de lagarto.'),
(29, 'Compress', 'Emissor', 'Comprime objetos em pequenas esferas.'),
(30, 'Warp Gate', 'Emissor', 'Cria portais de teletransporte.'),
(31, 'Muscle Augmentation', 'Emissor', 'Aumenta fibras musculares para força extrema.'),
(32, 'Overhaul', 'Emissor', 'Desmonta e reconstrói qualquer coisa que toca.'),
(33, 'Chronostasis', 'Emissor', 'Lentidão extrema ao perfurar com ponteiro de relógio.'),
(34, 'Strongarm', 'Mutante', 'Força física descomunal.'),
(35, 'Stress', 'Emissor', 'Mais estressado = mais forte.'),
(36, 'Ice Manipulation', 'Emissor', 'Controla gelo ao seu redor.'),
(37, 'Incite', 'Emissor', 'Motiva e fortalece aliados com discursos.'),
(38, 'Anthropomorph', 'Emissor', 'Controla objetos digitais como bonecos.'),
(39, 'Landmine', 'Emissor', 'Transforma objetos em explosivos.'),
(40, 'Anthropomorph (Clone)', 'Emissor', 'Controla objetos digitais como bonecos.'),
(41, 'Sloshed', 'Emissor', 'Desorienta inimigos com intoxicação.'),
(42, 'Unknown1', 'Emissor', 'Poder não revelado.'),
(43, 'Unknown2', 'Emissor', 'Poder não revelado.'),
(44, 'Mimicry', 'Emissor', 'Controla estruturas sólidas como extensão do corpo.'),
(45, 'Gecko Clone', 'Mutante', 'Fisiologia de réptil.');

-- LUGARES (COM LATITUDE E LONGITUDE ADICIONADAS)
INSERT INTO LUGAR (ID_Lugar, Nome, Cidade, Pais, Arco_Associado, Latitude, Longitude) VALUES
(1, 'U.A. High School', 'Musutafu', 'Japão', 'Introdução', 35.702300, 139.560000),
(2, 'USJ', 'Musutafu', 'Japão', 'Ataque da Liga dos Vilões', 35.703000, 139.561000),
(3, 'Kamino Ward', 'Yokohama', 'Japão', 'All Might vs All For One', 35.447700, 139.641800),
(4, 'Deika City', 'Kyushu', 'Japão', 'Guerra Paranormal', 32.803200, 130.707900);

-- BATALHAS
INSERT INTO BATALHA (ID_Batalha, Nome, Data, Duracao, ID_Lugar) VALUES
(1, 'Ataque à USJ', '2025-04-03', '30 minutos', 2),
(2, 'Resgate de Bakugo', '2025-06-01', '20 minutos', 3),
(3, 'Guerra Paranormal', '2025-11-20', '2 horas', 4),
(4, 'Incidente em Hosu', '2025-05-10', '45 minutos', 3),
(5, 'Ataque ao Campo de Treinamento Florestal', '2025-06-18', '1 hora', 4),
(6, 'Invasão ao QG da Shie Hassaikai', '2025-07-10', '40 minutos', 1),
(7, 'Confronto Exército Meta vs Liga', '2025-09-15', '50 minutos', 4);

-- PERSONAGENS
INSERT INTO PERSONAGEM (ID_Personagem, Nome, Data_Nascimento, Status, Alias) VALUES
-- Alunos
(1, 'Izuku Midoriya', '2009-07-15', 'Vivo', 'Deku'),
(2, 'Katsuki Bakugo', '2009-04-20', 'Vivo', 'Dynamight'),
(3, 'Shoto Todoroki', '2009-01-11', 'Vivo', 'Shoto'),
(4, 'Ochaco Uraraka', '2009-12-27', 'Viva', 'Uravity'),
(5, 'Tenya Iida', '2009-08-22', 'Vivo', 'Ingenium'),
(6, 'Eijiro Kirishima', '2009-10-16', 'Vivo', 'Red Riot'),
(7, 'Tsuyu Asui', '2009-02-12', 'Viva', 'Froppy'),
(18, 'Mina Ashido', '2009-07-30', 'Viva', 'Pinky'),
(19, 'Yuga Aoyama', '2009-05-30', 'Vivo', 'Can’t Stop Twinkling'),
(20, 'Denki Kaminari', '2009-06-29', 'Vivo', 'Chargebolt'),
(21, 'Momo Yaoyorozu', '2009-09-23', 'Viva', 'Creati'),
(22, 'Kyoka Jiro', '2009-08-01', 'Viva', 'Earphone Jack'),
-- Heróis
(8, 'Toshinori Yagi', '1980-06-10', 'Aposentado', 'All Might'),
(9, 'Shota Aizawa', '1994-11-08', 'Vivo', 'Eraser Head'),
(10, 'Enji Todoroki', '1979-08-08', 'Vivo', 'Endeavor'),
(11, 'Ryuko Tatsuma', '1985-01-17', 'Viva', 'Ryukyu'),
(12, 'Keigo Takami', '1997-12-28', 'Vivo', 'Hawks'),
(13, 'Tsunagu Hakamada', '1983-05-05', 'Vivo', 'Best Jeanist'),
(23, 'Hizashi Yamada', '1984-07-17', 'Vivo', 'Present Mic'),
(24, 'Nemuri Kayama', '1983-03-09', 'Viva', 'Midnight'),
(25, 'Snipe', '1975-12-01', 'Vivo', 'Snipe'),
(26, 'Ectoplasm', '1970-09-15', 'Vivo', 'Ectoplasm'),
(27, 'Cementoss', '1980-05-10', 'Vivo', 'Cementoss'),
-- Vilões
(14, 'Tenko Shimura', '2004-04-04', 'Vivo', 'Tomura Shigaraki'),
(15, 'Toya Todoroki', '1999-01-18', 'Vivo', 'Dabi'),
(16, 'Himiko Toga', '2008-08-07', 'Viva', 'Toga'),
(17, 'Shigaraki (Sensei)', '1940-01-01', 'Preso', 'All For One'),
(28, 'Jin Bubaigawara', '1984-05-10', 'Falecido', 'Twice'),
(29, 'Shuichi Iguchi', '1985-03-12', 'Vivo', 'Spinner'),
(30, 'Atsuhiro Sako', '1980-11-05', 'Vivo', 'Mr. Compress'),
(31, 'Kurogiri', '1972-08-29', 'Desconhecido', 'Kurogiri'),
(32, 'Goto Imasuji', '1975-02-21', 'Vivo', 'Muscular'),
(33, 'Kai Chisaki', '1991-03-29', 'Preso', 'Overhaul'),
(34, 'Hari Kurono', '1989-07-10', 'Vivo', 'Chronostasis'),
(35, 'Kendo Rappa', '1985-02-22', 'Vivo', 'Rappa'),
(36, 'Rikiya Yotsubashi', '1975-10-13', 'Vivo', 'Re-Destro'),
(37, 'Geten', '2000-01-01', 'Vivo', 'Geten'),
-- Frente de Liberação Paranormal
(38, 'Koku Hanabata', '1976-08-09', 'Vivo', 'Trumpet'),
(39, 'Tomoyasu Chikazoku', '1983-12-18', 'Vivo', 'Skeptic'),
-- Exército de Libertação Meta
(40, 'Chitose Kizuki', '1990-01-01', 'Falecida', 'Curious'),
(41, 'Tomoyasu Chikazoku', '1983-12-18', 'Vivo', 'Skeptic (Meta)'),
-- Shie Hassaikai – membros restantes
(42, 'Deidoro Sakaki', '1980-03-01', 'Preso', 'Sakaki'),
(43, 'Nemu Toya', '1988-10-25', 'Preso', 'Toya'),
(44, 'Tatsuyuki Tokuda', '1982-06-15', 'Preso', 'Tatsuyuki'),
(45, 'Joi Irinaka', '1992-09-01', 'Desaparecido', 'Mimic'),
(46, 'Shuichi Iguchi (Yakuza)', '1985-03-12', 'Vivo', 'Iguchi');

-- ALUNO
INSERT INTO ALUNO (ID_Personagem, Ano_Letivo, Turma) VALUES
(1, 1, '1-A'), (2, 1, '1-A'), (3, 1, '1-A'), (4, 1, '1-A'), (5, 1, '1-A'),
(6, 1, '1-A'), (7, 1, '1-A'), (18, 1, '1-A'), (19, 1, '1-A'), (20, 1, '1-A'),
(21, 1, '1-A'), (22, 1, '1-A');

-- HEROI
INSERT INTO HEROI (ID_Personagem, Nome_Heroi, Ranking, Num_Casos_Resolvidos, ID_Agencia) VALUES
(8, 'All Might', 1, 10000, NULL), (9, 'Eraser Head', NULL, 500, NULL), (10, 'Endeavor', 2, 5000, 1),
(11, 'Ryukyu', 10, 900, 2), (12, 'Hawks', 3, 3000, 1), (13, 'Best Jeanist', 4, 2500, 6),
(23, 'Present Mic', NULL, 200, NULL), (24, 'Midnight', NULL, 300, NULL), (25, 'Snipe', NULL, 150, NULL),
(26, 'Ectoplasm', NULL, 100, NULL), (27, 'Cementoss', NULL, 80, NULL);

-- VILAO
INSERT INTO VILAO (ID_Personagem, Nome_Vilao, Num_Crimes) VALUES
(14, 'Tomura Shigaraki', 150), (15, 'Dabi', 100), (16, 'Himiko Toga', 40), (17, 'All For One', 300),
(28, 'Twice', 40),
(29, 'Spinner', 10),
(30, 'Mr. Compress', 15),
(31, 'Kurogiri', 25),
(32, 'Muscular', 50),
(33, 'Overhaul', 70),
(34, 'Chronostasis', 25),
(35, 'Rappa', 15),
(36, 'Re-Destro', 80),
(37, 'Geten', 45),
(38, 'Trumpet', 30),
(39, 'Skeptic', 22),
(40, 'Curious', 18),
(41, 'Skeptic (Meta)', 22),
(42, 'Sakaki', 12),
(43, 'Toya', 10),
(44, 'Tatsuyuki', 11),
(45, 'Mimic', 20),
(46, 'Iguchi', 5);

-- INDIVIDUALIDADES DOS PERSONAGENS
INSERT INTO PERSONAGEM_POSSUI_INDIVIDUALIDADE (ID_Personagem, ID_Individualidade) VALUES
(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),
(8, 1), (9, 8), (10, 9), (11, 16), (12, 15), (13, 14),
(14, 10), (15, 11), (16, 12), (17, 13),
(18, 17), (19, 18), (20, 19), (21, 20), (22, 21),
(23, 22), (24, 23), (25, 24), (26, 25), (27, 26),
(28, 27), (29, 28), (30, 29), (31, 30), (32, 31),
(33, 32), (34, 33), (35, 34),
(36, 35), (37, 36), -- FLP
(38, 37), (39, 38),
-- Meta
(40, 39), (41, 40),
-- Hassaikai
(42, 41), (43, 42), (44, 43), (45, 44), (46, 45);

-- VILOES E ORGANIZAÇÕES
INSERT INTO VILAO_PERTENCE_ORGANIZACAO (ID_Vilao, ID_Organizacao) VALUES
(14, 1), (15, 1), (16, 1), (17, 1), (28, 1), (29, 1), (30, 1), (31, 1), (32, 1),
(33, 4), (34, 4), (35, 4),
(36, 3), (37, 3), (14, 2), (15, 2), (16, 2), (36, 2), (37, 2),
(38, 2), (39, 2), (40, 3), (41, 3),
(42, 4), (43, 4), (44, 4), (45, 4), (46, 4);

-- ESTÁGIOS
INSERT INTO ALUNO_ESTAGIA_AGENCIA (ID_Aluno, ID_Agencia, Data_Inicio_Estagio, Status_Estagio) VALUES
(1, 3, '2025-06-01', 'Concluído'),
(3, 1, '2025-06-08', 'Concluído'),
(4, 2, '2025-06-05', 'Concluído'),
(5, 7, '2025-06-10', 'Concluído'),
(6, 6, '2025-06-12', 'Concluído'),
(7, 2, '2025-06-15', 'Concluído'),
(18, 4, '2025-06-16', 'Concluído'),
(19, 7, '2025-06-17', 'Concluído'),
(20, 1, '2025-06-18', 'Concluído'),
(21, 5, '2025-06-19', 'Concluído'),
(22, 4, '2025-06-20', 'Concluído');

-- PARTICIPANTES DE BATALHA
INSERT INTO PARTICIPANTES_BATALHA (ID_Personagem, ID_Batalha) VALUES
(1, 1), (2, 1), (3, 1), (9, 1), (14, 1),
(1, 2), (2, 2), (3, 2), (8, 2), (15, 2),
(1, 3), (2, 3), (3, 3), (14, 3), (17, 3), (10, 3), (9, 3),
(14, 4), (15, 4), (28, 4), -- Hosu 
(14, 5), (16, 5), (30, 5), (31, 5), (32, 5), -- Floresta
(1, 6), (3, 6), (33, 6), (34, 6), (35, 6),
(36, 7), (37, 7), (14, 7), (15, 7),
(36, 3), (37, 3), (16, 3); 

-- LIDERANÇAS
UPDATE AGENCIA SET ID_Lider = 10 WHERE ID_Agencia = 1;
UPDATE AGENCIA SET ID_Lider = 11 WHERE ID_Agencia = 2;
UPDATE AGENCIA SET ID_Lider = 13 WHERE ID_Agencia = 6;
UPDATE ORGANIZACAO_VILOES SET ID_Lider = 17 WHERE ID_Organizacao = 1;