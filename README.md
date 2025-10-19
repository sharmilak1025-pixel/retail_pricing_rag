🛍️ Retail Competitor Pricing Intelligence with RAG & Agentic RAG
Overview
This Hugging Face Space demonstrates a full GenAI lifecycle for comparing competitor pricing in the retail domain using:
- 🧠 Deep Learning & NLP for product understanding
- 🔍 RAG (Retrieval-Augmented Generation) for grounded insights
- 🤖 Agentic RAG for autonomous pricing recommendations
Built with modular .py scripts and Streamlit UI, this app helps retailers analyze competitor prices and generate actionable strategies.

🚀 Features
- Web/API Ingestion: Scrapes competitor sites like Flipkart and Amazon
- Embeddings: Uses Sentence-BERT for semantic matching
- Vector Search: FAISS-based retrieval of similar products
- LLM Insights: GPT-4 or Claude for pricing strategy generation
- Agentic RAG: Simulated multi-agent flow for autonomous recommendations

🧩 File Structure
retail_pricing_rag/
├── app.py                  # Streamlit UI
├── ingest.py               # Data ingestion
├── embed.py                # Embedding pipeline
├── retrieve.py             # Vector search
├── generate.py             # LLM-based generation
├── agent.py                # Agentic RAG orchestration
├── requirements.txt
└── README.md



🛠️ Setup
Requirements
pip install -r requirements.txt


Run Locally
streamlit run app.py


Deploy on Hugging Face Spaces
- Create a new Space (SDK: Streamlit)
- Push this repo to the Space Git URL
- Hugging Face will auto-deploy your app

🧪 Sample Query
“Compare prices for Nike Air Zoom Pegasus 39 across Flipkart and Amazon. What pricing strategy should we adopt?”


📈 Future Enhancements
- Integrate LangGraph or CrewAI for real agent orchestration
- Add real-time API connectors for dynamic pricing feeds
- Benchmark latency and accuracy across LLMs
