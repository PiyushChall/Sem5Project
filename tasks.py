from textwrap import dedent

from agents import chief_developer, qa_engineer, senior_developer
from crewai import Task
from tools import search_tool, web_search_tool

game = input(
    "What is the name of the game you want to create? (e.g. Pong, 2048, Tetris, etc): ")

brainstorm = Task(description=dedent("""
    Brainstorm a game idea based on the instructions given.
    Research the game mechanics and design the game.
    These are some instruction to follow: 

    Instructions
    ------------
    {game}
    ------------
    Select which idea is the best for the game.
    If required take some human inputs.
    """),
                  max_iter=3,
                  human_input=True,
                  expected_output=dedent("""
        A detailed instruction on how the game should be built.
        """),
                  tools=[search_tool, web_search_tool],
                  agent=chief_developer)


programming = Task(
    description=dedent("""
    Create a game using Python. 
    You MUST use the pygame library for graphics and game loop.

    Instructions:
    ------------
    {game}
    ------------
    """),
    expected_output=dedent("""
    Your final output should be the python code for the game only,
    and nothing else.
    """),
    agent=senior_developer,
    Context=brainstorm,
)

reviewing = Task(
    description=dedent("""
    You are helping to create a Python game using pygame.

    Instructions:
    ------------
    {game}
    ------------

    Using the code you have been provided, check for logic errors,
    syntax errors, missing imports (including pygame), 
    variable declaration, and any errors.
    Try to fix them if possible.
    """),
    expected_output=dedent("""
    Your final output must be the full python code and nothing else.
    """),
    agent=qa_engineer,
    Context=programming,
)

evaluation = Task(
    description=dedent("""
    You are helping to create a Python game using pygame.

    Instructions:
    ------------
    {game}
    ------------

    You will overlook the code to ensure that it is correct
    and executes without any errors.  
    Run the code with pygame and check for any issues.
    """),
    expected_output=dedent("""
    Your final output must be the full python code and nothing else.
    """),
    agent=chief_developer,
    async_execution=False,
    Context=reviewing,
    output_file=game+".py")
