from dotenv import load_dotenv
from pydantic import BaseModel,Field
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch
import re

load_dotenv()

class Source(BaseModel):
    """Schema of a source used by the agent."""
    url:str = Field(description="The URL of the source")

class AgentResponse(BaseModel):
    """Schema for agent response with answer and sources."""
    answer:str = Field(description="The agent's answer to the query")
    sources:list[Source] = Field(default_factory=list,description="List of Sources to generate the answer")

llm = ChatGroq(temperature=0,model="openai/gpt-oss-20b")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)

structured_llm = llm.with_structured_output(AgentResponse)

def main():
    result = agent.invoke({"messages":HumanMessage(content="search for 2 job postings for an ai engineer using langchain in the Bhubaneswar Odisha on linkedin and list their details")})

    final_message = result["messages"][-1].content
    urls = re.findall(r'https?://[^\s\)"]+', final_message)

    formatted_response = AgentResponse(
        answer=final_message,
        sources=[Source(url=url) for url in urls]
    )

    print(formatted_response)

if __name__ == "__main__":
    main()