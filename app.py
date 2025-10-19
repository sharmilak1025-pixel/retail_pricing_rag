import streamlit as st
from ingest import fetch_competitor_data
from embed import embed_documents
from retrieve import search_similar_products
from generate import generate_insights
from agent import run_agentic_rag

st.title("🛒 Retail Competitor Pricing Intelligence")

query = st.text_input("Enter product name or SKU:")
if query:
    raw_data = fetch_competitor_data(query)
    docs = embed_documents(raw_data)
    results = search_similar_products(query, docs)
    insights = generate_insights(query, results)
    st.write("### Pricing Insights")
    st.write(insights)

    if st.button("Run Agentic RAG"):
        agent_output = run_agentic_rag(query)
        st.write("### Agent Recommendation")
        st.write(agent_output)
