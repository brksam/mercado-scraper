# 🛒 Mercado Livre Scraper

Um script simples e eficiente em **Python** para coletar dados de produtos diretamente do **Mercado Livre**, salvando os resultados automaticamente em uma planilha **Excel (.xlsx)**.

---

## 🚀 Funcionalidades

- Busca automática de produtos no [Mercado Livre](https://www.mercadolivre.com.br)
- Coleta de:
  - **Título**
  - **Link direto**
  - **Preço completo**
- Exportação automática para um arquivo `.xlsx`
- Cabeçalhos simulando um navegador real para evitar bloqueios de requisição

---

## 🧠 Tecnologias Utilizadas

- **Python 3**
- [Requests](https://pypi.org/project/requests/)
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)
- [Pandas](https://pypi.org/project/pandas/)
- [OpenPyXL](https://pypi.org/project/openpyxl/) (para exportar o Excel)

---

## ⚙️ Como usar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/brksam/mercado-scraper.git

2. ***Entre na pasta:**
   ```bash
   cd mercado

3. ***Instale as dependências:**
   ```bash
   pip install -r requirements.txt
4. ***Execute o script:**
   ```bash
   python mercado.py
5. ***igite o nome do produto que deseja buscar e aguarde a geração da planilha:**
   ```bash
   produtos_<NOME_DO_PRODUTO>.xlsx

## 📁 Estrutura do Projeto
```bash
mercado-scraper/
│
├── mercado.py # Script principal de scraping
├── requirements.txt # Dependências do projeto
├── .gitignore # Arquivos ignorados pelo Git
└── README.md # Documentação do projeto
```
## ⚠️ Aviso Importante

Este projeto foi criado exclusivamente para fins educacionais e de aprendizado.
O uso indevido para coleta massiva de dados pode violar os termos de uso do Mercado Livre.
Utilize com responsabilidade e moderação.

## 💡 Autor

👨‍💻 Samuel Souto (brksam)
📫 Contato: GitHub - @brksam

⭐ Se este projeto te ajudou, considere deixar uma estrela (Star) no repositório!
