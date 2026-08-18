Build a Multi-Agent Travel Planning System using LangGraph + MCP
This project extends the Multi-Agent Travel Planning System built in Part 1 by integrating MCP (Model Context Protocol) servers for real-time flight and weather data.

Part 1 of This Project
GitHub Repository:
https://github.com/Subashji2512/Travel_Agency.git

Requirements
APIs
Groq API: https://console.groq.com
Serp API: https://www.tavily.com/
AviationStack API: https://aviationstack.com/
Tools
PostgreSQL
serp MCP Server

Step 1: Create Python Environment
python -m venv .venv
Activate:
.venv\Scripts\activate

Step 2: Install Dependencies
pip install requirements.txt

Step 3: Install PostgreSQL
Download PostgreSQL:

https://www.postgresql.org/download/

Important: Note your PostgreSQL password and port number during installation.

Step 4: Create Database
CREATE DATABASE langgraph_memory_demo;
Step 5: Setup .env File
Create a .env file:

GROQ_API_KEY=your_groq_api_key

SERP_API_KEY=your_tavily_api_key

AVIATIONSTACK_API_KEY=your_aviationstack_api_key

DATABASE_URL=postgresql://postgres:Subash%402512@localhost:5432/tarvelbuddy
Step 6: Get API Keys
Groq: https://console.groq.com
SERP: https://serpAPI.com
AviationStack: https://aviationstack.com
Setup AviationStack MCP Server (Local MCP Server)
Repository:

https://github.com/Pradumnasaraf/aviationstack-mcp

Open PowerShell:

E:

cd E:\Multi_agent_system_with_MCP
Clone repository:

git clone https://github.com/Pradumnasaraf/aviationstack-mcp.git

cd aviationstack-mcp
Install UV
Check:

uv --version
Install:

pip install uv
If installation fails:

powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
Create .env File
AVIATION_STACK_API_KEY=your_api_key_here
Install Dependencies
uv sync
This will:

Create .venv
Install dependencies
Install AviationStack MCP package
Activate Environment
.venv\Scripts\activate
Start MCP Server
uv run -m aviationstack_mcp mcp run
or

python -m aviationstack_mcp mcp run
The server will remain running and wait for MCP requests.

Stop Server
CTRL + C
Run:
main.py
Example Prompt
Plan a complete 7 days Japan trip including flights, hotels and sightseeing under 2 lakhs.
Features
Multi-Agent Architecture using LangGraph
PostgreSQL Memory
SerpAPI Search Integration
AviationStack MCP Integration
Real-Time Travel Planning
