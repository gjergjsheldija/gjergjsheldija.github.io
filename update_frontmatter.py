
import os
import frontmatter

def process_blog_posts():
    blog_dir = "content/en/blog"
    for filename in os.listdir(blog_dir):
        if filename.endswith(".md") and filename != "_index.md":
            filepath = os.path.join(blog_dir, filename)
            with open(filepath, 'r') as f:
                try:
                    post = frontmatter.load(f)
                except:
                    print(f"Error loading frontmatter for {filename}")
                    continue
            
            if 'featured_image' not in post:
                image_name = os.path.splitext(filename)[0] + ".png"
                post['featured_image'] = f"/images/{image_name}"
                
                with open(filepath, 'w') as f:
                    f.write(frontmatter.dumps(post))
                print(f"Updated {filename}")

if __name__ == "__main__":
    process_blog_posts()
