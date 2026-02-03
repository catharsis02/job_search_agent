# Job Search Agent

An intelligent AI-powered job search agent that helps you find job postings using natural language queries. The agent leverages LangChain, Tavily Search, and Google's Gemini AI to search and retrieve job listings from LinkedIn and other sources.

## Features

- 🤖 Natural language job search queries
- 🔍 Powered by Tavily Search for comprehensive web searching
- 🧠 Uses Google Gemini 2.5 Flash for intelligent processing
- 📋 Structured output with job details and source URLs
- 🔗 Automatic extraction and organization of source links
- 📍 Location-based job searches
- 🎯 Technology/skill-specific filtering

## Prerequisites

- Python >= 3.12
- API Keys:
  - Google Generative AI API key
  - Tavily API key
  - (Optional) Groq API key

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Job_Search_Agent
```

2. Install dependencies using pip:
```bash
pip install -e .
```

Or install dependencies from pyproject.toml:
```bash
pip install langchain langchain-google-genai langchain-groq langchain-tavily python-dotenv pydantic tavily-python
```

3. Create a `.env` file in the project root and add your API keys:
```env
GOOGLE_API_KEY=your_google_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
GROQ_API_KEY=your_groq_api_key_here  # Optional
```

## Usage

### Basic Usage

Run the main script:
```bash
python main.py
```

### Example Queries

The agent can handle natural language queries like:

```python
from langchain_core.messages import HumanMessage

# Search for AI Engineer jobs in a specific location
result = agent.invoke({
    "messages": HumanMessage(
        content="search for 3 job postings for an ai engineer using langchain in Bhubaneswar Odisha on linkedin and list their details"
    )
})
```

### Custom Queries

You can modify the query in [main.py](main.py) to search for different positions:

- "Find 5 Python developer jobs in Bangalore"
- "Search for remote machine learning engineer positions"
- "Look for data scientist roles using TensorFlow in Mumbai"

## Project Structure

```
Job_Search_Agent/
├── __init__.py          # Package initialization
├── main.py              # Main application using Google Gemini
├── groq.py              # Alternative implementation using Groq
├── pyproject.toml       # Project dependencies and metadata
├── README.md            # This file
└── .env                 # Environment variables (not in repo)
```

## Code Overview

### Main Components

**Agent Response Schema:**
```python
class AgentResponse(BaseModel):
    answer: str                    # The agent's detailed answer
    sources: list[Source]          # List of source URLs
```

**Source Schema:**
```python
class Source(BaseModel):
    url: str                       # URL of the source
```

### Implementation Files

- **[main.py](main.py)**: Uses Google Gemini 2.5 Flash for job search queries with structured output
- **[groq.py](groq.py)**: Alternative implementation using Groq's GPT model with manual URL extraction

## Dependencies

Key dependencies include:
- `langchain` - LangChain framework for building AI agents
- `langchain-google-genai` - Google Generative AI integration
- `langchain-groq` - Groq API integration
- `langchain-tavily` - Tavily Search integration
- `pydantic` - Data validation using Python type annotations
- `python-dotenv` - Load environment variables from .env file

For a complete list, see [pyproject.toml](pyproject.toml).

## How It Works

1. **Query Processing**: The agent receives a natural language job search query
2. **Web Search**: Uses Tavily Search to find relevant job postings across the web
3. **AI Processing**: Google Gemini or Groq processes the search results
4. **Structured Output**: Returns formatted job details with source URLs
5. **Source Extraction**: Automatically extracts and organizes reference links

## Configuration

### Changing the LLM Model

**Using Google Gemini (default):**
```python
llm = ChatGoogleGenerativeAI(temperature=0, model="gemini-2.5-flash")
```

**Using Groq:**
```python
llm = ChatGroq(temperature=0, model="openai/gpt-oss-20b")
```

### Adjusting Search Parameters

Modify the query content in the `HumanMessage` to change:
- Number of results
- Job title/role
- Location
- Required skills/technologies
- Platform (e.g., LinkedIn, Indeed)

## Environment Variables

Required environment variables in `.env`:

```env
GOOGLE_API_KEY=<your-google-api-key>
TAVILY_API_KEY=<your-tavily-api-key>
GROQ_API_KEY=<your-groq-api-key>  # Only if using groq.py
```

## Development

### Code Formatting

The project uses:
- `black` for code formatting
- `isort` for import sorting

Format your code:
```bash
black .
isort .
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the MIT License.

## Acknowledgments

- [LangChain](https://langchain.com/) - Framework for building LLM applications
- [Tavily](https://tavily.com/) - AI-powered search API
- [Google Gemini](https://deepmind.google/technologies/gemini/) - Generative AI model
- [Groq](https://groq.com/) - Fast AI inference

## Support

For issues, questions, or contributions, please open an issue in the repository.

---

**Note**: This tool is for educational and research purposes. Always respect the terms of service of job platforms when scraping or accessing their data.