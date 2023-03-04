
import datetime
import tweepy
import random
import schedule
import time




def tweet_keanu_birthday():
    # API keys
    api_key = "1n0HXuKM4QooEx2rnhFGG8kkb"
    api_secrets = "wBwxNZJ3L2UOZjQ2VCjhLHHXePqdjipbZ5QeZqv1r1oDrKGfuZ"
    access_token = "1593170010775912448-ayo0xdSY0Qu3bxRj26lvYNabFyyqjF"
    access_secret = "tdplKPwLrRFEaUTPDGSXccD1zXYZMne523AFWvLro68YC"

    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(api_key, api_secrets)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)

    keanu_quote = ["My name can't be THAT tough to pronounce!",
                   "The simple act of paying attention can take you a long way.",
                   "Art is about trying to find the good in people, and making the world a more compassionate place.",
                   "Kissing someone is pretty intimate, actually very intimate, and your heart always kind of skips a beat before you do that.",
                   "I will always be in love with love.", "Grief changes shape, but it never ends.",
                   "The best way to change is to make mistakes. You can learn from your mistakes and then keep moving on.",
                   "It's always wonderful to get to know women, with the mystery and the joy and the depth. If you can make a woman laugh, you're seeing the most beautiful thing.",
                   "Life is good when you have a good sandwich.”",
                   "I wear my heart on my sleeve and that can hurt. To be vulnerable is an enriching way to live, but when it goes wrong it can be agonizing. But if you don't open your heart to people, you end up being excluded from the rest of the world.",
                   "I am not handsome or sexy. Of course, it’s not like I am hopeless.", "We're all stardust, baby!",
                   "I was an affable little lad. I had a lot of energy. I liked to run around, liked to laugh, I was pretty sweet.",
                   "I don’t have kids or anything like that, so I get to be less responsible! The day is kind of like, 'What, creatively, can I do?'",
                   "Sometimes life imitates art.",
                   "It’s believing in love. It’s believing that there’s someone for you. That there’s the ultimate person, the ideal who will be your soul mate and your perfect match and that all your pain and suffering will go away and you’ll live happily ever after and you’ll be together in a blissful union.",
                   "Money doesn’t mean anything to me. I’ve made a lot of money but I want to enjoy life and not stress myself building my bank account... We all know that good health is much more important.",
                   "I don't want to be part of a world where being kind is a weakness.",
                   "I have no martial arts background... I only know movie Kung Fu.",
                   "It’s called show business for a reason.",
                   "Try and respect others. Try and continue to get the most out of life, and find ways to get that in this situation, but also to respect it. Find ways to connect. If you can. I mean, just .... survive.",
                   "I am very grateful for the printing press and everything that has followed. Electricity is pretty great too.",
                   "I hate giving advice.", "I like Sundays. Sunday is the day of rest.",
                   "I'm absolutely a very happy person.",
                   "Here comes . I’m feeling my age, and I’ve ordered the Ferrari. I’m going to get the whole midlife crisis package.",
                   "I thought the one of the ultimate expressions of 'whoa' was in the first Matrix...The 'whoa' was wonderful in The Matrix.",
                   "I'm Hawaiian, everyone's got a cousin.",
                   "You know, I'm the lonely guy. I don't have anyone in my life.",
                   "I don't really have a hobby. Is reading a hobby?", "I like pretending. I’m an actor.",
                   "I was always hoping, even when I was young, that I could do different things. I’m really grateful for that. I’m very fortunate. I’m glad to be here.",
                   "I guess it's just to my tastes to keep life as simple as I can.",
                   "You know, I'm not an air guitar aficionado. But once in a while, the air guitar comes out.",
                   "If something is hurting you, why and how and how can it be changed?",
                   "Working on Bill & Ted was certainly an excellent adventure. I love those characters. I love the spirit of the film. I like the eternal goodness of these characters. I always thought of them as beautiful fools.",
                   "I don't know how much intelligence I have.”",
                   "I don't really do junk food anymore? But I hope hamburgers don't count as junk food.",
                   "I think that a picture can tell a thousand words, and none of them can be right. Or true.",
                   "All of these characters have some DNA of mine, I share it with the character.",
                   "I think if I had taken the blue pill, it says I would go back to sleep and I would have never known what was happening. Which sounds very depressing. So I'm glad I took the right pill.",
                   "I do look back. I still sometimes wake up and go, 'Gosh, I shouldn’t have done that!'",
                   "Energy cannot be created or destroyed, they say.",
                   "It's easy to stay grounded. The ground is very close. And we walk on it every day.",
                   "Once in a while, I have the moments, where you drink the whiskey and you get the records out and you start doing the DJ thing until four in the morning.",
                   "I’m not the biggest film star in the world [laughs] at all.", "I’m always looking for catharsis.",
                   "I has always been my hope to be a part of works of art that entertain and that people can come away with something more or positive as they walked out of the dark into the world.",
                   "Riding a motorcycle is like being a puppy.",
                   "I've been very fortunate in my life. Which I am grateful for.",
                   "Toronto's become like a shopping center now.", "Are we in The Matrix?' No!",
                   "I know that the ones who love us will miss us.",
                   "We are humans on a rock floating through space with a finite amount of time. So take that into account—how we treat ourselves, how we treat others and we are all in this together. Be excellent to each other!",
                   "I definitely have a bit of the gypsy in me.",
                   "Grief and loss, those are things that don’t ever go away. They stay with you.",
                   "Honestly, I try not to do anything I don’t want to do.", ]

    # Authenticate
    try:
        api.verify_credentials()
        print('Successful Authentication')
    except Exception as e:
        print(e)
        print('Failed authentication')

    today = datetime.date.today()
    today_format = today.strftime("%B %d, %Y")
    keanu_birthday = datetime.date(today.year, 9, 2)

    if keanu_birthday == today:
        tweet = str(today_format)+" - HAPPY BIRTHDAY KEANU REEVES!"
        api.update_status(tweet)
        return tweet
    else:
        random_quote = random.choice(keanu_quote)
        tweet = today_format+" - It is NOT Keanu's Birthday today!\nHere is a random Keanu quote instead:\n \"" + random_quote + "\" - Keanu Reeves"
        print(len(tweet))
        api.update_status(tweet)
        return tweet


schedule.every().day.at("12:20").do(tweet_keanu_birthday)


# Run the scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)





