import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="Anatomy AI Tutor")

st.title("Anatomy AI Tutor")
st.write("Ask about: Heart, Brain, Lungs, Liver, Kidneys")

SYSTEM_PROMPT = """
You are an educational anatomy tutor.

You are ONLY allowed to answer questions about:
- Heart
- Brain
- Lungs
- Liver
- Kidneys

If asked about anything else, politely say:
"This question is outside the current project scope."

Do not provide medical diagnosis.
Educational explanations only.
"""

user_input = st.text_input("Ask your question:")

if user_input:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ]
    )

    st.write("### AI Response:")
    st.write(response.choices[0].message.content)

