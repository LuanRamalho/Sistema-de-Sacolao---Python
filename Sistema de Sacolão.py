import tkinter as tk
from tkinter import ttk

# Preços dos produtos
produtos = {
    "batata Inglesa": 5.00,
    "batata Baroa": 7.00,
    "batata Doce": 4.00,
    "pimentao": 1.00,
    "alho": 10.00,
    "cebola": 3.00,
    "cebola Roxa": 6.00,
    "cebolinha": 1.50,
    "alface": 1.50,
    "agriao": 3.50,
    "rucula": 2.50,
    "espinafre": 3.00,
    "couve": 1.50,
    "couve-Flor": 5.00,
    "inhame": 4.50,
    "aipim": 3.50,
    "tomate": 6.00,
    "pepino": 4.50,
    "chuchu": 5.50,
    "abobora": 7.00,
    "abobrinha": 3.00    
}

# Função para calcular o total e o troco
def calcular_total():
    total = 0
    for produto, preco in produtos.items():
        quantidade = float(entries[produto].get() or 0)
        total += quantidade * preco

    total_var.set(f"R$ {total:.2f}")
    valor_pago = float(valor_pago_entry.get() or 0)
    troco = valor_pago - total
    troco_var.set(f"R$ {troco:.2f}")

# Configuração da janela principal
root = tk.Tk()
root.title("Sacolão")
root.geometry("600x750")
root.configure(bg="#f0f0f5")

# Título
title_label = tk.Label(root, text="Sacolão - Compras e Troco", font=("Helvetica", 24, "bold"), fg="#4CAF50", bg="#f0f0f5")
title_label.pack(pady=10)

# Canvas para barra de rolagem
canvas = tk.Canvas(root, width=550, height=420, bg="#f4f4f9", highlightthickness=0)
canvas.pack(pady=10)

scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

# Frame dentro do Canvas
scrollable_frame = tk.Frame(canvas, bg="#f4f4f9")
scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

entries = {}

# Adicionar campos para cada produto
for i, (produto, preco) in enumerate(produtos.items()):
    bg_color = "#e1f5fe" if i % 2 == 0 else "#b3e5fc"
    frame_produto = tk.Frame(scrollable_frame, bg=bg_color, bd=1, relief="solid")
    frame_produto.pack(fill="x", pady=2, padx=5)

    label = tk.Label(frame_produto, text=f"{produto.capitalize()} (R${preco}/kg):", font=("Arial", 12, "bold"), fg="#0288D1", bg=bg_color)
    label.pack(side="left", padx=15)

    entry = tk.Entry(frame_produto, width=10, justify="right", font=("Arial", 12))
    entry.pack(side="right", padx=10)
    entries[produto] = entry

# Botão para calcular o total com novas cores e tamanho maior
calcular_btn = tk.Button(scrollable_frame, text="Calcular Total", command=calcular_total,
                         font=("Arial", 12, "bold"), bg="navy", fg="honeydew", padx=20, pady=10)
calcular_btn.pack(pady=20)

# Exibir total
total_var = tk.StringVar(value="R$ 0.00")
total_frame = tk.Frame(root, bg="#ffcdd2", pady=10, padx=10, bd=2, relief="groove")
total_frame.pack(pady=10)

total_label = tk.Label(total_frame, text="Total:", font=("Arial", 16, "bold"), fg="#d32f2f", bg="#ffcdd2")
total_label.grid(row=0, column=0, sticky="w")
total_value = tk.Label(total_frame, textvariable=total_var, font=("Arial", 16), fg="#d32f2f", bg="#ffcdd2")
total_value.grid(row=0, column=1, padx=10)

# Campo para valor pago
valor_pago_frame = tk.Frame(root, bg="#fff3e0", pady=10, padx=10, bd=2, relief="groove")
valor_pago_frame.pack(pady=10)
valor_pago_label = tk.Label(valor_pago_frame, text="Valor pago pelo cliente:", font=("Arial", 14, "bold"), fg="#e65100", bg="#fff3e0")
valor_pago_label.grid(row=0, column=0, sticky="w")
valor_pago_entry = tk.Entry(valor_pago_frame, width=10, justify="right", font=("Arial", 12))
valor_pago_entry.grid(row=0, column=1, padx=10)

# Exibir troco
troco_var = tk.StringVar(value="R$ 0.00")
troco_frame = tk.Frame(root, bg="#bbdefb", pady=10, padx=10, bd=2, relief="groove")
troco_frame.pack(pady=10)

troco_label = tk.Label(troco_frame, text="Troco:", font=("Arial", 16, "bold"), fg="#1976d2", bg="#bbdefb")
troco_label.grid(row=0, column=0, sticky="w")
troco_value = tk.Label(troco_frame, textvariable=troco_var, font=("Arial", 16), fg="#1976d2", bg="#bbdefb")
troco_value.grid(row=0, column=1, padx=10)

# Iniciar o loop da interface
root.mainloop()
