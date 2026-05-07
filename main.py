import os
def clear_terminal():
    os.system("clear")

database = [

    # MARVEL
    {"name":"Iron Man","human":True,"male":True,"female":False,"hero":True,"villain":False,"movie":True,"series":False,"game":False,"anime":False,"marvel":True,"dc":False,"magic":False,"inventor":True,"scientist":True,"rich":True,"billionaire":True,"armor":True,"mask":True,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":False,"gamer":False,"singer":False,"politician":False,"animal":False,"superpowers":False,"leader":True,"smart":True,"funny":True,"strong":False,"flying":True,"red":True,"blue":False,"green":False,"black":False,"gold":True,"american":True,"avenger":True,"uses_technology":True,"weapon":True},

    {"name":"Captain America","human":True,"male":True,"female":False,"hero":True,"villain":False,"movie":True,"series":False,"game":False,"anime":False,"marvel":True,"dc":False,"magic":False,"inventor":False,"scientist":False,"rich":False,"billionaire":False,"armor":False,"mask":False,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":False,"gamer":False,"singer":False,"politician":False,"animal":False,"superpowers":True,"leader":True,"smart":True,"funny":False,"strong":True,"flying":False,"red":True,"blue":True,"green":False,"black":False,"gold":False,"american":True,"avenger":True,"soldier":True,"shield":True},

    {"name":"Thor","human":False,"male":True,"female":False,"hero":True,"villain":False,"movie":True,"series":False,"game":False,"anime":False,"marvel":True,"dc":False,"magic":True,"inventor":False,"scientist":False,"rich":False,"billionaire":False,"armor":False,"mask":False,"alien":False,"robot":False,"cyborg":False,"god":True,"youtuber":False,"gamer":False,"singer":False,"politician":False,"animal":False,"superpowers":True,"leader":True,"smart":False,"funny":True,"strong":True,"flying":True,"red":False,"blue":False,"green":False,"black":False,"gold":False,"american":False,"avenger":True,"hammer":True,"lightning":True},

    {"name":"Hulk","human":False,"male":True,"female":False,"hero":True,"villain":False,"movie":True,"series":False,"game":False,"anime":False,"marvel":True,"dc":False,"magic":False,"inventor":False,"scientist":True,"rich":False,"billionaire":False,"armor":False,"mask":False,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":False,"gamer":False,"singer":False,"politician":False,"animal":False,"superpowers":True,"leader":False,"smart":True,"funny":False,"strong":True,"flying":False,"red":False,"blue":False,"green":True,"black":False,"gold":False,"american":True,"avenger":True,"big":True,"rage":True},

    {"name":"Spider-Man","human":True,"male":True,"female":False,"hero":True,"villain":False,"movie":True,"series":True,"game":True,"anime":False,"marvel":True,"dc":False,"magic":False,"inventor":False,"scientist":False,"rich":False,"billionaire":False,"armor":False,"mask":True,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":False,"gamer":False,"singer":False,"politician":False,"animal":False,"superpowers":True,"leader":False,"smart":True,"funny":True,"strong":True,"flying":False,"red":True,"blue":True,"green":False,"black":False,"gold":False,"american":True,"avenger":True,"teenager":True,"web":True},

    {"name":"Doctor Strange","human":True,"male":True,"female":False,"hero":True,"villain":False,"movie":True,"series":True,"game":False,"anime":False,"marvel":True,"dc":False,"magic":True,"inventor":False,"scientist":False,"rich":False,"billionaire":False,"armor":False,"mask":False,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":False,"gamer":False,"singer":False,"politician":False,"animal":False,"superpowers":True,"leader":False,"smart":True,"funny":False,"strong":False,"flying":True,"red":True,"blue":False,"green":False,"black":False,"gold":False,"american":True,"avenger":True,"doctor":True,"cape":True},

    {"name":"Black Panther","human":True,"male":True,"female":False,"hero":True,"villain":False,"movie":True,"series":False,"game":False,"anime":False,"marvel":True,"dc":False,"magic":False,"inventor":False,"scientist":False,"rich":True,"billionaire":False,"armor":True,"mask":True,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":False,"gamer":False,"singer":False,"politician":True,"animal":True,"superpowers":True,"leader":True,"smart":True,"funny":False,"strong":True,"flying":False,"red":False,"blue":False,"green":False,"black":True,"gold":False,"american":False,"avenger":True,"king":True,"warrior":True},

    {"name":"Thanos","human":False,"male":True,"female":False,"hero":False,"villain":True,"movie":True,"series":False,"game":False,"anime":False,"marvel":True,"dc":False,"magic":False,"inventor":False,"scientist":False,"rich":False,"billionaire":False,"armor":True,"mask":False,"alien":True,"robot":False,"cyborg":False,"god":False,"youtuber":False,"gamer":False,"singer":False,"politician":False,"animal":False,"superpowers":True,"leader":True,"smart":True,"funny":False,"strong":True,"flying":False,"red":False,"blue":False,"green":False,"black":False,"gold":True,"american":False,"avenger":False,"purple":True,"big":True},

    {"name":"Loki","human":False,"male":True,"female":False,"hero":False,"villain":True,"movie":True,"series":True,"game":False,"anime":False,"marvel":True,"dc":False,"magic":True,"inventor":False,"scientist":False,"rich":False,"billionaire":False,"armor":False,"mask":False,"alien":False,"robot":False,"cyborg":False,"god":True,"youtuber":False,"gamer":False,"singer":False,"politician":False,"animal":False,"superpowers":True,"leader":False,"smart":True,"funny":True,"strong":False,"flying":False,"red":False,"blue":False,"green":True,"black":False,"gold":False,"american":False,"avenger":False,"trickster":True,"horns":True},

    # DC
    {"name":"Batman","human":True,"male":True,"female":False,"hero":True,"villain":False,"movie":True,"series":True,"game":True,"anime":False,"marvel":False,"dc":True,"magic":False,"inventor":True,"scientist":False,"rich":True,"billionaire":True,"armor":True,"mask":True,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":False,"gamer":False,"singer":False,"politician":False,"animal":True,"superpowers":False,"leader":True,"smart":True,"funny":False,"strong":True,"flying":False,"red":False,"blue":False,"green":False,"black":True,"gold":False,"american":True,"detective":True,"cape":True,"dark":True},

    {"name":"Superman","human":False,"male":True,"female":False,"hero":True,"villain":False,"movie":True,"series":True,"game":True,"anime":False,"marvel":False,"dc":True,"magic":False,"inventor":False,"scientist":False,"rich":False,"billionaire":False,"armor":False,"mask":False,"alien":True,"robot":False,"cyborg":False,"god":False,"youtuber":False,"gamer":False,"singer":False,"politician":False,"animal":False,"superpowers":True,"leader":True,"smart":True,"funny":False,"strong":True,"flying":True,"red":True,"blue":True,"green":False,"black":False,"gold":False,"american":True,"cape":True,"laser_eyes":True,"glasses":True},

    {"name":"Flash","human":True,"male":True,"female":False,"hero":True,"villain":False,"movie":True,"series":True,"game":True,"anime":False,"marvel":False,"dc":True,"magic":False,"inventor":False,"scientist":True,"rich":False,"billionaire":False,"armor":True,"mask":True,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":False,"gamer":False,"singer":False,"politician":False,"animal":False,"superpowers":True,"leader":False,"smart":True,"funny":True,"strong":False,"flying":False,"red":True,"blue":False,"green":False,"black":False,"gold":True,"american":True,"speed":True,"lightning":True,"time_travel":True},

    {"name":"Wonder Woman","human":True,"male":False,"female":True,"hero":True,"villain":False,"movie":True,"series":False,"game":True,"anime":False,"marvel":False,"dc":True,"magic":True,"inventor":False,"scientist":False,"rich":False,"billionaire":False,"armor":True,"mask":False,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":False,"gamer":False,"singer":False,"politician":False,"animal":False,"superpowers":True,"leader":True,"smart":True,"funny":False,"strong":True,"flying":False,"red":True,"blue":True,"green":False,"black":False,"gold":True,"american":False,"warrior":True,"princess":True,"lasso":True},

    {"name":"Joker","human":True,"male":True,"female":False,"hero":False,"villain":True,"movie":True,"series":True,"game":True,"anime":False,"marvel":False,"dc":True,"magic":False,"inventor":False,"scientist":False,"rich":False,"billionaire":False,"armor":False,"mask":False,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":False,"gamer":False,"singer":False,"politician":False,"animal":False,"superpowers":False,"leader":False,"smart":True,"funny":True,"strong":False,"flying":False,"red":False,"blue":False,"green":True,"black":False,"gold":False,"american":True,"clown":True,"crazy":True,"purple":True},

    # ANIME
    {"name":"Naruto Uzumaki","human":True,"male":True,"female":False,"hero":True,"villain":False,"movie":False,"series":True,"game":True,"anime":True,"marvel":False,"dc":False,"magic":True,"inventor":False,"scientist":False,"rich":False,"billionaire":False,"armor":False,"mask":False,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":False,"gamer":False,"singer":False,"politician":False,"animal":False,"superpowers":True,"leader":True,"smart":False,"funny":True,"strong":True,"flying":False,"red":False,"blue":False,"green":False,"black":False,"gold":False,"american":False,"ninja":True,"orange":True,"blonde_hair":True},

    {"name":"Goku","human":False,"male":True,"female":False,"hero":True,"villain":False,"movie":True,"series":True,"game":True,"anime":True,"marvel":False,"dc":False,"magic":False,"inventor":False,"scientist":False,"rich":False,"billionaire":False,"armor":False,"mask":False,"alien":True,"robot":False,"cyborg":False,"god":False,"youtuber":False,"gamer":False,"singer":False,"politician":False,"animal":False,"superpowers":True,"leader":False,"smart":False,"funny":True,"strong":True,"flying":True,"red":False,"blue":True,"green":False,"black":False,"gold":False,"american":False,"fighter":True,"orange":True,"spiky_hair":True},

    {"name":"Luffy","human":True,"male":True,"female":False,"hero":True,"villain":False,"movie":False,"series":True,"game":True,"anime":True,"marvel":False,"dc":False,"magic":False,"inventor":False,"scientist":False,"rich":False,"billionaire":False,"armor":False,"mask":False,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":False,"gamer":False,"singer":False,"politician":False,"animal":False,"superpowers":True,"leader":True,"smart":False,"funny":True,"strong":True,"flying":False,"red":True,"blue":True,"green":False,"black":False,"gold":False,"american":False,"pirate":True,"straw_hat":True,"stretchy":True},

    {"name":"Saitama","human":True,"male":True,"female":False,"hero":True,"villain":False,"movie":False,"series":True,"game":False,"anime":True,"marvel":False,"dc":False,"magic":False,"inventor":False,"scientist":False,"rich":False,"billionaire":False,"armor":False,"mask":False,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":False,"gamer":False,"singer":False,"politician":False,"animal":False,"superpowers":True,"leader":False,"smart":False,"funny":True,"strong":True,"flying":False,"red":False,"blue":False,"green":False,"black":False,"gold":False,"american":False,"bald":True,"yellow":True,"cape":True},

    {"name":"Gojo Satoru","human":True,"male":True,"female":False,"hero":True,"villain":False,"movie":False,"series":True,"game":True,"anime":True,"marvel":False,"dc":False,"magic":True,"inventor":False,"scientist":False,"rich":False,"billionaire":False,"armor":False,"mask":True,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":False,"gamer":False,"singer":False,"politician":False,"animal":False,"superpowers":True,"leader":False,"smart":True,"funny":True,"strong":True,"flying":False,"red":False,"blue":True,"green":False,"black":True,"gold":False,"american":False,"teacher":True,"white_hair":True,"blindfold":True},

    {"name":"Tanjiro","human":True,"male":True,"female":False,"hero":True,"villain":False,"movie":True,"series":True,"game":True,"anime":True,"marvel":False,"dc":False,"magic":False,"inventor":False,"scientist":False,"rich":False,"billionaire":False,"armor":False,"mask":False,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":False,"gamer":False,"singer":False,"politician":False,"animal":False,"superpowers":False,"leader":False,"smart":True,"funny":False,"strong":True,"flying":False,"red":False,"blue":False,"green":True,"black":True,"gold":False,"american":False,"swordsman":True,"demon_slayer":True,"scar":True},

    {"name":"Nezuko","human":False,"male":False,"female":True,"hero":True,"villain":False,"movie":True,"series":True,"game":True,"anime":True,"marvel":False,"dc":False,"magic":False,"inventor":False,"scientist":False,"rich":False,"billionaire":False,"armor":False,"mask":False,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":False,"gamer":False,"singer":False,"politician":False,"animal":False,"superpowers":True,"leader":False,"smart":False,"funny":False,"strong":True,"flying":False,"red":False,"blue":False,"green":False,"black":True,"gold":False,"american":False,"demon":True,"pink":True,"bamboo":True},

    # YOUTUBERS
    {"name":"MrBeast","human":True,"male":True,"female":False,"hero":False,"villain":False,"movie":False,"series":False,"game":False,"anime":False,"marvel":False,"dc":False,"magic":False,"inventor":False,"scientist":False,"rich":True,"billionaire":False,"armor":False,"mask":False,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":True,"gamer":False,"singer":False,"politician":False,"animal":False,"superpowers":False,"leader":True,"smart":True,"funny":True,"strong":False,"flying":False,"red":False,"blue":False,"green":False,"black":False,"gold":False,"american":True,"real_person":True,"famous":True,"challenge_videos":True},

    {"name":"PewDiePie","human":True,"male":True,"female":False,"hero":False,"villain":False,"movie":False,"series":False,"game":False,"anime":False,"marvel":False,"dc":False,"magic":False,"inventor":False,"scientist":False,"rich":True,"billionaire":False,"armor":False,"mask":False,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":True,"gamer":True,"singer":False,"politician":False,"animal":False,"superpowers":False,"leader":False,"smart":True,"funny":True,"strong":False,"flying":False,"red":False,"blue":False,"green":False,"black":False,"gold":False,"american":False,"real_person":True,"famous":True,"swedish":True},

    {"name":"Dream","human":True,"male":True,"female":False,"hero":False,"villain":False,"movie":False,"series":False,"game":False,"anime":False,"marvel":False,"dc":False,"magic":False,"inventor":False,"scientist":False,"rich":True,"billionaire":False,"armor":False,"mask":True,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":True,"gamer":True,"singer":False,"politician":False,"animal":False,"superpowers":False,"leader":False,"smart":True,"funny":True,"strong":False,"flying":False,"red":False,"blue":False,"green":True,"black":False,"gold":False,"american":True,"real_person":True,"famous":True,"minecraft":True},

    {"name":"Technoblade","human":True,"male":True,"female":False,"hero":True,"villain":False,"movie":False,"series":False,"game":False,"anime":False,"marvel":False,"dc":False,"magic":False,"inventor":False,"scientist":False,"rich":False,"billionaire":False,"armor":False,"mask":False,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":True,"gamer":True,"singer":False,"politician":False,"animal":True,"superpowers":False,"leader":True,"smart":True,"funny":True,"strong":False,"flying":False,"red":True,"blue":False,"green":False,"black":False,"gold":True,"american":True,"real_person":True,"minecraft":True,"pig":True},

    {"name":"TommyInnit","human":True,"male":True,"female":False,"hero":False,"villain":False,"movie":False,"series":False,"game":False,"anime":False,"marvel":False,"dc":False,"magic":False,"inventor":False,"scientist":False,"rich":False,"billionaire":False,"armor":False,"mask":False,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":True,"gamer":True,"singer":False,"politician":False,"animal":False,"superpowers":False,"leader":False,"smart":False,"funny":True,"strong":False,"flying":False,"red":True,"blue":False,"green":False,"black":False,"gold":False,"american":False,"real_person":True,"minecraft":True,"british":True},

    {"name":"DanTDM","human":True,"male":True,"female":False,"hero":False,"villain":False,"movie":False,"series":False,"game":False,"anime":False,"marvel":False,"dc":False,"magic":False,"inventor":False,"scientist":False,"rich":True,"billionaire":False,"armor":False,"mask":False,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":True,"gamer":True,"singer":False,"politician":False,"animal":False,"superpowers":False,"leader":False,"smart":True,"funny":True,"strong":False,"flying":False,"red":False,"blue":True,"green":False,"black":False,"gold":False,"american":False,"real_person":True,"minecraft":True,"british":True},

    {"name":"Markiplier","human":True,"male":True,"female":False,"hero":False,"villain":False,"movie":False,"series":False,"game":False,"anime":False,"marvel":False,"dc":False,"magic":False,"inventor":False,"scientist":False,"rich":True,"billionaire":False,"armor":False,"mask":False,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":True,"gamer":True,"singer":False,"politician":False,"animal":False,"superpowers":False,"leader":False,"smart":True,"funny":True,"strong":False,"flying":False,"red":True,"blue":False,"green":False,"black":True,"gold":False,"american":True,"real_person":True,"horror":True,"famous":True},

    {"name":"KSI","human":True,"male":True,"female":False,"hero":False,"villain":False,"movie":False,"series":False,"game":False,"anime":False,"marvel":False,"dc":False,"magic":False,"inventor":False,"scientist":False,"rich":True,"billionaire":False,"armor":False,"mask":False,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":True,"gamer":False,"singer":True,"politician":False,"animal":False,"superpowers":False,"leader":False,"smart":False,"funny":True,"strong":True,"flying":False,"red":False,"blue":False,"green":False,"black":True,"gold":False,"american":False,"real_person":True,"boxer":True,"british":True},

    # GAMES
    {"name":"Steve","human":True,"male":True,"female":False,"hero":True,"villain":False,"movie":False,"series":False,"game":True,"anime":False,"marvel":False,"dc":False,"magic":False,"inventor":False,"scientist":False,"rich":False,"billionaire":False,"armor":False,"mask":False,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":False,"gamer":False,"singer":False,"politician":False,"animal":False,"superpowers":False,"leader":False,"smart":False,"funny":False,"strong":True,"flying":False,"red":False,"blue":True,"green":False,"black":False,"gold":False,"american":False,"minecraft":True,"blocky":True,"pixelated":True,"survival":True},

    {"name":"Herobrine","human":False,"male":True,"female":False,"hero":False,"villain":True,"movie":False,"series":False,"game":True,"anime":False,"marvel":False,"dc":False,"magic":True,"inventor":False,"scientist":False,"rich":False,"billionaire":False,"armor":False,"mask":False,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":False,"gamer":False,"singer":False,"politician":False,"animal":False,"superpowers":True,"leader":False,"smart":True,"funny":False,"strong":True,"flying":True,"red":False,"blue":True,"green":False,"black":False,"gold":False,"american":False,"minecraft":True,"blocky":True,"white_eyes":True,"scary":True},

    {"name":"Mario","human":True,"male":True,"female":False,"hero":True,"villain":False,"movie":True,"series":True,"game":True,"anime":False,"marvel":False,"dc":False,"magic":False,"inventor":False,"scientist":False,"rich":False,"billionaire":False,"armor":False,"mask":False,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":False,"gamer":False,"singer":False,"politician":False,"animal":False,"superpowers":False,"leader":False,"smart":False,"funny":True,"strong":False,"flying":False,"red":True,"blue":True,"green":False,"black":False,"gold":False,"american":False,"plumber":True,"mustache":True,"nintendo":True},

    {"name":"Luigi","human":True,"male":True,"female":False,"hero":True,"villain":False,"movie":True,"series":True,"game":True,"anime":False,"marvel":False,"dc":False,"magic":False,"inventor":False,"scientist":False,"rich":False,"billionaire":False,"armor":False,"mask":False,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":False,"gamer":False,"singer":False,"politician":False,"animal":False,"superpowers":False,"leader":False,"smart":False,"funny":True,"strong":False,"flying":False,"red":False,"blue":True,"green":True,"black":False,"gold":False,"american":False,"plumber":True,"mustache":True,"nintendo":True},

    {"name":"Sonic","human":False,"male":True,"female":False,"hero":True,"villain":False,"movie":True,"series":True,"game":True,"anime":False,"marvel":False,"dc":False,"magic":False,"inventor":False,"scientist":False,"rich":False,"billionaire":False,"armor":False,"mask":False,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":False,"gamer":False,"singer":False,"politician":False,"animal":True,"superpowers":True,"leader":False,"smart":False,"funny":True,"strong":False,"flying":False,"red":False,"blue":True,"green":False,"black":False,"gold":False,"american":False,"speed":True,"hedgehog":True,"fast":True},

    {"name":"Link","human":True,"male":True,"female":False,"hero":True,"villain":False,"movie":False,"series":False,"game":True,"anime":False,"marvel":False,"dc":False,"magic":True,"inventor":False,"scientist":False,"rich":False,"billionaire":False,"armor":False,"mask":False,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":False,"gamer":False,"singer":False,"politician":False,"animal":False,"superpowers":False,"leader":False,"smart":True,"funny":False,"strong":True,"flying":False,"red":False,"blue":False,"green":True,"black":False,"gold":False,"american":False,"swordsman":True,"shield":True,"nintendo":True},

    {"name":"Zelda","human":True,"male":False,"female":True,"hero":True,"villain":False,"movie":False,"series":False,"game":True,"anime":False,"marvel":False,"dc":False,"magic":True,"inventor":False,"scientist":False,"rich":True,"billionaire":False,"armor":False,"mask":False,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":False,"gamer":False,"singer":False,"politician":True,"animal":False,"superpowers":True,"leader":True,"smart":True,"funny":False,"strong":False,"flying":False,"red":False,"blue":False,"green":False,"black":False,"gold":True,"american":False,"princess":True,"nintendo":True,"royal":True},

    {"name":"Freddy Fazbear","human":False,"male":True,"female":False,"hero":False,"villain":True,"movie":True,"series":False,"game":True,"anime":False,"marvel":False,"dc":False,"magic":False,"inventor":False,"scientist":False,"rich":False,"billionaire":False,"armor":False,"mask":False,"alien":False,"robot":True,"cyborg":False,"god":False,"youtuber":False,"gamer":False,"singer":True,"politician":False,"animal":True,"superpowers":False,"leader":True,"smart":False,"funny":False,"strong":True,"flying":False,"red":False,"blue":False,"green":False,"black":False,"gold":False,"american":False,"bear":True,"horror":True,"animatronic":True},

    {"name":"Sans","human":False,"male":True,"female":False,"hero":False,"villain":False,"movie":False,"series":False,"game":True,"anime":False,"marvel":False,"dc":False,"magic":True,"inventor":False,"scientist":False,"rich":False,"billionaire":False,"armor":False,"mask":False,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":False,"gamer":False,"singer":False,"politician":False,"animal":False,"superpowers":True,"leader":False,"smart":True,"funny":True,"strong":True,"flying":False,"red":False,"blue":True,"green":False,"black":False,"gold":False,"american":False,"skeleton":True,"lazy":True,"undertale":True},

    {"name":"Bendy","human":False,"male":True,"female":False,"hero":False,"villain":True,"movie":False,"series":False,"game":True,"anime":False,"cartoon":True,"marvel":False,"dc":False,"magic":True,"inventor":False,"scientist":False,"rich":False,"billionaire":False,"armor":False,"mask":False,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":False,"gamer":False,"singer":False,"politician":False,"animal":False,"superpowers":True,"leader":False,"smart":False,"funny":False,"strong":True,"flying":False,"red":False,"blue":False,"green":False,"black":True,"gold":False,"american":False,"horror":True,"ink":True,"demon":True},

    # MOVIES & SERIES
    {"name":"Harry Potter","human":True,"male":True,"female":False,"hero":True,"villain":False,"movie":True,"series":False,"game":True,"anime":False,"marvel":False,"dc":False,"magic":True,"inventor":False,"scientist":False,"rich":False,"billionaire":False,"armor":False,"mask":False,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":False,"gamer":False,"singer":False,"politician":False,"animal":False,"superpowers":True,"leader":True,"smart":True,"funny":False,"strong":False,"flying":True,"red":False,"blue":False,"green":False,"black":True,"gold":False,"american":False,"wizard":True,"glasses":True,"scar":True},

    {"name":"Hermione Granger","human":True,"male":False,"female":True,"hero":True,"villain":False,"movie":True,"series":False,"game":True,"anime":False,"marvel":False,"dc":False,"magic":True,"inventor":False,"scientist":False,"rich":False,"billionaire":False,"armor":False,"mask":False,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":False,"gamer":False,"singer":False,"politician":False,"animal":False,"superpowers":True,"leader":False,"smart":True,"funny":False,"strong":False,"flying":False,"red":False,"blue":False,"green":False,"black":False,"gold":False,"american":False,"witch":True,"student":True,"brown_hair":True},

    {"name":"Darth Vader","human":True,"male":True,"female":False,"hero":False,"villain":True,"movie":True,"series":True,"game":True,"anime":False,"marvel":False,"dc":False,"magic":True,"inventor":False,"scientist":False,"rich":False,"billionaire":False,"armor":True,"mask":True,"alien":False,"robot":True,"cyborg":True,"god":False,"youtuber":False,"gamer":False,"singer":False,"politician":False,"animal":False,"superpowers":True,"leader":True,"smart":True,"funny":False,"strong":True,"flying":False,"red":False,"blue":False,"green":False,"black":True,"gold":False,"american":False,"space":True,"lightsaber":True,"star_wars":True},

    {"name":"Luke Skywalker","human":True,"male":True,"female":False,"hero":True,"villain":False,"movie":True,"series":True,"game":True,"anime":False,"marvel":False,"dc":False,"magic":True,"inventor":False,"scientist":False,"rich":False,"billionaire":False,"armor":False,"mask":False,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":False,"gamer":False,"singer":False,"politician":False,"animal":False,"superpowers":True,"leader":True,"smart":True,"funny":False,"strong":True,"flying":False,"red":False,"blue":False,"green":False,"black":False,"gold":False,"american":False,"space":True,"lightsaber":True,"star_wars":True},

    {"name":"Shrek","human":False,"male":True,"female":False,"hero":True,"villain":False,"movie":True,"series":False,"game":True,"anime":False,"marvel":False,"dc":False,"magic":False,"inventor":False,"scientist":False,"rich":False,"billionaire":False,"armor":False,"mask":False,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":False,"gamer":False,"singer":False,"politician":False,"animal":False,"superpowers":False,"leader":False,"smart":False,"funny":True,"strong":True,"flying":False,"red":False,"blue":False,"green":True,"black":False,"gold":False,"american":False,"ogre":True,"big":True,"swamp":True},

    {"name":"Elsa","human":True,"male":False,"female":True,"hero":True,"villain":False,"movie":True,"series":False,"game":True,"anime":False,"marvel":False,"dc":False,"magic":True,"inventor":False,"scientist":False,"rich":True,"billionaire":False,"armor":False,"mask":False,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":False,"gamer":False,"singer":True,"politician":True,"animal":False,"superpowers":True,"leader":True,"smart":True,"funny":False,"strong":False,"flying":False,"red":False,"blue":True,"green":False,"black":False,"gold":False,"american":False,"princess":True,"queen":True,"ice":True},

    {"name":"Wednesday Addams","human":True,"male":False,"female":True,"hero":False,"villain":False,"movie":False,"series":True,"game":False,"anime":False,"marvel":False,"dc":False,"magic":False,"inventor":False,"scientist":False,"rich":False,"billionaire":False,"armor":False,"mask":False,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":False,"gamer":False,"singer":False,"politician":False,"animal":False,"superpowers":False,"leader":False,"smart":True,"funny":False,"strong":False,"flying":False,"red":False,"blue":False,"green":False,"black":True,"gold":False,"american":True,"dark":True,"school":True,"serious":True},

    {"name":"Gi-Hun Lee","human":True,"male":True,"female":False,"hero":True,"villain":False,"movie":False,"series":True,"game":False,"anime":False,"marvel":False,"dc":False,"magic":False,"inventor":False,"scientist":False,"rich":False,"billionaire":False,"armor":False,"mask":False,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":False,"gamer":False,"singer":False,"politician":False,"animal":False,"superpowers":False,"leader":False,"smart":False,"funny":False,"strong":False,"flying":False,"red":False,"blue":False,"green":True,"black":False,"gold":False,"american":False,"korean":True,"squid_game":True,"player":True},

    # REAL PEOPLE
    {"name":"Cristiano Ronaldo","human":True,"male":True,"female":False,"hero":False,"villain":False,"movie":False,"series":False,"game":False,"anime":False,"marvel":False,"dc":False,"magic":False,"inventor":False,"scientist":False,"rich":True,"billionaire":False,"armor":False,"mask":False,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":False,"gamer":False,"singer":False,"politician":False,"animal":False,"superpowers":False,"leader":True,"smart":False,"funny":False,"strong":True,"flying":False,"red":False,"blue":False,"green":False,"black":False,"gold":False,"american":False,"real_person":True,"footballer":True,"sports":True,"portuguese":True},

    {"name":"Lionel Messi","human":True,"male":True,"female":False,"hero":False,"villain":False,"movie":False,"series":False,"game":False,"anime":False,"marvel":False,"dc":False,"magic":False,"inventor":False,"scientist":False,"rich":True,"billionaire":False,"armor":False,"mask":False,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":False,"gamer":False,"singer":False,"politician":False,"animal":False,"superpowers":False,"leader":True,"smart":False,"funny":False,"strong":False,"flying":False,"red":False,"blue":True,"green":False,"black":False,"gold":False,"american":False,"real_person":True,"footballer":True,"sports":True,"argentinian":True},

    {"name":"Neymar","human":True,"male":True,"female":False,"hero":False,"villain":False,"movie":False,"series":False,"game":False,"anime":False,"marvel":False,"dc":False,"magic":False,"inventor":False,"scientist":False,"rich":True,"billionaire":False,"armor":False,"mask":False,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":False,"gamer":False,"singer":False,"politician":False,"animal":False,"superpowers":False,"leader":False,"smart":False,"funny":True,"strong":False,"flying":False,"red":False,"blue":False,"green":True,"black":False,"gold":False,"american":False,"real_person":True,"footballer":True,"sports":True,"brazilian":True},

    {"name":"Elon Musk","human":True,"male":True,"female":False,"hero":False,"villain":False,"movie":False,"series":False,"game":False,"anime":False,"marvel":False,"dc":False,"magic":False,"inventor":True,"scientist":False,"rich":True,"billionaire":True,"armor":False,"mask":False,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":False,"gamer":False,"singer":False,"politician":False,"animal":False,"superpowers":False,"leader":True,"smart":True,"funny":False,"strong":False,"flying":False,"red":False,"blue":False,"green":False,"black":False,"gold":False,"american":True,"real_person":True,"businessman":True,"space":True},

    {"name":"Taylor Swift","human":True,"male":False,"female":True,"hero":False,"villain":False,"movie":False,"series":False,"game":False,"anime":False,"marvel":False,"dc":False,"magic":False,"inventor":False,"scientist":False,"rich":True,"billionaire":True,"armor":False,"mask":False,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":False,"gamer":False,"singer":True,"politician":False,"animal":False,"superpowers":False,"leader":True,"smart":True,"funny":False,"strong":False,"flying":False,"red":True,"blue":False,"green":False,"black":False,"gold":True,"american":True,"real_person":True,"famous":True,"blonde_hair":True},

    {"name":"Billie Eilish","human":True,"male":False,"female":True,"hero":False,"villain":False,"movie":False,"series":False,"game":False,"anime":False,"marvel":False,"dc":False,"magic":False,"inventor":False,"scientist":False,"rich":True,"billionaire":False,"armor":False,"mask":False,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":False,"gamer":False,"singer":True,"politician":False,"animal":False,"superpowers":False,"leader":False,"smart":True,"funny":False,"strong":False,"flying":False,"red":False,"blue":False,"green":True,"black":True,"gold":False,"american":True,"real_person":True,"famous":True,"music":True},

    {"name":"Michael Jackson","human":True,"male":True,"female":False,"hero":False,"villain":False,"movie":False,"series":False,"game":False,"anime":False,"marvel":False,"dc":False,"magic":False,"inventor":False,"scientist":False,"rich":True,"billionaire":False,"armor":False,"mask":False,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":False,"gamer":False,"singer":True,"politician":False,"animal":False,"superpowers":False,"leader":True,"smart":True,"funny":False,"strong":False,"flying":False,"red":False,"blue":False,"green":False,"black":True,"gold":False,"american":True,"real_person":True,"dancer":True,"dead":True},

    {"name":"Albert Einstein","human":True,"male":True,"female":False,"hero":False,"villain":False,"movie":False,"series":False,"game":False,"anime":False,"marvel":False,"dc":False,"magic":False,"inventor":False,"scientist":True,"rich":False,"billionaire":False,"armor":False,"mask":False,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":False,"gamer":False,"singer":False,"politician":False,"animal":False,"superpowers":False,"leader":False,"smart":True,"funny":False,"strong":False,"flying":False,"red":False,"blue":False,"green":False,"black":False,"gold":False,"american":False,"real_person":True,"mustache":True,"dead":True,"genius":True},

    {"name":"Barack Obama","human":True,"male":True,"female":False,"hero":False,"villain":False,"movie":False,"series":False,"game":False,"anime":False,"marvel":False,"dc":False,"magic":False,"inventor":False,"scientist":False,"rich":True,"billionaire":False,"armor":False,"mask":False,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":False,"gamer":False,"singer":False,"politician":True,"animal":False,"superpowers":False,"leader":True,"smart":True,"funny":False,"strong":False,"flying":False,"red":False,"blue":True,"green":False,"black":False,"gold":False,"american":True,"real_person":True,"president":True,"famous":True},

    {"name":"Donald Trump","human":True,"male":True,"female":False,"hero":False,"villain":False,"movie":False,"series":False,"game":False,"anime":False,"marvel":False,"dc":False,"magic":False,"inventor":False,"scientist":False,"rich":True,"billionaire":True,"armor":False,"mask":False,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":False,"gamer":False,"singer":False,"politician":True,"animal":False,"superpowers":False,"leader":True,"smart":False,"funny":False,"strong":False,"flying":False,"red":True,"blue":False,"green":False,"black":False,"gold":True,"american":True,"real_person":True,"president":True,"businessman":True},

    # MEMES
    {"name":"Skibidi Toilet","human":False,"male":True,"female":False,"hero":False,"villain":False,"movie":False,"series":True,"game":False,"anime":False,"marvel":False,"dc":False,"magic":False,"inventor":False,"scientist":False,"rich":False,"billionaire":False,"armor":False,"mask":False,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":False,"gamer":False,"singer":False,"politician":False,"animal":False,"superpowers":False,"leader":False,"smart":False,"funny":True,"strong":False,"flying":False,"red":False,"blue":False,"green":False,"black":False,"gold":False,"american":False,"meme":True,"toilet":True,"youtube":True,"brainrot":True},

    {"name":"Gigachad","human":True,"male":True,"female":False,"hero":False,"villain":False,"movie":False,"series":False,"game":False,"anime":False,"marvel":False,"dc":False,"magic":False,"inventor":False,"scientist":False,"rich":False,"billionaire":False,"armor":False,"mask":False,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":False,"gamer":False,"singer":False,"politician":False,"animal":False,"superpowers":False,"leader":False,"smart":False,"funny":True,"strong":True,"flying":False,"red":False,"blue":False,"green":False,"black":True,"gold":False,"american":False,"meme":True,"sigma":True,"muscular":True,"famous":True},

    {"name":"Among Us Crewmate","human":False,"male":False,"female":False,"hero":False,"villain":False,"movie":False,"series":False,"game":True,"anime":False,"marvel":False,"dc":False,"magic":False,"inventor":False,"scientist":False,"rich":False,"billionaire":False,"armor":True,"mask":True,"alien":True,"robot":False,"cyborg":False,"god":False,"youtuber":False,"gamer":False,"singer":False,"politician":False,"animal":False,"superpowers":False,"leader":False,"smart":False,"funny":True,"strong":False,"flying":False,"red":True,"blue":True,"green":True,"black":True,"gold":False,"american":False,"meme":True,"space":True,"sus":True,"crewmate":True},

    {"name":"Big Chungus","human":False,"male":True,"female":False,"hero":False,"villain":False,"movie":False,"series":False,"game":False,"anime":False,"cartoon":True,"marvel":False,"dc":False,"magic":False,"inventor":False,"scientist":False,"rich":False,"billionaire":False,"armor":False,"mask":False,"alien":False,"robot":False,"cyborg":False,"god":False,"youtuber":False,"gamer":False,"singer":False,"politician":False,"animal":True,"superpowers":False,"leader":False,"smart":False,"funny":True,"strong":False,"flying":False,"red":False,"blue":False,"green":False,"black":False,"gold":False,"american":False,"meme":True,"rabbit":True,"big":True,"cute":True},

]
import tkinter as tk

questions = [
    ("Is your character a Human?", "human"),
    ("Is your character Male?", "male"),
    ("Is your character Female?", "female"),
    ("Is your character a Hero?", "hero"),
    ("Is your character a Villain?", "villain"),
    ("Is your character from a Movie?", "movie"),
    ("Is your character from a Series?", "series"),
    ("Is your character from a Game?", "game"),
    ("Is your character from an Anime?", "anime"),
    ("Is your character from a Cartoon?", "cartoon"),
    ("Is your character from Marvel?", "marvel"),
    ("Is your character from DC?", "dc"),
    ("Does your character use Magic?", "magic"),
    ("Is your character an Inventor?", "inventor"),
    ("Is your character a Scientist?", "scientist"),
    ("Is your character Rich?", "rich"),
    ("Is your character a Billionaire?", "billionaire"),
    ("Does your character wear Armor?", "armor"),
    ("Does your character wear a Mask?", "mask"),
    ("Is your character an Alien?", "alien"),
    ("Is your character a Robot?", "robot"),
    ("Is your character a Cyborg?", "cyborg"),
    ("Is your character a God?", "god"),
    ("Is your character a YouTuber?", "youtuber"),
    ("Is your character a Gamer?", "gamer"),
    ("Is your character a Singer?", "singer"),
    ("Is your character a Politician?", "politician"),
    ("Is your character an Animal?", "animal"),
    ("Does your character have Superpowers?", "superpowers"),
    ("Is your character a Leader?", "leader"),
    ("Is your character Smart?", "smart"),
    ("Is your character Funny?", "funny"),
    ("Is your character Strong?", "strong"),
    ("Can your character Fly?", "flying"),
]

scores = {}
current_question = 0
game_finished = False

for character in database:
    scores[character["name"]] = 0


def answer_question(user_answer):
    global current_question, game_finished

    if game_finished:
        return

    if current_question >= len(questions):
        show_result()
        return

    question_text, prop = questions[current_question]

    for character in database:
        real_value = character.get(prop, False)

        if real_value == user_answer:
            scores[character["name"]] += 2
        else:
            scores[character["name"]] -= 1

    current_question += 1

    if current_question >= len(questions):
        show_result()
    else:
        update_question()


def dont_know():
    global current_question, game_finished

    if game_finished:
        return

    current_question += 1

    if current_question >= len(questions):
        show_result()
    else:
        update_question()


def update_question():
    question_text, prop = questions[current_question]
    question_label.config(text=question_text)
    progress_label.config(text=f"Question {current_question + 1} / {len(questions)}")


def show_result():
    global game_finished
    game_finished = True

    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    best_name = sorted_scores[0][0]
    best_score = sorted_scores[0][1]

    result_text = f"I guess your character is:\n\n{best_name}\n\nScore: {best_score}"
    result_text += "\n\nOther possible characters:\n"

    for name, score in sorted_scores[1:20]:
        result_text += f"\n{name} - Score: {score}"

    question_label.pack_forget()

    result_box.config(state="normal")
    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, result_text)
    result_box.config(state="disabled")

    result_frame.pack(pady=15, fill="both", expand=True)

    progress_label.config(text="Finished!")

    yes_button.config(state="disabled")
    no_button.config(state="disabled")
    dont_know_button.config(state="disabled")


def restart_game():
    global scores, current_question, game_finished

    scores = {}

    for character in database:
        scores[character["name"]] = 0

    current_question = 0
    game_finished = False

    yes_button.config(state="normal")
    no_button.config(state="normal")
    dont_know_button.config(state="normal")

    result_frame.pack_forget()
    question_label.pack(pady=30)

    update_question()


# GUI
window = tk.Tk()
window.title("Python Akinator")
window.geometry("520x500")
window.resizable(False, False)
window.config(bg="#111111")

title_label = tk.Label(
    window,
    text="Python Akinator",
    font=("Arial", 24, "bold"),
    fg="white",
    bg="#111111"
)
title_label.pack(pady=20)

progress_label = tk.Label(
    window,
    text="Question 1",
    font=("Arial", 12),
    fg="#aaaaaa",
    bg="#111111"
)
progress_label.pack()

question_label = tk.Label(
    window,
    text="",
    font=("Arial", 16),
    fg="white",
    bg="#111111",
    wraplength=450,
    justify="center"
)
question_label.pack(pady=30)


# SCROLLABLE RESULT BOX
result_frame = tk.Frame(window, bg="#111111")

result_scrollbar = tk.Scrollbar(result_frame)
result_scrollbar.pack(side="right", fill="y")

result_box = tk.Text(
    result_frame,
    width=48,
    height=12,
    font=("Arial", 13),
    fg="white",
    bg="#222222",
    insertbackground="white",
    wrap="word",
    yscrollcommand=result_scrollbar.set
)
result_box.pack(side="left", fill="both", expand=True)

result_scrollbar.config(command=result_box.yview)
result_box.config(state="disabled")


button_frame = tk.Frame(window, bg="#111111")
button_frame.pack(pady=10)

yes_button = tk.Button(
    button_frame,
    text="Yes",
    font=("Arial", 14, "bold"),
    width=9,
    command=lambda: answer_question(True)
)
yes_button.grid(row=0, column=0, padx=6)

no_button = tk.Button(
    button_frame,
    text="No",
    font=("Arial", 14, "bold"),
    width=9,
    command=lambda: answer_question(False)
)
no_button.grid(row=0, column=1, padx=6)

dont_know_button = tk.Button(
    button_frame,
    text="Don't know",
    font=("Arial", 14, "bold"),
    width=10,
    command=dont_know
)
dont_know_button.grid(row=0, column=2, padx=6)

restart_button = tk.Button(
    window,
    text="Restart",
    font=("Arial", 12),
    command=restart_game
)
restart_button.pack(pady=15)

update_question()

window.mainloop()