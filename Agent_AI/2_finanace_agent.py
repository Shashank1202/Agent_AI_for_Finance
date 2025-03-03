from phi.agent import Agent 
from phi.model.groq import Groq 
from dotenv import load_dotenv
from phi.tools.yfinance import YFinanceTools

load_dotenv()

agent= Agent(
    model= Groq(id="llama-3.3-70b-versatile"),
    tools = [YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    show_tools_calls= True,
    markdown= True,
    instructions=["Use tables to display data."],
    debug_mode= True,

)


agent.print_response("summarize and compare analyst recommendations and fundamentals for TSLA and NVIDA stocks")