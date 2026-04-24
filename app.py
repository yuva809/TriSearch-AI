import streamlit as st
from rag import answer_query

st.title("🔍 Trisearch AI")

query = st.text_input("Ask something:")

if query:
    answer, results = answer_query(query)

    st.subheader("Answer")
    st.write(answer)

    st.subheader("Sources")
    for r in results:
        st.write("###", r["source"])
        st.write(r["text"])