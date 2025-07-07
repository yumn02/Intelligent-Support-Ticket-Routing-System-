from classify_email import classify_email
from config import GEMINI_API_KEY

sample_email = """
Hello, I'm having trouble logging into my account after your latest update. Can you help?
"""

result = classify_email(sample_email, GEMINI_API_KEY)
print(f"Predicted Category: {result}")
