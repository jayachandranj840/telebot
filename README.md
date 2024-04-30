# Telegram GPA Calculator

This is a simple Flask application that allows users to calculate their GPA (Grade Point Average) via a Telegram bot.

## Functionality

The Telegram bot provides the following functionality:

1. **Start Command**: Users can start the bot by sending the `/start` command. Upon starting, the bot provides instructions on how to use it and prompts the user to enter the number of subjects.
   
2. **Grade Point Input**: After starting, the bot prompts the user to enter the grade points of each subject one by one.

3. **Credit Point Input**: Once the grade points for all subjects are entered, the bot prompts the user to enter the credit points for each subject.

4. **GPA Calculation**: After all grade and credit points are entered, the bot calculates the GPA using the entered data and displays it to the user.

5. **Error Handling**: The bot includes error handling to ensure that users enter valid inputs and are guided appropriately.

## Setup

To set up this application, follow these steps:

1. Clone the repository to your local machine.

2. Install the required dependencies using `pip install -r requirements.txt`.

3. Replace the `TOKEN` variable in `app.py` with your Telegram bot token.

4. Deploy the Flask application to a server (e.g., Heroku, PythonAnywhere, etc.).

5. Set up a webhook for your Telegram bot using the `/setwebhook` endpoint provided by the Telegram Bot API. Set the webhook URL to the URL of your deployed Flask application.

6. Start using the Telegram bot by sending commands to it in your Telegram chat.

## alternate usage(run your pc as server using ngrok file)

1)Send the Zip file of code and extract it.(Cgp.py and ngrok)

2)search botfather→/start→/newbot(creation)→ Jaya(Botname)→Jaya_bot(username)

3)Open file in VScode and change the api token in the code that u have copiedfrom telegram.

4)install python extensions after running u get error for flask and requestsinstallation.

5)pip install flask or requests.

6)open ngrok → ngrok http 5000.

7)click the first link and signup by creating an account and verify it in theGmail.

8)click the second line that creates a API key and copy the below command  paste it in the command line → once again command ngrok http 5000 → server created.

9)Setup Webhook →https://api.telegram.org/bot"yourbottoken"/setWebhook?url="yoururl" (without“”)→paste the bot token and command line url.

10)once again start the bot and start using the bot.

Note: This will be run during your PC was ON becoz it acts as a server.

## Usage

To use the Telegram bot, follow these steps:

1. Start the bot by sending the `/start` command.

2. Follow the instructions provided by the bot to enter the number of subjects, grade points, and credit points.

3. The bot will calculate your GPA based on the entered data and display it to you.

4. You can restart the process at any time by sending the `/start` command again.

## Credits

This application was created by S.Jayachandran. Feel free to contribute to the project by submitting pull requests or reporting issues.

