import csv
from typing import List, Dict, Tuple
from dataclasses import dataclass


@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float


@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


# ---------------------------------------------------------------------------
# Scoring helpers
# ---------------------------------------------------------------------------

def _score_song(song: Song, user: UserProfile) -> float:
    """
    Scoring rule: judges one song against a user profile.

    Formula:
        score = 0.35 * mood_match
              + 0.30 * energy_proximity
              + 0.20 * genre_match
              + 0.15 * acoustic_match

    All components are in [0, 1], so the final score is also in [0, 1].
    """
    mood_score     = 1.0 if song.mood == user.favorite_mood else 0.0
    energy_score   = 1.0 - abs(song.energy - user.target_energy)
    genre_score    = 1.0 if song.genre == user.favorite_genre else 0.0
    acoustic_score = song.acousticness if user.likes_acoustic else (1.0 - song.acousticness)

    return (
        0.35 * mood_score
        + 0.30 * energy_score
        + 0.20 * genre_score
        + 0.15 * acoustic_score
    )


def _build_explanation(song: Song, user: UserProfile) -> str:
    """
    Builds a human-readable explanation for why a song was recommended.
    """
    reasons = []

    if song.mood == user.favorite_mood:
        reasons.append(f"mood matches your preference ({song.mood})")

    if song.genre == user.favorite_genre:
        reasons.append(f"genre matches ({song.genre})")

    energy_diff = abs(song.energy - user.target_energy)
    if energy_diff <= 0.15:
        reasons.append(
            f"energy ({song.energy:.2f}) is close to your target ({user.target_energy:.2f})"
        )

    if user.likes_acoustic and song.acousticness >= 0.6:
        reasons.append(f"warm acoustic feel ({song.acousticness:.0%} acoustic)")
    elif not user.likes_acoustic and song.acousticness <= 0.3:
        reasons.append(f"electronic texture ({song.acousticness:.0%} acoustic)")

    if not reasons:
        reasons.append("closest overall match in the catalog")

    return "Recommended because: " + ", ".join(reasons)


# ---------------------------------------------------------------------------
# OOP interface  (required by tests/test_recommender.py)
# ---------------------------------------------------------------------------

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """

    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """
        Ranking rule: scores every song, sorts descending, returns top k.
        """
        scored = [(song, _score_song(song, user)) for song in self.songs]
        scored.sort(key=lambda x: x[1], reverse=True)
        return [song for song, _ in scored[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Return a human-readable string explaining why a song was recommended for this user."""
        return _build_explanation(song, user)


# ---------------------------------------------------------------------------
# Functional interface  (required by src/main.py)
# ---------------------------------------------------------------------------

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file and returns a list of dicts.
    Required by src/main.py
    """
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            songs.append({
                "id":           int(row["id"]),
                "title":        row["title"],
                "artist":       row["artist"],
                "genre":        row["genre"],
                "mood":         row["mood"],
                "energy":       float(row["energy"]),
                "tempo_bpm":    float(row["tempo_bpm"]),
                "valence":      float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            })
    return songs


def _score_song_dict(song: Dict, user_prefs: Dict) -> Tuple[float, List[str]]:
    """Score a song against user preferences and return (total_score, reasons) where max score is 4.5."""
    score = 0.0
    reasons = []

    if song["genre"] == user_prefs.get("genre", ""):
        score += 1.0
        reasons.append("genre match (+1.0)")

    if song["mood"] == user_prefs.get("mood", ""):
        score += 1.0
        reasons.append("mood match (+1.0)")

    energy_score = 2.0 * (1.0 - abs(song["energy"] - user_prefs.get("energy", 0.5)))
    score += energy_score
    reasons.append(f"energy proximity (+{energy_score:.2f})")

    likes_acoustic = user_prefs.get("likes_acoustic", False)
    acoustic_score = 0.5 * (song["acousticness"] if likes_acoustic else (1.0 - song["acousticness"]))
    score += acoustic_score
    reasons.append(f"acoustic fit (+{acoustic_score:.2f})")

    return score, reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score every song, sort by score descending, and return the top k as (song, score, reasons) tuples."""
    scored = [
        (song, score, reasons)
        for song in songs
        for score, reasons in [_score_song_dict(song, user_prefs)]
    ]
    return sorted(scored, key=lambda x: x[1], reverse=True)[:k]
