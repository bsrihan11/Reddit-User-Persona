# Reddit User Persona Generator

This project uses **LangChain** and **Pydantic** to generate detailed Reddit user personas based on public data scraped from their posts and comments. The output is structured in a well-defined JSON schema (saved as a `.txt` file), capturing various facets of a user's online presence.

---

## Features

- **Mistral AI LLM**: Utilizes the Mistral AI's `mistral-large-dataset` for persona inference.
- **LangChain Integration**: Employs LangChain for templating, prompt chaining, and output parsing pipelines.
- **Reddit Scraping**: Collects user data from Reddit using the PRAW API.
- **Structured Output**: Uses `Pydantic` for strict type enforcement and easy JSON parsing.
- **Personality Profiling**: Infers MBTI-style personality traits such as energy orientation, identity, and thinking style.
- **Behavioral Analysis**: Identifies and summarizes the user's habits and behavior patterns from their online activity.
- **Location & Demographics**: Estimates age, gender, and location through contextual clues and citations.
- **Hobbies & Subreddit Mapping**: Lists the user's interests and the subreddits where they are most active.
- **Citation-Aware**: Each field is backed by direct Reddit URLs as evidence for transparency and traceability.
- **Quote or Motto Extraction**: Captures a short, signature phrase that reflects the user's online persona or tone.

---

## Output Structure

The model returns a single object structured as follows (saved in `.txt` format):

### Top-Level Fields in `UserPersona`

| Field                     | Type                    | Description                                                      |
|---------------------------|-------------------------|------------------------------------------------------------------|
| `username`                | `str`                   | The Reddit handle.                                               |
| `estimated_age_range`     | `FieldWithCitations`    | Age range (e.g., "18-24") and URLs.                              |
| `gender`                  | `FieldWithCitations`    | Gender inference with citation.                                  |
| `location`                | `FieldWithCitations`    | Location (if mentioned/implied).                                 |
| `occupation_or_education` | `FieldWithCitations`    | Job/education mentions.                                          |
| `personality`             | `Personality`           | MBTI-style traits (introvert, intuitive, etc.)                   |
| `hobbies_and_interests`   | `FieldWithListValue`    | List of hobbies or interests.                                    |
| `behavior_and_habits`     | `BehaviorAndHabits`     | Key observed behaviors and habits.                               |
| `most_active_subreddits`  | `FieldWithListValue`    | Subreddits the user engages with the most.                       |
| `quote_or_signature_style`| `FieldWithCitations`    | A motto or phrase capturing user’s voice.                        |

---

### Sub-Models Used

#### `FieldWithCitations`

```json
{
  "value": "Value of the attribute",
  "citations": ["https://reddit.com/…"]
}
```

#### `BehaviorAndHabits`

```json
{
  "behavior": "Behaviour category",
  "description": "Description of the behaviour inferred from posts and comments"
}

```

#### `FieldWithListValue`

```json
{
  "value": ["Array of values for this attribute"],
  "citations": ["https://reddit.com/…"]
}
```

#### `Personality`
Includes the following keys inside a nested `value` object:

```json
{
  "key_tones": ["kind", "sarcastic", "analytical"],
  "energy": "Introvert",
  "identity": "Turbulent",
  "mind": "Intuitive",
  "tactics": "Prospecting",
  "nature": "Thinking"
}
```
Also includes a `citations` list.

---

## Disclaimer

- **Do not share or reuse API credentials.** The Reddit and LLM API secrets used in this project are strictly meant for private, time-bound testing only.
- The shared API key used in this project will **automatically expire within 4 days** from submission. External use is prohibited.
- This persona generator is designed to run **entirely on your local machine** without needing any subscriptions or high-end hardware.

### To run the app locally, follow these steps:

```bash
python -m venv venv
venv\Scripts\activate     
pip install -r requirements.txt
python app.py
```





