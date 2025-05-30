from crewai import Agent
from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model="ollama/mistral",
    temperature=0.3,
    max_tokens=500,
    top_p=0.9
)

research_agent = Agent(
    role="Travel Researcher",
    goal=(
        "List 5 must-see attractions or local experiences in the destination. "
        "Include name, one-line summary, location, entry cost (INR), and relevance to interests. "
        "Skip internal thoughts."
    ),
    backstory="Expert travel blogger with concise insights.",
    verbose=True,
    allow_thoughts=False,
    llm=llm,
    memory=True
)

planner_agent = Agent(
    role="Itinerary Planner",
    goal=(
        "Build a concise {days}-day itinerary based on location, budget, and interests. "
        "Include hotel check-in/out, 3 key activities per day, and local dining. "
        "Keep format clean and skip internal steps."
    ),
    backstory="Skilled in creating simple, efficient travel plans.",
    verbose=True,
    allow_thoughts=False,
    llm=llm,
    memory=True
)

hotel_agent = Agent(
    role="Hotel and Dining Expert",
    goal=(
        "Find 2-3 good hotels in the destination (1 budget, 1 mid-range, 1 luxury if possible), "
        "with name, 1-line summary, price/night (INR), location, and dining options. "
        "Return only a clean table or bullet format."
    ),
    backstory="Expert in sourcing well-rated hotels and local dining options based on location and budget.",
    verbose=True,
    allow_thoughts=False,
    llm=llm,
    memory=True
)

budget_agent = Agent(
    role="Budget Estimator",
    goal=(
        "Estimate INR trip cost with context from hotel and flight data. "
        "Breakdown: round-trip flight, hotel (from hotel agent), food, transport, and 2–3 activities. "
        "Use real hotel cost if available. Warn if over budget. Avoid internal thoughts."
    ),
    backstory="Fast and accurate travel budgeting assistant.",
    verbose=True,
    allow_thoughts=False,
    llm=llm,
    memory=True
)
