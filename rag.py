from retrieve import retrieve
from openai import OpenAI

client = OpenAI()

def answer_query(query):
    results = retrieve(query)

    context = "\n".join([r["text"] for r in results])

    prompt = f"""
Answer the question ONLY using the context below.

Context:
{context}

Question:
{query}
"""

    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt
    )

    answer = response.output[0].content[0].text

    return answer, results