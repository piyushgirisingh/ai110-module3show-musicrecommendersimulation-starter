# Reflection: Comparing Profile Pairs

For each pair of profiles below, I compared their top 5 outputs and noted what changed and why.

---

## Pair 1: High-Energy Pop vs Chill Lofi

**High-Energy Pop** (genre=pop, mood=happy, energy=0.9, acoustic=False)  
**Chill Lofi** (genre=lofi, mood=chill, energy=0.35, acoustic=True)

These two profiles are opposites in almost every way, and the outputs reflect that clearly. High-Energy Pop put Sunrise City and Gym Hero at the top — both are pop songs with high energy and a driving beat. Chill Lofi returned Library Rain and Midnight Coding — slow, quiet lofi tracks with a relaxed mood and a lot of acoustic texture.

What is interesting is *why* Gym Hero keeps showing up near the top for Happy Pop listeners even though its mood is "intense," not "happy." The reason is that there are only two pop songs in the entire catalog. Once the system gives both of them the genre match bonus, Gym Hero is the second pop song — and its energy (0.93) is very close to the user's target. So the system picks it not because it matches the mood, but because it is the only other pop option available. If you imagine a music app doing this in real life, it would be like asking Spotify for happy pop and getting a pump-up gym track because the algorithm ran out of clearly happy pop songs and grabbed the nearest pop song it could find.

The Chill Lofi results felt more accurate. The lofi catalog has three songs and they all share a quiet, acoustic quality, so the top results naturally cluster together in a way that would feel right to a real listener.

---

## Pair 2: Deep Intense Rock vs Happy Soft Metal Fan

**Deep Intense Rock** (genre=rock, mood=intense, energy=0.92, acoustic=False)  
**Happy Soft Metal Fan** (genre=metal, mood=happy, energy=0.2, acoustic=True)

Both profiles ask for a heavy genre but everything else is different. Deep Intense Rock got exactly what it asked for — Storm Runner scored nearly perfect (4.44 out of 4.50) because genre, mood, and energy all aligned at once. This is the system working the way it is supposed to.

Happy Soft Metal Fan is where things break down. Iron Collapse — the only metal song — is angry, extremely loud (energy 0.97), and has almost no acoustic quality. It scored first anyway because the genre match bonus pushed it ahead of every other song, even ones that matched the user's mood and energy far better. The #2 result was Rooftop Lights, an indie pop song, which matched the "happy" mood but has nothing to do with metal. So the top two results pulled in completely opposite directions.

The comparison shows that the system works well when one song perfectly fits all preferences, but struggles when the catalog only has one representative of a genre and that song conflicts with everything else the user asked for. Deep Intense Rock was well served; Happy Soft Metal Fan was essentially abandoned.

---

## Pair 3: Acoustic EDM vs Non-Acoustic Mellow

**Acoustic EDM** (genre=edm, mood=euphoric, energy=0.9, acoustic=True)  
**Non-Acoustic Mellow** (genre=classical, mood=peaceful, energy=0.1, acoustic=False)

This pair tests what happens when acoustic preference conflicts with genre. For Acoustic EDM, the top result was Pulse Override — the one EDM song — which has acousticness of only 2%. The user said they love acoustic music, but the system recommended the most electronic song in the catalog. The genre bonus was so strong that the acoustic preference became nearly invisible in the final score.

Non-Acoustic Mellow had the opposite problem but handled it differently. Autumn Sonata scored first because it matched on genre (classical) and mood (peaceful), even though it is 97% acoustic and the user said they do not like acoustic music. The penalty for that mismatch was tiny compared to the genre and mood bonuses it received.

In plain terms: the system learned "this person likes EDM and classical" and acted on that, while almost completely ignoring the acoustic preference both users stated. This reveals that acoustic preference is the weakest signal in the scoring formula — it barely changes the outcome when any other signal is present.

---

## Pair 4: High-Energy Sad vs Stranded Listener

**High-Energy Sad** (genre=blues, mood=sad, energy=0.9, acoustic=False)  
**Stranded Listener** (genre=k-pop, mood=wistful, energy=0.5, acoustic=False)

These two profiles both have preferences that do not fit neatly into the catalog, but they fail in different ways.

High-Energy Sad got a confident #1 result — Rainy Monday Blues scored 3.50. But this is misleading. The song is slow, quiet, and low-energy (0.31), which is the opposite of what the user asked for in terms of energy. The system ranked it first because the genre and mood both matched exactly, which together added 3.0 points and overwhelmed the energy gap penalty. The recommendation looks correct on paper but would probably feel wrong to a real listener who wanted something with drive and intensity.

Stranded Listener received no genre or mood matches at all because k-pop and "wistful" do not exist in the catalog. The top five results were decided entirely by which songs happened to have energy close to 0.5 and low acousticness. Velvet Nights (r&b) came first — not because it is anything like k-pop, but because its energy was the closest match. There was no signal from the system that the listener's actual preferences were unmet. A real music app would ideally say "we don't have what you're looking for" rather than quietly recommending something unrelated.

---

## Pair 5: Drake / Hip-Hop vs Synthwave Tie Breaker

**Drake / Hip-Hop** (genre=hip-hop, mood=confident, energy=0.75, acoustic=False)  
**Synthwave Tie Breaker** (genre=synthwave, mood=moody, energy=0.75, acoustic=False)

These two profiles have identical energy and acoustic preferences — only genre and mood differ. Yet the quality of the results is completely different.

Synthwave Tie Breaker produced a near-perfect result. Night Drive Loop is the only synthwave song and it matched genre, mood, and energy all at once, scoring 4.39 out of 4.50. The gap to the second result was 3 full points. The system worked perfectly here.

Drake / Hip-Hop also got a strong #1 — Golden Era matched on genre, mood, and energy. But positions #2 through #5 were noticeably weaker. Shadow District (trap) came second because trap is adjacent in sound to hip-hop, which feels reasonable. But Night Drive Loop (synthwave) and Sunrise City (pop) appeared in the list purely because of energy proximity, with no genre or cultural connection to hip-hop at all.

The comparison shows that when a genre has only one representative, the system works well for that user's top pick but has nothing meaningful to offer beyond it. Both profiles had the same energy target and got a good #1 — but the hip-hop fan's #3–#5 were essentially random, while the synthwave fan's entire top 5 was at least energy-coherent.
