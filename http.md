# HTTP
HTTP (Hypertext Transfer Protocol) é a base da comunicação de dados da WWW (World Wide Web). É um protocolo de camada de aplicativo que define como as mensagens são formatadas e transferidas entre os clientes e os servidores.

## Solicitação
Mensagem enviada pelo cliente ao servidor

### Métodos
Ação que o cliente deseja executar
- Get: conseguir dados do servidor;
- Post: Envie dados para o servidor ;
- Put: Substituir um recurso existente pelosdados fornecidos;
- Delete: Excluir um recurso específico;
- Patch: Aplicar modificações a um recurso.

- URL: específica o local do recurso no servidor;
- Versão HTTP: a versão do protocolo HTTP que está sendo utilizada;
- Cabeçalhos: fornece informações adicionais sobre a solicitação, eles 
são pares de valores-chave;
- Corpo: contém dados que estão sendo enviados ao servidor.

## Hosting
É um serviço que permite que indivíduos e organizações tornem seus sites acessíveis na internet por meio de servidores  (armazenamento de arquivos de sites).
Há outros tipos de hospedagem como VPS (virtual private server), hospedagem em nuvem e hospedagem gerenciada do WordPress.

## Navegadores
É um software que permite ao usuário acessar e exibir páginas da web ou outro conteúdo online por meio de sua interface gráfica.

## Domain Name System
O Domain Name System (DNS) traduz os nomes de domínio em endereços IP. Este sistema utiliza uma estrutura semelhante a uma árvore com servidores raiz na parte superior, seguidos por servidores de domínio nível superior, servidores de nomes autoritativos para domínios e servidores DNS locais.

É um endereço legível usado para identificar e acessar sites.
O nome do domínio consiste em duas partes:
- Domínio de segundo nível: nome do site ou da organização;
- Domínio de nível superior: exemplo .com, .org ou .net.


## Conceitos
- Modelo Cliente-Servidor: o cliente envia uma solicitação ao servidor e o servidor processa essa solicitação e retorna uma resposta;
- Protocolo sem estado: 
    - Cada solicitação é tratada como uma transação independente;
    - Cada solicitação tem todos os dados necessários para que o servidor entenda e processe.

## HTTP Status Code
- 1xx - Informacional
- 2xx -  Sucesso
- 3xx - Redirecionamento
- 4xx - Client Error
- 5xx - Server Error