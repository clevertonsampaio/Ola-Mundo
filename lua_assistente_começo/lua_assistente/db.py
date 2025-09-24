import sqlite3
from datetime import datetime

DB_PATH = 'lua_db.sqlite'

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
      CREATE TABLE IF NOT EXISTS conversas (
        id INTEGER PRIMARY KEY,
        data TEXT, pergunta TEXT, resposta TEXT)
    ''')
    c.execute('''
      CREATE TABLE IF NOT EXISTS lembretes (
        id INTEGER PRIMARY KEY,
        data TEXT, lembrete TEXT)
    ''')
    conn.commit()
    conn.close()

def save_conversa(pergunta, resposta):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO conversas (data, pergunta, resposta) VALUES (?, ?, ?)",
              (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), pergunta, resposta))
    conn.commit()
    conn.close()

def save_lembrete(texto):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO lembretes (data, lembrete) VALUES (?, ?)",
              (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), texto))
    conn.commit()
    conn.close()