# ✈️ AI Multi-Agent Travel Planner + MCP

An AI-powered **multi-agent travel planning system** built with **LangGraph, Groq, MCP, SerpAPI, AviationStack, and PostgreSQL**.

This project is an extended version of my previous **Multi-Agent Travel Planning System**, where MCP is integrated to provide external travel data such as **flight, airport, airline, and hotel information**.

## 🔗 Part 1

Original project:

https://github.com/Subashji2512/Travel_Agency

---

## 🚀 What This Project Does

The user simply provides a travel request, for example:

> **"Plan a 7-day Japan trip from Chennai including flights, hotels and sightseeing under 2 lakhs."**

The system then:

1. Gets flight and airport information.
2. Searches for hotels.
3. Creates a complete itinerary.
4. Generates the final travel plan.

---

## 🧠 How It Works

The system uses **LangGraph** to manage multiple specialized agents.

```text
                         👤 User
                           │
                           ▼
                    ┌──────────────┐
                    │  LangGraph   │
                    └──────┬───────┘
                           │
              ┌────────────┴────────────┐
              │                         │
              ▼                         ▼
      ✈️ Flight Agent             🏨 Hotel Agent
              │                         │
              ▼                         ▼
     AviationStack MCP             Serp MCP
              │                         │
              └────────────┬────────────┘
                           │
                           ▼
                  🗓️ Itinerary Agent
                           │
                           ▼
                    🤖 Final Agent
                           │
                           ▼
                    ✈️ Travel Plan
```

### Agent Flow

**Flight Agent** and **Hotel Agent** work independently and can run in parallel.

* ✈️ **Flight Agent** → gets airport and airline information using AviationStack MCP.
* 🏨 **Hotel Agent** → searches for hotels using Serp MCP.
* 🗓️ **Itinerary Agent** → combines flight + hotel information and creates the itinerary.
* 🤖 **Final Agent** → generates the final response for the user.

---

# 🔌 MCP Integration

This project uses **Model Context Protocol (MCP)** to connect the AI agents with external tools.

Instead of directly writing API logic inside every agent, the application communicates with MCP servers through an MCP client.

### AviationStack MCP

Used for aviation-related information:

* ✈️ Airports
* 🛫 Airlines
* 🛬 Flight information

Example tools:

```text
list_airports
list_airlines
```

### Serp MCP

Used for searching travel information such as:

* 🏨 Hotels
* 📍 Destinations
* 🔎 Travel information

---

# 🛠️ Technologies Used

| Technology    | Purpose                   |
| ------------- | ------------------------- |
| Python        | Main programming language |
| LangGraph     | Multi-agent workflow      |
| Groq          | LLM                       |
| MCP           | External tool integration |
| AviationStack | Aviation information      |
| SerpAPI       | Travel and hotel search   |
| PostgreSQL    | Persistent memory         |
| Psycopg       | PostgreSQL connection     |
| AsyncIO       | Asynchronous MCP calls    |
| python-dotenv | Environment variables     |

---

# 📂 Project Structure

```text
Travel_Agency_with_MCP/
│
├── main.py
├── mcp_client.py
├── test_local_mcp.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── ...
```

### Main Files

**`main.py`**

Contains:

* LangGraph workflow
* Flight Agent
* Hotel Agent
* Itinerary Agent
* Final Agent
* PostgreSQL checkpointing

**`mcp_client.py`**

Contains the MCP client functions used to communicate with the external MCP servers.

---

# ⚙️ Setup

## 1. Clone the Repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd Travel_Agency_with_MCP
```

---

## 2. Create Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🗄️ PostgreSQL Setup

Install PostgreSQL and create a database:

```sql
CREATE DATABASE langgraph_memory;
```

The database is used by LangGraph to store persistent checkpoints.

---

# 🔐 Environment Variables

Create a `.env` file in the project directory:

```env
GROQ_API_KEY=your_groq_api_key
SERP_API_KEY=your_serp_api_key
AVIATIONSTACK_API_KEY=your_aviationstack_api_key

DATABASE_URL=postgresql://postgres:your_password@localhost:5432/langgraph_memory
```

### ⚠️ Important

Never upload your `.env` file to GitHub.

Add this to `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
*.pyc
```

---

# ✈️ AviationStack MCP Setup

Clone the AviationStack MCP server:

```bash
git clone https://github.com/Pradumnasaraf/aviationstack-mcp.git
```

Go inside the server:

```bash
cd aviationstack-mcp
```

### Install UV

Check:

```bash
uv --version
```

If `uv` is not installed:

```bash
pip install uv
```

Or on Windows:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Install MCP Dependencies

```bash
uv sync
```

### Configure AviationStack

Create a `.env` file inside the MCP server:

```env
AVIATION_STACK_API_KEY=your_aviationstack_api_key
```

### Start the MCP Server

```bash
uv run -m aviationstack_mcp mcp run
```

Keep this terminal running.

---

# ▶️ Run the Project

Open another terminal and activate the main project's environment:

```powershell
.venv\Scripts\activate
```

Run:

```bash
python main.py
```

You will see:

```text
Enter travel request:
```

Enter your travel requirements.

---

# 💬 Example

```text
Enter travel request:

Plan a 7 day Japan trip from Chennai including
flights, hotels and sightseeing under 2 lakhs.
```

The agents will process the request and generate a complete travel plan.

---

# 🗄️ PostgreSQL Memory

The project uses **LangGraph + PostgreSQL** for persistent state.

The workflow uses:

```text
User Request
     ↓
LangGraph State
     ↓
PostgreSQL Checkpoint
```

A `thread_id` is used to identify a conversation and maintain its state.

---

# ⭐ Key Features

* 🤖 Multi-Agent AI architecture
* 🔀 Parallel Flight and Hotel agents
* ✈️ AviationStack MCP integration
* 🏨 Serp MCP integration
* 🧠 Groq LLM
* 🗓️ AI-generated travel itinerary
* 🗄️ PostgreSQL persistent memory
* ⚡ Asynchronous MCP tool calls
* 🔌 Modular MCP client architecture

---


---

# 🔮 Future Improvements

* 🌦️ Weather MCP integration
* 🗺️ Maps MCP integration
* 💱 Currency conversion
* 🏨 Dedicated hotel APIs
* 🎫 Flight/hotel booking
* 💰 Automatic budget optimization
* 🌐 Streamlit web interface
* 🐳 Docker deployment
* 📱 Mobile application

---

# 👨‍💻 Author

**Subashji N**

AI / Machine Learning Engineer

**Skills:** Python • LangGraph • MCP • Generative AI • RAG • Machine Learning

---

⭐ If you found this project useful, consider giving the repository a star!
