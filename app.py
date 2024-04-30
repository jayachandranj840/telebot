from flask import Flask, request, Response
import requests

TOKEN =  "YOUR BOT TOKEN"
app = Flask(__name__)

# Initialize a dictionary to store user data
user_data = {}

def parse_message(message):
    chat_id = message['message']['chat']['id']
    text = message['message']['text']
    return chat_id, text

def tel_send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': text
    }

    r = requests.post(url, json=payload)
    return r

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = request.get_json()

        chat_id, text = parse_message(msg)

        if text == "/start":
            tel_send_message(chat_id, "Grade points according to Grade\n"
                                     "1. 'O'-->10\n"
                                     "2. 'A+'-->9\n"
                                     "3. 'A'-->8\n"
                                     "4. 'B+'-->7\n"
                                     "4. 'B'-->6\n"
                                     "5. 'C'-->5")
            tel_send_message(chat_id, "Enter the number of subjects:")
            # Initialize user data
            user_data[chat_id] = {
                'num_subjects': 0,
                'grades': [],
                'credits': [],
                'step': 'grade'
            }
        else:
            # Check if the user is in the GPA calculation process
            if chat_id in user_data:
                user_info = user_data[chat_id]
                if user_info['num_subjects'] == 0:
                    try:
                        num_subjects = int(text)
                        if num_subjects > 0:
                            user_info['num_subjects'] = num_subjects
                            tel_send_message(chat_id, "Enter the Grade point of subject 1:")
                        else:
                            tel_send_message(chat_id, "Please enter a valid number of subjects.")
                    except ValueError:
                        tel_send_message(chat_id, "Please enter a valid number of subjects.")
                else:
                    if user_info['step'] == 'grade':
                        try:
                            grade_point = float(text)
                            user_info['grades'].append(grade_point)
                            subject_number = len(user_info['grades'])
                            user_info['step'] = 'credit'
                            tel_send_message(chat_id, f"Enter the credit point of subject {subject_number}:")
                        except ValueError:
                            tel_send_message(chat_id, "Please enter a valid grade point.")
                    elif user_info['step'] == 'credit':
                        try:
                            credit_point = float(text)
                            user_info['credits'].append(credit_point)
                            subject_number = len(user_info['credits'])
                            user_info['step'] = 'grade'
                            if subject_number < user_info['num_subjects']:
                                tel_send_message(chat_id, f"Enter the Grade point of subject {subject_number + 1}:")
                            else:
                                # Calculate GPA
                                total_grade_points = sum([grade * credit for grade, credit in zip(user_info['grades'], user_info['credits'])])
                                total_credits = sum(user_info['credits'])
                                gpa = total_grade_points / total_credits
                                tel_send_message(chat_id, f"Your GPA is: {gpa:.2f}")
                        except ValueError:
                            tel_send_message(chat_id, "Please enter a valid credit point.")
            else:
                tel_send_message(chat_id, "Send /start to calculate your GPA")

        return Response('ok', status=200)
    else:
        return "<h1>Welcome!</h1>"


application = app
if __name__ == '__main__':
    app.run(debug=True)