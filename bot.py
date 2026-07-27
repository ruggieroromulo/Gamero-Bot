import os
import random
import discord
from discord import app_commands

# Tenta carregar .env se existir (uso local). No Replit, o token vem
# direto do Secrets (os.getenv já pega de lá também).
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()

# Guarda quantas vezes cada usuário sobreviveu/morreu (fica em memória,
# zera se o bot reiniciar - simples de propósito)
placar = {}

def registrar(user_id: int, sobreviveu: bool):
    dados = placar.setdefault(user_id, {"vivo": 0, "morto": 0})
    if sobreviveu:
        dados["vivo"] += 1
    else:
        dados["morto"] += 1


class MeuBot(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()


client = MeuBot()


@client.event
async def on_ready():
    print(f"Bot conectado como {client.user} (id: {client.user.id})")


@client.tree.command(name="roleta", description="Roleta russa clássica (1 em 6 chances)")
async def roleta(interaction: discord.Interaction):
    morreu = random.randint(1, 6) == 1
    registrar(interaction.user.id, sobreviveu=not morreu)
    if morreu:
        await interaction.response.send_message(
            f"🔫 **BANG!** {interaction.user.mention} se deu mal dessa vez! 💀"
        )
    else:
        await interaction.response.send_message(
            f"🔫 *click* {interaction.user.mention} sobreviveu... por enquanto. 😅"
        )


@client.tree.command(name="roleta_hardcore", description="Roleta russa com 3 balas no tambor (mais arriscado!)")
async def roleta_hardcore(interaction: discord.Interaction):
    morreu = random.randint(1, 6) <= 3  # 3 em 6 chances
    registrar(interaction.user.id, sobreviveu=not morreu)
    if morreu:
        await interaction.response.send_message(
            f"💀🔫 **BOOM!** {interaction.user.mention} tentou o modo hardcore e não teve sorte!"
        )
    else:
        await interaction.response.send_message(
            f"😰 *click* {interaction.user.mention} sobreviveu ao modo hardcore! Sortudo(a)."
        )


@client.tree.command(name="duelo", description="Desafie outro membro para um duelo de roleta russa")
@app_commands.describe(oponente="Quem vai duelar com você")
async def duelo(interaction: discord.Interaction, oponente: discord.Member):
    if oponente.id == interaction.user.id:
        await interaction.response.send_message("Não dá pra duelar com você mesmo! 😅")
        return
    if oponente.bot:
        await interaction.response.send_message("Bots não aceitam duelo (ainda).")
        return

    perdedor = random.choice([interaction.user, oponente])
    vencedor = oponente if perdedor == interaction.user else interaction.user

    registrar(vencedor.id, sobreviveu=True)
    registrar(perdedor.id, sobreviveu=False)

    await interaction.response.send_message(
        f"⚔️🔫 Duelo entre {interaction.user.mention} e {oponente.mention}!\n"
        f"💀 {perdedor.mention} caiu... {vencedor.mention} vence o duelo!"
    )


@client.tree.command(name="placar", description="Veja seu histórico na roleta russa")
async def placar_cmd(interaction: discord.Interaction):
    dados = placar.get(interaction.user.id, {"vivo": 0, "morto": 0})
    total = dados["vivo"] + dados["morto"]
    if total == 0:
        await interaction.response.send_message(
            "Você ainda não jogou nenhuma roleta! Use `/roleta` pra testar sua sorte."
        )
        return
    await interaction.response.send_message(
        f"📊 Placar de {interaction.user.mention}:\n"
        f"✅ Sobreviveu: {dados['vivo']}x\n"
        f"💀 Morreu: {dados['morto']}x\n"
        f"🎲 Total de jogos: {total}"
    )


if __name__ == "__main__":
    if not TOKEN:
        raise RuntimeError(
            "Token não encontrado. Configure DISCORD_TOKEN no .env (local) "
            "ou em Secrets (Replit)."
        )
    client.run(TOKEN)
