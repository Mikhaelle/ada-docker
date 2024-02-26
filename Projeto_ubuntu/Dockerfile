#Use a imagem oficial do Ubuntu como a imagem base
FROM ubuntu:latest

#Atualiza os pacotes e instale o software desejado
RUN apt-get update && apt-get install -y && rm -rf /var/lib/apt/lists/*

#Defina um diretório de trablho padrão
WORKDIR /app

#Comando padrão a ser executado quando o conteiner for iniciado
ENTRYPOINT [ "bash" ]
