# Intelligent Support Ticket Routing System

This is a project I built during my internship at AriesAI.  
The goal is to make a system that reads support emails, uses AI to understand them, and sends them to the right team.

## How it works

1. When a new email comes in (using Gmail Trigger in n8n), the system gets the email text.
2. The email is sent to a Python script (`classify_email.py`) that uses Gemini AI to choose one of these categories:
   - Billing Inquiry
   - Technical Issue
   - Sales Question
   - General Feedback
3. Then I clean the result and use a Switch node in n8n to decide where to send the email.
4. I added a placeholder to send a message later to Microsoft Teams.

## Files

- `classify_email.py`: the main Python script for classification using Gemini
- `test_classify.py`: for testing the script
- `config.py`: loads the API key from `.env`
- `.env.example`: shows how to write the API key
- `requirements.txt`: Python libraries used
- `n8n/Intelligent Support Ticket Routing System.json`: the exported n8n workflow

## Notes

I tested all 4 categories and made sure the system works.  
If needed, Teams messages can be added later.

For now, I used a **Set node instead of HTTP request** (to Microsoft Teams),  
because I don't have permission to send to the real channels yet.  
It can be added easily when access is available.
