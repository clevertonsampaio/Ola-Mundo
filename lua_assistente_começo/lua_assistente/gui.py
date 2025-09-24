import customtkinter as ctk
import threading
from voice_handler import speak, listen
import commands, db

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Lua – Assistente Pessoal")
        self.geometry("500x500")
        
        self.chat = ctk.CTkTextbox(self, state="disabled", wrap="word")
        self.chat.pack(fill="both", expand=True, padx=10, pady=(10, 5))

        self.entry = ctk.CTkEntry(self, placeholder_text="Digite algo ou fale 'Lua'...")
        self.entry.pack(fill="x", padx=10, pady=5)
        self.entry.bind("<Return>", self.enviar_texto)

        self.btn_voice = ctk.CTkButton(self, text="🎙️ Ativar por voz", command=self.start_listen)
        self.btn_voice.pack(pady=(0, 10))

    def start_listen(self):
        threading.Thread(target=self.listen_loop, daemon=True).start()

    def listen_loop(self):
        speak("Estou ouvindo. Diga 'Lua'.")
        while True:
            texto = listen()
            if "lua" in texto:
                comando = texto.replace("lua", "").strip()
                self.processar_comando(comando)
                if "sair" in comando:
                    break

    def enviar_texto(self, event=None):
        comando = self.entry.get().strip()
        if comando:
            self.processar_comando(comando)
            self.entry.delete(0, "end")

    def processar_comando(self, comando):
        resposta = commands.process(comando)
        db.save_conversa(comando, resposta)

        self.chat.configure(state="normal")
        self.chat.insert("end", f"👤 Você: {comando}\n🤖 Lua: {resposta}\n\n")
        self.chat.configure(state="disabled")
        self.chat.see("end")
        speak(resposta)
        if "sair" in comando:
            speak("Encerrando agora. Até logo!")
            self.quit()