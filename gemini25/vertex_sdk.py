# This is a python program that demonstrates how to inoke the Gemini model from Vertex AI on Google Cloud.

#!/usr/bin/env python


import os
from google import genai

GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID")
if not GCP_PROJECT_ID:
    raise EnvironmentError("GCP_PROJECT_ID environment variable is not set.")

# initialise the client with the API key (from AI Studio)
client = genai.Client(vertexai=True, project=GCP_PROJECT_ID, location="us-central1")
MODEL = "gemini-2.5-pro-exp-03-25"  # the model identifier

# Generate a completion using the model
response = client.models.generate_content(
    model=MODEL,
    contents="What is the shape of the Earth and why is it the way it is? Tell it as a Haiku",
)

print(response.text)
