# 🧠✈️ AI Travel Itinerary Planner (CrewAI + Streamlit)

A smart, AI-powered travel assistant that **automatically generates personalized travel itineraries** based on your **destination**, **budget**, and **interests**.  
Built using [CrewAI](https://github.com/joaomdmoura/crewAI) for multi-agent orchestration and [Streamlit](https://streamlit.io/) for a user-friendly interface.

---

## 🚀 Features

- ✅ **Tailored Travel Plans** – Custom itineraries based on user preferences  
- ✅ **Multi-Agent System** – Collaboration between 4 specialized AI agents:
  - 🧭 **Travel Researcher** – Discovers top attractions and experiences
  - 🏨 **Hotel Expert** – Recommends accommodations based on budget
  - 💰 **Budget Estimator** – Calculates total estimated trip costs
  - 📅 **Itinerary Planner** – Organizes your trip into a daily schedule
- ✅ **Budget Sensitivity** – Warns if your plan exceeds your limit  
- ✅ **Parallel Processing** – Agents operate in parallel for faster response  
- ✅ **Streamlit UI** – Interactive and intuitive web interface

---

## 🧩 Prerequisites

Make sure the following are installed on your system:

- Python 3.8 or higher  
- [Ollama](https://ollama.com/) (Local LLM runtime)  
- Mistral model (downloaded via Ollama)  
- `pip` package manager  

---

## 🛠️ Installation

1. Clone the Repository

```
git clone https://github.com/yourusername/ai-travel-planner.git
cd ai-travel-planner
```
2. Install Required Packages

```
pip install -r requirements.txt
```
If requirements.txt is not available, install dependencies manually:
```
pip install crewai streamlit langchain-ollama duckduckgo-search
```
3. Set Up Ollama and Mistral Model
Start the Ollama server:
```
ollama serve &
```
Download the Mistral model:

```
ollama pull mistral
```

## ▶️ Run the Application
Launch the Streamlit app:
```
streamlit run webapp.py
Open your browser and navigate to: http://localhost:8501
```

## 📝 How to Use
📍 Start Location – Enter the city you're traveling from

🗺️ Destination – Where you want to go

📆 Number of Days – Trip duration

💸 Budget – Total travel budget (in INR)

💡 Interests – Select your interests (e.g., Food, Culture, Nature)

Click "Generate Itinerary" and the AI agents will build a complete plan!

## 📁 Project Structure
```
├── agents.py          # Defines CrewAI agents and roles
├── tasks.py           # Agent task definitions and orchestration
├── webapp.py          # Streamlit UI logic
├── requirements.txt   # Required Python packages
└── README.md          # Project documentation
```

## ⚙️ Configuration Options
Customize your AI planner inside agents.py:

🔁 Model Settings – Change LLM model name (default is mistral)

🔥 LLM Parameters – Modify temperature, top_p, etc.

🧠 Agent Roles – Customize or add new expert agents

🛠️ Tools – Integrate external APIs or search tools

## 🧰 Troubleshooting
```
Problem	Solution
ModuleNotFoundError: crewai	pip install --upgrade crewai
Ollama not running	Run ollama serve &
Mistral model missing	Run ollama pull mistral
Streamlit not responding	Ensure you're using streamlit run
```

## 🙌 Acknowledgements

- [CrewAI](https://github.com/joaomdmoura/crewAI) – Multi-agent orchestration framework  
- [Ollama](https://ollama.com/) – Lightweight LLM runtime for local models  
- [Streamlit](https://streamlit.io/) – UI framework for building ML & data apps  
- The amazing [open-source Python community](https://www.python.org/psf/community/) 💙


## 📬 Contact

**Aniket Jawale**  
🔗 [GitHub](https://github.com/aniketjawale-github)  
🔗 [LinkedIn](https://www.linkedin.com/in/aniketjawalee/)  
📧 aniketajawale@gmail.com  
