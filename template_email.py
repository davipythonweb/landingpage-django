#criando uma lista de clientes
clientes = ["Ana", "Alana", "Davi"]

#criando um template de email
email_template = """
Ola, %(cliente)s 
Tem interesse em comprar %(produto)s?
Este produto eh otimo para resolver %(problema)s
click aqui para comprar %(link)s
Apenas %(quantidade)d unidades disponiveis!
Preco promocional $%(preco).2f
"""

#criando um loop para enviar o email para cada cliente
for cliente in clientes:
    print(
        email_template % {
            'cliente': cliente,
            'produto': 'caneta',
            'problema': 'na hora de escrever',
            'link': 'http://canetaslegais.com.br',
            'quantidade': 1,
            'preco': 40.5
        }
    )

