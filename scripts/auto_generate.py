import os
import subprocess

# === 生成ロジック ===
def generate_python_snippet(task):
    if task == "hello":
        return 'print("Hello, World!")'
    elif task == "sum":
        return "print(sum(range(1, 101)))"
    else:
        return "print('Default output')"

# === 保存 ===
def save_snippet(code):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    folder = os.path.join(base_dir, "code_snippets", "Python")
    os.makedirs(folder, exist_ok=True)

    file_path = os.path.join(folder, "snippet.py")
    with open(file_path, "w") as f:
        f.write(code)

    return file_path

# === 検品 ===
def validate(file_path):
    try:
        result = subprocess.run(
            ["python", file_path],
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.returncode == 0
    except:
        return False

# === メインループ ===
def main():
    task = input("Enter task (hello / sum): ")

    for attempt in range(3):
        print(f"\nAttempt {attempt + 1}")

        code = generate_python_snippet(task)
        file_path = save_snippet(code)

        if validate(file_path):
            print("✅ Valid code generated!")
            return
        else:
            print("❌ Invalid code, retrying...")

    print("⚠️ Failed after 3 attempts.")

if __name__ == "__main__":
    main()
