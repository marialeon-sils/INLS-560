import os                        # FOR BUILDING DIRECTORY
import re                        # REGULAR EXPRESSION

# Slugify function.
def slugify(title):
    """Convert the page title to a filename-friendly slug."""
    if title.lower() == "home":  # Ensure 'Home' becomes 'index.html'
        return "index.html"
    return re.sub(r'\W+', '-', title.strip().lower()) + ".html" # FOR REGULAR EXPRESSION

# Generate Nav Function.
def generate_nav(titles, active_title): # METHOD FOR GENERATING NAVIGATION
    """Generate a dynamic navigation bar with an active page highlight."""
    nav_links = ""
    for title in titles:                    # FOR LOOP
        filename = slugify(title)
        active_class = ' class="active"' if title == active_title else ""
        nav_links += f'\t\t\t<a href="{filename}"{active_class}>{title}</a>\n'
    return nav_links.strip()

# Create HTML Function.
def create_html_file(title, titles, output_dir="build"): # FOR BUILDING DIRECTORYS
    """Generate and write HTML content based on the page title."""
    filename = slugify(title)
    nav = generate_nav(titles, active_title=title)

    # F STRING BELLOW
    html_content = f"""                     
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <nav>
            {nav}
        </nav>
        <div class="content">
            <h1>{title}</h1>
            <p>This is the {title.lower()} content.</p>
        </div>
    </body>
    </html>
    """

    output_path = os.path.join(output_dir, filename)
    os.makedirs(output_dir, exist_ok=True)  # Ensure the directory exists

    with open(output_path, 'w') as file:
        file.write(html_content)

    print(f"Created {filename} in the '{output_dir}' directory.")

# Create CSS File Function.
def create_css_file():
    pass    # PASS STATEMENT

def main():
    """Main function to generate pages and styles. MUST HAVE HOME!!!"""
    titles = ["Home", "About Me", "My Experience", "My Projects"]   # DICTIONARY STATEMENT

    # Create HTML files for each title
    for title in titles:
        create_html_file(title, titles)

    # Create the style.css file
    #create_css_file() 
    # uncomment the create_css_file() function if you add the function.

if __name__ == "__main__":                # IF STATEMENT
    main()