# Rule-Based AI Chatbot

**DecodeLabs Industrial Training Kit — Batch 2026 — Project 1**

A simple rule-based chatbot built in Python that responds to predefined user inputs using dictionary-based lookup logic. This project demonstrates foundational AI engineering concepts: control flow, decision-making logic, and deterministic ("white box") response systems — the building blocks behind modern AI guardrails.

## Goal
Create a chatbot that:
- Runs in a continuous loop (`while True`)
- Sanitizes and normalizes user input (lowercase + strip whitespace)
- Matches input against a knowledge base of 5+ intents
- Falls back to a default response for unrecognized input
- Exits cleanly on a recognized command (`bye`, `exit`, `quit`)

## How It Works
Instead of a long, unstable `if-elif` ladder (which scales linearly, O(n)), this bot uses a dictionary (hash map) as its knowledge base. This gives instant, constant-time (O(1)) lookups no matter how many rules are added:

```python
reply = responses.get(user_input, "I do not understand. Could you rephrase that?")
```

This single line handles both the lookup and the fallback in one atomic operation.

## Project Structure
```
.
├── chatbot.py      Main chatbot program
└── README.md       Project documentation
```

## How to Run
1. Make sure Python 3 is installed.
2. Clone this repository:
   ```bash
   git clone https://github.com/Moosa26/DecodeLabs-Internship-Project-1.git
   cd DecodeLabs-Internship-Project-1
   ```
3. Run the chatbot:
   ```bash
   python3 chatbot.py
   ```
4. Chat with the bot. Type `bye`, `exit`, or `quit` to end the conversation.

## Example Conversation
```
You: hello
Bot: Hi there! How can I help you today?

You: what is your name
Bot: I'm RuleBot, a simple rule-based chatbot built for DecodeLabs Project 1.

You: thanks
Bot: Anytime! Let me know if you need anything else.

You: bye
Bot: Goodbye! Have a great day.
```

## Key Skills Demonstrated
- Control flow and loops
- String sanitization and normalization
- Dictionary-based decision logic
- Fallback and default handling
- Clean program exit strategy

## Possible Future Improvements
- Expand the vocabulary with more intents
- Add nested conditions for context-aware replies
- Give the bot a unique personality
- Combine with an LLM for a hybrid rule and generative architecture

---
Built as part of the DecodeLabs AI Internship Program (2026).
