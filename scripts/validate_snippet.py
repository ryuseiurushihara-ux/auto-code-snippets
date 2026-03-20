import subprocess
import os

def validate_python(file_path):
    try:
        result = subprocess.run(
            ["python", file_path],
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.returncode == 0
    except Exception as e:
        print("Validation error:", e)
        return False

def main():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(base_dir, "code_snippets", "Python", "snippet.py")

    if not os.path.exists(file_path):
        print("No snippet found.")
        return

    print("Validating snippet...")

    if validate_python(file_path):
        print("✅ Valid code")
    else:
        print("❌ Invalid code")

if __name__ == "__main__":
    main()
