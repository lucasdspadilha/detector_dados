Comp. Curr.: Processamento Digital de Imagens
Prof.: Gustavo Atzingen

Alunos:
Julio Schendroski. 
Lucas Padilha.
Pedro Paulo.
Vitorio Bergamin.

Link de visualização do programa em funcionamento:
https://www.youtube.com/watch?v=BWKt_p6RAPc&ab_channel=JulioSchendroski

Instruções para Executar e Testar o Código

  Este documento fornece instruções detalhadas para configurar e executar um
  código que processa imagens de dados e identifica pontos de interesse, visando
  contar a quantidade de dados na imagem e somar os valores voltados para a
  câmera. O código detecta os contornos dos dados e os pontos nas faces visíveis,
  informando tanto o número total de dados quanto a soma dos pontos apresentados.
  Abaixo estão os requisitos de sistema, instruções para instalação de bibliotecas e
  orientações para execução do script.

Requisitos do Sistema

  ● Python: Verifique se Python 3.x está instalado em seu sistema.
  ● Bibliotecas Python:
    ○ numpy
    ○ opencv-python
    
Ambiente para Execução
  Para testar e executar o código, você pode usar um aplicativo como o IP Webcam
  (disponível na Google Play Store) ou uma webcam/câmera conectada ao
  computador.
  ● Usando o IP Webcam:
    a. Baixe o aplicativo IP Webcam e inicie-o no dispositivo.
    b. Configure-o para criar um host local, que gerará uma URL de acesso
    ao vídeo.
    c. No código, utilize o endereço gerado pelo aplicativo, seguindo o
    formato:
    cv.VideoCapture('https://xxx.xxx.x.xxx:xxxx/video')
  ● Usando uma Webcam:
    a. Se estiver utilizando uma webcam conectada diretamente ao
    computador, configure o código para capturar o vídeo a partir do
    dispositivo padrão. Para isso, altere a linha para:
    cv.VideoCapture(0)
    
Requisitos de Configuração do Ambiente de Teste
  O código foi projetado para processar imagens de dados convencionais em um
  fundo preto, utilizando dados brancos com pontos pretos, conforme ilustrado no
  vídeo de exemplo.
    ● Fundo do Vídeo: O fundo deve ser preto para oferecer um contraste nítido
    com os dados, facilitando a detecção dos contornos e pontos.
    ● Tipo de Dado: Utilize dados convencionais (brancos com pontos pretos),
    com faces numeradas de 1 a 6 pontos.
    
Passos para Instalação e Configuração
  1. Instalar as Bibliotecas Necessárias:
  ○ Execute o seguinte comando para instalar as bibliotecas numpy e
  opencv-python:
  pip install numpy opencv-python
  2. Verificar Conectividade da captura de vídeo que será utilizada:
  ○ Assegure-se de que o dispositivo com o stream de vídeo esteja
  conectado e transmitindo dados.

Executando o Código
  1. Executar o Script:
    ○ No terminal, execute o seguinte comando:
    python detector_dados.py
  2. Visualização e Interação:
    ○ Saída: O código exibirá duas janelas:
      ■ "Source": Exibe a imagem binarizada.
      ■ "Processed": Exibe a imagem com pontos de interesse e
      contornos destacados.
      ○ Interromper a Execução: Pressione a tecla e para encerrar o
      programa.
