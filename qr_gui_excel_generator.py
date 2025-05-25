import tkinter as tk
from tkinter import filedialog, messagebox
import qrcode
from openpyxl import Workbook
from openpyxl.drawing.image import Image as XLImage
from PIL import Image
import os

def generate_qr_code(data):
    qr = qrcode.QRCode(box_size=2, border=1)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img

def save_excel_with_qr(ids, output_path):
    wb = Workbook()
    ws = wb.active
    ws.title = "QR Codes"
    ws.append(["ID", "QR Code"])

    temp_dir = "temp_qr_images"
    os.makedirs(temp_dir, exist_ok=True)

    for i, id_text in enumerate(ids, start=2):
        ws.cell(row=i, column=1, value=id_text)
        img = generate_qr_code(id_text)
        temp_path = os.path.join(temp_dir, f"{i}.png")
        img.save(temp_path)

        qr_image = XLImage(temp_path)
        qr_image.width = qr_image.height = 50
        ws.row_dimensions[i].height = 38

        ws.add_image(qr_image, f"B{i}")

    wb.save(output_path)

    for file in os.listdir(temp_dir):
        os.remove(os.path.join(temp_dir, file))
    os.rmdir(temp_dir)

def process_ids():
    try:
        ids = input_text.get("1.0", tk.END).strip().splitlines()
        if not ids:
            messagebox.showerror("Error", "No ID data provided.")
            return
        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                                 filetypes=[("Excel Files", "*.xlsx")],
                                                 title="Save As")
        if file_path:
            save_excel_with_qr(ids, file_path)
            messagebox.showinfo("Success", f"QR Code Excel saved to:\n{file_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

app = tk.Tk()
app.title("QR Code Excel Generator")
app.geometry("500x400")

tk.Label(app, text="Paste your IDs (one per line):").pack(pady=5)
input_text = tk.Text(app, height=15, width=60)
input_text.pack(padx=10, pady=5)

tk.Button(app, text="Generate Excel with QR Codes", command=process_ids, bg="green", fg="white").pack(pady=10)

app.mainloop()
