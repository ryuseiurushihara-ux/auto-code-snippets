import os

def generate_python_snippet(task):
    if task == "hello":
        return 'print("Hello, World!")'
    elif task == "sum":
        return "print(sum(range(1, 101)))"
    else:
        return "# Unknown task"

def save_snippet(language, code):
    folder = f"../code_snippets/{language}"
    os.makedirs(folder, exist_ok=True)
    
    file_path = os.path.join(folder, "snippet.py")
    with open(file_path, "w") as f:
        f.write(code)

if __name__ == "__main__":
    task = input("Enter task (hello / sum): ")
    
    code = generate_python_snippet(task)
    save_snippet("Python", code)
    
    print("Snippet generated.")
