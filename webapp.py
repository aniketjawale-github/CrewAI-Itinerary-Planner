import time
import streamlit as st
import asyncio
from tasks import create_crew

st.set_page_config(page_title="AI Travel Itinerary Planner", layout="wide")
st.title("✈️ AI Travel Itinerary Planner (CrewAI + Streamlit)")

# User Input Form
with st.form("trip_form"):
    col1, col2 = st.columns(2)
    with col1:
        start_location = st.text_input("Start Location (e.g., Mumbai)")
        days = st.number_input("Number of Days", min_value=1, value=3)
    with col2:
        destination = st.text_input("Destination (e.g., Manali)")
        budget = st.text_input("Budget (e.g., 45000)")

    interests = st.text_input("Interests (e.g., Food, Culture, Nature)")
    submit = st.form_submit_button("🚀 Generate Itinerary")

# Initialize session state
if "task_results" not in st.session_state:
    st.session_state.task_results = {}
if "timings" not in st.session_state:
    st.session_state.timings = {}

# Async function to run agents and update Streamlit UI
async def run_crew_and_update(crew, task_names, placeholders):
    overall_start = time.perf_counter()

    try:
        await asyncio.to_thread(crew.kickoff)
    except Exception as e:
        st.error(f"❌ Error while running Crew: {e}")
        return

    for task in crew.tasks:
        start = time.perf_counter()
        task_name = task.name
        placeholders[task_name].markdown("⏳ Generating output...")
        time.sleep(0.5)

        # ✅ THIS is the correct way to get actual unique result
        output = task.output or f"⚠️ No output received from {task_name}."
        st.session_state.task_results[task_name] = output

        end = time.perf_counter()
        st.session_state.timings[task_name] = f"{end - start:.2f} sec"

        placeholders[task_name].markdown(f"### ✅ {task_name} Output\n\n{output}\n---")

    total_time = time.perf_counter() - overall_start
    mm, ss = divmod(int(total_time), 60)
    st.success(f"✅ All agents completed in ⏱ {mm:02d}:{ss:02d}")

# On form submit
if submit:
    st.session_state.task_results = {}
    st.session_state.timings = {}

    crew, task_names = create_crew(start_location, destination, days, interests, budget)

    # Forcefully define expected task names if needed
    task_names = ["Research", "Hotel", "Budget", "Planner"]

    placeholders = {name: st.empty() for name in task_names}
    asyncio.run(run_crew_and_update(crew, task_names, placeholders))

# Final itinerary summary
if st.session_state.task_results:
    st.subheader("📋 Final Itinerary Summary")
    full_text = ""
    for task, output in st.session_state.task_results.items():
        time_taken = st.session_state.timings.get(task, "--")
        full_text += f"### {task} (⏱ {time_taken})\n{output}\n\n"
    st.text_area("Complete Itinerary", value=full_text.strip(), height=400)
