# QUEM FEZ O SISTEMA?

1. Renan Bezerra dos Santos - 553228
2. Lucas Alcântara Carvalho - 95111

# O QUE É O CODIGO?

O código é feito em python, ele será um leitor de um arquivo .cvs que é gerado na disciplina e na sprint de web da salesforce onde pega a posição x e y dos clicks do usuario no site de forma automatica.
OBS: como o site não está hospedado via deploy o arquivo .cvs ( na pasta dados da SRPINT3PYTHON) já está gerado o arquivo para rodar corretamente o arquivo (1) para dar o erro intencional para realizar o try exception finally.

# COMO RODAR?

Clone o projeto, execute o main.py, escolhe o arquivo .cvs sem espaço para o codigo rodar corretamente e retornar a quantidade de clicks que o usuario fez em cada parte da pagina ( header main e footer) e também retorna a % onde o usuario mais clicou e qual componente o usuario teve mais interatividade.
OBS: para você realizar o erro e entrar no tramamento de try exception intencionalmente ti tem duas opcoes: ou quando for selecionar o arquivo sair sem selecionar o arquivo dara um erro, e também o erro de você selecionar o .cvs (1) que contem espaço, o erro acontece pois o read_cvs do pandas não aceita leitura de arquivos com espaço.
