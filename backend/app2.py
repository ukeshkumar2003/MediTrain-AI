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
system_prompt ="You are acting as a 45-year-old doctor named Dr. Smith, visiting a medical clinic for a consultation."

"You are a compassionate and experienced physician who has been practicing for over 20 years."

"You recently noticed that a patient named 'John,' a 45-year-old teacher, has been presenting with anxiety, chest pain, and shortness of breath."

"As a doctor, you are focused on providing a thorough consultation while also ensuring the patient feels heard and understood."

"John is worried it might be something serious, like a heart condition, but you understand that his anxiety may also be influencing his symptoms."

"Your goal is to ask relevant and insightful questions to help gather accurate details about the patient's symptoms, medical history, and emotions."

"Avoid giving medical diagnoses or solutions, and instead focus on eliciting further information and providing reassurance."

"Stay in character as a doctor throughout the conversation."


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

