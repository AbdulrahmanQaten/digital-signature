# main.py
import tkinter as tk
from tkinter import messagebox
from crypto_utils import generate_keys, sign_message, verify_signature
import base64

signature_global = None

def generate_keys_gui():
    generate_keys()
    messagebox.showinfo("مفاتيح", "✅ تم توليد المفاتيح بنجاح!")

def sign_text():
    global signature_global
    msg = message_entry.get("1.0", "end").strip()
    if not msg:
        messagebox.showwarning("تنبيه", "الرجاء إدخال رسالة أولاً.")
        return
    signature = sign_message(msg)
    signature_global = base64.b64encode(signature).decode()
    signature_display.delete("1.0", "end")
    signature_display.insert("1.0", signature_global)
    messagebox.showinfo("توقيع", "✅ تم توقيع الرسالة بنجاح!")

def verify_text():
    msg = message_entry.get("1.0", "end").strip()
    sig_text = signature_display.get("1.0", "end").strip()
    if not msg or not sig_text:
        messagebox.showwarning("تنبيه", "الرجاء إدخال الرسالة والتوقيع.")
        return
    try:
        signature = base64.b64decode(sig_text)
    except Exception:
        messagebox.showerror("خطأ", "❌ التوقيع غير صالح.")
        return

    valid = verify_signature(msg, signature)
    if valid:
        messagebox.showinfo("التحقق", "✅ التوقيع صحيح ولم يتم التعديل على الرسالة.")
    else:
        messagebox.showerror("التحقق", "❌ التوقيع غير صحيح أو تم التعديل على الرسالة.")

# واجهة
root = tk.Tk()
root.title("توقيع رقمي للرسائل")
root.geometry("600x500")

tk.Label(root, text="📝 الرسالة:", font=("Arial", 12)).pack(anchor="w", padx=10, pady=(10,0))
message_entry = tk.Text(root, height=7, font=("Arial", 12))
message_entry.pack(padx=10, fill="both")

tk.Button(root, text="🔐 توليد مفاتيح", command=generate_keys_gui).pack(pady=5)
tk.Button(root, text="✍️ توقيع الرسالة", command=sign_text).pack(pady=5)

tk.Label(root, text="🔏 التوقيع:", font=("Arial", 12)).pack(anchor="w", padx=10, pady=(10,0))
signature_display = tk.Text(root, height=7, font=("Arial", 12))
signature_display.pack(padx=10, fill="both")

tk.Button(root, text="🧐 التحقق من التوقيع", command=verify_text).pack(pady=10)

root.mainloop()
