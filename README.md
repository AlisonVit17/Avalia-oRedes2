<html>

  <head>
    <lang = pt-br>
  </head>

  <body>
    <h2> Execução do projeto:</h2> <br>
      Para executar o projeto, basta executar os clientes e os servidores em diferentes contêineres. <br>Vale ressaltar que o código cliente 1 e o código do cliente 2
      precisarão alterar o ip do servidor para o ip que o contêiner dos roteadores assumir. <br>
      Por exemplo:  
      <blockquote> clientegateway1 pode ser executado diversas vezes em contêineres distintos, só será necessário que o ip do servidor do clientegateway1 esteja de acordo
      com o contêiner que executar o gateway um.
      A mesma "ciência" vale para o cliente 2 e o gateway 2.</blockquote>
    <hr>
      Por fim, basta apenas que seja baixada as bibliotecas utilizadas.
    <br>
    <h2>
      Protocolo escolhida:
    </h2>
    O protocolo escolhido foi o protocolo UDP, tendo em vista que se trata de um protocolo não orientado a conexão, o mesmo é mais simples de ser executado.
    <hr>
    <h2>
      Topologia escolhida:
    </h2>
   Topologia bridge (criam uma rede virtual dentro do Docker host para que os contêineres se comuniquem entre si. São de mais fácil implementação).  
  </body>
</html>

