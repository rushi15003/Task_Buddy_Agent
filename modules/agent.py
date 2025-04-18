# agent.py

from modules.tool_wrapper import Tool
from tools.timer_tool import timer_tool
from tools.currency_converter import currency_converter
from modules.gemini_wrapper import call_gemini

class TaskBuddyAgent:
    def __init__(self):
        self.tools = {
            "timer_tool": Tool(timer_tool, "timer_tool", "Start a timer for a given number of seconds"),
            "currency_converter": Tool(currency_converter, "currency_converter", "Convert currency between units"),
        }

    def observe(self, user_input: str) -> str:
        return user_input.strip()

    def act(self, user_input: str) -> str:
        user_input_lower = user_input.lower()

        # Timer tool
        if "timer" in user_input_lower:
            try:
                import re
                match = re.search(r'(\d+)', user_input_lower)
                duration = int(match.group(1)) if match else 5
                return self.tools["timer_tool"].call(duration)
            except Exception as e:
                return f"⚠️ Could not parse timer duration: {e}"

        # Currency converter
        elif "convert" in user_input_lower or "currency" in user_input_lower:
            try:
                parts = user_input_lower.split()
                amount = float(parts[1])
                from_currency = parts[2]
                to_currency = parts[-1]
                return self.tools["currency_converter"].call(amount, from_currency, to_currency)
            except Exception as e:
                return f"⚠️ Could not parse currency input: {e}"

        # Fallback to Gemini
        return call_gemini(user_input)
