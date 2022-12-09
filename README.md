<h1>API_Instrumentos &#x1F4BB</h1>
<h2>API criada com Python/FastAPI com banco de dados MongoDB &#x1F40D &#x1F343</h2>

<hr>

<h1>&#x2705 Rotas</h1>
<h2>&#x1F7E1 POST</h2>
<h3>/instrumento</h3>

    "nome_instrumento": str, -> Obrigatório
    "marca": str, -> Obrigatório 
    "modelo": str, -> Obrigatório
    "est_preco": int, -> Obrigatório
    "obs": str, -> Não Obrigatório
    "orquestra": bool -> Obrigatório
    
<hr>

<h2>&#x1F7E2 GET ALL</h2>
<h3>/instrumento</h3>
<h3>/instrumento?paginacao_limite={limite}
Traz todo os objetos do banco de dados

<hr>

<h2>&#x1F7E2 GET ID</h2>
<h3>/instrumento/{id}</h3>
Traz um objeto específico

<hr>

<h2>&#x26AA UPDATE ID</h2>
<h3>/instrumento/{id}</h3>

    "nome_instrumento": str
    "marca": str
    "modelo": str
    "est_preco": int
    "obs": str
    "orquestra": bool
    
<hr>
    
<h2>&#x1F534 DELETE ID</h2>
<h3>/instrumento/{id}</h3>

Deleta do banco de dados o Objeto específico

