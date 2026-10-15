# ChatBot 🤖

A simple **rule-based chatbot** written in Python. PyBot matches your message against a list of known phrases and replies accordingly — a great beginner project for learning `if/elif` logic, string methods, and loops.

## How to Run

1. Clone this repository:

```bash
   git clone https://github.com/<your-username>/pybot.git
   cd pybot
```

2. Run it (Python 3.7+, no external dependencies):

```bash
   python pybot.py
```

3. Type a message and press Enter. Type `bye` to exit.

## Commands PyBot Understands

| You type | PyBot replies |
| --- | --- |
| `hello`, `hi`, `hey`, `hiya` | Greeting |
| `how are you` | Small talk |
| `what's your name`, `who are you` | Introduction |
| `help` | Lists everything it knows |
| `bye`, `goodbye`, `quit`, `exit` | Ends the chat |
| anything else | "Sorry, I don't understand..." |

## Example Session

```javascript
PyBot: Hi ! I'm PyBot. Type 'bye' to exit.

You: hello
PyBot: Hi !
You: what's your name
PyBot: I'm PyBot, a simple rule-based chatbot.
You: bye
PyBot: Goodbye !
```

## Project Structure

```javascript
pybot/
├── pybot.py    # The chatbot (single file)
└── README.md   # This file
```

## How It Works

1. `get_reply()` lowercases and strips your input, then checks it against tuples of known phrases.
2. `chat()` runs an infinite loop, printing PyBot's reply each round until you say goodbye.

## License

MIT — free to use and modify.