import discord
import random, os

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'Bot {client.user} kullanıma hazır!, Komutlarınızı yazmak için en başa / sembolünü kullanın!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$komut_listesi'):
        with open("cevretxt/komut_listesi.txt", "r", encoding="utf-8") as f:
            content = f.read()
        messages = [content[i:i+2000] for i in range(0, len(content), 2000)]
        for msg in messages:
            await message.channel.send(msg)

    elif message.content.startswith('$cevre_kirliligi_nedir'):
        with open("cevretxt/cevre.txt", "r", encoding="utf-8") as f:
            content = f.read()
        messages = [content[i:i+2000] for i in range(0, len(content), 2000)]
        for msg in messages:
            await message.channel.send(msg)

    elif message.content.startswith('$cevreyi_kirliligini_nasil_onleriz'):
        with open("cevretxt/temiz.txt", "r", encoding="utf-8") as f:
            content = f.read()
        messages = [content[i:i+2000] for i in range(0, len(content), 2000)]
        for msg in messages:
            await message.channel.send(msg)

    elif message.content.startswith('$cevre_kirliligi_fotograflari'):
        kirlicevre_foto = random.choice(os.listdir('kirlicevre'))
        with open(f'kirlicevre/{kirlicevre_foto}', 'rb') as cevrefoto:
            resim = discord.File(cevrefoto)
        await message.channel.send(file=resim)

client.run("MTIwNTkxOTE0NjQ0NjE1OTk5NA.GeVkyr.uCToi766Cyoqp2uOTnMAsTaIlJM63qWLeUicZo")
