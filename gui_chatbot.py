import tkinter as tk
from tkinter import scrolledtext

def get_bot_response(user_input):
    # Phase 1: Sanitization & Normalization (Page 10 Blueprint)
    clean_input = user_input.lower().strip()
    
    # Phase 2: Process (Deterministic Logic Skeleton)
    
    # 1. Standard Guardrails & Exit Commands
    if clean_input in ['exit', 'quit', 'bye', 'goodbye', 'close', 'terminate']:
        return "Goodbye! Terminating control layer safely."
        
    # 2. Greetings & Salutations
    elif clean_input in ['hello', 'hi', 'hey', 'as salam o alaikum', 'salam', 'wasup']:
        return "Hello! I am a deterministic logic engine. How can I assist you today?"
        
    elif clean_input in ['how are you', 'how is it going', 'are you fine']:
        return "As a rule-based system, I don't have feelings, but my processes are running at 100% efficiency!"

    # 3. Identity & Project Core Queries (DecodeLabs Context)
    elif clean_input in ['who are you', 'what is your name', 'tell me about yourself']:
        return "I am Project 1: The Rule-Based AI Chatbot, built for DecodeLabs Foundation Phase."
        
    elif clean_input in ['what is this project', 'project goal', 'project objective']:
        return "The goal of this project is to demonstrate control flow and explicit if-else decision-making logic."
        
    elif clean_input in ['batch', 'which batch is this', 'batch details']:
        return "This project is engineered for Batch: 2026 under the Industrial Training Kit framework."

    # 4. Technical Concepts (Page 8 & 9 Details)
    elif clean_input in ['what is an ai guardrail', 'guardrail', 'ai guardrails', 'nemo']:
        return "AI guardrails (like NVIDIA NeMo) act as a deterministic filter for probabilistic LLM outputs to ensure safety."
        
    elif clean_input in ['what is a white box model', 'white box', 'whitebox']:
        return "A white box model provides 100% hard-coded traceability with zero hallucination risk. Explicit explanations are always available."
        
    elif clean_input in ['what is ipo model', 'ipo blueprint', 'ipo']:
        return "The IPO (Input-Process-Output) model is the foundational blueprint for transparent and controlled AI systems."

    # 5. Operational Queries & Help
    elif clean_input in ['help', 'commands', 'what can you do', 'menu']:
        return "I can answer queries about: 1. Project Goals, 2. AI Guardrails, 3. White Box Models, 4. IPO Blueprints, 5. Batch Details. Try asking one!"
        
    elif clean_input in ['who created you', 'developer', 'author']:
        return "I was developed by an Artificial Intelligence Engineer intern at DecodeLabs as a foundation phase milestone."
        
    elif clean_input in ['clear', 'reset']:
        return "To clear the screen, please restart the logic engine module."

    # 6. Catch-all fallback condition for unknown inputs (Ensures 100% hard-coded safety)
    else:
        return "Input not recognized. I am a strict logic engine and can only respond to predefined rules. Type 'help' for valid inputs."

def send_message():
    user_text = user_entry.get()
    if not user_text.strip():
        return
    
    # Display user message
    chat_area.configure(state='normal')
    chat_area.insert(tk.END, "You: " + user_text + "\n", "user_style")
    
    # Get and display bot response
    bot_text = get_bot_response(user_text)
    chat_area.insert(tk.END, "Chatbot: " + bot_text + "\n", "bot_style")
    chat_area.insert(tk.END, "-" * 40 + "\n", "separator_style")
    
    chat_area.configure(state='disabled')
    chat_area.yview(tk.END)
    user_entry.delete(0, tk.END)
    
    # If exit command, close window after 1.5 seconds
    if bot_text == "Goodbye! Terminating control layer safely.":
        root.after(1500, root.destroy)

# --- GUI Layout Setup (Inspired by DecodeLabs Cyan/Dark Aesthetics) ---
root = tk.Tk()
root.title("DecodeLabs: Logic Engine (Project 1)")
root.geometry("450x550")
root.configure(bg="#1e1e1e") # Dark theme back feed

# Header Banner
header = tk.Label(root, text="DETERMINISTIC AI GUARDRAIL", bg="#008080", fg="white", font=("Courier", 12, "bold"), pady=10)
header.pack(fill=tk.X)

# Chat Area
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, bg="#2d2d2d", fg="#ffffff", font=("Arial", 10))
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_area.configure(state='disabled')

# Text Styles/Colors
chat_area.tag_config("user_style", foreground="#00ffcc", font=("Arial", 10, "bold"))
chat_area.tag_config("bot_style", foreground="#ffcc00", font=("Arial", 10))
chat_area.tag_config("separator_style", foreground="#555555")

# Input Frame
input_frame = tk.Frame(root, bg="#1e1e1e")
input_frame.pack(fill=tk.X, side=tk.BOTTOM, padx=10, pady=10)

# Entry Box
user_entry = tk.Entry(input_frame, bg="#3d3d3d", fg="white", insertbackground="white", font=("Arial", 11))
user_entry.pack(fill=tk.X, side=tk.LEFT, expand=True, ipady=5)
user_entry.bind("<Return>", lambda event: send_message())

# Send Button
send_btn = tk.Button(input_frame, text="SEND", bg="#008080", fg="white", activebackground="#005757", activeforeground="white", command=send_message, width=8)
send_btn.pack(side=tk.RIGHT, padx=(5, 0))

# Initialize Welcome Message
chat_area.configure(state='normal')
chat_area.insert(tk.END, "System: Online [White Box Mode]\n", "bot_style")
chat_area.insert(tk.END, "Chatbot: Welcome! Type your message below.\n", "bot_style")
chat_area.insert(tk.END, "-" * 40 + "\n", "separator_style")
chat_area.configure(state='disabled')

root.mainloop()