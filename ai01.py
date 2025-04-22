import streamlit as st
import pandas as pd
import random
from gtts import gTTS
import os
import uuid
from datetime import datetime

# Mood-based suggestions
mood_workouts = {
    "Happy": "HIIT Workout + Protein-rich meal",
    "Sad": "Yoga + Comfort food (healthy version)",
    "Stressed": "Meditation + Light cardio",
    "Anxious": "Stretching + Herbal tea"
}

motivations = [
    "You're stronger than your excuses!",
    "Each step counts — keep going!",
    "Your energy is your superpower!",
    "Cheat days don't mean defeat days. Get back stronger!"
]

# Streamlit UI
st.set_page_config(page_title="AWAKEO AI Assistant", layout="centered")
st.title("🧠 AWAKEO - Your AI Fitness Buddy")

st.subheader("Enter Your Daily Inputs")
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
age = st.number_input("Age", 10, 100)
height = st.number_input("Height (in cm)", 100, 250)
weight = st.number_input("Weight (in kg)", 30, 200)
health_condition = st.selectbox("Health Condition", ["Healthy", "Diabetic", "Hypertensive", "Obese"])
mood = st.selectbox("How do you feel today?", list(mood_workouts.keys()))
sleep_hours = st.slider("Sleep (in hours)", 0.0, 12.0, step=0.5)
water_intake = st.slider("Water Intake (litres)", 0.0, 5.0, step=0.1)
steps = st.number_input("Steps Today", 0, 50000)
food_input = st.text_area("What did you eat today?")

if st.button("Get Suggestions"):
    st.markdown(f"### Workout & Diet Plan Recommendation for **{mood}**")
    st.success(mood_workouts[mood])

    score = int((steps / 10000) * 30 + sleep_hours * 5 + water_intake * 5)
    st.markdown(f"### Your AWAKEO Health Score: `{min(score, 100)}`")

    # Voice Note Generation
    msg = random.choice(motivations)
    tts = gTTS(msg)

    # Save the file with a unique name to avoid streamlit caching issues
    filename = f"motivation_{uuid.uuid4().hex}.mp3"
    tts.save(filename)

    # Stream audio file
    st.audio(filename, format="audio/mp3")
    st.success(f"💬 AI Motivation: {msg}")
