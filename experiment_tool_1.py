import streamlit as st
import pandas as pd
import time
from datetime import datetime
import os
import re

# -------------------------------
# SESSION STATE INITIALIZATION
# -------------------------------
if "initialized" not in st.session_state:
    st.session_state.initialized = True
    st.session_state.start_time = time.time()
    st.session_state.data = {}
    st.session_state.step = "baseline"

# -------------------------------
# SAVE FUNCTION
# -------------------------------
def save_data(data_dict):
    os.makedirs("data", exist_ok=True)
    df = pd.DataFrame([data_dict])
    df.to_csv(
        f"data/research_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
        index=False
    )

# -------------------------------
# STEP 1: CREATIVITY (60 SECONDS)
# -------------------------------
if st.session_state.step == "baseline":
    st.title("Task 1: Brainstorming")

    st.write(
        "List as many **creative uses for a Brick** as possible.\n\n"
        "⏱️ You have **60 seconds**. This task will automatically advance when time is up."
    )

    creative_input = st.text_area("Your ideas:", height=200)

    elapsed = time.time() - st.session_state.start_time
    remaining = max(0, 60 - int(elapsed))

    st.write(f"⏳ Time remaining: **{remaining} seconds**")

    if remaining == 0:
        st.session_state.data["baseline_creativity"] = creative_input
        st.session_state.step = "main_task"
        st.session_state.start_time = time.time()
        st.rerun()

# -------------------------------
# STEP 2: DECISION TASK
# -------------------------------
elif st.session_state.step == "main_task":
    st.title("Task 2: Arctic Colony Planning")

    st.info("🔐 PROTOCOL CODE: **ALFA‑99** — Remember this for later.")

    col1, col2 = st.columns(2)

    # -------- LEFT COLUMN --------
    with col1:
        st.subheader("Your Plan")
        st.write(
            "You are managing the **water supply** of a small Arctic research colony.\n\n"
            "Explain **how you would manage the water** and "
            "**how long you believe the supply will last**, based on the information available."
        )
        plan = st.text_area(
            "Write your plan here:",
            height=300
        )

    # -------- RIGHT COLUMN --------
    with col2:
        st.subheader("Resource Assistant")

        group = st.radio(
            "Experimental Group (Internal Only)",
            ["Control", "Treatment"]
        )

        if group == "Treatment":
            st.write("🤖 **AI Assistant Active**")
            query = st.text_input("Ask the AI for data or calculations:")

            if query:
                if re.search(r"\d", query):
                    st.warning(
                        "AI Assistant Analysis:\n\n"
                        "• Total water: 1,000 liters\n"
                        "• Daily usage: 150 liters/day\n\n"
                        "Conclusion: The water supply will last approximately 10 days."
                    )
                else:
                    st.write("AI: Please include numerical values in your question.")

        else:
            st.write("📚 **Static Database Active**")
            st.text(
                "Reference Data:\n"
                "• Total water: 1,000 liters\n"
                "• Daily consumption: 150 liters/day"
            )

    if st.button("Finalize Plan"):
        st.session_state.data["final_plan"] = plan
        st.session_state.step = "post_test"
        st.rerun()

# -------------------------------
# STEP 3: MEMORY & DECISION PROBE
# -------------------------------
elif st.session_state.step == "post_test":
    st.title("Final Assessment")

    mem_q = st.text_input(
        "1. What was the PROTOCOL CODE mentioned earlier?"
    )

    logic_q = st.number_input(
        "2. How many days did you conclude the water would last?",
        min_value=0,
        step=1
    )

    if st.button("Complete Research"):
        st.session_state.data.update({
            "memory_answer": mem_q,
            "logic_answer": logic_q
        })
        save_data(st.session_state.data)
        st.success("✅ Thank you! Your responses have been saved.")