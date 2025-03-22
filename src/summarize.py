from langchain.tools import Tool
from langchain.agents import initialize_agent, AgentType
from langchain_community.llms import Ollama

llm = Ollama(model="mistral") # Initialize llm in the global scope

def summarize_invoice(invoice_text):
    return llm(invoice_text)

summary_tool = Tool(name="Invoice Summarizer", func=summarize_invoice, description="Summarizes invoices.")        
summary_agent = initialize_agent(tools=[summary_tool], llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

def summarize(text):
    return summary_agent.run(text)