from flask import Flask, render_template, request
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv
import markdown
import os

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

app = Flask(__name__)

class AgentGroq:
    def __init__(self):
        self.agent = Agent(
            model=Groq(id="llama-3.3-70b-versatile"),
            description="Você é um especialista em recomendação de animes. "
                        "Você deve recomendar animes baseado no anime que o usuário escolheu. "
                        "Também deve retornar um pequeno resumo de cada anime.",
            tools=[DuckDuckGoTools()],
            show_tool_calls=True,
            markdown=True
        )

    def gerar_resposta(self, anime_title):
        prompt = f"Baseado no anime {anime_title}, recomende 20 animes (10 famosos, 10 menos famosos) com gêneros semelhantes e sinopses parecidas."
        raw_response = self.agent.run(prompt)
        texto = raw_response.content if hasattr(raw_response, "content") else str(raw_response)
        return markdown.markdown(texto)

@app.route("/", methods=["GET", "POST"])
def index():
    resposta_html = ""
    if request.method == "POST":
        anime = request.form["anime"]
        if anime.strip():
            agente = AgentGroq()
            resposta_html = agente.gerar_resposta(anime)
    return render_template("index.html", resposta=resposta_html)