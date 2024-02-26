#Use a imagem oficial do Nginx como a imagem base
FROM nginx:latest

#Copie o arquivo de config personalizado para dentro do conteiner
COPY  index.html /usr/share/nginx/html/

#Exponha a porta 80 para permitir o acesso ao servidor web
EXPOSE 80