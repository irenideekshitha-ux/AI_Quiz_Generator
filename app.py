
import streamlit as st
from quiz_generator import generate_quiz

st.set_page_config(
    page_title="AI Quiz Generator",
    page_icon="📝",
    layout="centered"
)

st.title("📝 AI Quiz Generator")
st.write("Generate quiz questions based on your selected topic.")

topic = st.selectbox(
    "Select the quiz topic",
    ["Python", "Java", "AI"]
)

num = st.number_input(
    "Enter the number of questions",
    min_value=1,
    max_value=30,
    value=5,
    step=1
)

if st.button("Generate Quiz"):
    quiz = generate_quiz(topic, int(num))

    if quiz:
        st.subheader("Generated Quiz")

        for i, q in enumerate(quiz, 1):
            st.markdown(f"**Q{i}. {q['question']}**")

            for option in q["options"]:
                st.write(f"- {option}")

            with st.expander(f"View Answer {i}"):
                st.success(f"Correct Answer: {q['answer']}")

            st.divider()

        st.success(
            f"Quiz generated successfully: {len(quiz)} questions!"
        )

    else:
        st.warning(
            "No questions available for this topic. "
            "Please check your question bank."
        )
