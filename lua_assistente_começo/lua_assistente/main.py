import db, gui

if __name__ == "__main__":
    db.init_db()
    app = gui.App()
    app.mainloop()