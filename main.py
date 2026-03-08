from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

BOT_TOKEN = "ВАШ_BOT_TOKEN"
CHAT_ID = "-1003866882588"

@app.route('/send_anketa', methods=['POST'])
def send_anketa():
    name = request.form.get('name')
    contact = request.form.get('contact')
    about = request.form.get('about')
    phone = request.form.get('phone')

    text = f"""
🏎 Нова анкета F1

👤 Ім'я: {name}
📱 Контакт: {contact}
📞 Телефон: {phone}

📝 Про себе:
{about}
"""

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": text
    })

    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)