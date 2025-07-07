# classify_email.py
import sys
import google.generativeai as genai

def classify_email(email_body, api_key):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = f"""
    Classify the following customer support email into one of the following categories only:
    - Technical Issue
    - Billing Inquiry
    - Sales Question
    - General Feedback

    Return ONLY the category name as plain text. No explanation.

    Email:
    {email_body}
    """

    try:
        chat = model.start_chat()
        response = chat.send_message(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        return "General Feedback"

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python classify_email.py '<email_body>' '<GEMINI_API_KEY>'", file=sys.stderr)
        sys.exit(1)
    
    email_body = sys.argv[1]
    api_key = sys.argv[2]
    result = classify_email(email_body, api_key)
    print(result)
