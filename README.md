# 🎌 Recomendador de Animes com IA

Este projeto é um sistema de recomendação de animes baseado em **Inteligência Artificial**, desenvolvido com **Flask** e integrado à API **Groq (LLaMA-3.3-70B)** utilizando a biblioteca **Agno**.

O usuário digita o nome de um anime, e o sistema recomenda 20 animes semelhantes — divididos entre **famosos e menos conhecidos** — com uma **sinopse resumida de cada um**.

---

## 🚀 Funcionalidades

- 🔍 Input de anime para base de recomendação  
- 🧠 IA com modelo LLaMA-3.3-70B via Groq  
- 🧾 Output em **Markdown formatado**  
- 🎨 Estilo de terminal retrô com **responsividade**  
- ⏳ Animação de carregamento enquanto a IA processa  
- 📜 Resposta clara, visualmente amigável, e estilizada  

---

## 🛠️ Tecnologias Utilizadas

- [Python 3.10+](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Agno](https://pypi.org/project/agno/)
- [Groq API](https://console.groq.com/)
- [Markdown](https://python-markdown.github.io/)
- [HTML5 + CSS3](https://developer.mozilla.org/pt-BR/docs/Web)
- [JavaScript (loader)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

---

## ⚙️ Como Executar Localmente

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/recomendador-animes.git
cd recomendador-animes
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate    # Linux/macOS
venv\Scripts\activate       # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure sua chave `.env`

Crie um arquivo `.env` com:

```
GROQ_API_KEY=sua_chave_aqui
```

> 🔑 Você pode obter a chave em: [https://console.groq.com](https://console.groq.com)

### 5. Rode a aplicação

```bash
python app/main.py
```

Acesse em: [http://localhost:5000](http://localhost:5000)

---

## 📁 Estrutura de Pastas

```
Recomendation_animes/
├── app/
│   ├── main.py
│   ├── templates/
│   │   └── index.html
│   └── static/
│       └── style.css
├── .env
├── README.md
├── requirements.txt
```

---

## ✅ Exemplo de Uso

Digite no terminal da página:

> **Naruto**

E receba uma lista com:
- 10 animes populares semelhantes a *Naruto*
- 10 animes menos conhecidos, mas com sinopse e gênero parecidos

---

## 🧠 Créditos

- IA por [Groq + Meta LLaMA-3.3-70B](https://groq.com/)
- Interface por [Rodrigo Bueno](#)
- Assistente IA por [OpenAI ChatGPT]

---

## 📃 Licença

Este projeto está sob a licença MIT.
