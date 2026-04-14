# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

**VibeMatch 1.0**

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

**Goal / Task:** This system suggests songs from a small catalog based on a user's preferred genre, mood, energy level, and acoustic taste. It is a classroom project — not for real users.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

**Algorithm Summary:** Every song gets points for matching genre (+1), matching mood (+1), being close in energy (up to +2), and fitting the acoustic preference (up to +0.5). The song with the highest total score wins. Energy was made twice as important as genre after testing showed genre was dominating too much.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

**Data Used:** 20 songs across 17 genres with features like energy, mood, acousticness, and tempo. 15 of the 17 genres have only one song, so most genre preferences have no backup option.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

It works best when all four signals point to the same song. The Deep Intense Rock profile got a near-perfect score of 4.44/4.50 because genre, mood, and energy all matched at once. Lofi listeners also get consistent results because the catalog has three lofi songs that share similar qualities.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

One of the clearest weaknesses discovered through experimentation is that the system structurally disadvantages low-energy listeners. Because 45% of the catalog (9 out of 20 songs) has an energy level above 0.7, a user who prefers calm or quiet music has very few close matches available, and the energy proximity formula still awards partial points to high-energy songs even when the gap is large. This means a user targeting an energy level of 0.1 has only one song within a reasonable range, while a high-energy user has seven — so the quality of recommendations is not equal across different listener types. The problem compounds because low-energy songs in the catalog are almost entirely acoustic, so a user who wants calm but non-acoustic music (such as quiet electronic or ambient) will always be pushed toward songs that conflict with their acoustic preference. In a real product, this kind of imbalance would quietly serve some users well while consistently frustrating others, without any visible error or warning in the system.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

To evaluate the system, nine user profiles were tested: three standard profiles (High-Energy Pop, Chill Lofi, Deep Intense Rock), one personal profile based on a real listener taste (hip-hop / confident / energy 0.75), and five adversarial profiles designed to expose edge cases (High-Energy Sad, Acoustic EDM, Non-Acoustic Mellow, Happy Soft Metal Fan, and Stranded Listener with no matching genre or mood in the catalog). For each profile the top five recommendations were inspected and scored manually against what a reasonable listener would expect.

The most surprising result was the Acoustic EDM profile. A user who said they loved acoustic music and preferred EDM received Pulse Override — the least acoustic song in the entire catalog — as their top recommendation. The genre match bonus was so large that it completely cancelled out the acoustic preference, meaning the system told an acoustic-loving user to listen to a fully electronic song and then explained it as a good match. A second surprise came from the High-Energy Sad profile: even though the user wanted high-energy music, the sad blues song ranked first by a wide margin because the genre and mood bonuses together outweighed the energy gap. The system appeared to recommend correctly, but for the wrong reason. A third finding was that for the Stranded Listener profile — a user whose genre and mood did not exist in the catalog at all — the system silently fell back to ranking songs by energy alone, with no indication to the user that none of their actual preferences were being honored.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

**Ideas for Improvement:**
- Add a warning when no songs match the user's genre or mood instead of silently returning unrelated results.
- Expand the catalog to at least 3 songs per genre so genre match is actually meaningful.
- Add a diversity rule so the top 5 results don't all come from the same energy range.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

**Intended Use:** For learning how rule-based recommenders work in a classroom setting. **Not intended for:** real music discovery — the catalog is too small, it ignores listening history, and it gives confident results even when none of the user's preferences are actually met.

Personal Reflection:

**My biggest learning moment** was when I tested the "Acoustic EDM" profile. I told the system the user loved acoustic music, but it recommended Pulse Override — the least acoustic song in the entire catalog — as the #1 result. It even explained why it was a "good match." That was the moment I realized the formula looked correct on paper but was actually broken in practice. The genre bonus was so large it erased everything else. It taught me that a number can be technically valid and still produce a completely wrong answer.

**How AI tools helped, and when I had to double-check.** Using AI to run experiments and analyze the catalog saved a lot of time — it quickly counted how many songs were in each genre and energy bucket, which would have taken me much longer manually. But I had to verify the math myself for specific profiles. For example, the AI predicted Rainy Monday Blues would rank first for a high-energy sad profile, and I checked the arithmetic by hand to confirm it. The output was right, but understanding why required reading the formula carefully myself. The tool helped me move fast; I still had to think through what the numbers actually meant.

**What surprised me about simple algorithms feeling like recommendations.** When the Deep Intense Rock profile returned Storm Runner at 4.44 out of 4.50, it genuinely felt like a good recommendation — the kind a friend who knew my taste might make. But the algorithm has no idea what rock music sounds like. It just matched three labels and a number. That gap between "feels right" and "actually understands" is what I think about now when I use Spotify or YouTube Music. The suggestions feel personal, but underneath they are probably closer to this than I expected.

**What I would try next.** I would add a tempo range preference to the user profile, because two songs can have the same energy but feel completely different at 70 BPM versus 140 BPM. I would also try building a version that learns from feedback — if a user skips a song, lower its genre's weight for that session. That would make the system actually adapt instead of giving the same answer every time.
