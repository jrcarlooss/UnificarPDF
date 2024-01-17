import os
import fitz  # PyMuPDF

# Diretório contendo os arquivos PDF a serem combinados
diretorio = r'' # digite aqui o caminho para pasta contendo os arquivos em pdf

# Lista todos os arquivos no diretório
arquivos = [arquivo for arquivo in os.listdir(diretorio) if arquivo.lower().endswith('.pdf')]

# Objeto para armazenar o PDF combinado
pdf_combinado = fitz.open()

# Loop pelos arquivos no diretório e adicionar cada PDF ao objeto pdf_combinado
for arquivo in arquivos:
    caminho_arquivo = os.path.join(diretorio, arquivo)

    # Abre cada arquivo PDF
    pdf_documento = fitz.open(caminho_arquivo)

    # Adiciona todas as páginas ao PDF combinado
    pdf_combinado.insert_pdf(pdf_documento)

# Caminho para o arquivo PDF combinado
caminho_pdf_combinado = os.path.join(diretorio, 'arquivo_combinado.pdf')

# Salva o PDF combinado em um novo arquivo
pdf_combinado.save(caminho_pdf_combinado)
pdf_combinado.close()

print(f'Arquivos PDF combinados com sucesso. O arquivo combinado está em: {caminho_pdf_combinado}')
