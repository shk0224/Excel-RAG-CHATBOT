import os

# Creating directories (inside current folder = EXCEL-BASED-RAG)
os.makedirs("data", exist_ok=True)
os.makedirs("src", exist_ok=True)
os.makedirs("static", exist_ok=True)
os.makedirs("templates", exist_ok=True)

# Creating files
open("data/your_excel_file.xlsx", "a").close()

open("src/__init__.py", "a").close()
open("src/helper.py", "a").close()
open("src/prompt.py", "a").close()

open("static/style.css", "a").close()
open("templates/chat.html", "a").close()

open("app.py", "a").close()
open("store_index.py", "a").close()
open("requirements.txt", "a").close()
open("Dockerfile", "a").close()
open(".env", "a").close()
open("setup.py", "a").close()
open("README.md", "a").close()

print("✅ Created inside:", os.getcwd())