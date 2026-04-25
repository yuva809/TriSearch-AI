"""
rag.py — LLM answer generation layer for Trisearch AI.

FIX 1: Switched from the deprecated client.responses.create() (Responses API)
        to client.chat.completions.create() (Chat Completions API), which is
        the correct standard OpenAI SDK call.

FIX 2: Added try/except around the OpenAI call so API errors (rate limits,
        bad keys, network failures) return a user-friendly message instead of
        crashing the Streamlit app with an unhandled exception.

Author: Yuvanesh Raju
"""

from retrieve import retrieve
from openai import OpenAI

client = OpenAI()


def answer_query(query: str):
    """
    Retrieve relevant passages and generate a grounded answer via GPT-4o-mini.

    Returns:
        answer  (str)  — LLM-generated answer or error message
        results (list) — top-K retrieved chunks from retrieve()
    """
    results = retrieve(query)

    if not results:
        return "No relevant documents found for your query.", []

    context = "\n\n".join([
        f"[Source: {r['source']}]\n{r['text']}"
        for r in results
    ])

    # FIX 1: correct Chat Completions API call
    # Old (broken): client.responses.create(model=..., input=prompt)
    # New (correct): client.chat.completions.create(model=..., messages=[...])
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a precise research assistant. "
                        "Answer the user's question using ONLY the context provided. "
                        "If the context does not contain enough information to answer, "
                        "say so clearly. Do not fabricate details."
                    ),
                },
                {
                    "role": "user",
                    "content": (
                        f"Context:\n{context}\n\n"
                        f"Question: {query}"
                    ),
                },
            ],
            temperature=0.2,     # low temp for factual retrieval tasks
            max_tokens=512,
        )
        # FIX 1: correct response accessor for Chat Completions
        # Old (broken): response.output[0].content[0].text
        # New (correct): response.choices[0].message.content
        answer = response.choices[0].message.content

    # FIX 2: graceful error handling — surfaces a readable message in the UI
    except Exception as e:
        answer = (
            f"⚠️ Could not generate an answer: {e}\n\n"
            "Please check your OpenAI API key and network connection."
        )

    return answer, results
