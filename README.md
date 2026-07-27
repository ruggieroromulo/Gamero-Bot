# Gamero Bot

Bot de Discord com comandos de roleta russa, feito com [discord.py](https://github.com/Rapptz/discord.py) e slash commands.

## Comandos

- `/roleta` — roleta russa clássica (1 em 6 chances de "morrer")
- `/roleta_hardcore` — versão mais arriscada (3 em 6 chances)
- `/duelo @membro` — desafia outro membro para um duelo
- `/placar` — mostra seu histórico de vitórias e derrotas

## Como rodar

1. Clone o repositório e instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

2. Copie `.env.example` para `.env` e adicione o token do seu bot:

   ```
   DISCORD_TOKEN=seu_token_aqui
   ```

3. Execute:

   ```bash
   python bot.py
   ```
