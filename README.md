# Python_Flask_Biblioteca

# Desafio Stemis

Bem vindo ao Desafio Stemis!

Este desafio compreende uma das etapas do processo seletivo para a vaga de estagiário em backend.

O desafio consiste na criação de uma API REST usando Python Flask, com simples funções de CRUD, para alguma aplicação interessante e relevante, da sua escolha. Por exemplo, você pode criar um catálogo de produtos, um carrinho de compras, uma gestão de usuários, um sistema de avaliação de serviços (o projeto pode ser algo simples, mas quanto melhor o projeto, mais você se destaca). O importante é que a sua API seja funcional e compreenda as 4 principais operações.

Nunca se esqueça, uma boa API é uma API documentada.

Para conhecer mais sobre a Stemis acesse o nosso [site](https://www.stemis.com.br).

Para ficar informado sobre futuros processos seletivos, siga a gente no Instagram [@stemis.tec](https://www.instagram.com/stemis.tec)





# Documentaçao da API livraria


API Livraria é uma aplicação Flask que permite gerenciar uma coleção de livros em um banco de dados. Você pode realizar operações CRUD (Create, Read, Update, Delete) nos livros da livraria usando esta API.



Endpoints da API
1. Listar Todos os Livros
Endpoint: /livraria
Método HTTP: GET


Este endpoint permite listar todos os livros disponíveis na livraria.



Exemplo de Solicitação:
http
Copy code
GET /livraria
Exemplo de Resposta (200 OK):
json
Copy code
[
    {
        "id": 1,
        "titulo": "O Senhor dos Anéis",
        "autor": "J.R.R. Tolkien",
        "num_paginas": 1178,
        "custo": 29.99
    },
    {
        "id": 2,
        "titulo": "Dom Quixote",
        "autor": "Miguel de Cervantes",
        "num_paginas": 863,
        "custo": 19.99
    }
    // Outros livros...
]


2. Listar um Livro por ID
Endpoint: /livraria/<id>
Método HTTP: GET

Este endpoint permite listar um livro específico pelo seu ID.

Exemplo de Solicitação:
http
Copy code
GET /livraria/1
Exemplo de Resposta (200 OK):
json
Copy code
{
    "id": 1,
    "titulo": "O Senhor dos Anéis",
    "autor": "J.R.R. Tolkien",
    "num_paginas": 1178,
    "custo": 29.99
}
3. Adicionar um Novo Livro
Endpoint: /livraria/add
Método HTTP: POST

Este endpoint permite adicionar um novo livro à livraria.

Exemplo de Solicitação:
http
Copy code
POST /livraria/add
Content-Type: application/json

{
    "titulo": "Harry Potter e a Pedra Filosofal",
    "autor": "J.K. Rowling",
    "num_paginas": 320,
    "custo": 24.99
}
Exemplo de Resposta (201 Created):
json
Copy code
{
    "Message": "Seu livro foi adicionado com sucesso"
}
4. Atualizar um Livro Existente
Endpoint: /livraria/atualizar/<id>
Método HTTP: PUT

Este endpoint permite atualizar as informações de um livro existente com base no seu ID.

Exemplo de Solicitação:
http
Copy code
PUT /livraria/atualizar/1
Content-Type: application/json

{
    "titulo": "O Senhor dos Anéis: A Sociedade do Anel"
}
Exemplo de Resposta (200 OK):
json
Copy code
{
    "Message": "Livro atualizado com sucesso"
}
5. Excluir um Livro
Endpoint: /livraria/delete/<id>
Método HTTP: DELETE

Este endpoint permite excluir um livro da livraria com base no seu ID.

Exemplo de Solicitação:
http
Copy code
DELETE /livraria/delete/1
Exemplo de Resposta (200 OK):
json
Copy code
{
    "Message": "Livro excluído com sucesso"
}
Erros e Mensagens
A API retorna mensagens de erro apropriadas em caso de problemas. Os principais erros possíveis incluem:

400 Bad Request: Campos obrigatórios faltando ou dados inválidos na solicitação.
404 Not Found: Livro não encontrado com base no ID fornecido.
500 Internal Server Error: Erro interno do servidor ao executar uma operação.
Considerações Finais
Esta é uma documentação básica da API Livraria, que fornece operações CRUD para gerenciar livros em uma livraria. Você pode estender esta documentação com informações adicionais, como autenticação, autorização, validações e exemplos detalhados de solicitações e respostas, conforme necessário para o seu projeto. Certifique-se de configurar corretamente seu ambiente de desenvolvimento e banco de dados antes de usar a API.