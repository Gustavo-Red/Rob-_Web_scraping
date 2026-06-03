# 🤖 Robô de Web Scraping — Verificador de Domínios .br

## 📌 Sobre o projeto

> **Web Scraping** é a habilidade de pegar informações da internet, de sites, para você fazer o que quiser com elas.

Este projeto é um robô que verifica automaticamente se domínios `.br` estão disponíveis para registro, consultando o site [registro.br](https://registro.br/). Ele lê uma lista de domínios de uma planilha Excel e salva os resultados em um arquivo `.txt`.

---

## 🎥 Demonstração

[Assista ao projeto em funcionamento](https://youtu.be/Su6bCune1mQ)

---

## ⚙️ Como funciona

1. Lê uma lista de domínios de uma planilha `.xls`
2. Abre o navegador Chrome automaticamente
3. Pesquisa cada domínio no site registro.br
4. Captura o resultado ("disponível" ou "não disponível")
5. Salva todos os resultados num arquivo `resultado.txt`

---

## 🛠️ Tecnologias utilizadas

- **Python 3.12**
- **Selenium 4** — automação do navegador
- **xlrd** — leitura de planilhas `.xls`
- **ChromeDriver** — intermediário entre o Selenium e o Chrome

---

## 📁 Estrutura do projeto

```
Projeto_Webscraping/
├── Robô_webscraping05.py   # script principal
├── dominios.xls            # planilha com a lista de domínios
└── resultado.txt           # arquivo gerado com os resultados
```

---

## ▶️ Como executar

### 1. Clone o repositório
```bash
git clone https://github.com/Gustavo-Red/Robo_Web_scraping.git
```

### 2. Crie e ative um ambiente virtual
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install selenium xlrd
```

### 4. Baixe o ChromeDriver compatível com sua versão do Chrome
- Acesse: https://googlechromelabs.github.io/chrome-for-testing/
- Extraia e mova para um caminho acessível

### 5. Ajuste o caminho do ChromeDriver e da planilha no script
```python
service = Service('/seu/caminho/chromedriver')
workbook = xlrd.open_workbook('/seu/caminho/dominios.xls')
```

### 6. Execute
```bash
python Robô_webscraping05.py
```

---

## 📄 Exemplo de saída

```
O domínio meusite.com.br está como 'não disponível'
O domínio pythoncurso.com.br está como 'disponível'
O domínio loja.com.br está como 'não disponível'
```

---
