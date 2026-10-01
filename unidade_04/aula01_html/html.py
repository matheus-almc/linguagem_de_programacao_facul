# Criando uma página HTML usando Python

html_code = """
<!DOCTYPE html>
<html>
<head>
    <title>Exemplo de Front-end com Python</title>
</head>

<body>
    <h1>Olá, mundo!</h1>

    <p>
        Esta é uma página web criada usando Python no PyCharm.
    </p>
</body>
</html>
"""


# Criando o arquivo HTML
with open("pagina.html", "w", encoding="utf-8") as arquivo:
    arquivo.write(html_code)


print("Página HTML criada com sucesso!")