from tasks import create_crew

def main():
    start_location = input("What is your starting location? ")
    destination = input("Where are you going? ")
    days = int(input("How many days? "))
    interests = input("What are your interests (e.g., museums, hiking, food)? ")
    budget = input("What is your approximate budget (e.g., 45000)? ")

    # Create the full crew with tasks and agents
    crew = create_crew(start_location, destination, days, interests, budget)

    print("\n📡 Live Travel Plan Updates\n")
    
    try:
        results = crew.kickoff()  # Run directly to show live logs
    except Exception as e:
        print(f"❌ Error while running Crew: {e}")
        return

    for task, result in results.items():
        print(f"\n✅ {task.agent.role} finished:\n")
        print(result)
        print("\n" + "-" * 50)

if __name__ == "__main__":
    main()
