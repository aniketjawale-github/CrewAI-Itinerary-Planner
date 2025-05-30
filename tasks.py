from crewai import Task, Crew
from agents import research_agent, hotel_agent, planner_agent, budget_agent

def create_crew(start_location, destination, days, interests, budget):
    research_task = Task(
        description=(
            f"Suggest 3 must-visit places or food experiences in {destination} for interests: {interests}.\n"
            f"For each, include: name, 1-line summary, 2-line description, location, and cost (if any)."
        ),
        agent=research_agent,
        expected_output="List of 3 concise recommendations, each under 80 words.",
        name="Research"
    )

    hotel_task = Task(
        description=(
            f"Suggest 2 hotel options in {destination} for a {days}-day stay under ₹{budget}.\n"
            f"Include: name, type (budget/mid), location, price per night, total cost, and food availability."
        ),
        agent=hotel_agent,
        expected_output="2 hotel options with compact details under 150 words total.",
        name="Hotel"
    )

    budget_task = Task(
        description=(
            f"Estimate cost for a {days}-day trip from {start_location} to {destination} with interests: {interests}.\n"
            f"Include: flight, hotel (budget & mid), food/day, 3 activities, transport. Warn if above ₹{budget}."
        ),
        agent=budget_agent,
        context=[research_task, hotel_task],
        expected_output="Brief bullet-point cost estimate with total and warning if over budget.",
        name="Budget"
    )

    plan_task = Task(
        description=(
            f"Create a {days}-day itinerary for {destination} with hotel check-in/out, morning-afternoon-evening plans, dining spots, and timing.\n"
            f"Ensure it's under ₹{budget} and aligned with interests: {interests}."
        ),
        agent=planner_agent,
        context=[research_task, hotel_task, budget_task],
        expected_output="Daily schedule with hotel and activity details in ~200 words max.",
        name="Planner"
    )

    crew = Crew(
        agents=[research_agent, hotel_agent, budget_agent, planner_agent],
        tasks=[research_task, hotel_task, budget_task, plan_task],
        verbose=True,
        sequential=True
    )

    # 🟢 Return crew and task names for UI mapping
    return crew, ["Research", "Hotel", "Budget", "Planner"]
