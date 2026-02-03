from dotenv import load_dotenv
from pydantic import BaseModel,Field
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

class Source(BaseModel):
    """Schema of a source used by the agent."""

    url:str = Field(description="The URL of the source")

class AgentResponse(BaseModel):
    """Schema for agent response with answer and sources."""

    answer:str = Field(description="The agent's answer to the query")
    sources:list[Source] = Field(default_factory=list,description="List of Sources to generate the answer")

llm = ChatGoogleGenerativeAI(temperature=0,model="gemini-2.5-flash")
tools = [TavilySearch()]
agent = create_agent(model=llm,tools = tools,response_format=AgentResponse)



def main():
    # search("Hello")
    result = agent.invoke({"messages":HumanMessage(content="search for 3 job postings for an ai engineer using langchain in the Bhubaneswar Odisha on linkedin and list their details")})
    print(result)

if __name__ == "__main__":
    main()
