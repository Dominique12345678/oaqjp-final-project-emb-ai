"use strict";

async function RunSentimentAnalysis() {
  const input = document.getElementById("textToAnalyze").value;
  const target = document.getElementById("result");
  const section = document.getElementById("resultSection");
  section.hidden = false;
  target.textContent = "Analyzing...";
  try {
    const response = await fetch("/emotionDetector?textToAnalyze=" + encodeURIComponent(input));
    target.textContent = await response.text();
  } catch (_) {
    target.textContent = "Unable to connect. Please try again.";
  }
}

document.getElementById("analyze").addEventListener("click", RunSentimentAnalysis);
