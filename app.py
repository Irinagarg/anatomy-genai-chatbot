import streamlit as st

st.set_page_config(page_title="Anatomy AI Tutor")

st.title("🧠 Anatomy AI Tutor")
st.write("Ask about: Heart, Brain, Lungs, Liver, Kidneys")

question = st.text_input("Ask your question:")

def anatomy_response(user_input):
    user_input = user_input.lower()

    if "heart" in user_input:
        return """
        ❤️ HEART:
        The heart is a muscular organ that pumps blood throughout the body.
        
        • Location: Thoracic cavity
        • Chambers: 4 (Right/Left Atrium, Right/Left Ventricle)
        • Function: Circulates oxygenated & deoxygenated blood
        • Major vessels: Aorta, Pulmonary artery, Vena cava
        """

    elif "brain" in user_input:
        return """
        🧠 BRAIN:
        The brain is the control center of the nervous system.
        
        • Parts: Cerebrum, Cerebellum, Brainstem
        • Function: Controls thoughts, memory, movement
        • Protected by: Skull & cerebrospinal fluid
        """

    elif "lungs" in user_input:
        return """
        🫁 LUNGS:
        The lungs are responsible for gas exchange.
        
        • Function: Oxygen in, Carbon dioxide out
        • Structure: Bronchi → Bronchioles → Alveoli
        • Location: Thoracic cavity
        """

    elif "liver" in user_input:
        return """
        🧬 LIVER:
        The liver is the largest internal organ.
        
        • Function: Detoxification, metabolism, bile production
        • Location: Upper right abdomen
        • Important role in digestion
        """

    elif "kidney" in user_input or "kidneys" in user_input:
        return """
        🩺 KIDNEYS:
        The kidneys filter blood and produce urine.
        
        • Function: Remove waste, balance fluids
        • Structure: Nephron (functional unit)
        • Location: Retroperitoneal area
        """

    else:
        return "Please ask about Heart, Brain, Lungs, Liver, or Kidneys."

if question:
    answer = anatomy_response(question)
    st.success(answer)
