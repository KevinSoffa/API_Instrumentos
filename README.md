# API_Instrumentos
API criada com Python/FastAPI com banco de dados MongoDB

<hr>

# Rotas
## POST
### /instrumento

    "nome_instrumento": str, -> Obrigatório
    "marca": str, -> Obrigatório 
    "modelo": str, -> Obrigatório
    "est_preco": int, -> Obrigatório
    "obs": str, -> Não Obrigatório
    "orquestra": bool -> Obrigatório
    
<hr>

## GET ALL
### /instrumento
Traz todo os objetos do banco de dados

<hr>

## GET ID
### /instrumento/{id}
Traz um objeto específico

<hr>

## UPDATE ID
### /instrumento/{id}

    "nome_instrumento": str, -> Não Obrigatório
    "marca": str, -> Não Obrigatório 
    "modelo": str, -> Não Obrigatório
    "est_preco": int, -> Não Obrigatório
    "obs": str, -> Não Obrigatório
    "orquestra": bool -> Não Obrigatório
    
<hr>
    
## DELETE ID
### /instrumento/{id}

Deleta do banco de dados o Objeto específico

