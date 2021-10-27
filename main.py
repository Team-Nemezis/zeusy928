import datetime
import random
import time
from discord.ext import commands
from discord.utils import get
import discord
import praw
from pantheon import pantheon
import asyncio
import numpy

client = discord.Client()

reddit = praw.Reddit(
    client_id="902889726950903868",
    client_secret="_IZsW0edDK9XMNJF3EsjUxR2SMXmmXCZ",
    user_agent="my user agent"
)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    global meme
    var = ("""
                            Copyright © ZEUS PVT. LTD 2020 All Rights Reserved

            All files and information contained in this program are copyright by Zeus Production, and may 
            not be duplicated, copied, modified or adapted, in any way without our written permission. 
            Our program may contain our service marks or trademarks as well as those of our affiliates 
            or other companies, in the form of words, graphics, and logos. Your use of our program or 
            Services does not constitute any right or license for you to use our service marks or trademarks,
            without the prior written permission of Zeus Production. Our Content, as found within our 
            programs and Services, is protected under United States and foreign copyrights. The copying, 
            redistribution,use or publication by you of any such Content, is strictly prohibited. Your use of 
            our programs and Services does not grant you any ownership rights to our Content.
            """)
    roast = ["You are the reason why god created middle finger bro",
             "Roses are red, Violets are blue what the hell happened to you",
             "If your brain was dynamite, there wouldn’t be enough to blow your hat off.",
             "You are more disappointing than an unsalted pretzel.",
             "Light travels faster than sound which is why you seemed bright until you spoke.",
             "You have so many gaps in your teeth it looks like your tongue is in jail.",
             "I’ll never forget the first b we met. But I’ll keep trying.", "Your face makes onions cry.",
             "You look so pretty. Not at all gross, today.", "I’m not insulting you, I’m describing you.",
             "You are the human version of period cramps",
             "Roses are red, Violets are blue i've 5 fingers and the middles one is for you"]

    therivili = ['poda myre', 'oombikko naye', 'poda patti', 'po nayinte mone', 'vedichi', 'poda kunda', 'vaapa myre',
                 'achanod vilikan para kunne', 'poda thayyoli',
                 'po polayadi mone', 'fuck you', 'getlost dickhead', 'son of a bitch, ', 'pissoff', 'asshole',
                 'bastard', 'cunt']
    users = ['Aashin', 'Gourigay', 'Nutz_shibu', 'Abhi', 'Berry', 'Amartya', 'Disco kundi', 'Valimol'
                                                                                            "Milan", 'Vyshnav', ]
    league_players = ['KakoosMan', 'IronSheddi', 'Zeusy928', 'MARTy69', 'bussydestroyer', 'CringeLordXxX',
                      'NUTZZ SHIBU', 'DiscoKundi']

    def remove(string):
        return string.replace(" ", "")

    if message.content.startswith("$teamsel"):
        teamnum = message.content

        random.shuffle(league_players)
        team1 = league_players[0], league_players[1], league_players[2], league_players[7]
        team2 = league_players[3], league_players[4], league_players[5], league_players[6]

        await message.channel.send("\n\n****```TEAM 1```****")

        for i in team1:
            await message.channel.send(i)
        await message.channel.send("\n\n****```TEAM 2```****")

        for i in team2:
            await message.channel.send(i)

    rand_user = random.choice(users)
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send(f'{message.author.name}  ndha mwonuse jada ano')
    if message.content.startswith('$intro'):
        await message.channel.send("ZEUS: NJAN thanne")
    if message.content.startswith("$theri"):
        selected = random.choice(therivili)
        if message.author.name == "SLAYER":
            await message.channel.send("You are too small for this")
        else:
            await message.channel.send(selected)

    if message.content.startswith("$addtheri"):
        theri = message.content
        if theri == "   ":
            print("error")
        else:
            mtheri = str.lstrip(theri, "$addtheri ")
            therivili.append(mtheri)
            print(therivili)

    if message.content.startswith("$help"):
        await message.channel.send(
            """
            $help : 
        $theri :
        $addtheri:
        $hello :
        $intro
        $roast
        $iamsed
        $dateandtime
        $iamhappy
        $wish
        $truth 
        $dare
        $user
        $sing
        $love
        $meme
        /a - z    
        """
        )
    if message.content.startswith("$roast"):
        a = message.content
        a.split(" ")
        b = a.replace("$roast", ' ')
        selroast = random.choice(roast)
        await message.channel.send(f"{selroast} {b}")

    if message.content.startswith("$iamsed"):
        sed = ["ayin ?", 'poda myre', "poyi moonjikko", "onn poda erka", "Andi moonjiko", "eyy ntha ivide naye", ]
        await message.channel.send(random.choice(sed))
    if message.content.startswith("$toss"):
        out = ['head', 'tail']
        random.shuffle(out)
        await message.channel.send(out[1])

    if message.content.startswith("$iamhappy"):
        await message.channel.send("poyi karenjal")
    if message.content.startswith("$dateandtime"):
        t1 = datetime.datetime.now().strftime("%H:%M:%S")
        d4 = datetime.date.today().strftime("%b-%d-%Y")
        await message.channel.send(f"DATE: {d4}")
        await message.channel.send(f"TIME: {t1}")
    if message.content.startswith("$copyrights"):
        await message.channel.send(var)
    if message.content.startswith("$admin"):
        print(message.author.name)
        if message.author.name == "ZEUS":
            adminpass = input("pass>> ")
            if adminpass == "oomb":
                while True:
                    mnj = input("admin>> ")
                    await message.channel.send(mnj)
                    if mnj == "exit":
                        break
        else:
            sed = "thaan eathado myre"
            await message.channel.send(sed)

    if message.content.startswith("$poda myre"):
        await message.channel.send("Antachan vedi  kundante mone")
    if message.content.startswith("$nice"):
        await message.channel.send("Thenks")
    if message.content.startswith("$wish"):
        await message.channel.send("HAPPY BIRTHDAY ")

    songs = ['നീ എന്റെ ലോല ലോലമാം ഉൾപ്പൂവിലെ മൃദുദളങ്ങൾ മധുകണങ്ങൾ തഴുകുമെന്നോ..',
             "Njanum Njanumentalum,  Aa Nalpathuperum,Poomaram Kondu Kappalundakki Kappalilane Aa Kuppayakkari,"
             "KUPPAYAM Pokki Njanonnu Nokki,",
             "Njan apple thinnum njn cola kudikum njan sundaranalle njan sundaranallee",
             "Appangal embadum ottakku chuttammayiAmmayi chuttathu marumonukkayi Appangal embadum ottakku chuttammayi "
             "Ammayi chuttathu marumonukkayi Appangal embadum ottakku chuttammayi Ammayi chuttathu marumonukkayi"]

    if message.content.startswith("$sing"):
        song = random.choice(songs)
        await message.channel.send(song)

    truth = [f"What is your favorite body part for {rand_user} to suck on?",
             f"Would you prefer to dominate {rand_user} in bed or do you want {rand_user} to dominate you in bed?",
             f" {rand_user}Do you like being nibbled on or lightly bitten? Where?",
             f"What's your favorite sex toy to use on {rand_user}?", f"What's the kinkiest thing you've ever done?",
             f"What’s the hottest sex dream you’ve ever had?",
             f"Tell me one thing {rand_user} could do that would make you immediately orgasm.",
             "Which is your favorite kind of sex: soft, slow, and sweet or aggressive, fast, and feisty?",
             f"If  {rand_user} gave you a free pass to hook up with one celebrity, who would it be and why?",
             f"What item of clothing do you think {rand_user} in server look sexiest in?",
             f"Describe {rand_user}s in-bed personality in three words.",
             f"If {rand_user} were handcuffed to the bed, what would you do to {rand_user}?",
             f" If you were to create an original sex move, what would you call it?",
             "Is there something you've seen in a steamy movie that you'd like to try?",
             f"What mattress move of {rand_user} is your favorite? Give me all the dirty details about why you like it,"
             f" What kind of foreplay would you like to try the next time {rand_user} and {rand_user} are in bed? ",
             f"Where do you think {rand_user} most romantic kiss took place? Tell me everything you remember about it.",
             f" When {rand_user}s on top of you, what's your favorite part of me to watch?",
             f"How often do you masturbate? How often is it about {rand_user}?",
             f"What is your least favorite sex position and why?",
             f"25. How do you feel about threesomes? Have you ever had one, and if not, would you ever have one?",
             f"What do you think the sexiest part of {rand_user} body is",
             "What do you think the sexiest part of your body is?",
             f"What were you thinking when you first saw {rand_user} naked?",
             "When was the first time that you had an orgasm?", "Who would you hate to see naked?",
             "How long have you gone without a shower?", "How long have you gone without brushing your teeth?",
             "What have you seen that you wish you could unsee?",
             "If you switched genders for the day, what would you do?",
             "What's one food that you will never order at a restaurant?",
             "What's the worst weather to be stuck outside in if all you could wear was a bathing suit?",
             "What's the most useless piece of knowledge you know?",
             "Is it better to use shampoo as soap or soap as shampoo?", "Who's hotter? You or your friend?",
             "If you had to choose, who would you stop being friends with?", "ande olle etha classile aane kande",
             "anake ehtra crush ind, full list idikke", "what is your father name",
             "have you seen any relative person masterbating", "what are your top three turn-ons?",
             "who is the sexiest person here?", "who here has the best ass?",
             "what is the naughtiest thing you've done in public?",
             "what would you do if you were the opposite gender for a month?",
             "who here would you most like to make out with?",
             "what secret about you did you tell someone in confidence and they told a lot of people?", ]

    dare = ["Face Reveal", "Place whipped cream on your favorite parts of my body. Now, lick it off.",
            "Eat a banana in the most sensual way possible",
            "tell something to me right now that you've been fantasizing about.",
            "Stimulate two parts of your body at once. Use your hands on one part and lips on another.",
            "In your most sultry voice, tell me what you loved about the last time you watched porn.",
            "Eat a piece of fruit in the most sensual way possible", "play me a song you’d like to have sex to.",
            f" Demonstrate a move on {rand_user} that you saw and liked while watching porn.",
            "Take off your underwear….", "Send a naked selfie to your partner.",
            "Watch a porn video and act like them.", "Lick your nipples",
            f"Send a naughty text message to y{rand_user}.", "Mastrubate now ",
            "Show the most embarrassing photo on your phone",
            "Show the last five people you texted and what the messages said",
            "Let the rest of the group DM someone from your Instagram account", "Eat a raw piece of garlic",
            "Keep three ice cubes in your mouth until they melt", "Say something dirty to the person on your left",
            "Remove four items of clothing", "Show your orgasm face", "Write your name on the floor with your tongue.",
            "message someone you haven't talked to for a year or more of the other's choice ",
            "Text your crush and ask them out on a date",
            "pick the third number on your recent calls and send them a stupid poem",
            "call the person of the other's players' choice and tell them what they ask you to",
            "make you profile picture a embarrassing picture for a day", "send a screenshot of your selfie gallery",
            "text a random person writing something of the others' choice", ]

    if message.content.startswith("$truth"):
        trth = random.choice(truth)
        await message.channel.send(trth)
    if message.content.startswith("$dare"):
        dre = random.choice(dare)
        await message.channel.send(dre)
    if message.content.startswith("$info"):
        await message.channel.send("""Father of MoonjiMon , @ZEUS
                                       Iam 5 months old    
                                       I'm a bitch and a boss, I'ma shine like gloss
                                       Married to @MoonjiMol""")
    if message.content.startswith("$user"):
        await message.channel.send(rand_user)
    if message.content.startswith("$users"):
        await message.channel.send(users)
    if message.content.startswith("$love"):
        await message.channel.send("Moonji Molee Ummmaa")
        for i in range(5):
            await message.channel.send("Umma ")

    if message.content.startswith("$aashin"):
        await message.channel.send("AASHIN uyir baaki ellam myr")
        for i in range(5):
            await message.channel.send("Aashin ")

    a = ['anus', 'arse', 'buttass', 'ass-hat', 'ass-jabber', 'ass-pirate' 'assbag ', 'assbanger ', 'assbite',
         'asscock ', 'sassface', 'assfuck ', 'assfucker', 'asshat', 'asshead']
    b = ['bampot ', 'bastard', 'bitch ', 'blow job', 'boner', 'brotherfucker ', 'butt plug', 'buttfucker']
    c = ['camel toe', 'chesticle', 'chode', 'cock ', 'cockface ', 'coochie ', 'cum ', 'cunthole ', 'cuntrag ']
    d = ['dick ', 'dildo ', 'dookie ', 'dumass ', 'douche ', 'dyke ', 'dipshit ', 'dike ', 'dago ', 'Doggy style']
    e = ['earwax', 'ecstasy', 'Echi', 'E oru mandan aano myre']
    f = ['faggot', 'fuck', ' fatass', 'fucker', 'fudgepacker', 'fagtard', 'fag', 'feltch']
    g = ['gay', 'gaylord', 'gooch', 'grahanam', 'gomathav']
    h = ['handjob', 'heeb', 'hell', 'hoe', 'homo', 'humping']
    i = ['Iron man', 'Iron sheddi', 'Ind', 'Iravum yen pakalum', 'Ila']
    j = ['jackass', 'jerk off', 'jungle bunny', 'jap', 'Jetty', 'Jhonny sins']
    ka = ['kooch', 'kundi', 'kunna', 'kolapathakam', 'kundan', 'kummanam']
    l = ['lameass', 'lesbian', f'lonely(Like{rand_user})', 'loka udayip', 'lolan', 'lokadurandam']
    m = ['myr', 'moonjal', 'mangandi moran', f'moyanth {rand_user}', 'motherfucker', 'muff', f'mwonjan {rand_user}']
    n = ['nigga', 'nudes', 'nutsack', 'niglet', 'NO NUT NOVEMBER', "nayinte mon", 'Naari', 'Nomanclature of atoms']
    o = ['Otta', 'Ole kundi', 'onte andi', 'orotta thalla', 'OoOoOoO']
    p = ['piss', 'penis', 'pp banger', 'poon', 'prick', 'polayadi mon', 'porn hub', 'poorimon', 'poda thayyoli']
    q = ['queef', 'queer', 'queerhole', 'qock(:D)']
    r = ['rimjob', 'renob', 'rathri kali', 'ravile vidunna vanam', 'rocket', f'Rocket man aka {rand_user}']
    s = ['sex', 'shit', 'suckass', 'snatch', 'sed', 'slut', 'spank', 'suku is vedi']
    t = ['Thooral', 'Thayyoli', 'tard', 'tits', 'tittyfuck', 'testis', 'testicle', 'Thund', 'Thokk']
    u = ['unclefucker', 'urine', 'underwear', 'undi', 'usman nte mola', 'united kozhikode', 'u r gay']
    v = ['vali', 'vedi', 'vanam', 'vagina', ]
    w = ['wank', 'whore', 'wop', 'wetback', ]
    x = ['xnxx', 'xvideos', 'xhamster', 'xangels', 'X foot', 'xxx porn tv', 'XXX shades', 'XXl Cock', 'Xcams', ]
    y = ['Yeda myre y okke vech ndha ullath', 'Y this kolaveri', "Yoyo honey singh", 'Yoda', 'Yeek']
    z = ['Z']

    if message.content.startswith("/a" or "/A"):
        ra = random.choice(a)
        await message.channel.send(f"A for {ra}")
    if message.content.startswith("/b" or "/B"):
        rb = random.choice(b)
        await message.channel.send(f"B for {rb}")

    if message.content.startswith("/c" or "/C"):
        rc = random.choice(c)
        await message.channel.send(f"C for {rc}")

    if message.content.startswith("/d" or "/D"):
        rd = random.choice(d)
        await message.channel.send(f"D for {rd}")

    if message.content.startswith("/e" or "/E"):
        re = random.choice(e)
        await message.channel.send(f"E for {re}")

    if message.content.startswith("/f" or "/F"):
        rf = random.choice(f)
        await message.channel.send(f"F for {rf}")

    if message.content.startswith("/g" or "/G"):
        rg = random.choice(g)
        await message.channel.send(f"G for {rg}")

    if message.content.startswith("/h" or "/H"):
        rh = random.choice(h)
        await message.channel.send(f"H for {rh}")

    if message.content.startswith("/i" or "/I"):
        ri = random.choice(i)
        await message.channel.send(f"I for {ri}")

    if message.content.startswith("/j" or "/J"):
        rj = random.choice(j)
        await message.channel.send(f"J for {rj}")

    if message.content.startswith("/k" or "/K"):
        rk = random.choice(ka)
        await message.channel.send(f"K for {rk}")

    if message.content.startswith("/l" or "/L"):
        rl = random.choice(l)
        await message.channel.send(f"L for {rl}")

    if message.content.startswith("/m" or "/M"):
        rm = random.choice(m)
        await message.channel.send(f"M for {rm}")

    if message.content.startswith("/n" or "/N"):
        rn = random.choice(n)
        await message.channel.send(f"N for {rn} ")
    if message.content.startswith("/o" or "/O"):
        ro = random.choice(o)
        await message.channel.send(f"O for {ro} ")
    if message.content.startswith("/p" or "/P"):
        rp = random.choice(p)
        await message.channel.send(f"P for {rp} ")

    if message.content.startswith("/q" or "/Q"):
        rq = random.choice(q)
        await message.channel.send(f"Q for {rq} ")

    if message.content.startswith("/r" or "/R"):
        rr = random.choice(r)
        await message.channel.send(f"R for {rr} ")
    if message.content.startswith("/s" or "/S"):
        rs = random.choice(s)
        await message.channel.send(f"S for {rs} ")
    if message.content.startswith("/t" or "/T"):
        rt = random.choice(t)
        await message.channel.send(f"T for {rt} ")
    if message.content.startswith("/u" or "/U"):
        ru = random.choice(u)
        await message.channel.send(f"U for {ru} ")
    if message.content.startswith("/v" or "/V"):
        rv = random.choice(v)
        await message.channel.send(f"V for {rv} ")
    if message.content.startswith("/w" or "/W"):
        rw = random.choice(w)
        await message.channel.send(f"W for {rw} ")
    if message.content.startswith("/x" or "/X"):
        rx = random.choice(x)
        await message.channel.send(f"X for {rx} ")
    if message.content.startswith("/y" or "/Y"):
        ry = random.choice(y)
        await message.channel.send(f"Y for {ry} ")
    if message.content.startswith("/z" or "/Z"):
        rz = random.choice(z)
        await message.channel.send(f"Z for {rz} ")
    if message.content.startswith("$r"):
        a = message.content
        a.split(" ")
        b = a.replace("$r", '')
        meme = reddit.subreddit(b).hot()
        post_to_pick = random.randint(1, 10)
        for i in range(0, post_to_pick):
            submission1 = meme.__next__()
        embed = discord.Embed()
        embed.set_image(url=submission1.url)
        embed.add_field(name="Moonjimon ", value=submission1.title)
        await message.channel.send(embed=embed)
    if message.content.startswith("$shinu"):
        shinu = [
            "https://cdn.discordapp.com/attachments/754046901414002711/790230503940161536/Screenshot_2020-12-20-00-22-48-98.jpg",
            "https://cdn.discordapp.com/attachments/754046901414002711/790231000365138000/Screenshot_20201202-195435_Discord.jpg",
            "https://cdn.discordapp.com/attachments/754046901414002711/790231000667258920/Screenshot_20201202-195331_Discord.jpg",
            "https://cdn.discordapp.com/attachments/754665315446816800/790231957832859649/unknown.png",
            "https://cdn.discordapp.com/attachments/754046901414002711/790230722841149440/IMG_20201214_005551.jpg",
            "https://cdn.discordapp.com/attachments/754046901414002711/790236468378599454/Adobe_20201220_204647.jpg",
            "https://cdn.discordapp.com/attachments/754665315446816800/790237212859039764/Screenshot_2020-11-28-00-03-00-33.png",
            "https://cdn.discordapp.com/attachments/754046901414002711/790238533600280576/Adobe_20201220_205457.png",
            "https://cdn.discordapp.com/attachments/754046901414002711/790239323030814740/Adobe_20201220_205805.jpg",
            "https://cdn.discordapp.com/attachments/754046901414002711/790239672264687676/Adobe_20201220_205931.jpg",
            "https://cdn.discordapp.com/attachments/754046901414002711/790239323030814740/Adobe_20201220_205805.jpg",
            "https://cdn.discordapp.com/attachments/754046901414002711/790240555220729906/Adobe_20201220_210247.jpg",
            "https://cdn.discordapp.com/attachments/754046901414002711/790242549804957716/Adobe_20201220_211046.png",
            "https://cdn.discordapp.com/attachments/754046901414002711/790243071890554910/Adobe_20201220_211303.jpg",
            "https://cdn.discordapp.com/attachments/754665315446816800/790251485350199356/unknown.png",
            "https://cdn.discordapp.com/attachments/779597466651459594/790259977004515328/Adobe_20201220_221957.jpg"

            ]
        snrand = random.choice(shinu)
        await message.channel.send(snrand)
    if message.content.startswith("$ash"):
        ash = ["https://cdn.discordapp.com/attachments/754046901414002711/790231541015511070/20201205_184032.jpg",
               "https://cdn.discordapp.com/attachments/754046901414002711/790231542462283806/IMG_20201125_234648.jpg",
               "https://cdn.discordapp.com/attachments/754046901414002711/790231542738845716/IMG_20201125_092035.jpg",
               "https://cdn.discordapp.com/attachments/754046901414002711/790245694253301770/Adobe_20201220_212320.jpg",
               "https://cdn.discordapp.com/attachments/754046901414002711/790249628510453800/Adobe_20201220_213755.jpg",
               "https://cdn.discordapp.com/attachments/779597466651459594/790259977004515328/Adobe_20201220_221957.jpg"]
        rnash = random.choice(ash)
        await message.channel.send(rnash)
    if message.content.startswith("$vazha"):
        vazha = [
            "https://cdn.discordapp.com/attachments/754046901414002711/790230571287707658/Screenshot_2020-12-16-23-34-30-63.jpg",
            "https://cdn.discordapp.com/attachments/754046901414002711/790233552348381184/Adobe_20201212_004022.jpg",
            "https://cdn.discordapp.com/attachments/754046901414002711/790233776059187230/Screenshot_2020-12-12-02-58-31-86_572064f74bd5f9fa804b05334aa4f912.jpg",
            "https://cdn.discordapp.com/attachments/754046901414002711/790249628510453800/Adobe_20201220_213755.jpg",
            "https://cdn.discordapp.com/attachments/754046901414002711/790250334466998332/Adobe_20201220_214132.jpg",
            "https://cdn.discordapp.com/attachments/754046901414002711/790250658841755698/Adobe_20201220_214314.jpg",
            "https://cdn.discordapp.com/attachments/779597466651459594/790259977004515328/Adobe_20201220_221957.jpg"]
        rvazha = random.choice(vazha)
        await message.channel.send(rvazha)
    if message.content.startswith("$gourigay"):
        gay = ["https://cdn.discordapp.com/attachments/754046901414002711/790231001137283112/Snapchat-1475834200.jpg",
               "https://cdn.discordapp.com/attachments/754046901414002711/790234124791185428/Screenshot_2020-12-08-13-59-37-41_572064f74bd5f9fa804b05334aa4f912.jpg",
               "https://cdn.discordapp.com/attachments/754046901414002711/790234125037994024/IMG_20201207_113348.jpg",
               "https://cdn.discordapp.com/attachments/754046901414002711/790234125516668998/IMG_20201207_113309.jpg",
               "https://cdn.discordapp.com/attachments/754665315446816800/790234377530376232/unknown.png",
               "https://cdn.discordapp.com/attachments/754665315446816800/790236449856290876/unknown.png",
               "https://cdn.discordapp.com/attachments/754665315446816800/790232087638048788/unknown.png",
               "https://cdn.discordapp.com/attachments/754665315446816800/790238144208699402/IMG_20201017_230150_001.jpg",
               "https://cdn.discordapp.com/attachments/754665315446816800/790238144372670524/17097305_126860117839443_5416369167093200325_o.png",
               "https://cdn.discordapp.com/attachments/754665315446816800/790238148890329128/IMG_20201109_154000_926.png",
               "https://cdn.discordapp.com/attachments/754665315446816800/790238149959221268/IMG-20201021-WA0099.jpg",
               "https://cdn.discordapp.com/attachments/754665315446816800/790238155919589397/Snapchat-614094123.jpg",
               "https://cdn.discordapp.com/attachments/754665315446816800/790238161548345354/Snapchat-1055865726.jpg",
               "https://cdn.discordapp.com/attachments/754665315446816800/790238159275294760/Snapchat-1039253628.jpg",
               "https://cdn.discordapp.com/attachments/754665315446816800/790238159275294760/Snapchat-1039253628.jpg",
               "https://cdn.discordapp.com/attachments/754665315446816800/790238155348377610/Screenshot_20201021-195412_Facebook.png"
               "https://cdn.discordapp.com/attachments/754665315446816800/790248386744942602/unknown.png",
               "https://cdn.discordapp.com/attachments/754665315446816800/790246816804765736/unknown.png",
               "https://cdn.discordapp.com/attachments/754046901414002711/790249628510453800/Adobe_20201220_213755.jpg",
               "https://cdn.discordapp.com/attachments/779597466651459594/790259977004515328/Adobe_20201220_221957.jpg"]
        rgay = random.choice(gay)
        await message.channel.send(rgay)

    if message.content.startswith("$spin"):
        list = []

        messages2 = message.content
        messages2.split(" ")
        stripped = str.lstrip(messages2, "$spin")
        b = stripped.split(" ")
        print(b)
        res = [x for x in b if x]
        print(res)
        choice = random.choice(res)

        spinner = await message.channel.send("Spinning")
        time.sleep(0.5)
        await spinner.edit(content="Spinning.")
        time.sleep(0.5)
        await spinner.edit(content="Spinning..")
        time.sleep(0.5)
        await spinner.edit(content="Spinning...")
        time.sleep(0.5)
        await spinner.edit(content="Spinning....")
        time.sleep(0.5)

        await message.channel.send(f"Winner is {choice}")
        await spinner.delete()


client.run('OTAyODg5NzI2OTUwOTAzODY4.YXk_lQ.0owFG1PT-tD-reIepSMEiDi04qc')
