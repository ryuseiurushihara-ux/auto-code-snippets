import os

def load_template(task):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    template_dir = os.path.join(base_dir, "templates", "Python")

    if task == "api":
        file_name = "api_request.py"
    elif task == "json":
        file_name = "json_parse.py"
    elif task == "file":
        file_name = "file_read.py"
    else:
        return "print('Invalid task')"

    file_path = os.path.join(template_dir, file_name)

    with open(file_path, "r") as f:
        return f.read()

def save_snippet(code):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    output_dir = os.path.join(base_dir, "code_snippets", "Python")
    os.makedirs(output_dir, exist_ok=True)

    file_path = os.path.join(output_dir, "snippet.py")

    with open(file_path, "w") as f:
        f.write(code)

    return file_path

def main():
    task = input("Enter task (api / json / file): ")

    code = load_template(task)
    file_path = save_snippet(code)

    print("Snippet generated at:", file_path)

if __name__ == "__main__":
    main()
