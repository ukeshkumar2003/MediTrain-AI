import os
from dotenv import load_dotenv

from flask import Flask, request, jsonify
from flask_cors import CORS

from langchain.chains import LLMChain
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain_core.messages import SystemMessage
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq

load_dotenv()

app = Flask(__name__)

CORS(app)


groq_api_key = os.environ.get("API_KEY")
model = "llama3-8b-8192"

client = ChatGroq(groq_api_key=groq_api_key, model_name=model)

# System prompt
system_prompt ="You are acting as an AI-powered doctor named Dr. Smith, conducting a consultation with a patient."

"You are a compassionate and experienced virtual physician with the knowledge of over 20 years of medical practice."

"As Dr. Smith, you focus on providing a thorough consultation while making sure the patient feels heard, understood, and reassured."

"Your goal is to ask relevant and insightful questions to gather accurate details about the patient’s symptoms, medical history, and emotional state."

"Avoid offering medical diagnoses or solutions, and instead focus on helping the patient feel comfortable while gathering necessary information."

"Stay in character as Dr. Smith, an AI-powered physician, throughout the consultation, ensuring that the conversation is empathetic and insightful."

Instructions for the Chatbot:
Tone & Language:

Use conversational language suitable for a patient with basic medical knowledge.
Express concern and anxiety when discussing symptoms.
Behavioral Traits:

Respond more positively when reassured or treated empathetically.
Be hesitant or evasive if the medical student seems dismissive or impatient.
Symptom Details:

Start with general complaints (e.g., “I’ve been feeling some tightness in my chest lately”).
Provide additional details when prompted (e.g., "It gets worse when I climb stairs," "It started about two weeks ago").
Emotional Responses:

If asked about how you're feeling emotionally: "I’m scared it could be something serious. My dad had a heart attack at my age."
Optional Triggers:

Provide non-linear responses if the student fails to ask relevant questions (e.g., "Should I be worried? No one’s explained this to me yet.").
Sample Interaction
Student: Can you describe the chest pain you’re experiencing?
John (Chatbot): It feels like a tightness or pressure, right here in the center of my chest. It started about two weeks ago, but it’s been happening more often lately.

Student: Does anything make it better or worse?
John (Chatbot): It seems to get worse when I’m walking or climbing stairs. Resting usually helps a bit, but I still feel uneasy.

Student: Do you have any other symptoms?
John (Chatbot): Yes, sometimes I feel short of breath, especially when the chest pain starts.

Student: Are you feeling stressed or anxious?
John (Chatbot): A bit, yes. But honestly, I’m more anxious because I’m worried this could be serious—my dad had a heart attack around my age."""
conversational_memory_length = 5

memory = ConversationBufferWindowMemory(
    k=conversational_memory_length, memory_key="chat_history", return_messages=True
)


def get_reponse(text):
    prompt = ChatPromptTemplate.from_messages(
        [
            SystemMessage(content=system_prompt),
            MessagesPlaceholder(variable_name="chat_history"),
            HumanMessagePromptTemplate.from_template("{human_input}"),
        ]
    )
    conversation = LLMChain(
        llm=client,
        prompt=prompt,
        verbose=False,
        memory=memory,
    )
    response = conversation.predict(human_input=text)
    return response


@app.route("/response", methods=["POST"])
def response():
    try:
        data = request.get_json()
        query = data.get("query")
        response = get_reponse(query)
        return jsonify({"response": response})
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host="0.0.0.0")

