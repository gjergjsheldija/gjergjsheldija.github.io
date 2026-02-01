# list_models.py
# This script lists the available models to find the correct one for image generation.

import os
from google import genai

print("--- Listing available Gemini models ---")

try:
    # Using the client pattern that works for your SDK version.
    # It should automatically use the GEMINI_API_KEY from the environment.
    client = genai.Client()
    
    # Assuming the method to list models is client.models.list()
    # We will print the name and supported generation methods for each model.
    for model in client.models.list():
        # The exact attributes might be different, so we'll try to print common ones.
        try:
            print(f"Model name: {model.name}")
            print(f"  Supported methods: {model.supported_generation_methods}")
            print("-" * 20)
        except AttributeError:
            # If the above fails, just print the whole model object
            print(model)
            print("-" * 20)

except Exception as e:
    print(f"\nAn error occurred while trying to list models: {e}")
    print("This might happen if 'client.models.list()' is not the correct method name.")

