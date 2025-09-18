from crewai import Agent, Task, Crew


def analyzer_agent(llm, rag_tool):

    agent2 = Agent(
        role = "Senior generative AI engineer",
        goal = "Determine wheter  agent is secure or not, depending on usecase", #"Design a communication protocol for agents to communicate with each other and with humans.",
        backstory = "You are a senior generative AI engineer with expertise in designing secure communication protocols for AI agents.",
        verbose = True,
        allow_delegation = False,
        llm = llm,
        tools = [rag_tool],
        max_retry_limits = 1
    )


    task1 = Task(
    #
        # We don't need a fix prompt anymore. We may use a dynamic prompt unpacking from input messages
        # description = "What is the best way to design a communication protocol for agents to communicate with each other and with humans?",
        description = input[0].parts[0].content if input else "What is the best way to design a communication protocol for agents to communicate with each other and with humans?",
        # If we have multiple prompts, we may loop over the input and create multiple tasks
        # 
        expected_output = "A secure communication protocol that ensures privacy and integrity of the messages exchanged between agents and humans.",
        agent = agent2,
    )

    crew = Crew(
        agents = [agent2],
        tasks = [task1],
        verbose = True
    )

    # task_output = await crew.kickoff_async()
    return crew.kickoff()