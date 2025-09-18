import os, json
from smolagents import LiteLLMModel

from langchain_ollama import OllamaLLM
from crewai import Crew, Task, Agent, LLM

from services.srv_agent1 import agent_similar_companies
from services.srv_rag import create_rag_tool
from services.srv_analyzer_agent import analyzer_agent

HTML_FOLDER = "./media"

model1 = LiteLLMModel(
    # model_id = "gemini/gemini-1.5-flash",
    model_id = "ollama/qwen2.5:0.5b"
    # api_key = os.getenv("GEMINI_API_KEY")
)

config_rag = {
    "llm": {
        "provider": "ollama",
        "config": {
            "model" : "qwen2.5:0.5b"
            }
    },
    "embedder": {
        "provider": "ollama",
        "config": {
            "model": "nomic-embed-text"
        }
    }
}

# https://www.sec.gov/edgar/search/#/q=aws&filter_forms=10-K 




if __name__ == "__main__":


    company_description = f"""
        AItomatizate is a company that designs and implements AI-powered automation solutions, transforming manual and repetitive processes into autonomous, intelligent, and scalable workflows. We focus on sectors such as finance, logistics, customer service, and regulatory compliance (such as EDGAR scraping), helping companies reduce costs, minimize errors, and free up their teams for high-value strategic tasks. We automate the complex so you can focus on what's important.
    """
    # company_description2 = """**Chevrolet** – An iconic American automotive brand under General Motors, Chevrolet designs, manufactures, and markets a wide range of vehicles including cars, trucks, SUVs, and electric models, known for durability, innovation, and broad consumer appeal across global markets."""
    # resp = agent_similar_companies(model1, company_description)
    # print(resp)

    rag_tool = create_rag_tool(config_rag, HTML_FOLDER)
    # agent2 = analyzer_agent(model1, rag_tool)
    # print(agent2)
    



    