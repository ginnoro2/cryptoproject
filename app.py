# app.py
def add(a, b):
    return a + b

# Vulnerable function (for SAST demo)
def unsafe_eval(user_input):
    return eval(user_input)  # ⚠️ Dangerous!
