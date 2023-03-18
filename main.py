# Octopath Traveler 2 Build Randomizer
import random

itemSword = [
    "Conquerer's Sword",
    "Serpent Slayer",
    "Battle-Tested Blade",
    "Lost Tribe's Blade",
    "Eclipse Edge",
    "Sword of Oaths",
    "Divine Splendor",
    "Expert's Obsidian Edge",
    "Giant's Blade",
    "Forbidden Blade",
    "Skypiercer",
    "Sanctum Sword",
    "Keepsake Sword",
    "Hypno Sword",
    "Evil Slayer",
    "Starsplitter",
    "Ogre's Bane",
    "Bastard Sword",
    "Great Blade",
    "Guardian's Iceblade",
    "Bloodsucker",
    "Soulsucker"
    "Aegis Sword",
    "Master Rod",
    "Firestarter",
    "Clan Mei Sword",
    "Stonesplitter",
    "Enchanted Edge",
    "Crescent Saber",
    "Reaper's Blade",
    "Quartz Blade",
    "Warrior's Sword",
    "Little Crow",
    "Refined Sword",
    "Heavy Blade",
    "Champion's Sword",
    "Heretic's Greatsword",
    "Magic Eater",
    "Silver Sword",
    "Guard's Saber",
    "Spirit Scimitar",
    "Broadsword",
    "Iron Blade",
    "Nameless Sword",
    "Long Sword",
    "Knight's Sword",
    "Imitation Sword",
    "Rotted Wood",
    "Sword of the Sands",
    "Desert Blade",
    "Thief's Sword",
    "Makeshift Sword",
]

itemPolearm = [
    "Battle-Tested Spear",
    "Lost Tribe's Spear",
    "Gravity Lance",
    "Spear of Strength",
    "Tornado Glaive",
    "Forbidden Spear",
    "Fire Dragon's Glaive",
    "Monster Bone Spear",
    "Thunder's Roar",
    "Obsidian Lance",
    "Seraphim Spear",
    "Venom Lance",
    "Well-Worn Pole",
    "Crimson Spear",
    "Hyperion Spear",
    "Rare Metal Glaive",
    "Sea God's Spear",
    "Nightmare Glaive",
    "Clan Mei Spear",
    "Paladin's Lance",
    "Lightning Glaive",
    "Scorched Bone Spear",
    "Heavy Bone Spear",
    "Matching Trident",
    "Soldier's Spear",
    "Fuscina",
    "Master Harpoon",
    "Vanguard's Javelin",
    "Gluttonous Glaive",
    "Slashing Glaive",
    "Steel Lance",
    "Sandstorm Spear",
    "Spear of Sleep",
    "War Glaive",
    "Memorial Harpoon",
    "Bone Spear",
    "Lance",
    "Long Spear",
    "Spear",
    "Imitation Spear",
    "Desert Spear",
    "Distinguished Lance",
    "Handmade Spear",
    "Makeshift Spear"
]

itemDagger = [
    "Dancer's Blade",
    "Battle-Tested Dagger",
    "Lost Tribe's Dagger",
    "Tonfa",
    "Vengeful Knife",
    "Ruinous Dagger",
    "Diamond Dagger",
    "Dagger in the Rough",
    "Mooneater",
    "Forbidden Dagger",
    "Lockpick",
    "Bloodstained Knife",
    "Breaker's Blade",
    "Ornate Dagger",
    "Dagger of Seclusion",
    "Assassin's Dagger",
    "Mysterious Dagger",
    "Champion Seeker",
    "Marietta",
    "Piercing Dagger",
    "Doombreaker",
    "Wind Whisperer",
    "Poison Dagger",
    "Moonfang",
    "Obsidian Dagger",
    "Black Dagger",
    "Stealthy Knife",
    "Drifting Dagger",
    "Stinging Dagger",
    "Jade Dagger",
    "Magus Knife",
    "Crystal Dagger",
    "Swordbreaker",
    "Quartz Dagger",
    "Falcon Knife",
    "Handbreaker",
    "Kukri",
    "Needle Dagger",
    "Bronze Knife",
    "Dagger",
    "Silver-Plated Knife",
    "Thief's Dagger",
    "Snakebite",
    "Fruit Knife",
    "Sharp Stone",
    "Makeshift Knife"
]

itemAxe = [
    "Lionheart's Axe",
    "Battle-Tested Axe",
    "Lost Tribe's Axe",
    "Reaper's Sickle",
    "Hero's Axe",
    "Forbidden Axe",
    "Flayer's Admonishment",
    "Royal Guard's Hatchet",
    "Axe of the Conquerer",
    "Cleaver of Destruction",
    "Stupefying Stone Axe",
    "Icy Axe",
    "Imperial Axe",
    "Frontier Axe",
    "Contaminated Iron Ingot",
    "Double Tomahawk",
    "Guardian's Great Axe",
    "Dark Slasher",
    "Pirate's Axe",
    "Platinum Hatchet",
    "Quartz Axe",
    "Grand Cleaver",
    "Bone Cleaver",
    "Guardian's Axe",
    "Guillotine's Blade",
    "Silver Hatchet",
    "Frost Axe",
    "Rock Cleaver",
    "Axe of Avarice",
    "Helmcleaver",
    "Strong Axe",
    "Poisoned Hatchet",
    "Battle Hatchet",
    "Guard's Great Axe",
    "Iron Axe",
    "War Axe",
    "Woodcutter's Great Axe",
    "Beastling's Hatchet",
    "Handaxe",
    "Woodcutter's Axe",
    "Rotted Axe",
    "Demolition Axe",
    "Small Axe",
    "Snake Fang",
    "Makeshift Axe"
]

itemBow = [
    "Hunter's Bow",
    "Battle-Tested Bow",
    "Lost Tribe's Bow",
    "Exorcising Bow",
    "Floyd's Neo Bow",
    "Befuddling Greatbow",
    "Forbidden Bow",
    "Bow of Carnage",
    "Protector's Bow",
    "Art of Archery",
    "Leviathan Greatbow",
    "Tornado Bow",
    "Mechanical Bow",
    "Evening Mist",
    "Master's Greatbow",
    "Ancient Bow",
    "King of Beasts",
    "Black Bow",
    "Combat Bow",
    "Absolute Zero Bow",
    "Sniper's Bow",
    "Expert's Bow",
    "Raging Beast",
    "Marksman's Bow",
    "Battle Bow",
    "Knight's Greatbow",
    "Cupid's Bow",
    "Steel Bow",
    "Soldier's Bow",
    "Mirage Bow",
    "Sailor's Bow",
    "Assault Bow",
    "Tenacious Bow",
    "Shadow Bow",
    "Guard's Greatbow",
    "Traveler's Bow",
    "Giant's Bow",
    "Composite Bow",
    "Beastling's Bow",
    "Shortbow",
    "Bow",
    "Handmade Bow",
    "Makeshift Bow"
]

itemStaff = [
    "Spiritlord's Staff",
    "Battle-Tested Staff",
    "Lost Tribe's Staff",
    "Forbidden Staff",
    "Sunshadow Staff",
    "Staff of Carnage",
    "Diamond Rod",
    "Great Sage's Staff",
    "Bellowing Baton",
    "Sacred Flame Staff",
    "Rough-Hewn Rod",
    "Abyssal Rod",
    "Hallowed Rod",
    "Ancient Staff",
    "Yggdrasil Staff",
    "Psychic Staff",
    "Wisdom Wand",
    "Chef's Ladle",
    "Quartz Rod",
    "Fortune Wand",
    "Sapphire Rod",
    "Jade Staff",
    "Magus Wand",
    "Oak Staff",
    "Magic Breaker",
    "Aegis Mace",
    "Conjurer's Staff",
    "Mage Wand",
    "Rod of Wisdom",
    "Lapis Rod",
    "Light Wand",
    "Thunder Mace",
    "Stone Rod",
    "Wooden Staff",
    "Mace",
    "Sinner's Staff",
    "Pilgrim Rod",
    "Charm Rod",
    "Flamebringer's Staff",
    "Staff of Judgement",
    "Stick",
    "Giant's Club",
    "Morning Star",
    "Flail",
    "Makeshift Staff"
]

itemShield = [
    "Cursed Shield",
    "Battle-Tested Shield",
    "Forbidden Shield",
    "Wise King's Shield",
    "Shield of Strength",
    "Giant Shield",
    "Aegis Shield",
    "Protector's Shield",
    "Adamantine Buckler",
    "Sun Shield",
    "Quartz Shield",
    "Swift Shield",
    "Heavy Greatshield",
    "Diamond Shield",
    "Platinum Shield",
    "Master's Shield",
    "Shield of Serenity",
    "Spiked Shield",
    "Plate Buckler",
    "Silver Shield",
    "Tattered Sacred Shield",
    "Crested Greatshield",
    "Feather Shield",
    "Shell Buckler",
    "Guard's Shield",
    "Sturdy Shield",
    "Iron Shield",
    "Rabbit Shield",
    "Weathered Treasure Shield",
    "Kite Shield",
    "Bronze Shield",
    "Leather Buckler",
    "Round Shield",
    "Buckler",
    "Resplendent Shield",
    "Gray Shield",
    "Small Shield",
    "Wooden Shield",
    "Bodyguard's Vantage",
    "Makeshift Shield"
]

itemHelmet = [
    "Cursed Helm",
    "Mechanical Top Hat",
    "Imperial Helm",
    "Dragon's Helm",
    "Gimmick Goggles",
    "Royal Guard's Helm",
    "Great Helm",
    "Art of Disguise",
    "Mermaid Circlet",
    "Dazzling Tiara",
    "Gaudy Hat",
    "Cloth Headband",
    "Forgotten Hat",
    "Antique Ceremonial Mask",
    "Lighthouse Keeper's Bandana",
    "Platinum Helm",
    "Ancient Circlet",
    "Soldier's Hat",
    "Fighter's Headband",
    "Knight's Helm",
    "Starlight Hat",
    "Horned Helm",
    "Worker's Helmet",
    "Hasty Helm",
    "Silent Bandana",
    "Black Cap",
    "Gelid Helm",
    "Skull Helm",
    "Cassius",
    "Battle Bandana",
    "Guard's Helm",
    "Bronze Helm",
    "Guard's Hat",
    "Headgear",
    "Fur Cap",
    "Hide Hood",
    "Silver Hairpiece",
    "Peddler's Feathered Cap",
    "Feathered Hat",
    "Pointed Hat",
    "Festival Garland",
    "Sanctum Knight's Helm",
    "Leather Helm",
    "Pathfinder's Hat",
    "Cloth Hood",
    "Gray Helm",
    "Black Hood",
    "Leather Hat",
    "Ordinary Hat"
]

itemArmor = [
    "Cursed Armor",
    "Dragon Mail",
    "Desert Plate",
    "Sublime Ornamental Armor",
    "Vest of Joy",
    "Imperial Armor",
    "Royal Guard's Mail",
    "Star's Gown",
    "Quartz Robe",
    "Quick Cloak",
    "Blessed Vestments",
    "Resplendent Costume",
    "Butler's Tailcoat",
    "Lightning Armor",
    "Conjurer's Raiment",
    "Ornate Costume",
    "Antique Coat",
    "Protector's Vestments",
    "Platinum Mail",
    "Knight's Armor",
    "Desert Armor",
    "Mage's Robe",
    "White Wolf Scarf",
    "Bone Mail",
    "Acrobat's Mantle",
    "Nimble Mantle",
    "Denim Work Clothes",
    "Dojo Hakama",
    "Dyed Clothes",
    "Elemental Robe",
    "Falcon Coat",
    "Gorgeous Sari",
    "Iron Mail",
    "Guard's Armor",
    "Beastling Battle Armor",
    "Sailor's Vest",
    "Wind Robe",
    "Copper Breastplate",
    "Hunting Attire",
    "Quality Vest",
    "Fur Robe",
    "Pilgrim's Robe",
    "Simple Costume",
    "Feather Mantle",
    "Champion's Garb",
    "Charm Robe",
    "Traveler's Mantle",
    "Sanctum Knight's Armor",
    "Fur Armor",
    "Old Armor",
    "Worker's Jacket",
    "Desert Attire",
    "Frog Membrane",
    "Tough Waistcoat",
    "Prisoner's Clothes",
    "Black Atttire",
    "Robe",
    "Tattered Dress",
    "Apothecary's Attire",
    "Villager's CLothes"
]

itemAccessory = [
    "Spurning Ribbon",
    "Alluring Ribbon",
    "EXP Augmentor",
    "JP Augmentor",
    "Brooch of Joy",
    "Cait Powder",
    "Octopuff Pot",
    "Dragon's Scarf",
    "Beastly Scarf",
    "Warding Necklace",
    "Divine Necklace",
    "Melia's Amulet",
    "Enfeebling Amulet",
    "Prosperity Charm",
    "Charm of Compassion",
    "Blessing in Disguise",
    "Finisher's Claws",
    "Stone of Truth",
    "Fang of Ferocity",
    "Gale Feather",
    "Eye of Calamity",
    "Victory Ring",
    "Hand-Sewn Robes",
    "Foreign Ring",
    "Alpione's Amulet",
    "Librarian's Amulet",
    "Champion's Belt",
    "Mikka's Amulet",
    "Laila's Amulet",
    "Sisters' Amulet",
    "Jade Ring",
    "Shadowsage Necklace",
    "Rosary of Redemption",
    "Coat of Arms",
    "Blazon of Protection",
    "Scarlet Stone of Protection",
    "Crescent Moon Necklace",
    "Moonshell Necklace",
    "Moonshell Bracelet",
    "Physical Belt",
    "Mental Belt",
    "Mighty Belt",
    "Elemental Augmentor",
    "Guardian Amulet",
    "Elemental Ward",
    "Empowering Necklace",
    "Stimulating Necklace",
    "Protective Necklace",
    "Unerring Necklace",
    "Enlightening Necklace",
    "Sprightly Necklace",
    "Critical Necklace",
    "Empowering Bracelet",
    "Stimulating Bracelet",
    "Protective Bracelet",
    "Unerring Bracelet",
    "Enlightening Bracelet",
    "Sprightly Bracelet",
    "Critical Bracelet",
    "Empowering Ring",
    "Stimulating Ring",
    "Protective Ring",
    "Unerring Ring",
    "Enlightening Ring",
    "Sprightly Ring",
    "Critical Ring",
    "Falcon Ring",
    "Empowering Earring",
    "Stimulating Earring",
    "Protective Earring",
    "Unerring Earring",
    "Enlightening Earring",
    "Sprightly Earring",
    "Critical Earring",
    "Ancient Necklace",
    "Wargod's Talisman",
    "Silver Locket",
    "Angel's Ring",
    "Traveler's Charm",
    "Tattered Shoes",
    "Inferno Amulet",
    "Blizzard Amulet",
    "Tempest Amulet",
    "Thunderstorm Amulet",
    "Void Amulet",
    "Gleaming Amulet",
    "Fire Amulet",
    "Ice Amulet",
    "Wind Amulet",
    "Lightning Amulet",
    "Dark Amulet",
    "Light Amulet",
    "Antidote Stone",
    "Wakeful Stone",
    "Articulate Stone",
    "Bright Stone",
    "Calming Stone",
    "Clarity Stone",
    "Conscious Stone",
    "Vivifying Stone"
]

supportSkill = [
    "Bolstering Break",
    "Summon Strength",
    "Latent Power Plus",
    "Deal More Damage",
    "The Show Goes On",
    "Ever Evasive",
    "Hard Worker",
    "Invigorate and Inspire",
    "Grows on Trees",
    "Boost-Start",
    "Hang Tough",
    "Full Power",
    "Resilience",
    "Inner Strength",
    "Evil Ward",
    "Rise Again"
    "Incidental Attack",
    "Fleetfoot",
    "Ensnare",
    "Life in the Shadows",
    "Heighten Senses",
    "Eagle Eye",
    "More Rare Monsters",
    "Salt the Wound",
    "Vigorous Victor",
    "Hale and Hearty",
    "Inspiriting Break",
    "Preventative Measures",
    "A Step Ahead",
    "Upgraded Accessories",
    "BP in Adversity",
    "Fruits of Labor",
    "Master of Offense",
    "Peak Performance",
    "Invigorating Break",
    "Arms Refinement",
    "Purification",
    "SP Saver",
    "Divine Wrath",
    "BP Regeneration",
    "SP Recovery",
    "Lasting Memory",
    "Price of Power",
    "Of Equal Might",
    None
]

job = [
    "Warrior",
    "Dancer",
    "Merchant",
    "Scholar",
    "Cleric",
    "Thief",
    "Hunter",
    "Apothecary",
    "Inventor",
    "Armsmaster",
    "Conjurer",
    "Arcanist"
]
"""
print("Job: " + random.choice(job))
print("Support skill: " + random.choice(supportSkill))
print("Support skill: " + random.choice(supportSkill))
print("Support skill: " + random.choice(supportSkill))
print("Support skill: " + random.choice(supportSkill))
print("Sword: " + random.choice(itemSword))
print("Polearm: " + random.choice(itemPolearm))
print("Dagger: " + random.choice(itemDagger))
print("Axe: " + random.choice(itemAxe))
print("Bow: " + random.choice(itemBow))
print("Staff: " + random.choice(itemStaff))
print("Shield: " + random.choice(itemShield))
print("Helmet: " + random.choice(itemHelmet))
print("Armor: " + random.choice(itemArmor))
print("Accessory: " + random.choice(itemAccessory))
print("Accessory: " + random.choice(itemAccessory))
"""

#                0Job  1Skl  2Skl  3Skl  4Skl  5Primary
skillOsvald   = [None, None, None, None, None, "Scholar"]
skillCastti   = [None, None, None, None, None, "Apothecary"]
skillTemenos  = [None, None, None, None, None, "Cleric"]
skillOchette  = [None, None, None, None, None, "Hunter"]
skillPartitio = [None, None, None, None, None, "Merchant"]
skillAgnea    = [None, None, None, None, None, "Dancer"]
skillThrone   = [None, None, None, None, None, "Thief"]
skillHikari   = [None, None, None, None, None, "Warrior"]


#                0Swd  1Plm  2Dgr  3Axe  4Bow  5Stf  6Shd  7Hlm  8Arm  9Ac1  10Ac2
equipOsvald   = [None, None, None, None, None, None, None, None, None, None, None]
equipCastti   = [None, None, None, None, None, None, None, None, None, None, None]
equipTemenos  = [None, None, None, None, None, None, None, None, None, None, None]
equipOchette  = [None, None, None, None, None, None, None, None, None, None, None]
equipPartitio = [None, None, None, None, None, None, None, None, None, None, None]
equipAgnea    = [None, None, None, None, None, None, None, None, None, None, None]
equipThrone   = [None, None, None, None, None, None, None, None, None, None, None]
equipHikari   = [None, None, None, None, None, None, None, None, None, None, None]


travelerOsvald = [skillOsvald, equipOsvald, "Osvald"]
travelerCastti = [skillCastti, equipCastti, "Castti"]
travelerTemenos = [skillTemenos, equipTemenos, "Temenos"]
travelerOchette = [skillOchette, equipOchette, "Ochette"]
travelerPartitio = [skillPartitio, equipPartitio, "Partitio"]
travelerAgnea = [skillAgnea, equipAgnea, "Agnea"]
travelerThrone = [skillThrone, equipThrone, "Throné"]
travelerHikari = [skillHikari, equipHikari, "Hikari"]

travelerOctopath = [travelerOsvald,
                    travelerCastti,
                    travelerTemenos,
                    travelerOchette,
                    travelerPartitio,
                    travelerAgnea,
                    travelerThrone,
                    travelerHikari]

# Return random equipment. Item defines type of equipment.
def randomEquip(item):
    match item:
        case 0:
            return random.choice(itemSword)
        case 1:
            return random.choice(itemPolearm)
        case 2:
            return random.choice(itemDagger)
        case 3:
            return random.choice(itemAxe)
        case 4:
            return random.choice(itemBow)
        case 5:
            return random.choice(itemStaff)
        case 6:
            return random.choice(itemShield)
        case 7:
            return random.choice(itemHelmet)
        case 8:
            return random.choice(itemArmor)
        case 9:
            return random.choice(itemAccessory)
        case 10:
            return random.choice(itemAccessory)
        case _:
            return None

# Return a random job.
# If the primary job is rolled, use no subjob.
# Reroll if there are more subjobs than contracts.
def randomJob(skillTraveler, octopathTraveler):
    while True:
        subjob = random.choice(job)

        # Check for too many duplicate subjobs
        count = 0
        for traveler in octopathTraveler:
            if traveler[0][0] == subjob:
                count = count + 1

        if subjob == "Arcanist" or subjob == "Conjurer" or subjob == "Armsmaster" or subjob == "Inventor":
            limit = 1
        else:
            limit = 3

        if count <= limit:
            if subjob == skillTraveler[5]:
                subjob = None
            return subjob



# Assign random subjob and support skills.
# Duplicate support skills are rerolled.
def randomJobSkills(skillTraveler, octopathTraveler):
    skillTraveler[0] = randomJob(skillTraveler, octopathTraveler)

    skillTraveler[1] = random.choice(supportSkill)

    skillTraveler[2] = random.choice(supportSkill)
    while skillTraveler[2] == skillTraveler[1]:
        if skillTraveler[2] == None:
            break
        else:
            skillTraveler[2] = random.choice(supportSkill)

    skillTraveler[3] = random.choice(supportSkill)
    while skillTraveler[3] == skillTraveler[2] or skillTraveler[3] == skillTraveler[2]:
        if skillTraveler[3] == None:
            break
        else:
            skillTraveler[3] = random.choice(supportSkill)

    skillTraveler[4] = random.choice(supportSkill)
    while skillTraveler[4] == skillTraveler[1] or skillTraveler[4] == skillTraveler[2] or skillTraveler[4] == skillTraveler[3]:
        if skillTraveler[4] == None:
            break
        else:
            skillTraveler[4] = random.choice(supportSkill)


# Assign random equipment.
# If equipment can't be used, use None.
def randomEquipment(travelerEquipment, travelerSkills):
    primaryJob = travelerSkills[5]
    subJob = travelerSkills[0]
    sword = False
    polearm = False
    dagger = False
    axe = False
    bow = False
    staff = False

    if primaryJob == "Scholar" or subJob == "Scholar":
        staff = True
    if primaryJob == "Apothecary" or subJob == "Apothecary":
        axe = True
    if primaryJob == "Cleric" or subJob == "Cleric":
        staff = True
    if primaryJob == "Hunter" or subJob == "Hunter":
        axe = True
        bow = True
    if primaryJob == "Merchant" or subJob == "Merchant":
        polearm = True
        bow = True
    if primaryJob == "Dancer" or subJob == "Dancer":
        dagger = True
    if primaryJob == "Thief" or subJob == "Thief":
        sword = True
        dagger = True
    if primaryJob == "Warrior" or subJob == "Warrior":
        sword = True
        polearm = True
    if subJob == "Inventor":
        sword = True
        axe = True
    if subJob == "Arcanist":
        dagger = True
        staff = True
    if subJob == "Armsmaster":
        sword = True
        polearm = True
        dagger = True
        axe = True
        bow = True
        staff = True
    if subJob == "Conjurer":
        bow = True
        staff = True

    if sword == True:
        travelerEquipment[0] = random.choice(itemSword)
    else:
        travelerEquipment[0] = None

    if polearm == True:
        travelerEquipment[1] = random.choice(itemPolearm)
    else:
        travelerEquipment[1] = None

    if dagger == True:
        travelerEquipment[2] = random.choice(itemDagger)
    else:
        travelerEquipment[2] = None

    if axe == True:
        travelerEquipment[3] = random.choice(itemAxe)
    else:
        travelerEquipment[3] = None

    if bow == True:
        travelerEquipment[4] = random.choice(itemBow)
    else:
        travelerEquipment[4] = None

    if staff == True:
        travelerEquipment[5] = random.choice(itemStaff)
    else:
        travelerEquipment[5] = None

    travelerEquipment[6] = random.choice(itemShield)
    travelerEquipment[7] = random.choice(itemHelmet)
    travelerEquipment[8] = random.choice(itemArmor)
    travelerEquipment[9] = random.choice(itemAccessory)
    travelerEquipment[10] = random.choice(itemAccessory)

def randomBuild(traveler, octopathTraveler):
    randomJobSkills(traveler[0], octopathTraveler)
    randomEquipment(traveler[1], traveler[0])

def randomOctopath(travelers):
    randomBuild(travelers[0], travelers)
    randomBuild(travelers[1], travelers)
    randomBuild(travelers[2], travelers)
    randomBuild(travelers[3], travelers)
    randomBuild(travelers[4], travelers)
    randomBuild(travelers[5], travelers)
    randomBuild(travelers[6], travelers)
    randomBuild(travelers[7], travelers)

def results(travelers):
    for traveler in travelers:
        print(traveler[2] + "'s Build")
        print("Secondary Job: " + str(traveler[0][0]))
        print("Support Skill 1: " + str(traveler[0][1]))
        print("Support Skill 2: " + str(traveler[0][2]))
        print("Support Skill 3: " + str(traveler[0][3]))
        print("Support Skill 4: " + str(traveler[0][4]), end="\n\n")
        if traveler[1][0] != None:
            print("Sword: " + traveler[1][0])
        if traveler[1][1] != None:
            print("Polearm: " + traveler[1][1])
        if traveler[1][2] != None:
            print("Dagger: " + traveler[1][2])
        if traveler[1][3] != None:
            print("Axe: " + traveler[1][3])
        if traveler[1][4] != None:
            print("Bow: " + traveler[1][4])
        if traveler[1][5] != None:
            print("Staff: " + traveler[1][5])
        print("Shield: " + traveler[1][6])
        print("Headgear: " + traveler[1][7])
        print("Armor: " + traveler[1][8])
        print("Accessory 1: " + traveler[1][9])
        print("Accessory 2: " + traveler[1][10], end="\n\n\n\n\n")

print("Octopath Traveler 2 Build Randomizer", end="\n\n\n")

randomOctopath(travelerOctopath)
results(travelerOctopath)
input()