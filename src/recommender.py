import csv
from typing import List, Dict, Tuple, Optional
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

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file into a list of dictionaries."""
    songs: List[Dict] = []

    with open(csv_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            song = {
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": int(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            }
            songs.append(song)

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score a song against a user's preferences and return reasons."""
    score = 0.0
    reasons: List[str] = []

    # Compare genre using a strong bonus for exact matches.
    preferred_genre = user_prefs.get("favorite_genre", user_prefs.get("genre"))
    song_genre = song.get("genre")
    if preferred_genre is not None and song_genre is not None:
        if str(preferred_genre).lower() == str(song_genre).lower():
            score += 2.0
            reasons.append("Genre match (+2.0)")

    # Compare mood using a smaller but meaningful bonus.
    preferred_mood = user_prefs.get("favorite_mood", user_prefs.get("mood"))
    song_mood = song.get("mood")
    if preferred_mood is not None and song_mood is not None:
        if str(preferred_mood).lower() == str(song_mood).lower():
            score += 1.0
            reasons.append("Mood match (+1.0)")

    # Compare energy similarity on a 0.0 to 1.0 scale.
    # A closer match receives more points, and a larger difference receives fewer.
    target_energy = user_prefs.get("target_energy", user_prefs.get("energy"))
    song_energy = song.get("energy")
    if target_energy is not None and song_energy is not None:
        try:
            target_energy_value = float(target_energy)
            song_energy_value = float(song_energy)
            energy_similarity = max(0.0, 1.0 - abs(song_energy_value - target_energy_value))
            score += energy_similarity
            reasons.append(f"Energy similarity (+{energy_similarity:.2f})")
        except (TypeError, ValueError):
            reasons.append("Energy similarity skipped (invalid values)")
    else:
        reasons.append("Energy similarity skipped (missing values)")

    return round(score, 2), reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Rank and return the top-scoring songs for a user."""
    scored_recommendations: List[Tuple[Dict, float, str]] = []

    # Score each song and keep the score plus explanation together.
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons)
        scored_recommendations.append((song, score, explanation))

    # Sort all scored songs from highest score to lowest score.
    ranked_recommendations = sorted(
        scored_recommendations,
        key=lambda item: item[1],
        reverse=True,
    )

    # Return only the top k recommendations.
    return ranked_recommendations[:k]
