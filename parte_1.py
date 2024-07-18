import chromadb

chroma_client = chromadb.Client()
chroma_client = chromadb.PersistentClient(path="db")
collection = chroma_client.get_or_create_collection(name="artigo")

def quebra_texto(texto, pedaco_tamanho=1000, sobrepor=200):
    if pedaco_tamanho <= sobrepor:
        raise ValueError("pedaco necessita ser maior do que o sobrepor")

    pedacos = []
    inicio = 0
    while inicio < len(texto):
        final = inicio + pedaco_tamanho
        pedacos.append(texto[inicio:final])
        if final >= len(texto):
            inicio = len(texto)
        else:
            inicio += pedaco_tamanho - sobrepor

    return pedacos


with open("texto.txt", "r", encoding="utf-8") as file:
    texto = file.read()

pedacos = quebra_texto(texto)

for i, pedaco in enumerate(pedacos):
    print(f"pedaco {i+1}:")
    print(pedaco)
    print(len(pedaco))
    print()

    collection.add(documents=pedaco, ids=[str(i)])