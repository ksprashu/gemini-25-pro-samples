# This program demonstrates how to use the Gemini API with a key from AI Studio.

#!/usr/bin/env python

import os
from google import genai

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise EnvironmentError("GEMINI_API_KEY environment variable is not set.")

# initialise the client with the API key (from AI Studio)
client = genai.Client(api_key=GEMINI_API_KEY)
MODEL = "gemini-2.5-pro-exp-03-25"  # the model identifier

# Generate a completion using the model
response = client.models.generate_content(
    model=MODEL,
    contents="What is the shape of the Earth and why is it the way it is? Tell it as a Haiku",
)

print(response.text)
