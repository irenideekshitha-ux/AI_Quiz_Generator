import streamlit as st
from quiz_generator import generate_quiz

st.title("AI Quiz Generator")

topic = st.text_input("Enter the quiz topic (Python, Java, AI)")

num = st.number_input(
    "Enter the number of questions",
    min_value=1,
    max_value=20,
    value=1
)

if st.button("Generate Quiz"):

    quiz = generate_quiz(topic, num)

    st.subheader("Generated Quiz")

    for i, q in enumerate(quiz, 1):
        st.write(f"Q{i}. {q['question']}")

        for option in q["options"]:
            st.write(f"- {option}")

        st.write(f"Answer: {q['answer']}")
        st.write("---")