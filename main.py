import tkinter as tk
from openai import OpenAI

# API key AI
client = OpenAI(api_key="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")

def generate_code():
    user_input = entry.get()

    prompt = f"Viết code Python cho bài toán sau:\n{user_input}"

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        result = response.choices[0].message.content
        output.delete("1.0", tk.END)
        output.insert(tk.END, result)

    except Exception as e:
        output.insert(tk.END, str(e))

# Giao diện
root = tk.Tk()
root.title("AI Code Generator")

tk.Label(root, text="Nhập yêu cầu:").pack()

entry = tk.Entry(root, width=50)
entry.pack()

tk.Button(root, text="Tạo code", command=generate_code).pack()

output = tk.Text(root, height=15, width=60)
output.pack()

root.mainloop()