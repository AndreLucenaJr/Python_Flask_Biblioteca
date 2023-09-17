# Python_Flask_Biblioteca

# Desafio Stemis

Bem vindo ao Desafio Stemis!

Este desafio compreende uma das etapas do processo seletivo para a vaga de estagiário em backend.

O desafio consiste na criação de uma API REST usando Python Flask, com simples funções de CRUD, para alguma aplicação interessante e relevante, da sua escolha. Por exemplo, você pode criar um catálogo de produtos, um carrinho de compras, uma gestão de usuários, um sistema de avaliação de serviços (o projeto pode ser algo simples, mas quanto melhor o projeto, mais você se destaca). O importante é que a sua API seja funcional e compreenda as 4 principais operações.

Nunca se esqueça, uma boa API é uma API documentada.

Para conhecer mais sobre a Stemis acesse o nosso [site](https://www.stemis.com.br).

Para ficar informado sobre futuros processos seletivos, siga a gente no Instagram [@stemis.tec](https://www.instagram.com/stemis.tec)






# Documentaçao da API livraria

A API Livraria é uma aplicação Flask que permite gerenciar uma coleção de livros em um banco de dados. Você pode realizar operações CRUD (Create, Read, Update, Delete) nos livros da livraria usando esta API.


# Endpoints da API

# 1. Listar Todos os Livros
Endpoint: /livraria
Método HTTP: GET

Este endpoint permite listar todos os livros disponíveis na livraria.

Exemplo de Solicitação:

 GET http://lucena2307.pythonanywhere.com/livraria

Exemplo de Resposta (200 OK):


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


