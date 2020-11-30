import discord
from discord.ext import commands
import datetime
import random

from urllib import parse, request
import re

bot = commands.Bot(command_prefix='!', description="Omah's Bot")

#Mayusculas

@bot.command()
async def Omah(ctx):
    await ctx.send('Omah Dios Creador Del Universo')

@bot.command()
async def Barty(ctx):
    await ctx.send('Barty Pro Mata MVP++ 24/7')

@bot.command()
async def Slaim(ctx):
    await ctx.send('Slime Programador')

@bot.command()
async def Quinque(ctx):
    await ctx.send('Caca')

@bot.command()
async def Apri(ctx):
    await ctx.send('Enderman')

@bot.command()
async def Dards(ctx):
    await ctx.send('Nuc')

@bot.command()
async def Hypixel(ctx):
    await ctx.send(random.choice(['Viva Bedwars!!!!', 'Hypixel Manda', 'Hypixel pro Cube Caca', 'Hypixel tiene los mejores modos del mundo, Que esperas? Ven a jugar, Mc.Hypixel.net']))

@bot.command()
async def ResidentEvil(ctx):
    await ctx.send('Un Policia Murió Por Una Pala')

@bot.command()
async def Mambru(ctx):
    await ctx.send('Mambrú Se Fue A La Guerra Que Dolor Que Dolor Que Pena')

@bot.command()
async def Prd(ctx):
    await ctx.send(random.choice(["Ganaras Un Bedwars", "Hoy Ella Te Hablará", "Perderas 100m En Skyblock", "Encontraras Una Moneda En El Piso", "Tus Padres Te Compraran Una PS5", "El Onmitrix será tuyo", "Aprenderas a hacer el Kamui", "Aprobaras La Escuela", "Moriras El Dia De Tu Muerte"]))

@bot.command()
async def Ball8(ctx):
    await ctx.send(random.choice(["Si", "No", "No Estoy Seguro", "Probablemente Si", "Tal Vez", "Obvio", "Claro Que No!", "Claro Que Si"]))

@bot.command()
async def List(ctx):
    await ctx.send('**Lista De Comandos:** Omah, Barty, Apri, Dards, Quinque, Hypixel, ResidentEvil, Mambru, Ball8, Prd')

#Minuscula

@bot.command()
async def omah(ctx):
    await ctx.send('Omah Dios Creador Del Universo')

@bot.command()
async def barty(ctx):
    await ctx.send('Barty Pro Mata MVP++ 24/7')

@bot.command()
async def slaim(ctx):
    await ctx.send('Slime Programador')

@bot.command()
async def quinque(ctx):
    await ctx.send('Caca')

@bot.command()
async def apri(ctx):
    await ctx.send('Enderman')

@bot.command()
async def dards(ctx):
    await ctx.send('Nuc')

@bot.command()
async def hypixel(ctx):
    await ctx.send(random.choice(['Viva Bedwars!!!!', 'Hypixel Manda', 'Hypixel pro Cube Caca', 'Hypixel tiene los mejores modos del mundo, Que esperas? Ven a jugar, Mc.Hypixel.net']))

@bot.command()
async def residentevil(ctx):
    await ctx.send('Un Policia Murió Por Una Pala')

@bot.command()
async def mambru(ctx):
    await ctx.send('Mambrú Se Fue A La Guerra Que Dolor Que Dolor Que Pena')

@bot.command()
async def prd(ctx):
    await ctx.send(random.choice(["Ganaras Un Bedwars", "Hoy Ella Te Hablará", "Perderas 100m En Skyblock", "Encontraras Una Moneda En El Piso", "Tus Padres Te Compraran Una PS5", "El Onmitrix será tuyo", "Aprenderas a hacer el Kamui", "Aprobaras La Escuela", "Moriras El Dia De Tu Muerte"]))

@bot.command()
async def ball8(ctx):
    await ctx.send(random.choice(["Si", "No", "No Estoy Seguro", "Probablemente Si", "Tal Vez", "Obvio", "Claro Que No!", "Claro Que Si"]))

@bot.command()
async def list(ctx):
    await ctx.send('**Lista De Comandos:** omah, barty, apri, dards, quinque, hypixel, residentevil, mambru, ball8, prd')


bot.run('Token Id')
