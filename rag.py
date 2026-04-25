"""
rag.py — LLM answer generation layer for Trisearch AI.

FIX (speed): Added stream=True support via answer_query_stream().
             Tokens are yielded one by one so Streamlit can display
             them in real-time instead of waiting for the full response.

answer_query()        — original non-streaming call (kept for compatibility)
answer_query_stream() — new streaming generator used by app.py

Author: Yuvanesh Raju
"""

from retrieve import retrieve
from openai import OpenAI

client = OpenAI()

SYSTEM_PROMPT = (
    "You are a precise research assistant. "
    "Answer the user's question using ONLY the context provided. "
    "If the context does not contain enough information to answer, "
    "say so clearly. Do not fabricate details."
)


def _build_context(results: list) -> str:
    return "\n\n".join([
        f"[Source: {r['source']}]\n{r['text']}"
        for r in results
    ])


def answer_query(query: str):
    """
    Non-streaming version — returns (answer_str, results).
    Kept for backward compatibility with test_local.py.
    """
    results = retrieve(query)
    if not results:
        return "No relevant documents found for your query.", []

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user",   "content": f"Context:\n{_build_context(results)}\n\nQuestion: {query}"},
            ],
            temperature=0.2,
            max_tokens=512,
        )
        answer = response.choices[0].message.content
    except Exception as e:
        answer = (
            f"⚠️ Could not generate an answer: {e}\n\n"
            "Please check your OpenAI API key and network connection."
        )
    return answer, results


def answer_query_stream(query: str):
    """
    FIX (speed): Streaming generator.

    Yields tuples of ("token", token_str) or ("results", results_list).

    Usage in Streamlit:
        for kind, value in answer_query_stream(query):
            if kind == "results":
                results = value
            elif kind == "token":
                accumulated += value   # display token by token

    Why this is faster for the user:
    - retrieve() still takes the same time (local, fast)
    - Instead of waiting 2-3 s for GPT-4o-mini to finish the FULL response,
      the user sees the first token appear within ~0.5 s and reads as it streams.
    - Total wall-clock time is the same but perceived latency drops dramatically.
    """
    results = retrieve(query)
    if not results:
        yield ("results", [])
        yield ("token", "No relevant documents found for your query.")
        return

    yield ("results", results)

    try:
        stream = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user",   "content": f"Context:\n{_build_context(results)}\n\nQuestion: {query}"},
            ],
            temperature=0.2,
            max_tokens=512,
            stream=True,          # KEY: stream tokens as they arrive
        )
        for chunk in stream:
            delta = chunk.choices[0].delta.content
            if delta:
                yield ("token", delta)

    except Exception as e:
        yield ("token", f"⚠️ Could not generate an answer: {e}\n\nPlease check your OpenAI API key.")
