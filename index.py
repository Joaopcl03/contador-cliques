import tkinter as tk

def criar_janela():
    contagem = [0]  # lista para poder modificar dentro da função

    def ao_clicar():
        contagem[0] += 1
        label.config(text=f"Cliques: {contagem[0]}")

    janela = tk.Tk()
    janela.title("Contador de Cliques")
    janela.geometry("300x150")

    label = tk.Label(janela, text="Cliques: 0", font=("Arial", 20))
    label.pack(pady=20)

    botao = tk.Button(janela, text="Clique aqui!", command=ao_clicar, font=("Arial", 14))
    botao.pack()

    def resetar():
        contagem[0] = 0
        label.config(text="Cliques: 0")

    botao_reset = tk.Button(janela, text="Resetar", command=resetar, font=("Arial", 14))
    botao_reset.pack(pady=5)

    janela.mainloop()

if __name__ == "__main__":
    criar_janela()