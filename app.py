import tkinter as tk
from tkinter import messagebox
from model import predict_news

def check_news():
    input_text = entry.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showwarning("Input Needed", "Please enter a news article.")
        return
    label, confidence = predict_news(input_text)
    result = f"🧠 Prediction: {label}\n🔍 Confidence: {confidence}%"
    result_label.config(text=result)

# GUI setup
root = tk.Tk()
root.title("📰 Fake News Detector (Offline)")
root.geometry("500x400")
root.resizable(False, False)

tk.Label(root, text="Enter News Text:", font=("Arial", 14)).pack(pady=10)
entry = tk.Text(root, height=10, width=55, font=("Arial", 12))
entry.pack()

tk.Button(root, text="Check News", font=("Arial", 12), command=check_news).pack(pady=10)
result_label = tk.Label(root, text="", font=("Arial", 13), fg="blue")
result_label.pack(pady=10)

root.mainloop()
