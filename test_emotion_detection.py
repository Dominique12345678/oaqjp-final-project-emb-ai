"""Unit tests for five emotion categories; network requests are mocked."""

import unittest
from unittest.mock import patch, Mock

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Verify correct formatting and dominant-emotion selection."""

    def _check_emotion(self, winning_emotion):
        scores = {
            "anger": 0.05,
            "disgust": 0.05,
            "fear": 0.05,
            "joy": 0.05,
            "sadness": 0.05,
        }
        scores[winning_emotion] = 0.8
        fake_response = Mock(status_code=200)
        fake_response.json.return_value = {
            "emotionPredictions": [{"emotion": scores}]
        }
        with patch("EmotionDetection.emotion_detection.requests.post", return_value=fake_response):
            outcome = emotion_detector("This is a sample statement")
        self.assertEqual(outcome["dominant_emotion"], winning_emotion)
        for key in scores:
            self.assertEqual(outcome[key], scores[key])

    def test_joy(self):
        self._check_emotion("joy")

    def test_anger(self):
        self._check_emotion("anger")

    def test_disgust(self):
        self._check_emotion("disgust")

    def test_sadness(self):
        self._check_emotion("sadness")

    def test_fear(self):
        self._check_emotion("fear")

    def test_blank_input(self):
        result = emotion_detector("  ")
        self.assertTrue(all(value is None for value in result.values()))

    def test_api_bad_request(self):
        fake_response = Mock(status_code=400)
        with patch("EmotionDetection.emotion_detection.requests.post", return_value=fake_response):
            result = emotion_detector("some text")
        self.assertIsNone(result["dominant_emotion"])


if __name__ == "__main__":
    unittest.main()
