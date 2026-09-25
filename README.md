# Campus Cyber Shield v6 — Investigation Edition

Presentation-ready Streamlit cybersecurity awareness simulator.

## New in v6
- Investigation Mode: inspect Sender, Domain, Link, Urgency, and Message Content before classification.
- Enhanced five-clue final boss.
- Player Profile with codename, XP, Cyber Credits, best streak, achievements, and theme.
- Persistent profile saving to `campus_cyber_shield_saves.json`.
- Cosmetic theme locker with Cyber Credit costs.
- Completion Certificate with score, accuracy, XP, level, streak, and achievements.
- Existing cyber ambience, correct-answer and wrong-answer sounds retained.

## Run
`pip install streamlit`
then
`streamlit run app.py`

Keep the WAV files beside `app.py`.

Saving uses a JSON file beside the app. It persists on a deployment with persistent filesystem storage.
