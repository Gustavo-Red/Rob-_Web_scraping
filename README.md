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
