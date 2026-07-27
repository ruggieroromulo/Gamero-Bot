# Gamero Bot

A Discord bot with Russian roulette slash commands, built with [discord.py](https://github.com/Rapptz/discord.py).

## Commands

- `/roleta` — classic Russian roulette (1 in 6 chance of "dying")
- `/roleta_hardcore` — riskier version (3 in 6 chance)
- `/duelo @member` — challenge another member to a duel
- `/placar` — shows your win/loss history

## Screenshots

| `/roleta` | `/roleta_hardcore` |
|---|---|
| ![roleta](screenshots/roleta.png) | ![roleta_hardcore](screenshots/roleta_hardcore.png) |

| `/duelo` | `/placar` |
|---|---|
| ![duelo](screenshots/duelo.png) | ![placar](screenshots/placar.png) |

## Getting started

1. Clone the repository and install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Copy `.env.example` to `.env` and add your bot token:

   ```
   DISCORD_TOKEN=your_token_here
   ```

3. Run it:

   ```bash
   python bot.py
   ```
