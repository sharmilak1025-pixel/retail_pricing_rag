from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

llm = ChatOpenAI(temperature=0.3)

def generate_insights(query, results):
    prompt = PromptTemplate.from_template(
        "Compare these competitor prices for '{query}': {results}. What pricing strategy should we adopt?"
    )
    return llm.predict(prompt.format(query=query, results=results))