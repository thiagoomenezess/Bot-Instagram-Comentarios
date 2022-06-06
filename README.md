# Bot-Instagram-Comentarios / funciona com Chrome
 
 - Bot para comentários no instagram com interface gráfica
 - Colocar dados do usuário (login e senha) para login automático, onde foi adicionado 30 segundos após login, para os que possuem verificação em 2 etapas.
 - Colocar o link da foto do instagram para o BOT procurar as pessoas que curtiram e criar uma lista com esses nomes.
 - Escrever o comentário que gostaria de postar nas fotos.
 - Para evitar erros, foi adicionado um campo para digitar seu próprio nome de usuário, assim evitando o BOT de adicionar seu perfil a lista de curtidas e posteriormente publicar comentário.
 - Digitar um número para o BOT rolar a página para baixo, para carregar o máximo de pessoas possível.

## O BOT funciona da seguinte maneira:

 - Entra na foto do link digitado, clica no item "outras pessoas" e abre a página que contém as pessoas que curtiram a foto;
 - Cria uma lista com esses nomes - excluindo o perfil digitado no campo da UI -;
 - Através de um laço, entra no perfil de cada usuário da lista e realiza um comentário na primeira foto do perfil.