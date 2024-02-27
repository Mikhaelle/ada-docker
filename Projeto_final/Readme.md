### Imagens no DockerHub

- Frontend: https://hub.docker.com/repository/docker/mikhabueno/my-frontend-app
- Backend: https://hub.docker.com/repository/docker/mikhabueno/backend_image
- Db: https://hub.docker.com/repository/docker/mikhabueno/mysql_image


### Startando aplicação

```
 docker-compose up --build
``` 

### Comportamento esperado

No http://localhost:8080/ uma tela com um campo irá aparecer, digite uma mensagem e clique no botão 'Submit'. É esperado que apareça uma mensagem do tipo : Mensagem {menssagem} guardada no banco com successo