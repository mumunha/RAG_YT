import chromadb
from openai import OpenAI


# OpenAI.api_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

client = OpenAI(api_key="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")


questao = input("Como posso lhe ajudar? ")

chroma_client = chromadb.Client()
chroma_client = chromadb.PersistentClient(path="db")
collection = chroma_client.get_or_create_collection(name="artigo")

results = collection.query(query_texts=questao, n_results=2)

conteudo = results["documents"][0][0] + results["documents"][0][1]

prompt = """
Você é um assistente do Restaurante Sabores.
Use o seguinte contexto para responder a questão, não use nenhuma informação adicional, se nao houver informacao no contexto, responda: Desculpe mas não consigo ajudar.
Sempre termine a resposta com: Foi um prazer lhe atender, não deixe de provar nossos sabores.
"""

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": prompt,
        },
        {"role": "system", "content": conteudo},
        {"role": "user", "content": questao},
    ],
)

answer = completion.choices[0].message.content

print(answer)