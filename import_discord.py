# Устанавливаем библиотек
import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

# Устонавливаем префикс для команд
bot = commands.Bot(command_prefix = '!' , intents = discord.Intents.default())

# Устонавливаем события
@bot.event
async def on_ready():
    print(f'I Temurmalik')

# Пишим команду
@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f'./{attachment.filename}')
            await ctx.send(get_class(model_path = "./keras_model.h5" , labels_path = "labels.txt" , image_path = f"/{attachment.filename}"))
    else:
        await ctx.send('Вы забыли загрузить картинку')

# Устонавливаем токкен
bot.run('MTE2MTY5MTM4NzkxNDM3NTI3OA.GKmk2D.Cv8_6IMR9MJrT-3gkZlU9HCD70v0JB-4_n191U')