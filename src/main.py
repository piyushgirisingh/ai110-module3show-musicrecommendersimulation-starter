"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    # Additional user profiles
    high_energy_pop   = {"label": "High-Energy Pop",    "genre": "pop",  "mood": "happy",   "energy": 0.9,  "likes_acoustic": False}
    chill_lofi        = {"label": "Chill Lofi",         "genre": "lofi", "mood": "chill",   "energy": 0.35, "likes_acoustic": True}
    deep_intense_rock = {"label": "Deep Intense Rock",  "genre": "rock", "mood": "intense", "energy": 0.92, "likes_acoustic": False}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n" + "=" * 40)
    print("  TOP RECOMMENDATIONS")
    print(f"  Genre: {user_prefs['genre']}  |  Mood: {user_prefs['mood']}  |  Energy: {user_prefs['energy']}")
    print("=" * 40)

    for rank, (song, score, reasons) in enumerate(recommendations, start=1):
        print(f"\n#{rank}  {song['title']} by {song['artist']}")
        print(f"    Score: {score:.2f} / 4.50")
        print("    Why:")
        for reason in reasons:
            print(f"      • {reason}")

    print("\n" + "=" * 40)

    for profile in [high_energy_pop, chill_lofi, deep_intense_rock]:
        label = profile["label"]
        prefs = {k: v for k, v in profile.items() if k != "label"}
        recs  = recommend_songs(prefs, songs, k=3)

        print("\n" + "=" * 40)
        print(f"  {label.upper()}")
        print(f"  Genre: {prefs['genre']}  |  Mood: {prefs['mood']}  |  Energy: {prefs['energy']}")
        print("=" * 40)

        for rank, (song, score, reasons) in enumerate(recs, start=1):
            print(f"\n#{rank}  {song['title']} by {song['artist']}")
            print(f"    Score: {score:.2f} / 4.50")
            print("    Why:")
            for reason in reasons:
                print(f"      • {reason}")

        print("\n" + "=" * 40)


if __name__ == "__main__":
    main()
