#how to put text into a list 
#triple qoutes allow you to input one big string 
text = """Hey, Roman numeral seven, bae, drop it like it's hot
If this world was mine, I'd take your dreams and make 'em multiply
If this world was mine, I'd take your enemies in front of God
Introduce 'em to that light, hit them strictly with that fire
Fah-fah, fah-fah-fah, fah-fah, fah
Hey, Roman numeral seven, bae, drop it like it's hot
If this world was mine, I'd take your dreams and make 'em multiply
If this world was mine, I'd take your enemies in front of God
Introduce 'em to that light, hit them strictly with that fire
It's a vibe, do your dance, let 'em watch
She a fan, he a flop, they just wanna kumbaya, nah

[Chorus: SZA, SZA & Kendrick Lamar]
In this world, concrete flowers grow
Heartache, she only doin' what she know
Weekends, get it poppin' on the low
Better days comin' for sure
If this world were—
If it was up to me
I wouldn't give these nobodies no sympathy
I'd take away the pain, I'd give you everything
I just wanna see you win, wanna see
If this world were mine
See rap shows near New York City
Get tickets as low as $32

You might also like

hey now
Kendrick Lamar

squabble up
Kendrick Lamar

wacced out murals
Kendrick Lamar

[Verse 2: Kendrick Lamar & SZA]
It go in (When you), out (Ride it), do it real slow (Slide)
Baby, you a star, strike, pose
When I'm (When you), with you (With me), everything goes (Slow)
Come and (Put that), put that (On my), on my (Titi), soul (Soul)
'Rari (Red), crown (Stack), wrist (Stay), froze (Really)
Drip (Tell me), pound (If you), on the way home (Love me)

[Chorus: Kendrick Lamar & SZA]
In this world, concrete flowers grow
Heartache, she only doin' what she know
Weekends, get it poppin' on the low
Better days comin' for sure
If this world were—
If it was up to me
I wouldn't give these nobodies no sympathy
I'd take away the pain, I'd give you everything
I just wanna see you win, wanna see
If this world were mine

[Verse 3: Kendrick Lamar & SZA]
I can't lie
I trust you, I love you, I won't waste your time
I turn it off just so I can turn you on
I'ma make you say it loud
I'm not even trippin', I won't stress you out
I might even settle down for you, I'ma show you I'm a pro
I'ma take my time and turn it off
Just so I can turn you on, baby
Weekends, get it poppin' on the low
Better days comin' for sure"""
#split gives you a list og a bunch of strings
print(text.split())

lyrics_count = {}
for word in text.split():
    if word in lyrics_count:
       lyrics_count[word] += 1
    else:
        lyrics_count[word] = 1
print(lyrics_count)