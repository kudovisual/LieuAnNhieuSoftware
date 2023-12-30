# Libary import / Import thư viện
import tkinter as tk
import sys

# Hàm def
def main():
    root = tk.Tk()
    root.title("Info | by KudoVisual ™")
    
    # Window size / Kích thước cửa sổ
    root.geometry("400x300")

    # Window icon / Icon của cửa sổ
    icon_path = 'icon.ico'
    root.iconbitmap(icon_path)

    label = tk.Label(root, text="© 2024 Copyright by LieuAnNhieu Software & KudoVisual.")
    label.pack()

    # Window display / Hiển thị cửa sổ
    root.mainloop()

if __name__ == "__main__":
    main()
# © 2024 Copyright by KudoVisual
    # CODE BY KUDOVISUAL
        # Không lấy code và chỉnh sửa để thành phần mềm của bạn. Bạn đạo nhái là tui đến nhà đập luôn đấy nhá :)