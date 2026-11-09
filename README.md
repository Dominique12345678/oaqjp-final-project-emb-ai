# Final Project

AI-based Emotion Detection Web Application using Python, Flask and the Watson NLP service endpoint used in the IBM Skills Network course.

## Project structure

- `EmotionDetection/__init__.py`: Python package entry point.
- `EmotionDetection/emotion_detection.py`: Watson NLP integration and output formatting.
- `server.py`: Flask application and blank-input handling.
- `templates/index.html`: Web page.
- `static/mywebscript.js` and `static/style.css`: Frontend behaviour and presentation.
- `test_emotion_detection.py`: Deterministic unit tests for the five emotions, using mocked API responses.
- `requirements.txt`: Runtime and development dependencies.

## Run

```bash
python3 -m pip install -r requirements.txt
python3 server.py
```

Open http://localhost:5000 in the browser. The Watson NLP endpoint must be reachable for live text analysis. If it is not available, the web application displays a service error rather than fabricated results.

## Test and static analysis

```bash
python3 -m unittest -v test_emotion_detection.py
python3 -m pylint server.py EmotionDetection test_emotion_detection.py
```

Unit tests mock HTTP calls to validate the application logic independently of external service availability. **They do not demonstrate live Watson NLP service availability.**

## Submission instructions

The public GitHub repository should be named `oaqjp-final-project-emb-ai` and forked from `ibm-developer-skills-network/oaqjp-final-project-emb-ai` if required by the course.

Screenshots, terminal results, the actual Pylint score, and GitHub publication must be obtained by running the project in the course environment. They are not included as fabricated evidence.
