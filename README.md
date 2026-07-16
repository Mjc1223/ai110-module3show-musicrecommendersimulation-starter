# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

This project uses a simple content-based recommender. Each song is described by a set of features, and the system compares those features to a user’s taste profile.

- Each `Song` uses features such as:
  - `genre`: the broad style of the song
  - `mood`: the emotional feel, such as happy, chill, intense, or relaxed
  - `energy`: how active or intense the song feels
  - `tempo_bpm`: how fast the song is
  - `valence`: how positive or bright the song feels
  - `danceability` and `acousticness`: extra signals about rhythm and sound style

- Each `UserProfile` stores information about what the user seems to prefer:
  - `favorite_genre`: the style they like most
  - `favorite_mood`: the mood they usually enjoy
  - `target_energy`: the intensity level they tend to prefer
  - `likes_acoustic`: whether they often prefer acoustic or more electronic-sounding songs

- The `Recommender` computes a score for each song by comparing the song’s features to the user profile:
  - genre and mood matches receive a boost
  - numeric features such as energy, tempo, valence, danceability, and acousticness are compared to the user’s preferred values
  - songs that are closer to the user’s preferred values receive higher scores

- The recommendation process is:
  1. Input the user profile and the song catalog from `songs.csv`
  2. Compare each song to the user’s preferences
  3. Calculate a weighted similarity score for every song
  4. Rank the songs from highest score to lowest
  5. Output the top 5 recommended songs

- Final algorithm recipe:
  - Add **2.0 points** for an exact genre match
  - Add **1.0 point** for an exact mood match
  - Add up to **1.0 point** based on how close the song’s energy is to the user’s target energy
  - Add up to **1.0 point** for tempo similarity
  - Add up to **1.0 point** for valence similarity
  - Add up to **0.5 points** for danceability similarity
  - Add up to **0.5 points** for acousticness similarity
  - For numerical features, values closer to the user’s target receive more points
  - After every song is scored, the system sorts the songs from highest score to lowest and returns the top recommendations

Simple flow:

UserProfile -> Compare with each Song -> Score based on genre, mood, energy, tempo, valence, danceability, and acousticness -> Rank songs -> Show top recommendations

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:
1. Sunrise City
   Score: 3.98
   Reasons:
     - Genre match (+2.0)
     - Mood match (+1.0)
     - Energy similarity (+0.98)

2. Gym Hero
   Score: 2.87
   Reasons:
     - Genre match (+2.0)
     - Energy similarity (+0.87)

3. Rooftop Lights
   Score: 1.96
   Reasons:
     - Mood match (+1.0)
     - Energy similarity (+0.96)

4. Neon Skyline
   Score: 0.99
   Reasons:
     - Energy similarity (+0.99)

5. Velvet Static
   Score: 0.99
   Reasons:
     - Energy similarity (+0.99)
```


---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

Potential biases:

- This recommender may over-prioritize exact genre and mood matches because those features receive fixed bonus points. As a result, a song from a different genre that closely matches the user’s preferred energy, tempo, and emotional feel might rank lower than expected.
- The system also depends on manually assigned song features, so inaccurate labels or numerical values could affect the recommendations.
- Because the user profile contains specific target values, the recommender may favor songs that are very similar and provide less variety or discovery.

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



