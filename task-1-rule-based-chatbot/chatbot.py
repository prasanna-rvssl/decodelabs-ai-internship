# DecodeLabs - Artificial Intelligence Internship
# Project 1: Rule-Based AI Chatbot

import tkinter as tk


# --------------------------------------------------
# Knowledge Base
# --------------------------------------------------

responses = {
    # Greetings
    "hello": "Hello! Welcome to DecodeBot. How can I help you?",
    "hi": "Hi! How can I help you today?",
    "hey": "Hey! Nice to meet you.",
    "hello there": "Hello! Welcome to DecodeBot. How can I help you?",
    "hi there": "Hi! How can I help you today?",
    "hey there": "Hey! Nice to meet you.",

    # General conversation
    "how are you": "I'm doing great! Thanks for asking.",
    "how r u": "I'm doing great! Thanks for asking.",
    "how are u": "I'm doing great! Thanks for asking.",
    "how are you doing": "I'm doing great! Thanks for asking.",

    # Artificial Intelligence
    "what is ai": (
        "Artificial Intelligence is the simulation of human "
        "intelligence in machines that can perform tasks such "
        "as learning, reasoning and decision-making."
    ),

    "what is artificial intelligence": (
        "Artificial Intelligence is a field of computer science "
        "that focuses on creating machines capable of performing "
        "tasks that normally require human intelligence."
    ),

    "tell me about ai": (
        "Artificial Intelligence is the simulation of human "
        "intelligence in machines that can perform tasks such "
        "as learning, reasoning and decision-making."
    ),

    "what is ai used for": (
        "AI is used in areas such as recommendation systems, "
        "virtual assistants, image recognition and automation."
    ),

    # Chatbot information
    "your name": "I'm DecodeBot, a simple rule-based chatbot.",
    "what is your name": "I'm DecodeBot, a simple rule-based chatbot.",
    "what's your name": "I'm DecodeBot, a simple rule-based chatbot.",
    "who are you": "I'm DecodeBot, your rule-based virtual assistant.",

    # Capabilities
    "what can you do": (
        "I can answer basic questions, respond to greetings, "
        "and provide information about Artificial Intelligence."
    ),

    # Help
    "help": (
        "I can respond to greetings, answer basic AI questions "
        "and have a simple conversation with you."
    ),

    # Thanks
    "thank you": "You're welcome!",
    "thanks": "You're welcome!",

    # Time-based greetings
    "good morning": "Good morning! How can I help you?",
    "good afternoon": "Good afternoon! How can I help you?",
    "good evening": "Good evening! How can I help you?"
}


# Exit commands
exit_commands = ["bye", "exit", "quit", "goodbye"]


# --------------------------------------------------
# Rule-Based Response Function
# --------------------------------------------------

def get_response(user_input):

    user_input = user_input.lower().strip()

    # Remove common punctuation
    user_input = (
        user_input
        .replace("!", "")
        .replace("?", "")
        .replace(".", "")
    )

    # Handle empty input
    if not user_input:
        return "Please enter a message."

    # Handle exit commands
    if user_input in exit_commands:
        return "Goodbye! Have a great day."

    # Dictionary lookup with fallback
    return responses.get(
        user_input,
        "Sorry, I don't understand that. "
        "Try asking me about AI or type 'help'."
    )


# --------------------------------------------------
# Add Message Bubble
# --------------------------------------------------

def add_message(sender, message, message_type):

    # Main row for the message
    message_row = tk.Frame(
        chat_frame,
        bg=WHITE
    )

    if message_type == "bot":
        message_row.pack(
            fill=tk.X,
            padx=18,
            pady=(12, 4),
            anchor="w"
        )

        # Sender name
        sender_label = tk.Label(
            message_row,
            text="BOT",
            font=("Segoe UI", 9, "bold"),
            bg=WHITE,
            fg=BLUE
        )

        sender_label.pack(
            anchor="w",
            padx=(2, 0),
            pady=(0, 4)
        )

        # Message bubble
        bubble = tk.Label(
            message_row,
            text=message,
            font=("Segoe UI", 11),
            bg=LIGHT_BLUE,
            fg=TEXT,
            justify=tk.LEFT,
            anchor="w",
            wraplength=480,
            padx=12,
            pady=9
        )

        bubble.pack(anchor="w")

    else:
        message_row.pack(
            fill=tk.X,
            padx=18,
            pady=(12, 4),
            anchor="e"
        )

        # Sender name
        sender_label = tk.Label(
            message_row,
            text="YOU",
            font=("Segoe UI", 9, "bold"),
            bg=WHITE,
            fg=NAVY
        )

        sender_label.pack(
            anchor="e",
            padx=(0, 2),
            pady=(0, 4)
        )

        # Message bubble
        bubble = tk.Label(
            message_row,
            text=message,
            font=("Segoe UI", 11),
            bg=USER_BLUE,
            fg=TEXT,
            justify=tk.LEFT,
            anchor="e",
            wraplength=400,
            padx=12,
            pady=9
        )

        bubble.pack(anchor="e")

    # Update scrolling
    chat_canvas.update_idletasks()
    chat_canvas.configure(
        scrollregion=chat_canvas.bbox("all")
    )

    chat_canvas.yview_moveto(1.0)


# --------------------------------------------------
# Send Message
# --------------------------------------------------

def send_message(event=None):

    user_message = input_box.get().strip()

    if not user_message:
        return

    # Display user's message
    add_message(
        "You",
        user_message,
        "user"
    )

    # Get chatbot response
    bot_response = get_response(user_message)

    # Display bot response
    root.after(
        150,
        lambda: add_message(
            "Bot",
            bot_response,
            "bot"
        )
    )

    # Clear input box
    input_box.delete(0, tk.END)

    # Clean input for exit check
    cleaned_input = (
        user_message.lower()
        .strip()
        .replace("!", "")
        .replace("?", "")
        .replace(".", "")
    )

    # Close application after exit command
    if cleaned_input in exit_commands:
        root.after(
            1200,
            root.destroy
        )


# --------------------------------------------------
# Mouse Wheel Scrolling
# --------------------------------------------------

def scroll_chat(event):

    chat_canvas.yview_scroll(
        int(-1 * (event.delta / 120)),
        "units"
    )


# --------------------------------------------------
# Main Window
# --------------------------------------------------

root = tk.Tk()

root.title("DecodeBot - Rule-Based AI Chatbot")
root.geometry("720x760")
root.minsize(600, 650)


# --------------------------------------------------
# Application Colors
# --------------------------------------------------

NAVY = "#1F3A5F"
BLUE = "#2F6FA3"
LIGHT_BLUE = "#EAF2F8"
USER_BLUE = "#DCE9F5"
LIGHT_BACKGROUND = "#F4F7FB"
WHITE = "#FFFFFF"
TEXT = "#263238"


root.configure(
    bg=LIGHT_BACKGROUND
)


# --------------------------------------------------
# Header
# --------------------------------------------------

header = tk.Frame(
    root,
    bg=NAVY,
    height=105
)

header.pack(
    fill=tk.X
)

header.pack_propagate(False)


title_label = tk.Label(
    header,
    text="DECODEBOT",
    font=("Segoe UI", 24, "bold"),
    bg=NAVY,
    fg=WHITE
)

title_label.pack(
    pady=(18, 2)
)


subtitle_label = tk.Label(
    header,
    text="Rule-Based AI Chatbot",
    font=("Segoe UI", 11),
    bg=NAVY,
    fg="#DCE7F5"
)

subtitle_label.pack()


# Online status
status_label = tk.Label(
    header,
    text="● Online",
    font=("Segoe UI", 9),
    bg=NAVY,
    fg="#B9E4C9"
)

status_label.place(
    relx=0.94,
    rely=0.18,
    anchor="ne"
)


# --------------------------------------------------
# Chat Area
# --------------------------------------------------

chat_outer_frame = tk.Frame(
    root,
    bg=LIGHT_BACKGROUND
)

chat_outer_frame.pack(
    fill=tk.BOTH,
    expand=True,
    padx=25,
    pady=20
)


# Canvas
chat_canvas = tk.Canvas(
    chat_outer_frame,
    bg=WHITE,
    highlightthickness=0
)

chat_canvas.pack(
    side=tk.LEFT,
    fill=tk.BOTH,
    expand=True
)


# Scrollbar
scrollbar = tk.Scrollbar(
    chat_outer_frame,
    orient=tk.VERTICAL,
    command=chat_canvas.yview
)

scrollbar.pack(
    side=tk.RIGHT,
    fill=tk.Y
)


chat_canvas.configure(
    yscrollcommand=scrollbar.set
)


# Frame inside canvas
chat_frame = tk.Frame(
    chat_canvas,
    bg=WHITE
)


chat_window = chat_canvas.create_window(
    (0, 0),
    window=chat_frame,
    anchor="nw"
)


# Make the inner frame match canvas width
def configure_chat_width(event):

    chat_canvas.itemconfig(
        chat_window,
        width=event.width
    )


chat_canvas.bind(
    "<Configure>",
    configure_chat_width
)


chat_frame.bind(
    "<Configure>",
    lambda event: chat_canvas.configure(
        scrollregion=chat_canvas.bbox("all")
    )
)


# Enable mouse-wheel scrolling
chat_canvas.bind_all(
    "<MouseWheel>",
    scroll_chat
)


# --------------------------------------------------
# Initial Bot Message
# --------------------------------------------------

welcome_message = (
    "Hello! Welcome to DecodeBot. How can I help you?\n\n"
    "Type 'help' to see what I can do."
)

add_message(
    "Bot",
    welcome_message,
    "bot"
)


# --------------------------------------------------
# Input Area
# --------------------------------------------------

input_container = tk.Frame(
    root,
    bg=LIGHT_BACKGROUND
)

input_container.pack(
    fill=tk.X,
    padx=25,
    pady=(0, 20)
)


input_box = tk.Entry(
    input_container,
    font=("Segoe UI", 11),
    bg=WHITE,
    fg=TEXT,
    insertbackground=TEXT,
    relief=tk.FLAT,
    borderwidth=0
)

input_box.pack(
    side=tk.LEFT,
    fill=tk.X,
    expand=True,
    ipady=12,
    padx=(0, 10)
)


# --------------------------------------------------
# Send Button
# --------------------------------------------------

send_button = tk.Button(
    input_container,
    text="SEND",
    font=("Segoe UI", 10, "bold"),
    bg=BLUE,
    fg=WHITE,
    activebackground=NAVY,
    activeforeground=WHITE,
    relief=tk.FLAT,
    cursor="hand2",
    padx=25,
    pady=10,
    command=send_message
)

send_button.pack(
    side=tk.RIGHT
)


# --------------------------------------------------
# Keyboard Support
# --------------------------------------------------

input_box.bind(
    "<Return>",
    send_message
)

input_box.focus()


# --------------------------------------------------
# Start Application
# --------------------------------------------------

root.mainloop()