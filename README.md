# Simple app based on python to interact with gemini API
Overview:

    This is a basic Python application that starts a local web server using Python’s built-in http.server module.

Introduction:

    * It serves an HTML form where users can enter question(s) and view AI-generated responses.
    * The application uses the Gemini 1.5 Flash model.

Purpose:

    # The purpose of this project is to demonstrate how to build a simple, lightweight web interface using Python’s built-in HTTP server to interact with Google's Gemini AI model (gemini-1.5-flash). 

    # It allows users to input prompts and get AI-generated responses in real time, without relying on heavy frameworks.

Features:

    1. Users can enter multiple questions and receive responses.
    2. Prompts are sent to the Gemini API.
    3. AI-generated responses are displayed on the same page.
    4. Built using Python’s built-in HTTP server (no external frameworks).

Limitation:

    1. While users can ask multiple questions, the app does not store any history of previous responses.

Technology Stack:

    1. Backend: Python(3.9.6)
    2. Frontend: Basic HTML, CSS, and JavaScript
    3. AI Integration: Gemini API (model: gemini-1.5-flash)


Project Structure:

    .
    ├── my_app.py
    ├── index.html
    ├── requirements.txt
    ├── .env # Not committed (holds your Gemini API key)
    ├── .gitignore
    └── README.md
    ├── config.py


Prerequisites:

    Before you begin, please ensure you have the following installed on your local machine:

    1. Python 3.7 or higher
    2. Git (to clone the repository)
    3. Virtualenv (optional but recommended for creating isolated Python environments)

Best Practices:

    1. Use a Virtual Environment:
        It’s recommended to create a virtual environment to keep dependencies isolated from your global Python installation. This helps avoid version conflicts and keeps your system clean.

        create a new virtual environment in your local: python -m venv your_venv_name
        to activate your virutal environment:           source your_venv_name/bin/activate 

    2. Install Dependencies:
        Once the virtual environment is activated, install the required packages using the provided requirements.txt file.

        install the requirements.txt file which exists in git repo using the command below:
        command: pip install -r requirements.txt

    3. Set Your Gemini API Key:

        Create a .env file in the root of your project directory and add your API key like this:        
        GEMINI_API_KEY="your-gemini-api-key"
        This file helps to keep your sensitive information out of your codebase and easy to update.




Installation Guide:

    1. Get your Gemini API key:
        Go to https://aistudio.google.com/app/apikey and sign in with your Google account to obtain your personal Gemini API key.

    2. Clone this repository to your local machine:
        command: git clone <your-repo-url>

    3. Navigate to the project folder:
        command: cd <project-folder>
    
    4. Activate the virtual environment:
        command: source your_venv_name/bin/activate
    
    5. Install the requirements.txt file:
        command: pip install -r requirements.txt
    
    
How to run:

    1. Open your terminal or command prompt, navigate to the project folder, and run the app:
       command: python my_app.py

    2. Open your web browser and go to: http://localhost:8000/


Usage:

    1. After running the app and opening http://localhost:8000/ in your browser, you’ll see a form.

    2. Enter your question(s) in the text area and click the "Submit" button.

    3. If you want to clear the text area click the "Clear" button.

    4. After clicking submit, you'll see "Please wait, generating response..." while the app fetches the reply. The AI-generated response will then appear below the form.

    5. You can enter new question(s) one after another, but the app doesn’t store any history.


Additional Notes:

    The project includes a .gitignore file to keep sensitive files like your .env (which stores your API key) and the virtual environment folder from being accidentally committed to the repository.

    Make sure not to commit your .env file or virtual environment folder to keep your API keys and local setup private.





### Author
Vinothkumar AK
[akvinothkumar881996@gmail.com](mailto:akvinothkumar881996@gmail.com)