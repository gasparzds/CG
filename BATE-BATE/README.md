DIAGRAMA DE UML:

![Mapa mental de metas moderno simples claro branco vermelho e preto](https://github.com/gasparzds/CG/assets/61299557/b2e8e556-cc85-4316-bf1f-39a374ca5a38)


CLASSE: MOVENDO_TEXTO -> 
  
  
  Atributos:

  
      FONT: É usada para definir o tipo e tamanho do texto que será mostrado na tela
      TEXT: É uma váriavel que armazena o textoque será exibido na tela
      LARGURA: Aqui armazena a largura total da tela
      ALTURA: Aqui armazena a altura total da tela
      TEXTO_SURF: O texto é criado nesta superfície para então ser aparecer na tela principal
      RECT: representa um retângulo em torno do texto, que é possivel manipular a posição do texto na tela
      VELOCIDADE_x: velocidade horizontal do texto no eixo x
      VELOCIDADE_y: velocidade vertical do texto no eixo y
  
  
  Metodos:

  
      GERAR_NUMERO_NAO_ZERO(SELF): tem a função de gerar um número aleatóriamente, menos o numero 0. 
      MOVE(SELF): Ajusta a posição do texto na tela, levando em consideração a velocidade X e Y
      CHANGE_COLOR(SELF): Essa função alterar a cor do texto

CLASSE: GAME -> 


  Atributos:

  
      LARGURA: Define a largura da janela do jogo em pixels
      ALTURA: Define a altura da janela do jogo em pixels
      TELA: Aqui está a janela principal do jogo onde tudo é apresentado
      CLOCK: controlar a taxa de atualização do jogo, é onde pode ser aumentado a velocidade do texto
      MOVENDOTEXTO: é onde está toda a regra do movimento do texto, o que vai acontecer quando ele bate
  Metodos: 

  
      RUN(SELF): chamado para iniciar o jogo



  CLASSE: GAME -> 
  
  Atributos:

  
      GAME: Esta variável é usada para poder acessar os métodos do jogo
  Metodos: 

  
      IF__NAME__ == __MAIN__


      


  
