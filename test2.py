import tkinter as tk
import pyperclip

def copy_to_clipboard():
    text = "Nội dung bạn muốn sao chép"  # Thay thế bằng nội dung bạn muốn sao chép
    pyperclip.copy(text)
    print("Đã sao chép nội dung vào clipboard")

# Tạo cửa sổ chính của Tkinter
root = tk.Tk()
root.title("Copy to Clipboard")

# Tạo nút copy và gán chức năng copy_to_clipboard
copy_button = tk.Button(root, text="Copy", command=copy_to_clipboard)
copy_button.pack(pady=20)

# Chạy vòng lặp chính của Tkinter
root.mainloop()
