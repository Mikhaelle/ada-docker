# Comandos docker

## Ver versão do docker

```
docker -v
```

## Baleia 

### Com menssagem

```
docker run docker/whalesay cowsay Mikhaelle_Ada
```

### Chuva 
- i - interarivo
- t - terminal
- rm - remove o container
```
docker run -it --rm docker/surprise
```

## Executar um container
```
docker run <nome imagem>
``` 

## Ver container 
### Containers rodando
```
docker ps
docker container ls
``` 

### Já executados
```
docker ps -a
``` 

## Executar uma imagem linux
```
docker run -it ubuntu bash
``` 

## Executar uma imagem node
```
docker run -it node
``` 

## Executar em segundo plano 
- d - rodar segundo plano
- p - porta
- primeira porta acessa a aplicação (local) a segunda expõe a porta do container (serviço)
```
docker run -d -p 80:80 httpd
``` 

## Parando o container
```
docker stop <id>
docker stop <name>
``` 

## Reiniciando container 
```
docker start <id>
docker start <name>
``` 

## Removendo container 
```
docker rm <id>
docker rm <name>
``` 

## Nomeando container 
```
docker run -d -p 80:80 --name apache_ada httpd
``` 


## Logs do container 
- f continua rodando
```
docker logs apache_ada
docker logs -f apache_ada
``` 

## Ver imagens    
```
docker image ls
``` 

## baixa imagem 
```
docker pull <nome-da-imagem>
``` 

## Buildar dockerfile  
```
docker build <diretorio> ou .
``` 


## Nomeando imagem  
```
docker build -t nome:tag
``` 

## Removendo imagem  
```
docker rmi <imagem>
``` 

## Apaga tudo que não é utilizado   
```
docker system prune
``` 

## Entrar em um container
```
 docker exec -it <nome/id> bash
``` 

## Dados sobre o container
```
 docker inspect <id>
``` 

## Listando volumes
```
 docker volume ls
``` 

## Criando volumes
```
 docker volume create
``` 

## Remover volumes
```
 docker volume rm <name>
``` 

