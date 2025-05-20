import openai
import streamlit as st

def generate_therapeutic_summary(name, age, region, sector, score):
    openai.api_key = st.secrets["OPENAI_API_KEY"]

    prompt = (
        f"{name} is {age} years old, lives in {region}, and works in {sector}. "
        f"Their climate anxiety score is {score}/100. Write a short and emotionally intelligent reflection (3-5 sentences) "
        f"as if written by a calm, compassionate therapist. Use affirming and emotionally supportive language."
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # or "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": "You are a kind and emotionally intelligent therapist."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8,
            max_tokens=150
        )

        return response.choices[0].message["content"]

    except Exception as e:
        return f"Error generating summary: {str(e)}"
