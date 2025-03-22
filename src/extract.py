from langchain.llms import Ollama
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool

llm = Ollama(model="mistral")

def extract_invoice_details(text):
    prompt = f"Extract the invoice details from this text:\n\n{text}\n\nReturn as JSON."
    return llm.invoke(prompt)

extract_tool = Tool(name="Invoice Extractor", func=extract_invoice_details, description="Extracts invoice details.")

agent = initialize_agent(tools=[extract_tool], llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

def extract(text):
    return agent.invoke(text)
