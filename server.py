from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from groq import Groq
from database import DATABASE
import os
app = Flask(__name__)
CORS(app)
groq_api_key = os.getenv("GROQ_API_KEY")


if not groq_api_key:
   raise ValueError("GROQ_API_KEY not found. Please export it first.")


client = Groq(api_key=groq_api_key)
@app.route("/")
def home():
   return render_template("index.html")




# 🤖 AI Chat Endpoint
@app.route("/chat", methods=["POST"])
def chat():
   data = request.get_json()


   if not data or "message" not in data:
       return jsonify({"reply": "Invalid request"}), 400


   user_message = data["message"]


   try:
       response = client.chat.completions.create(
           model="llama-3.1-8b-instant", # Free & Fast Groq Model
           messages=[
               {
                   "role": "system",
                   "content": """
                   You are Nagrik Seva AI Assistant.
                   Help Indian citizens with:
                   - Income certificate
                   - Pension schemes
                   - Government bonds
                   - Bill payments
                   - Application tracking
                   - Civic services


                   Keep answers simple, clear and practical.
                   """
               },
               {"role": "user", "content": user_message}
           ],
           temperature=0.5,
           max_tokens=100
       )


       ai_reply = response.choices[0].message.content


       return jsonify({"reply": ai_reply})


   except Exception as e:
       return jsonify({"reply": f"AI Error: {str(e)}"}), 500
  
@app.route("/bonds")
def bonds():
   return jsonify(DATABASE)  




# ─────────────────────────────────────────────
# Run Server
# ─────────────────────────────────────────────


if __name__ == "__main__":
   app.run(debug=True, port=8000)
