"""Roast Your Own Agent: one line roasting my own agent.

The line is 136 characters, inside the competition's 1-140 gate.
It roasts the classic failure modes: confident wrong answers, endless
hedging, eager agreement, and a tool call that goes nowhere.
"""

LINE = "I answer with total confidence, hedge for three paragraphs, agree with whatever you said, then call a tool that does absolutely nothing."


def main():
    print(LINE)


if __name__ == "__main__":
    main()
