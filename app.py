"""
app.py — Trisearch AI  |  Polished Streamlit UI
Author: Yuvanesh Raju
"""

import streamlit as st
from rag import answer_query

# ── Page config ───────────────────────────────────────────────────
st.set_page_config(
    page_title="Trisearch AI",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Custom CSS ────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;1,9..40,300&display=swap');

*, *::before, *::after { box-sizing: border-box; }

html, body, [data-testid="stAppViewContainer"] {
    background: #09090f !important;
    color: #e8e6f0 !important;
    font-family: 'DM Sans', sans-serif !important;
}

[data-testid="stAppViewContainer"] { background: #09090f !important; }

[data-testid="block-container"] {
    padding: 2rem 3rem !important;
    max-width: 900px !important;
    margin: 0 auto !important;
}

#MainMenu, footer, header { visibility: hidden; }
[data-testid="stToolbar"] { display: none; }

/* ── Hero Header ── */
.trisearch-header {
    text-align: center;
    padding: 3.5rem 0 2rem;
}

.trisearch-logo-mark {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 52px;
    height: 52px;
    background: linear-gradient(135deg, #7c5cfc 0%, #c084fc 100%);
    border-radius: 14px;
    margin-bottom: 1.2rem;
    font-size: 26px;
    box-shadow: 0 0 40px rgba(124, 92, 252, 0.4);
}

.trisearch-title {
    font-family: 'Syne', sans-serif !important;
    font-size: 2.6rem !important;
    font-weight: 800 !important;
    letter-spacing: -0.03em !important;
    background: linear-gradient(135deg, #ffffff 30%, #a78bfa 100%);
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    background-clip: text !important;
    margin: 0 0 0.4rem !important;
    line-height: 1.1 !important;
}

.trisearch-sub {
    font-size: 0.95rem !important;
    color: #6b6882 !important;
    letter-spacing: 0.04em !important;
    font-weight: 300 !important;
    margin: 0 !important;
}

.trisearch-pills {
    display: flex;
    gap: 0.5rem;
    justify-content: center;
    margin-top: 1rem;
    flex-wrap: wrap;
}

.pill {
    font-size: 0.72rem;
    font-weight: 500;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    padding: 0.3rem 0.75rem;
    border-radius: 999px;
    border: 1px solid #2a2740;
    color: #8b80b0;
    background: #13111f;
}

/* ── Search Box ── */
.stTextInput > div > div > input {
    background: #13111f !important;
    border: 1.5px solid #2a2740 !important;
    border-radius: 14px !important;
    color: #e8e6f0 !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 1.05rem !important;
    font-weight: 400 !important;
    padding: 0.85rem 1.2rem !important;
    transition: border-color 0.2s, box-shadow 0.2s !important;
    caret-color: #7c5cfc !important;
}

.stTextInput > div > div > input:focus {
    border-color: #7c5cfc !important;
    box-shadow: 0 0 0 3px rgba(124, 92, 252, 0.15) !important;
    outline: none !important;
}

.stTextInput > div > div > input::placeholder { color: #3d3857 !important; }
.stTextInput label { display: none !important; }

/* ── Answer Card ── */
.answer-card {
    background: #13111f;
    border: 1px solid #2a2740;
    border-radius: 18px;
    padding: 1.8rem 2rem;
    margin: 1.8rem 0 1.2rem;
    position: relative;
    overflow: hidden;
}

.answer-card::before {
    content: "";
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, #7c5cfc, #c084fc, #7c5cfc);
}

.answer-label {
    font-family: 'Syne', sans-serif;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #7c5cfc;
    margin-bottom: 0.85rem;
}

.answer-text {
    font-size: 1rem;
    line-height: 1.75;
    color: #cbc8e0;
    font-weight: 300;
}

/* ── Sources ── */
.sources-label {
    font-family: 'Syne', sans-serif;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #4d4870;
    margin: 1.8rem 0 0.8rem;
}

.source-card {
    background: #0e0d1a;
    border: 1px solid #1e1c2e;
    border-radius: 12px;
    padding: 1rem 1.25rem;
    margin-bottom: 0.6rem;
    transition: border-color 0.2s;
}

.source-card:hover { border-color: #3a3458; }

.source-header {
    display: flex;
    align-items: center;
    gap: 0.6rem;
    margin-bottom: 0.5rem;
    flex-wrap: wrap;
}

.source-filename {
    font-family: 'Syne', sans-serif;
    font-size: 0.85rem;
    font-weight: 600;
    color: #a89fd4;
    flex: 1;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    min-width: 0;
}

.source-meta { font-size: 0.75rem; color: #4d4870; white-space: nowrap; }

.source-score {
    font-size: 0.72rem;
    font-weight: 600;
    color: #7c5cfc;
    background: rgba(124, 92, 252, 0.1);
    padding: 0.2rem 0.55rem;
    border-radius: 999px;
    white-space: nowrap;
}

.source-badge {
    font-size: 0.68rem;
    font-weight: 600;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    padding: 0.15rem 0.5rem;
    border-radius: 6px;
    white-space: nowrap;
}

.badge-pdf      { background: rgba(239,68,68,0.12);   color: #f87171; }
.badge-pptx     { background: rgba(249,115,22,0.12);  color: #fb923c; }
.badge-docx     { background: rgba(59,130,246,0.12);  color: #60a5fa; }
.badge-eml      { background: rgba(16,185,129,0.12);  color: #34d399; }
.badge-glossary { background: rgba(234,179,8,0.12);   color: #fbbf24; }
.badge-other    { background: rgba(148,163,184,0.12); color: #94a3b8; }

.source-text {
    font-size: 0.83rem;
    line-height: 1.65;
    color: #4a4768;
    font-style: italic;
    border-top: 1px solid #1a1828;
    margin-top: 0.5rem;
    padding-top: 0.6rem;
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
}

/* ── Error ── */
.error-card {
    background: rgba(239,68,68,0.06);
    border: 1px solid rgba(239,68,68,0.2);
    border-radius: 12px;
    padding: 1.2rem 1.5rem;
    margin-top: 1rem;
    color: #f87171;
    font-size: 0.9rem;
    line-height: 1.6;
}

/* ── Empty state ── */
.empty-state {
    text-align: center;
    padding: 4rem 1rem;
}

.empty-icon { font-size: 2rem; margin-bottom: 0.75rem; opacity: 0.25; }
.empty-text { font-size: 0.88rem; color: #2e2b47; }

.example-queries {
    display: flex;
    flex-direction: column;
    gap: 0.4rem;
    max-width: 480px;
    margin: 1.5rem auto 0;
}

.example-q {
    font-size: 0.8rem;
    color: #3a3660;
    padding: 0.5rem 1rem;
    border: 1px dashed #1e1c2e;
    border-radius: 8px;
    text-align: left;
}

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: #09090f; }
::-webkit-scrollbar-thumb { background: #2a2740; border-radius: 999px; }
::-webkit-scrollbar-thumb:hover { background: #3d3858; }
</style>
""", unsafe_allow_html=True)


# ── Header ────────────────────────────────────────────────────────
st.markdown("""
<div class="trisearch-header">
    <div class="trisearch-logo-mark">⟡</div>
    <h1 class="trisearch-title">Trisearch AI</h1>
    <p class="trisearch-sub">Hybrid semantic · BM25 · glossary retrieval with LLM-powered answers</p>
    <div class="trisearch-pills">
        <span class="pill">⟡ Semantic</span>
        <span class="pill">◈ BM25 Lexical</span>
        <span class="pill">◇ Glossary Boost</span>
        <span class="pill">◆ RAG · GPT-4o-mini</span>
    </div>
</div>
""", unsafe_allow_html=True)


# ── Search Input ──────────────────────────────────────────────────
query = st.text_input(
    label="query",
    placeholder="Ask anything — e.g.  What does frm_brand_awareness measure?",
    key="main_query",
)


# ── Badge helper ──────────────────────────────────────────────────
def _badge(source: str) -> str:
    s = source.lower()
    if s.endswith(".pdf"):          return '<span class="source-badge badge-pdf">PDF</span>'
    if s.endswith(".pptx"):         return '<span class="source-badge badge-pptx">PPTX</span>'
    if s.endswith(".docx"):         return '<span class="source-badge badge-docx">DOCX</span>'
    if s.endswith(".eml"):          return '<span class="source-badge badge-eml">EMAIL</span>'
    if "glossary" in s or s.endswith(".json"):
                                    return '<span class="source-badge badge-glossary">GLOSSARY</span>'
    return                                 '<span class="source-badge badge-other">DOC</span>'


# ── Main Logic ────────────────────────────────────────────────────
if query:
    with st.spinner("Retrieving and generating answer…"):
        answer, results = answer_query(query)

    is_error = answer.startswith("⚠️")

    if is_error:
        st.markdown(f'<div class="error-card">{answer}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="answer-card">
            <div class="answer-label">✦ Answer</div>
            <div class="answer-text">{answer}</div>
        </div>
        """, unsafe_allow_html=True)

    if results:
        st.markdown(
            f'<div class="sources-label">↳ {len(results)} source{"s" if len(results) != 1 else ""} retrieved</div>',
            unsafe_allow_html=True,
        )
        for r in results:
            meta     = r.get("meta", "")
            score    = r.get("score", 0)
            badge    = _badge(r["source"])
            meta_str = f'<span class="source-meta">{meta}</span>' if meta else ""
            safe_txt = r["text"].replace("<", "&lt;").replace(">", "&gt;")

            st.markdown(f"""
            <div class="source-card">
                <div class="source-header">
                    {badge}
                    <span class="source-filename">{r["source"]}</span>
                    {meta_str}
                    <span class="source-score">{score:.3f}</span>
                </div>
                <div class="source-text">{safe_txt}</div>
            </div>
            """, unsafe_allow_html=True)

else:
    st.markdown("""
    <div class="empty-state">
        <div class="empty-icon">⟡</div>
        <div class="empty-text">Type a question above to search across your documents</div>
        <div class="example-queries">
            <div class="example-q">What was the main finding of the brand study?</div>
            <div class="example-q">What does frm_brand_awareness measure?</div>
            <div class="example-q">What are the cooking habits of probable trialists?</div>
            <div class="example-q">What competitors appear in the frozen meal market?</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
