import os
import subprocess

# === テンプレート読み込み ===
def load_template(task):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    template_dir = os.path.join(base_dir, "templates", "Python")

    mapping = {
        "api": "api_request.py",
        "json": "json_parse.py",
        "file": "file_read.py"
    }

    if task not in mapping:
        return None

    file_path = os.path.join(template_dir, mapping[task])

    with open(file_path, "r") as f:
        return f.read()

# === 保存 ===
def save_snippet(code):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    output_dir = os.path.join(base_dir, "code_snippets", "Python")
    os.makedirs(output_dir, exist_ok=True)

    file_path = os.path.join(output_dir, "snippet.py")

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
    task = input("Enter task (api / json / file): ").strip().lower()

    for attempt in range(3):
        print(f"\nAttempt {attempt + 1}")

        code = load_template(task)

        if code is None:
            print("❌ Invalid task")
            return

        file_path = save_snippet(code)

        if validate(file_path):
            print("✅ 完成：動作確認済みコード生成")
            print("Path:", file_path)
            return
        else:
            print("❌ エラー検出 → 再生成")

    print("⚠️ 3回失敗（テンプレート見直し必要）")

if __name__ == "__main__":
    main()
