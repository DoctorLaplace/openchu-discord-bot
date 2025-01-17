import discord
import random
import asyncio
import time


class dataSocket():
    def __init__(self, data):
        self.data = None

    def setData(self, input):
        self.data = input

    def getData(self):
        return self.data






class ability():
    def __init__(self, name = "UNDEFINED_NAME", type = 0, description = "The Pokemon uses a move!", deathDesc = "The Pokemon doesn't feel so good Mr. Stark!"):
        self.name = name
        self.type = type
        self.description = description
        self.deathDesc = deathDesc





    def dealDamage(self, pokemonAttacking):
        if (self.type == 0):
            return pokemonAttacking.strength*3
        if (self.type == 1):
            return pokemonAttacking.dexterity*3
        if (self.type == 2):
            return pokemonAttacking.constitution*3
        if (self.type == 3):
            return pokemonAttacking.intelligence*3
        if (self.type == 4):
            return pokemonAttacking.wisdom*3
        if (self.type == 5):
            return pokemonAttacking.charisma*3










class abilitySet():
    def __init__(self):
        self.abilityGroup = []






class BattleArena():

    def __init__(self, player1, player2, pokemon1, pokemon2):
            self.player1 = None
            self.player2 = None

            self.pokemon1 = None
            self.pokemon2 = None

    def setPlayer1(self, p):
        self.player1 = p

    def setPlayer2(self, p):
        self.player2 = p

    def setPokemon(self, pat1, pat2):
        self.pokemon1 = pat1
        self.pokemon2 = pat2





class Pokemon():

    

    def __init__(self, strength = 100, dexterity = 0, constitution = 0, intelligence = 0, wisdom = 0, charisma = 0, hitpoints = 100, maxHitpoints = 100, 
                 name = "UNDEFINED POKEMON", picture = None, moveList = []):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

        self.maxHitpoints = maxHitpoints
        self.hitpoints = hitpoints
        self.name = name
        self.picture = picture

        self.moves = dataSocket([])
        self.abilities = abilitySet()


    def attack(self, target, movSignature):
        damage = 0
        if movSignature == 0:
            damage = self.attack_bodySlam(target)
        if movSignature == 1:
            damage = self.attack_doritoBurst(target)
        if movSignature == 2:
            damage = self.attack_dab(target)
        if target.hitpoints <= 0:
            target.hitpoints = 0
        return damage



    def isDeafeated(self):
        if (self.hitpoints <= 0):
            return True
        else:
            return False





    def attack_bodySlam(self, target):
        target.hitpoints -= self.strength*2
        return self.strength*2

    def attack_doritoBurst(self, target):
        target.hitpoints -= self.dexterity*2
        return self.dexterity*2

    def attack_dab(self, target):
        target.hitpoints -= self.charisma*999
        return self.charisma*999



    def getName(self):
        return self.name
    def getHitpoints(self):
        return self.hitpoints
    def getMaxHitpoints(self):
        return self.maxHitpoints
    def takeDamage(self, damage):
        self.hitpoints -= damage


    def getMoveList(self):
        return self.abilities.abilityGroup

    def getMoveListStr(self):
        string = ""
        for i in range(len(self.abilities.abilityGroup)):
            string += self.abilities.abilityGroup[i].name + " [" + str(i) + "]\n"
        return string






class MyClient(discord.Client):
    global count
    checkPlayer1 = False
    checkPlayer2 = False
    p1Set = False
    p2Set = False
    battleZone = BattleArena(None, None, None, None)
    battleActive = False
    battleChannel = None

    playerTurnNum = 1

    player1DataSocket = dataSocket(None)
    player2DataSocket = dataSocket(None)


    rkick = ability("Round House Kick", 0, "***<A> kicks the sh\*t out of <B>!***", "***<A> round house kicks <B> into a lifetime medical debt. <B> has been defeated!***")
    axekick = ability("Axe Kick", 0, "***<A> gives <B> scoliosis with a graceful axe kick!***","***<A> makes <B> 3 inches shorter from spinal compression! <B> has been defeated!***")
    dab = ability("Dab", 5, "***<A> drops mad disrepect on <B>!***", "***<B> disintigrates from unshielded exposure to pure dank!***")
    shrekAbilities = abilitySet()
    shrekAbilities.abilityGroup = [rkick, axekick, dab]
    pok1 = Pokemon(37, 17, 40, 14, 22, 97, 500, 500, "Shrek", None)
    pok1.abilities = shrekAbilities


    #fthrower = ability("flamethrower", 4, "***<a> uses a world war 2 flamethrower on <b>!***")
    #ifirework = ability("illegal firework", 1, "***<a> recklessly lights an illegal firework aimed at <b>!***")
    #hfive = ability("overly excited high-five", 5, "***<a> gives <b> a high five at mach 3!***")
    #darabilities = abilityset()
    #darabilities.abilitygroup = [fthrower, ifirework, hfive]
    #pok2 = pokemon(21, 24, 15, 12, 40, 27, 350, 350, "darmander", none)
    #pok2.abilities = darabilities


    bPeel = ability("Banana Peel", 1, "***<A> throws a slippery banana peel under <B>'s foot! <B> slips and goes flying!***", "***<B> activates their Life Alert™ and is taken out of the match!***")
    mTouch = ability("Meme Touch", 5, "***<B> is hit by <A>, and for a moment sees the Memeiverse!***", "***<B>'s eyes flare with light! The enlightenment is too much! In a brilliant burst <B> explodes into Doritos™ and Mountain Dew™***")
    wNumberOne = ability("We Are Number One", 3, "***<A> is Number One!***", "****<B> cannot handle <A>'s Aura, and forfeits!***")
    vWink = ability("Villianous Wink", 4, "***<A> gives <B> a villianous wink!***", "***<B> is too flustered to continue!***")
    robAbilities = abilitySet()
    robAbilities.abilityGroup = [bPeel, mTouch, wNumberOne, vWink]
    pok2 = Pokemon(8, 20, 18, 43, 58, 333, 400, 400, "Robbie Rotten", None)
    pok2.abilities = robAbilities





    #pok2 = Pokemon(10, 10, 10, 10, 10, 10, 100, 100, "Darmander", None)
    #pok2.moves.data = ['Flamethrower', 'Illegal Firework', 'Overly Excited High-Five']


    battleZone.setPokemon(pok1, pok2)

    spoofMode = False

    async def displayPokemonStatus(self, channel, pokemon):
        hpBar = "█"
        backBar = "░"
        healthStr = ""
        barStr = ""

        if pokemon.hitpoints < 0:
            pokemon.hitpoints = 0
        if pokemon.hitpoints > pokemon.maxHitpoints:
            pokemon.hitpoints = maxHitpoints



        pkHit = pokemon.getHitpoints()
        pkHitMax = pokemon.getMaxHitpoints()

        healthTicks =  round((pkHit / pkHitMax), 2)*50
        barTicks = 50 - healthTicks

        for i in range(int(healthTicks)):
            healthStr += hpBar
        for i in range(int(barTicks)):
            barStr += backBar

        await channel.send(">>> " + pokemon.getName() + ": " + healthStr + barStr +
                           "\nMoves:\n" + str(pokemon.getMoveListStr()) + "" 
                           #+ "Strength: " + str(pokemon.strength)
                           #+ " Dexterity: " + str(pokemon.dexterity)
                           #+ " Constitution: " + str(pokemon.constitution)
                           #+ " Intelligence: " + str(pokemon.intelligence)
                           #+ " Wisdom: " + str(pokemon.wisdom)
                           #+ " Charisma: " + str(pokemon.charisma)
                           )


    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')  

        guild = self.get_guild(801480291305783326)
        channel = self.get_channel(801480291305783333)


        pikamood = False
        # pikamood
        if pikamood == True:
            await channel.send("Open-chu uses vibe")
            counter = 0
            messages = await channel.history(limit=50).flatten()
            for i in range(5):
                randomNum = random.randint(1,3)
                randomHistory = random.randint(1,50)
                if randomNum == 1:
                    await messages[randomHistory].add_reaction("💖")
                if randomNum == 2:
                    await messages[randomHistory].add_reaction("❤")
                if randomNum == 3:
                    await messages[randomHistory].add_reaction("💜")
                if randomNum == 4:
                    await messages[randomHistory].add_reaction("💛")
                if randomNum == 5:
                    await messages[randomHistory].add_reaction("💝")
            

    async def on_message(self, message):
        global count
        

        if message.author == self.user and self.spoofMode == False:
            return

        if message.content == 'Openchu spoof':
            if self.spoofMode == False:
                self.spoofMode = True
                await message.channel.send("```Spoofmode On```")
            else:
                self.spoofMode = False
                await message.channel.send("```Spoofmode Off```")

        if message.content == 'o1' and self.spoofMode == True:
            await message.channel.send("I am player 2")
        if message.content == 'o2' and self.spoofMode == True:
            await message.channel.send("Darmander use glock!")




        if message.content == 'Hello Openchu!':
            await message.channel.send("Pika!")

        battlemode = True
        # pikamood
        if (message.content == 'Initiate Battle' or message.content == 'i1') and battlemode == True:
            await message.channel.send("Players! Are you ready?!")
            self.checkPlayer1 = True
            self.checkPlayer2 = True
            self.battleChannel = message.channel
            await self.lockingParticipants(message.channel)
        
        if message.content == 'p1' and self.checkPlayer1 == True:
            checkPlayer1 = False
            self.battleZone.setPlayer1(message.author)
            self.p1Set = True
            await message.channel.send("Player one locked in as " + message.author.name + "!...")
            print(message.author)

        if message.content == 'p2' and self.checkPlayer2 == True:
            checkPlayer2 = False
            self.battleZone.setPlayer2(message.author)
            self.p2Set = True
            await message.channel.send("Player two locked in as " + message.author.name + "!...")
            print(message.author)


        if self.battleZone.player1 != None:
            if message.author.id == self.battleZone.player1.id:
                self.player1DataSocket.setData(message.content)
                print("Player one socket is now: " + message.content)
                #print(str(message.author.id) + " ==? " + str(self.battleZone.player1.id))
                #await message.channel.send("Player one socket is now: " + message.content)


        if self.battleZone.player2 != None:
            if message.author.id == self.battleZone.player2.id:
                self.player2DataSocket.setData(message.content)
                print("Player two socket is now: " + message.content)
                #await message.channel.send("Player two socket is now: " + message.content)




        if message.content == 'Battle Cycle':
            self.battleChannel = message.channel
            self.battleActive = True
            await lockingParticipants()
            #await self.battleThinkCycle()
            print("Program is free now.")

        if message.content == 'End Battle Cycle':
            self.battleActive = False



    async def lockingParticipants(self, messageChannel):
        lookingForPlayers = True
        while lookingForPlayers == True:
            print("Searching for players...")
            await messageChannel.send("Searching for players...")
            await asyncio.sleep(1)
            if self.p1Set == True and self.p2Set == True:
                lookingForPlayers = False
                self.battleChannel = messageChannel
                self.battleActive = True
                await self.battleThinkCycle()
                print("Program is free now.")
        print("No longer looking for players...")
        await messageChannel.send("No longer looking for players...")
            




    async def battleThinkCycle(self):
        count = 0
        print(self.battleZone.pokemon2.name)
        await self.battleChannel.send("A battle is about to begin between " + self.battleZone.player1.name + " and " + self.battleZone.player2.name + "!...")
        while self.battleActive == True:
            count += 1
            #await self.battleChannel.send("Battle heartbeat " + str(count) + " - It is player" + str(self.playerTurnNum) + "'s turn")
            await asyncio.sleep(2)


            if self.playerTurnNum == 1:
                turnCount = 0
                takenTurn = False
                await self.battleChannel.send(self.battleZone.player1.name + " it is your turn!...")
                await self.displayPokemonStatus(self.battleChannel,self.battleZone.pokemon1)
                while takenTurn == False and self.battleActive == True:
                    turnCount += 1
                    #await self.battleChannel.send("Primed")
                    await asyncio.sleep(2)
                    if self.player1DataSocket.getData() != None:
                        if len(self.player1DataSocket.getData()) > 3 and self.player1DataSocket.getData()[0] == 'a':
                            commandNum = self.player1DataSocket.getData()[2]

                            tempDesc = self.battleZone.pokemon1.abilities.abilityGroup[int(commandNum)].description
                            tempDesc = tempDesc.replace("<A>", self.battleZone.pokemon1.name)
                            tempDesc = tempDesc.replace("<B>", self.battleZone.pokemon2.name)

                            await self.battleChannel.send(tempDesc)                
                            damage = 0
                            description = ""
                            damage = self.battleZone.pokemon1.abilities.abilityGroup[int(commandNum)].dealDamage(self.battleZone.pokemon1)
                            self.battleZone.pokemon2.hitpoints -= damage
                            await self.battleChannel.send("***" + str(self.battleZone.pokemon2.name) + " takes " + str(damage) + " damage!...***")

                            if (self.battleZone.pokemon2.isDeafeated()):
                                defeatDesc = self.battleZone.pokemon1.abilities.abilityGroup[int(commandNum)].deathDesc
                                defeatDesc = defeatDesc.replace("<A>", self.battleZone.pokemon1.name)
                                defeatDesc = defeatDesc.replace("<B>", self.battleZone.pokemon2.name)
                                await self.battleChannel.send(defeatDesc)

                            self.playerTurnNum = 2
                            takenTurn = True
                            self.player1DataSocket.setData(None)
                            self.player2DataSocket.setData(None)



            if self.playerTurnNum == 2:
                turnCount = 0
                takenTurn = False
                await self.battleChannel.send(self.battleZone.player2.name + " it is your turn!...")
                await self.displayPokemonStatus(self.battleChannel,self.battleZone.pokemon2)
                while takenTurn == False and self.battleActive == True:
                    turnCount += 1
                    #await self.battleChannel.send("Primed")
                    await asyncio.sleep(2)
                    if self.player2DataSocket.getData() != None:
                        if len(self.player2DataSocket.getData()) > 3 and self.player2DataSocket.getData()[0] == 'a':
                            commandNum = self.player2DataSocket.getData()[2]

                            tempDesc = self.battleZone.pokemon2.abilities.abilityGroup[int(commandNum)].description
                            tempDesc = tempDesc.replace("<A>", self.battleZone.pokemon2.name)
                            tempDesc = tempDesc.replace("<B>", self.battleZone.pokemon1.name)

                            await self.battleChannel.send(tempDesc)                
                            damage = 0
                            description = ""
                            damage = self.battleZone.pokemon2.abilities.abilityGroup[int(commandNum)].dealDamage(self.battleZone.pokemon2)
                            self.battleZone.pokemon1.hitpoints -= damage
                            await self.battleChannel.send("***" + str(self.battleZone.pokemon1.name) + " takes " + str(damage) + " damage!...***")

                            if (self.battleZone.pokemon1.isDeafeated()):
                                defeatDesc = self.battleZone.pokemon2.abilities.abilityGroup[int(commandNum)].deathDesc
                                defeatDesc = defeatDesc.replace("<A>", self.battleZone.pokemon2.name)
                                defeatDesc = defeatDesc.replace("<B>", self.battleZone.pokemon1.name)
                                await self.battleChannel.send(defeatDesc)

                            self.playerTurnNum = 1
                            takenTurn = True
                            self.player1DataSocket.setData(None)
                            self.player2DataSocket.setData(None)


   








        await self.battleChannel.send("The battle has ended!...")


        





botkey = None
# Place the path to your external botkey text file. This makes sure that Git does not commit your botkey to the open internet!
with open('C:/Users/silve/Desktop/Discord Bots/Openchu/Openchu_Key.txt', 'r') as file:
    botkey = file.read().replace('\n', '')
    print(botkey)

client = MyClient()
client.run(botkey)