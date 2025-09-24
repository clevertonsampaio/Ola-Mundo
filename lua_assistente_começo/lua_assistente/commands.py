from openai import OpenAI
import webbrowser
import requests
import db
from datetime import datetime

# Inicializa cliente OpenAI (coloque sua chave aqui)
client = OpenAI(api_key="SUA_CHAVE_API_AQUI")

# Histórico de conversa
conversation_history = [
    {"role": "system", "content": "Você é Lua, uma assistente pessoal amigável e útil em português."}
]

def process(cmd: str):
    # --- Comandos fixos ---
    if "seu nome" in cmd:
        return "Meu nome é Lua, sua assistente pessoal."
    if "horas" in cmd:
        return f"Agora são {datetime.now().strftime('%H:%M')}."
    if "abrir" in cmd:
        site = cmd.replace("abrir", "").strip()
        url = site if site.startswith("http") else f"https://{site}"
        webbrowser.open(url)
        return f"Abrindo {site}."
    if "lembrete" in cmd:
        texto = cmd.replace("lembrete", "").strip()
        db.save_lembrete(texto)
        return f"Lembrete salvo: {texto}"
    if "clima" in cmd:
        loc = "Votorantim"
        r = requests.get(f"http://wttr.in/{loc}?format=3")
        return r.text

    # --- Conversa em tempo real com GPT ---
    conversation_history.append({"role": "user", "content": cmd})

    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=conversation_history,
        max_tokens=200
    )

    resposta = resp.choices[0].message.content.strip()
    conversation_history.append({"role": "assistant", "content": resposta})
    return resposta