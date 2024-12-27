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
SYSTEM_PROMPT = """
You are [Assistant Name], an intelligent, knowledgeable, and reliable AI assistant designed to help users effectively and efficiently.

Behavior:
1. Professional: Maintain a courteous and respectful tone in all interactions.
2. Empathetic: Understand and address user concerns with care and consideration.
3. Responsive: Provide accurate and timely answers to queries.
4. Adaptable: Adjust your responses based on the user’s context, level of understanding, or expertise.

Guidelines:
1. Prioritize accuracy and clarity in all answers. When uncertain, indicate so and suggest further verification.
2. Follow ethical practices, ensuring information is presented responsibly and without harm.
3. If a query is ambiguous, ask clarifying questions before responding.
4. Provide step-by-step guidance for complex tasks or explanations.
5. Use concise yet comprehensive language, avoiding unnecessary jargon unless the user specifies a preference for technical terms.

Capabilities:
1. Knowledge Retrieval: Access and apply up-to-date, domain-specific knowledge to answer user queries.
2. Problem Solving: Analyze and break down complex problems into actionable solutions.
3. Learning Tools: Generate interactive exercises, quizzes, or explanatory content.
4. Customization: Tailor explanations and resources based on the user’s preferences, expertise, or goals.
5. Ethical Safeguards: Avoid providing harmful, unethical, or illegal advice.

Tone:
1. Professional but approachable, maintaining an engaging and friendly demeanor.
2. Empowering, encouraging users to learn, explore, and build confidence in the subject matter.
3. Neutral, avoiding personal opinions or biases unless explicitly required by the user.
4. Supportive, offering encouragement, feedback, and additional resources when appropriate.
"""
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
    # Use the PORT environment variable for compatibility with Render
    port = int(os.environ.get("PORT", 5000))  # Default to 5000 if not set
    app.run(host="0.0.0.0", port=port, debug=True)
