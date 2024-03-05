import tkinter as tk
from tkinter import ttk, messagebox
import random

class BankAppGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Banco Segurin - Aplicación Bancaria")
        self.master.geometry("400x300")
        self.master.resizable(False, False)
        self.master.configure(bg="#FFFFFF")  # Color de fondo blanco
        self.saldo = 0
        self.nombre = tk.StringVar()
        self.apellido = tk.StringVar()
        self.password = tk.StringVar()
        self.monto = tk.DoubleVar()
        self.plazo = tk.IntVar()
        self.ingresos = tk.DoubleVar()
        self.status_text = tk.StringVar()  # Variable para el texto del estado de la solicitud
        self.create_widgets()

    def create_widgets(self):
        self.bank_name_label = tk.Label(self.master, text="Banco Segurin", bg="#0B3C5D", fg="white", font=("Arial", 14, "bold"))
        self.bank_name_label.pack(fill=tk.X, padx=10, pady=10)

        self.notebook = ttk.Notebook(self.master)  # Usando ttk.Notebook
        self.register_tab = tk.Frame(self.notebook, bg="#FFFFFF")  # Color de fondo blanco
        self.main_tab = tk.Frame(self.notebook, bg="#FFFFFF")  # Color de fondo blanco
        self.notebook.add(self.register_tab, text="Registro")
        self.notebook.add(self.main_tab, text="Principal")
        self.notebook.pack(expand=True, fill=tk.BOTH)

        self.create_register_page()
        # No crear la página principal aquí, la crearemos después del registro

    def create_register_page(self):
        self.register_frame = tk.LabelFrame(self.register_tab, text="Registro de Usuario", bg="#E5E5E5")
        self.register_frame.pack(padx=20, pady=20)

        tk.Label(self.register_frame, text="Nombres:", bg="#E5E5E5").grid(row=0, column=0, sticky="w")
        self.nombre_entry = tk.Entry(self.register_frame, textvariable=self.nombre)
        self.nombre_entry.grid(row=0, column=1)

        tk.Label(self.register_frame, text="Apellidos:", bg="#E5E5E5").grid(row=1, column=0, sticky="w")
        self.apellido_entry = tk.Entry(self.register_frame, textvariable=self.apellido)
        self.apellido_entry.grid(row=1, column=1)

        tk.Label(self.register_frame, text="Contraseña:", bg="#E5E5E5").grid(row=2, column=0, sticky="w")
        self.password_entry = tk.Entry(self.register_frame, show="*", textvariable=self.password)
        self.password_entry.grid(row=2, column=1)

        tk.Button(self.register_frame, text="Registrarse", bg="#0B3C5D", fg="white", font=("Arial", 10, "bold"), command=self.register_user).grid(row=3, columnspan=2, pady=10)

    def create_main_page(self):
        self.main_frame = tk.LabelFrame(self.main_tab, text="Bienvenido", bg="#E5E5E5")
        self.main_frame.pack(padx=20, pady=20)

        tk.Label(self.main_frame, text=f"Hola, {self.nombre.get()} {self.apellido.get()}", bg="#E5E5E5").pack(pady=10)

        tk.Button(self.main_frame, text="Consultar Saldo", bg="#0B3C5D", fg="white", font=("Arial", 10, "bold"), command=self.consultar_saldo).pack(pady=5)
        tk.Button(self.main_frame, text="Solicitar Préstamo", bg="#0B3C5D", fg="white", font=("Arial", 10, "bold"), command=self.show_loan_form).pack(pady=5)

    def show_loan_form(self):
        self.create_loan_form()

    def create_loan_form(self):
        self.clear_frame(self.main_frame)

        self.loan_frame = tk.LabelFrame(self.main_frame, text="Solicitud de Préstamo", bg="#E5E5E5")
        self.loan_frame.pack(padx=20, pady=20)

        tk.Label(self.loan_frame, text="Monto:", bg="#E5E5E5").grid(row=0, column=0, sticky="w")
        self.monto_entry = tk.Entry(self.loan_frame, textvariable=self.monto)
        self.monto_entry.grid(row=0, column=1)

        tk.Label(self.loan_frame, text="Plazo (meses):", bg="#E5E5E5").grid(row=1, column=0, sticky="w")
        self.plazo_entry = tk.Entry(self.loan_frame, textvariable=self.plazo)
        self.plazo_entry.grid(row=1, column=1)

        tk.Label(self.loan_frame, text="Ingresos anuales:", bg="#E5E5E5").grid(row=2, column=0, sticky="w")
        self.ingresos_entry = tk.Entry(self.loan_frame, textvariable=self.ingresos)
        self.ingresos_entry.grid(row=2, column=1)

        tk.Button(self.loan_frame, text="Aplicar", bg="#0B3C5D", fg="white", font=("Arial", 10, "bold"), command=self.submit_loan_application).grid(row=3, columnspan=2, pady=10)

    def consultar_saldo(self):
        self.saldo = random.randint(100, 10000)
        messagebox.showinfo("Consulta de Saldo", f"Tu saldo es: ${self.saldo}")

    def submit_loan_application(self):
        if self.monto.get() and self.plazo.get() and self.ingresos.get():
            messagebox.showinfo("Solicitud Enviada", "Tu solicitud ha sido enviada con éxito.")
            self.create_progress_bar()
            self.master.after(100, self.update_progress, 0)
        else:
            messagebox.showerror("Error", "Todos los campos son requeridos.")

    def create_progress_bar(self):
        self.clear_frame(self.main_frame)

        self.progress_frame = tk.LabelFrame(self.main_frame, text="Estado de Solicitud", bg="#E5E5E5")
        self.progress_frame.pack(padx=20, pady=20)

        self.progress_bar = ttk.Progressbar(self.progress_frame, orient="horizontal", length=200, mode="determinate")
        self.progress_bar.grid(row=0, column=0, columnspan=2, pady=10)

        self.status_label = tk.Label(self.progress_frame, textvariable=self.status_text, bg="#E5E5E5")
        self.status_label.grid(row=1, column=0, columnspan=2)

    def update_progress(self, progress):
        if progress < 25:
            self.status_text.set("Solicitud Pendiente")
        elif progress < 60:
            self.status_text.set("Solicitud Recibida")
        elif progress < 90:
            self.status_text.set("En Verificación")
        else:
            self.status_text.set("Solicitud Conforme")

        self.progress_bar["value"] = progress

        if progress < 100:
            self.master.after(random.randint(500, 1000), self.update_progress, progress + random.randint(2, 5))
        else:
            self.show_loan_result()

    def show_loan_result(self):
        if self.status_text.get() == "Solicitud Conforme":
            messagebox.showinfo("Solicitud Conforme", "¡Felicidades! Tu préstamo ha sido aprobado.")
        else:
            messagebox.showinfo("Solicitud en Revisión", "Tu solicitud de préstamo está en revisión.")

    def register_user(self):
        if self.nombre.get() and self.apellido.get() and self.password.get():
            self.create_main_page()  # Mostrar la página principal después del registro exitoso
            self.notebook.select(self.main_tab)  # Cambiar a la pestaña principal
        else:
            messagebox.showerror("Error", "Todos los campos son requeridos.")

    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

def main():
    root = tk.Tk()
    app = BankAppGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
