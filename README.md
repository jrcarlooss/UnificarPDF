# Combinação de PDFs em Python 📝

Um script simples em **Python** para combinar múltiplos arquivos PDF em um único PDF. Ideal para unir relatórios, apostilas ou qualquer conjunto de PDFs de forma rápida e automatizada.

---

## Funcionalidades

- Combina todos os arquivos PDF de um diretório em um único arquivo.
- Mantém a ordem dos arquivos conforme aparecem na pasta.
- Gera um arquivo chamado `arquivo_combinado.pdf`.
- Fácil de usar e configurar.

---

## Tecnologias e Bibliotecas

- **Python 3.x**
- **PyMuPDF (fitz)** – biblioteca para manipulação de PDFs.

---

## Como usar

1. Clone ou baixe este repositório.
2. Instale a biblioteca necessária:

```bash
pip install PyMuPDF

diretorio = r'C:\caminho\para\seus\pdfs'  # Substitua pelo caminho da sua pasta

O arquivo combinado será salvo na mesma pasta como arquivo_combinado.pdf.
