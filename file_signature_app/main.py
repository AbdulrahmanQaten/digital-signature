# main.py
import tkinter as tk
from tkinter import filedialog, messagebox
from crypto_utils import generate_keys, sign_message, verify_signature

def generate_keys_gui():
    generate_keys()
    messagebox.showinfo("تم", "✅ تم توليد المفاتيح بنجاح!")

def sign_file():
    filepath = filedialog.askopenfilename(title="اختر ملفًا لتوقيعه")
    if not filepath:
        return
    with open(filepath, "rb") as f:
        content = f.read()
    sign_message(content)
    messagebox.showinfo("تم", "✅ تم توقيع الملف بنجاح!")

def verify_file():
    filepath = filedialog.askopenfilename(title="اختر الملف الأصلي")
    if not filepath:
        return
    with open(filepath, "rb") as f:
        content = f.read()

    sig_path = filedialog.askopenfilename(title="اختر ملف التوقيع", filetypes=[("Signature", "*.sig")])
    if not sig_path:
        return
    with open(sig_path, "rb") as f:
        signature = f.read()

    result = verify_signature(content, signature)
    if result:
        messagebox.showinfo("النتيجة", "✅ التوقيع صحيح وسليم!")
    else:
        messagebox.showerror("النتيجة", "❌ التوقيع غير صحيح أو تم تعديل الملف!")

# واجهة
root = tk.Tk()
root.title("نظام التوقيع الرقمي")
root.geometry("400x300")

tk.Label(root, text="نظام التوقيع الرقمي", font=("Arial", 16)).pack(pady=20)

tk.Button(root, text="توليد مفاتيح", command=generate_keys_gui, width=30).pack(pady=10)
tk.Button(root, text="توقيع ملف", command=sign_file, width=30).pack(pady=10)
tk.Button(root, text="التحقق من توقيع", command=verify_file, width=30).pack(pady=10)

root.mainloop()
