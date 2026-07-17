# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

VibePulse
---

## 2. Intended Use  

This recommender is designed to generate personalized song recommendations from a small catalog for a listener based on simple content features such as genre, mood, and energy, and it is mainly for students and instructors exploring how recommendation systems work in practice. It generates top-ranked song suggestions by comparing song attributes to a user preference profile, and it assumes the user has stable preferences that can be represented with clear labels and a target energy level (for example, favorite genre, favorite mood, and desired intensity). This project is intended for classroom exploration and learning, not for real production users, so its goal is transparency and experimentation rather than large-scale commercial accuracy.

---

## 3. How the Model Works  

This model is a simple content-based recommender that compares each song in the catalog to a listener profile and gives every song a score. The profile includes a favorite genre, favorite mood, and target energy level. A song gets a strong boost if its genre matches the listener, a smaller boost if its mood matches, and then receives additional points based on how close its energy level is to the listener's target energy. After all songs are scored, the system sorts them from highest to lowest and returns the top recommendations with short reason labels (for example, genre match or energy similarity) so the ranking is easy to understand.

Because this model uses only song attributes and a manually defined user profile, it is easy to explain and test, but it is also limited. It does not learn from listening history or other users, and it currently emphasizes exact category matches and energy closeness more than broader musical context. This makes it a good educational example of how recommendation rules turn input features into ranked predictions.

---

## 4. Data  

This project uses a small hand-curated catalog of 20 songs from data/songs.csv. Each song includes structured attributes that the recommender can score directly: title, artist, genre, mood, energy, tempo (BPM), valence, danceability, and acousticness. The catalog covers a broad but limited mix of genres, including pop, lofi, rock, electronic, ambient, jazz, folk, indie pop, indie folk, hip hop, house, synthwave, latin, classical, country, and rnb, and it includes moods such as happy, chill, intense, calm, focused, relaxed, energetic, romantic, hopeful, playful, reflective, nostalgic, and serene. I did not add or remove any rows from the provided starter dataset during this assignment, so all experiments were run on the same fixed catalog. Important parts of musical taste are still missing, including lyrics, language preference, cultural context, artist familiarity, listening history, skip behavior, time-of-day context, and evolving preferences over time, which means the model can only represent a simplified view of user taste.

---

## 5. Strengths  

This recommender works best for users with clear, consistent preferences for one genre and one mood, especially when their target energy is not extreme. In the evaluation, it produced intuitive top results for profiles like High-Energy Pop, Chill Lofi, and Deep Intense Rock, where the highest-ranked songs had expected genre or mood matches and close energy values. The scoring pattern it captures well is straightforward similarity: songs with exact genre and mood alignment plus nearby energy tend to rise to the top, and the generated reasons make this behavior transparent. This made the recommendations easy to interpret and generally consistent with what I expected from the weighted rules.

---

## 6. Limitations and Bias 

This system has important limitations because it only uses a few hand-crafted features and does not learn from real listening behavior. It does not consider lyrics, language, artist loyalty, listening context, skip history, or how tastes change over time, so it can miss why a listener actually likes a song. The small 20-song catalog also limits fairness and coverage across styles, and some genres or moods may have too few examples to compete consistently.

There is also clear filter-bubble risk in the current scoring logic. Because exact genre match (+2.0) and mood match (+1.0) are strong fixed bonuses, the model repeatedly pushes similar songs to the top and can keep reinforcing the same taste profile instead of introducing variety. Over time, this kind of rule can narrow what a user sees, reduce discovery across genres, and under-rank songs that are close in overall feel but use different labels.

The weighting can also bias outcomes toward users whose preferences fit the available categories, while users with mixed or evolving tastes may receive weaker personalization. For example, a song with different genre tags but very close energy and emotional feel can still be ranked lower than a category match, which may unintentionally favor dominant labels in the dataset and disadvantage underrepresented styles.

---

## 7. Evaluation  

I checked whether the recommender behaved as expected by running it against four distinct user profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock, and a conflicting edge-case profile. I looked for whether the highest-ranked tracks matched the intended mood and energy preferences and whether the explanations reflected the scoring logic in a way that felt understandable.

The tested profiles represent different listening styles: High-Energy Pop (upbeat pop with high energy), Chill Lofi (calmer low-energy lofi/chill), Deep Intense Rock (high-energy intense rock), and a Conflicting Edge Case (pop and happy preferences but very low target energy). What may be surprising is that the conflicting profile still ranked pop/happy songs highly, even when their energy was not close to the target, because fixed genre and mood bonuses are strong enough to offset weaker energy similarity.

```text
Profile: High-Energy Pop
----------------------------------------
1. Sunrise City
   Score: 3.92
   Reasons:
     - Genre match (+2.0)
     - Mood match (+1.0)
     - Energy similarity (+0.92)

2. Gym Hero
   Score: 2.97
   Reasons:
     - Genre match (+2.0)
     - Energy similarity (+0.97)

3. Rooftop Lights
   Score: 1.86
   Reasons:
     - Mood match (+1.0)
     - Energy similarity (+0.86)

4. Storm Runner
   Score: 0.99
   Reasons:
     - Energy similarity (+0.99)

5. Backstreet Sparks
   Score: 0.98
   Reasons:
     - Energy similarity (+0.98)
```

```text
Profile: Chill Lofi
----------------------------------------
1. Library Rain
   Score: 4.00
   Reasons:
     - Genre match (+2.0)
     - Mood match (+1.0)
     - Energy similarity (+1.00)

2. Midnight Coding
   Score: 3.93
   Reasons:
     - Genre match (+2.0)
     - Mood match (+1.0)
     - Energy similarity (+0.93)

3. Focus Flow
   Score: 2.95
   Reasons:
     - Genre match (+2.0)
     - Energy similarity (+0.95)

4. Spacewalk Thoughts
   Score: 1.93
   Reasons:
     - Mood match (+1.0)
     - Energy similarity (+0.93)

5. Coffee Shop Stories
   Score: 0.98
   Reasons:
     - Energy similarity (+0.98)
```

```text
Profile: Deep Intense Rock
----------------------------------------
1. Storm Runner
   Score: 3.96
   Reasons:
     - Genre match (+2.0)
     - Mood match (+1.0)
     - Energy similarity (+0.96)

2. Gym Hero
   Score: 1.98
   Reasons:
     - Mood match (+1.0)
     - Energy similarity (+0.98)

3. Backstreet Sparks
   Score: 0.93
   Reasons:
     - Energy similarity (+0.93)

4. Sunrise City
   Score: 0.87
   Reasons:
     - Energy similarity (+0.87)

5. Neon Skyline
   Score: 0.86
   Reasons:
     - Energy similarity (+0.86)
```

```text
Profile: Conflicting Edge Case
----------------------------------------
1. Sunrise City
   Score: 3.38
   Reasons:
     - Genre match (+2.0)
     - Mood match (+1.0)
     - Energy similarity (+0.38)

2. Gym Hero
   Score: 2.27
   Reasons:
     - Genre match (+2.0)
     - Energy similarity (+0.27)

3. Rooftop Lights
   Score: 1.44
   Reasons:
     - Mood match (+1.0)
     - Energy similarity (+0.44)

4. Paper Skyline
   Score: 1.00
   Reasons:
     - Energy similarity (+1.00)

5. Spacewalk Thoughts
   Score: 0.92
   Reasons:
     - Energy similarity (+0.92)
```

Pairwise profile comparisons:

1. High-Energy Pop vs Chill Lofi: High-Energy Pop prioritizes songs like Sunrise City and Gym Hero, while Chill Lofi puts Library Rain and Midnight Coding at the top. This makes sense because genre and mood bonuses differ (pop/happy vs lofi/chill), and the energy target shifts from high (0.90) to low (0.35).
2. High-Energy Pop vs Deep Intense Rock: Both profiles favor high-energy songs, but the top result changes from Sunrise City to Storm Runner. This is reasonable because Deep Intense Rock gets both genre and mood matches on Storm Runner, while High-Energy Pop gets those boosts on pop/happy tracks instead.
3. High-Energy Pop vs Conflicting Edge Case: Both profiles share pop/happy preferences, but the conflicting profile introduces a very low energy target (0.20), which lifts low-energy songs like Paper Skyline into the top five. This shows energy can influence rank, but genre and mood still strongly anchor the first positions.
4. Chill Lofi vs Deep Intense Rock: Chill Lofi recommendations cluster around low-energy calm tracks, while Deep Intense Rock surfaces intense, high-energy tracks. The difference matches the opposite targets in both category labels and energy direction.
5. Chill Lofi vs Conflicting Edge Case: Chill Lofi has coherent lofi/chill signals and therefore returns lofi-heavy results, but the conflicting profile mixes pop/happy labels with low energy and creates a more mixed top five. This makes sense because the conflicting profile pulls the scorer in two directions.
6. Deep Intense Rock vs Conflicting Edge Case: Deep Intense Rock consistently rewards intense, high-energy songs, while the conflicting profile introduces lower-energy options and fewer intense tracks. This contrast is expected because their target energies are far apart (0.95 vs 0.20), even though both still rely on the same fixed category bonus structure.

---

## 8. Future Work  

If I continue improving this recommender, I would add more user preference inputs beyond genre, mood, and energy, such as preferred tempo range, valence, danceability, acousticness, favorite artists, and a short recent listening history. I would also improve recommendation explanations by showing a clearer score breakdown per feature, adding a simple "why this was recommended" summary sentence, and displaying one contrast note like "this song ranked above X because of stronger mood alignment."

To improve diversity, I would add a re-ranking step so the top 5 are not all from the same genre or same mood, while still keeping overall relevance high. I would also test a novelty control that intentionally includes at least one "nearby but different" song to reduce filter-bubble effects and increase discovery.

To handle more complex user tastes, I would move from a single fixed profile to a blended preference model that supports multiple favorite genres or moods with different weights (for example, 60% chill lofi and 40% indie pop). I would also update preferences over time using user feedback signals (like skip, like, or replay) so the system can adapt when tastes change.

Additional recommendations to make this project stronger:

- Expand the catalog size and balance representation across genres/moods to reduce small-dataset bias.
- Add simple offline evaluation metrics (precision@k or hit-rate on a labeled validation set) to compare scoring versions more objectively.
- Run fairness and robustness checks across diverse profile types, especially edge-case and mixed-preference users.
- Keep an experiment log of weight changes and outcomes so model updates are reproducible and easy to compare.

---

## 9. Personal Reflection  

I learned that recommender systems are kind of controlled in a way and depending on how a particular recommender system is set up, will be dependent on how it operates. This was even surprising when I decided to test the different users and in the conflicting edge case profile it still ranked certain songs higher due to the constraints of the code being strong. For instance some songs still can rank high even if one feature is a poor match. This opened my eyes on how I vew music recommendation apps now, because they go based off of design choices within the apps and not neutral truth. This also shows that weighting features can favor familiarity over discovery and real systems need feedback loops, diversity controls, and fairness checks.

Using AI tools helped me speed up writing, structure my analysis, and compare profile outputs more clearly, especially when turning terminal results into readable reflections. I still had to verify AI-assisted content against actual code behavior and terminal output whenever numbers or ranking details were mentioned, because small wording mistakes can misrepresent what the model actually did. If I continued this project, I would expand profile features, add simple user-feedback updates over time, and introduce diversity-aware ranking so the system can stay personalized without repeatedly recommending the same style.
