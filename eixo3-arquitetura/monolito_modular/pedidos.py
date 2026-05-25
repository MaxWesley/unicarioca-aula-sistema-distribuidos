from usuarios import usuarios
from produtos import produtos

def gerar_pedido(id_usuario, id_produto):

    usuario = usuarios.get(id_usuario)
    produto = produtos.get(id_produto)

    return {
        "usuario": usuario,
        "produto": produto["nome"],
        "preco": produto["preco"],
        "status": "pedido criado"
    }

