# Tic-Tac-Toe

Tic-tac-toe é o nome em inglês para um jogo bastante popular, conhecido no Brasil como Jogo da Velha.

As regras são simples: temos dois jogadores, um com a marca "x" e outro com a marca "o", e um tabuleiro quadriculado com 9 casas, 3 fileiras e 3 colunas.

A cada turno, o jogador pode colocar sua marca numa das casas vazias do tabuleiro, e o objetivo é completar uma fileira, coluna ou diagonal inteira apenas com a sua marca.

O jogo se desenvolve num balanço estratégico em que ambos jogadores tentam completar uma linha ao mesmo tempo que impede as ameaças do oponente de completar uma dele. Se todas as casas forem preenchidas sem que um jogador complete uma linha, o jogo termina em empate.


## Requisitos

1) Ter o Python instalado: https://www.python.org/
2) Acessando via terminal:

```bash
# clone este repositório
$ git clone <https://github.com/aldeoliveira/tictactoe>

# acesse a pasta do projeto
$ cd tictactoe

# inicialize o projeto
$ python index.py
```


## Como jogar

Para jogar nessa versão em Python do tic-tac-toe, utilizam-se comandos do mouse e do teclado:

Comandos do mouse:

Botão esquerdo -> para colocar uma marca no tabuleiro, clique numa casa com o botão esquerdo do mouse. O primeiro clique marcará um "x", o segundo um "o", e assim alternadamente.

Comandos do teclado:

Z -> Desfaz a última marca. Pode-se desfazer até apagar todas as marcas.

R -> Reinicia a partida.

ESPAÇO -> Faz uma marca sugerida pelo computador, com base no algoritmo Newell & Simmon.



## Descrição do algoritmo Newell & Simmon:

Este tic-tac-toe para Python utiliza o algoritmo Newell & Simmon para decidir o melhor lance, com uma modificação no quarto passo. O algoritmo segue as seguintes etapas:

1. Vitória Imediata

	- Se houver uma fileira, coluna ou diagonal com duas marcas aliadas e um espaço em branco,
	
	    - Então jogar no espaço em branco.
 
2. Bloquear vitória

	- Se houver uma fileira, coluna ou diagonal com duas marcas inimigas e um espaço em branco, 
	
	    - Então jogar no espaço em branco.

3. Ataque duplo

	- Se houverem duas fileiras, colunas ou diagonais com uma marca aliada e duas casas vazias, e
	
	- Se a casa de interceptação estiver vazia,
	
	    - Então marcar a casa de interceptação.

4. Bloquear ataque duplo

    - Se houverem duas fileiras, colunas ou diagonais com uma marca inimiga e duas casas vazias, e
	
    - Se a casa de interceptação estiver vazia,
	
        - Então essa é uma casa de ataque duplo para o oponente.
	
	- Se houver apenas uma casa de ataque duplo para o oponente:
	
	    - Então marcar essa casa.
	
	- Se houver mais de uma casa:
	
	    - Então...
	
	    - Se houver uma casa que gere uma ameaça imediata e para bloquear essa ameaça o oponente precisar marcar uma casa que não seja de ataque duplo
	
	        - Então escolher essa casa.

5. Jogar no centro

	- Se a casa central estiver vazia,
	
	    - Marcar a casa central.

6. Jogar no canto oposto

	- Se há uma marca inimiga num canto, e
	
	- Se o canto oposto estiver vazio,
	
	    - Então marcar o canto oposto.

7. Canto vazio

	- Se houver um canto vazio,
	
	    - Então marcar o canto vazio.

8. Lado vazio

	- Se ouver um lado vazio,
	
	    - Então jogar no lado vazio.

## Technical Stack

Versão do Python: 3.7.3

Versão do Pygame: 1.9.6

## Sobre Mim

Olá, meu nome é André e sou formado em Engenharia Mecânica pela Universidade Federal de Viçosa.

Gosto muito de desenvolvimento de software e ciência de dados, e este repositório servirá para subir projetos que faço tanto como divertimento como para aprimorar minhas habilidades nessas disciplinas.

Espero desenvolver com o tempo aptidão para iniciar uma carreira nessas áreas, e que este projeto, como outros, sirvam como bons exemplos das técnicas que já domino.