"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from typing import Dict, List, Tuple

from .recommender import load_songs, recommend_songs


def build_profiles() -> List[Tuple[str, Dict[str, object]]]:
    """Create a set of user profiles to evaluate the recommender."""
    return [
        (
            "High-Energy Pop",
            {
                "favorite_genre": "pop",
                "favorite_mood": "happy",
                "target_energy": 0.90,
                "likes_acoustic": False,
            },
        ),
        (
            "Chill Lofi",
            {
                "favorite_genre": "lofi",
                "favorite_mood": "chill",
                "target_energy": 0.35,
                "likes_acoustic": True,
            },
        ),
        (
            "Deep Intense Rock",
            {
                "favorite_genre": "rock",
                "favorite_mood": "intense",
                "target_energy": 0.95,
                "likes_acoustic": False,
            },
        ),
        (
            "Conflicting Edge Case",
            {
                "favorite_genre": "pop",
                "favorite_mood": "happy",
                "target_energy": 0.20,
                "likes_acoustic": False,
            },
        ),
    ]


def main() -> None:
    songs = load_songs("data/songs.csv")
    profiles = build_profiles()

    for profile_name, profile in profiles:
        recommendations = recommend_songs(profile, songs, k=5)

        print(f"Profile: {profile_name}")
        print("-" * 40)
        for index, (song, score, explanation) in enumerate(recommendations, start=1):
            print(f"{index}. {song['title']}")
            print(f"   Score: {score:.2f}")
            print("   Reasons:")
            for reason in explanation.split("; "):
                if reason:
                    print(f"     - {reason}")
            print()


if __name__ == "__main__":
    main()
