# Description
Designed and built a simple automation bot to encourage healthy hydration habits by sending scheduled reminders to users on Discord's voice chat. The purpose of this project was to explore how simple automation can improve everyday habits and user experience through accessible tools like Discord.

This project focuses on user convenience, habit formation and lightweight automation.

# Tech Stack
* Python
* Discord API (**`discord.py`**)
* Async Scheduling (e.g., Tasks / Loops)
* Time-Based Event Handling

# How It Works
1. User adds the bot to a Discord server.
2. User sets the preferred reminder interval with the command **`$join <seconds>`** while in the voice chat (If no interval is specified, the bot defaults to **`1200`** seconds).
3. Background scheduler triggers reminders within the call.
