from smolagents import DuckDuckGoSearchTool, CodeAgent

def agent_similar_companies(model, company_description):
    
    agent = CodeAgent(
        model = model,
        tools = [DuckDuckGoSearchTool()]
    )

    # task = f"Find the top 5 companies similar to {company} and return the list of companies as a python list of strings"
    prompt = f"""
        You are a research assistant specialized in market analysis.  
        Your task is: 
            This is my company description: {company_description}, find on the internet another company whose main business activity is the closest possible, meaning it is a **direct competitor**.  

        Your output must **always** be the name of the company found

        Do not add extra text, explanations.  
        Return only the plain text.  

        Example output:
        Pepsico
    """

    resp = agent.run(task=prompt, max_steps=3)
    # print(agent)
    return resp

