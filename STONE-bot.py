import random
import discord
import asyncio

def cases(u,p,e):
   if u ==p:
      return
   if u ==e[0] and p==e[1] :
      return False
   if u ==e[0] and p==e[2] :
      return True
   if u ==e[1] and p==e[2] :
      return False
   if u ==e[1] and p==e[0] :
      return True
   if u ==e[2] and p==e[1] :
      return True
   if u ==e[2] and p==e[0] :
      return False 
from discord.ext import commands
client = commands.Bot(command_prefix = ".")

def check(author):
    def inner_check(message):
        return message.author == author
    return inner_check
"""def drive_PlayerChoice(c):
   try:
      c.send(None)
   except StopIteration as e:
      return e.value"""
   	
   
       
@client.event
async def on_ready():
   print("Bot is ready")
@client.command()
async def play(ctx):
   await ctx.send("Welcome to Stone - Paper - Scissor \n A Game Made For Legends")
   await ctx.send("Rule : \nYou have to play five rounds of  Stone-Paper-scissor and who so ever have more points will win \nHope you enjoy the game!!")
   i=1
   u_count=0
   p_count=0
   while i<=5 :
      await ctx.send(f"Round {i}  : " )
      #e= False
      elmts=["Stone" , "Paper", "Scissor"]
      await ctx.send("What is your choice ( Stone , Paper , Scissor)\nPress 1,2,3 respectively")
      user_choice="Not Defined"
      
      playerChoice = await client.wait_for('message', check=check(ctx.author), timeout=30)
      if playerChoice.content=="1":
         user_choice= "Stone"
      elif playerChoice.content=="2":
         user_choice= "Paper"
      elif playerChoice.content=="3":
         user_choice= "Scissor"
      else:
         await ctx.send("Please enter a valid input")
         break
               
      pc_choice="Not Defined"
      pc_choice=random.choice(elmts)
      winner= cases( user_choice, pc_choice ,elmts ) 
      await ctx.send(f"Your choice : {user_choice}")
      await ctx.send(f"My choice: {pc_choice}")
      if winner == True :
         await ctx.send("You won this round !!!!")
         u_count+=1
      elif winner== False :
         await ctx.send("You lose this round !!!!")
         p_count+=1
      elif winner == None:
         await ctx.send("Draw!!!")
      i+=1
   await ctx.send(f"Your Total Points : {u_count}")
   await ctx.send("My Total Points : {p_count}")
   if u_count > p_count:
      await ctx.send("Hurray !!! You won ........")
   if u_count < p_count:
      await ctx.send("Sad !! You lose.........")
   if u_count ==p_count :
      await ctx.send("Oopss ..its a tie.....")

client.run("NzQxNjE4NzQxMzgwMzgyNzky.Xy6MRg.BhujsDqE1B8DOyqnOl3sLYX-YwI")