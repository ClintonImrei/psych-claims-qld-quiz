import streamlit as st

# ---------------------------
# Quiz data
# ---------------------------

quiz = [
    {
        "question": "1. What is the legal definition of a psychological injury in QLD?",
        "options": [
            "Any stress experiencedat work",
            "A diagnosable psychological disorder arising out of employment",
            "Feeling overwhelmed while working",
            "Conflict with coworkers"
        ],
        "answer": 2,
        "explanation": "Only diagnosable psychological disorders caused by employment meet the definition of injury."
    },
    {
        "question": "2. Which of the following is typically considered 'management action'?",
        "options": [
            "Bullying by a coworker",
            "A performance review",
            "Client threatening behaviour",
            "A workplace accident"
        ],
        "answer": 2,
        "explanation": "Performance reviews are a classic example of management action under the Act."
    },
    {
        "question": "3. For a psychological injury to be accepted, employment must be:",
        "options": [
            "One possible factor",
            "A minor contributing factor",
            "The major significant contributing factor",
            "Completely unrelated"
        ],
        "answer": 3,
        "explanation": "Employment must be the major significant contributing factor to the disorder."
    },
    {
        "question": "4. Which scenario is MOST likely to be excluded?",
        "options": [
            "Worker traumatised after a robbery at work",
            "Worker distressed after being placed on a performance plan",
            "Worker traumatised after witnessing violence",
            "Worker diagnosed with PTSD after client assault"
        ],
        "answer": 2,
        "explanation": "Performance management is management action, and if reasonable, the claim is excluded."
    },
    {
        "question": "5. 'Taken in a reasonable way' refers to:",
        "options": [
            "Whether the worker agrees with the decision",
            "Whether management communicated and executed the action appropriately",
            "Whether HR approved it",
            "Whether the outcome was positive"
        ],
        "answer": 2,
        "explanation": "It refers to whether the action was implemented reasonably—not whether the worker liked it."
    },
    {
        "question": "6. Which of the following is NOT usually considered management action?",
        "options": [
            "Discipline",
            "Dismissal",
            "Counselling and support services",
            "A coworker prank gone wrong"
        ],
        "answer": 4,
        "explanation": "A coworker prank is not management action; it's interpersonal conflict."
    },
    {
        "question": "7. A worker reports long-term stress due to high workload with no managerial action involved. What is MOST relevant?",
        "options": [
            "Automatically excluded",
            "Injury test + causation assessment",
            "Management action assessment",
            "Not compensable"
        ],
        "answer": 2,
        "explanation": "High workload typically requires an injury + causation assessment, not management action analysis."
    },
    {
        "question": "8. A stress claim involving bullying by a coworker is:",
        "options": [
            "Automatically excluded",
            "Automatically accepted",
            "Accepted if evidence supports it and no exclusion applies",
            "Only accepted if management agrees"
        ],
        "answer": 3,
        "explanation": "Bullying by coworkers is not management action, so normal injury + causation tests apply."
    },
    {
        "question": "9. Which best represents 'causation'?",
        "options": [
            "The worker feels stress at work",
            "The workplace event contributed to the disorder",
            "The worker dislikes their job",
            "The worker cried during a meeting"
        ],
        "answer": 2,
        "explanation": "Causation is about whether employment contributed to the diagnosed disorder."
    },
    {
        "question": "10. A final liability decision must consider:",
        "options": [
            "The worker’s feelings",
            "Whether management action was reasonable",
            "Clinical evidence, causation, and exclusions",
            "Only employer statements"
        ],
        "answer": 3,
        "explanation": "All liability decisions must consider medical evidence, causation, and any applicable exclusions."
    }
]

# ---------------------------
# Streamlit app layout
# ---------------------------

st.set_page_config(page_title="QLD Psych Injury Claims Quiz", page_icon="🧠")

st.title("🧠 QLD Psychological Injury Claims Quiz")
st.write(
    """
This interactive quiz is designed to test general knowledge about psychological injury claims 
under the QLD workers’ compensation framework.

**Important:** This is an educational tool only and does not constitute legal advice or a liability decision.
"""
)

st.markdown("---")

st.subheader("📋 Questions")

# Render questions with radio buttons
for idx, q in enumerate(quiz):
    st.markdown(f"**{q['question']}**")
    st.radio(
        "Select your answer:",
        q["options"],
        key=f"q_{idx}",
        index=None  # no default selected
    )
    st.markdown("---")

# Submit button logic
if st.button("✅ Submit answers"):
    score = 0
    results = []

    for idx, q in enumerate(quiz):
        user_answer = st.session_state.get(f"q_{idx}")
        correct_answer_text = q["options"][q["answer"] - 1]

        if user_answer == correct_answer_text:
            score += 1
            results.append((q["question"], True, correct_answer_text, q["explanation"]))
        else:
            results.append((q["question"], False, correct_answer_text, q["explanation"]))

    st.subheader("📊 Results")
    st.write(f"Your score: **{score} / {len(quiz)}**")

    if score == 10:
        st.success("Outstanding! You clearly understand psychological injury claims.")
    elif score >= 7:
        st.success("Great job! You have a solid understanding.")
    elif score >= 4:
        st.info("Not bad — but you might benefit from a refresher.")
    else:
        st.warning("This is a complex area. Further study and guidance are recommended.")

    st.markdown("---")
    st.subheader("🔍 Question-by-question feedback")

    for question_text, is_correct, correct_answer_text, explanation in results:
        if is_correct:
            st.success(f"✅ {question_text}")
            st.write(f"**Correct answer:** {correct_answer_text}")
        else:
            st.error(f"❌ {question_text}")
            st.write(f"**Correct answer:** {correct_answer_text}")
        st.write(f"**Explanation:** {explanation}")
        st.markdown("---")

# Reset button
if st.button("🔄 Reset quiz"):
    for idx in range(len(quiz)):
        key = f"q_{idx}"
        if key in st.session_state:
            del st.session_state[key]
    st.experimental_rerun()
