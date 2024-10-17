import os

import agentops
from agents import chief_developer, qa_engineer, senior_developer
from crewai import Crew, Process
from tasks import brainstorm, evaluation, programming, reviewing, game
from tools import llm

agentop_api_key = os.environ['AGENTOP_API_KEY']
agentops.init(agentop_api_key)


#mechanism = input("What Specific mechanism would you like to add: ")

crew = Crew(agents=[senior_developer, qa_engineer, chief_developer],
            tasks=[brainstorm, programming, reviewing, evaluation],
            process=Process.hierarchical,
            manager_llm=llm)

result = crew.kickoff(inputs={"game": game})
print(result)
