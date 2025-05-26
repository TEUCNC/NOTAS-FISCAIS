import os

# Defina o caminho para a área de trabalho
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Caminho da nova pasta
folder_name = "Notas Fiscais"
folder_path = os.path.join(desktop_path, folder_name)

# Cria a pasta
os.makedirs(folder_path, exist_ok=True)
print(f"Pasta criada em: {folder_path}")
