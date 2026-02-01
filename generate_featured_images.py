# This script generates featured images for blog posts using the Gemini API.
#
# Prerequisites:
# 1. An API key for the Gemini API, accessible via the GEMINI_API_KEY
#    environment variable.
# 2. The script needs to be run from the root of your Hugo project.
# 3. You need to have the following Python packages installed:
#
#    pip install google-generativeai pillow python-frontmatter
#    (Note: The exact google library may differ if you have a pre-release version)
#
# How to run:
# 1. Set the GEMINI_API_KEY environment variable:
#    export GEMINI_API_KEY="your-api-key"
# 2. **Run `python3 list_models.py` to find your image generation model name.**
# 3. **Update the `IMAGE_GENERATION_MODEL` variable in this script with the correct model name.**
# 4. Run the script:
#    python generate_featured_images.py
#

import os
import frontmatter
import time
import io
from pathlib import Path
from google import genai
from PIL import Image

# --- Configuration ---
BLOG_DIR = Path("content/en/blog")
IMAGE_DIR = Path("static/images")
API_KEY = os.environ.get("GEMINI_API_KEY")

# --- ¡¡¡ IMPORTANT !!! ---
# You must replace this with the correct model name for image generation.
# The current value is a guess and might not be correct.
#
# Run the `list_models.py` script to see a list of available models.
# Look for a model that supports the 'generateContent' method. You mentioned
# wanting to use "nanonabana", so look for a model with a similar display name,
# like 'Nano Banana Pro'.
IMAGE_GENERATION_MODEL = "models/gemini-pro-vision"  # <-- REPLACE THIS

def generate_image(prompt):
    """
    Generates an image using the Gemini API's generateContent method
    with a specific image generation model.
    """
    if not API_KEY:
        raise ValueError("GEMINI_API_KEY environment variable not set.")

    print(f"  -> Generating image with model: {IMAGE_GENERATION_MODEL}")
    print(f"  -> Prompt: {prompt[:100]}...")

    # Instantiate the client, which likely picks up authentication from the environment.
    client = genai.Client()

    # Using generate_content with a specific image model.
    response = client.models.generate_content(
        model=IMAGE_GENERATION_MODEL,
        contents=[prompt]
    )

    # --- DEBUGGING: Print the full API response ---
    print("  -> Full API Response:")
    print(response)
    # --- END DEBUGGING ---

    # Process the response to find the image data.
    for part in response.parts:
        if hasattr(part, 'inline_data') and part.inline_data is not None:
            print("  -> Found image data in response part.")
            # part.as_image() returns a PIL Image
            pil_image = part.as_image()
            # We need to save it to bytes to return it
            img_byte_arr = io.BytesIO()
            pil_image.save(img_byte_arr, format='PNG')
            return img_byte_arr.getvalue()

    raise ValueError(f"No image data found in response. If you see a response above, check its structure.")


def process_blog_post(file_path):
    """
    Processes a single blog post: generates an image, saves it, and updates
    the frontmatter.
    """
    print(f"Processing {file_path}...")
    try:
        post = frontmatter.load(file_path)

        if "featured_image" in post.metadata and post.metadata["featured_image"]:
            print("  -> Skipping, featured_image already exists.")
            return

        title = post.metadata.get("title", file_path.stem)
        
        content_words = post.content.split()
        content_snippet = " ".join(content_words[:100])

        prompt = (
            f"Create a visually appealing and relevant featured image for a blog post. "
            f"The style should be modern and suitable for a tech blog. "
            f"The blog post is titled '{title}'. "
            f"Here is a snippet from the post for context: '{content_snippet}...'"
        )

        image_data = generate_image(prompt)
        
        image_filename = f"{file_path.stem}.png"
        image_path = IMAGE_DIR / image_filename
        
        with open(image_path, "wb") as f:
            f.write(image_data)
        print(f"  -> Image saved to {image_path}")

        image_url = f"/images/{image_filename}"
        post.metadata["featured_image"] = image_url
        frontmatter.dump(post, file_path)
        print(f"  -> Updated frontmatter with featured_image: {image_url}")

    except Exception as e:
        print(f"  -> An error occurred while processing {file_path}: {e}")

def main():
    """
    Main function to iterate through all blog posts and process them.
    """
    if not API_KEY:
        print("Error: GEMINI_API_KEY environment variable not set.")
        return

    if not BLOG_DIR.exists():
        print(f"Error: Blog directory not found at '{BLOG_DIR}'")
        return

    if not IMAGE_DIR.exists():
        IMAGE_DIR.mkdir(parents=True)
        print(f"Created image directory at '{IMAGE_DIR}'")

    blog_posts = [f for f in BLOG_DIR.glob("*.md") if f.name != "_index.md"]
    total_posts = len(blog_posts)

    for i, file_path in enumerate(blog_posts):
        print(f"--- [Post {i+1}/{total_posts}] ---")
        process_blog_post(file_path)
        
        if i < total_posts - 1:
            print("--- Waiting for 60 seconds before the next request... ---")
            time.sleep(60)

    print("--- Script finished ---")

if __name__ == "__main__":
    main()