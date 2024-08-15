import tkinter as tk
from tkinter import ttk
import subprocess

# Variável para definir o banco de dados Prolog
DB_FILE = 'motos.pl'

# Função para realizar a consulta no Prolog
def consulta_prolog(pergunta):
    try:
        # Comando para iniciar o SWI-Prolog e carregar o banco de dados
        prolog_command = f"swipl -q -f {DB_FILE} -g \"{pergunta}\" -t halt"
        
        # Executa o comando Prolog e captura a saída
        result = subprocess.run(prolog_command, shell=True, capture_output=True, text=True)
        
        # Captura e retorna a saída do comando Prolog
        resposta = result.stdout.strip()
        return resposta
    except Exception as e:
        return f"Erro ao executar o comando Prolog: {str(e)}"

# Função para buscar os modelos da marca selecionada
def buscar_modelos():
    marca = combo_marca.get().lower()  # Obtém a marca selecionada
    consulta = f"findall(Modelo, modelo({marca}, Modelo), Result), (Result = [] -> write('Nenhum modelo encontrado.') ; writeln(Result))"  # Prepara a consulta Prolog

    # Consulta o Prolog e obtém os modelos
    resposta = consulta_prolog(consulta)

    # Limpa a lista de modelos
    lista_modelos.delete(0, tk.END)

    # Verifica se a resposta tem resultados e exibe-os
    if resposta:
        # Remove os caracteres de retorno de carro e quebras de linha extras
        modelos = resposta.split('\n')
        for modelo in modelos:
            modelo = modelo.strip()
            if modelo and modelo != 'Nenhum modelo encontrado.':  # Ignora linhas vazias e mensagem padrão
                lista_modelos.insert(tk.END, modelo)
            elif modelo == 'Nenhum modelo encontrado.':
                lista_modelos.insert(tk.END, modelo)
    else:
        lista_modelos.insert(tk.END, "Nenhum modelo encontrado.")

# Criação da interface gráfica
root = tk.Tk()
root.title("Busca de Modelos de Motos")

# Frame para a seleção da marca
frame_marca = tk.Frame(root)
frame_marca.pack(pady=10)

# Label para a marca
label_marca = tk.Label(frame_marca, text="Selecione a marca:")
label_marca.pack(side=tk.LEFT, padx=5)

# Combobox para escolher a marca
marcas = ["Honda", "BMW"]
combo_marca = ttk.Combobox(frame_marca, values=marcas)
combo_marca.pack(side=tk.LEFT, padx=5)
combo_marca.current(0)  # Define a primeira marca como padrão

# Botão para buscar os modelos
btn_buscar = tk.Button(root, text="Buscar Modelos", command=buscar_modelos)
btn_buscar.pack(pady=10)

# Listbox para exibir os modelos
lista_modelos = tk.Listbox(root, width=40, height=10)
lista_modelos.pack(pady=10)

# Inicia o loop principal do tkinter
root.mainloop()
