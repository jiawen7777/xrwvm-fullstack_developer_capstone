from fastapi import FastAPI, HTTPException
from textblob import TextBlob
from pydantic import BaseModel

app = FastAPI()


@app.get("/analyze/{text}")
async def analyze_sentiment(text):
    if not text:
        raise HTTPException(status_code=400, detail="No text provided for analysis.")

    # Perform sentiment analysis
    analysis = TextBlob(text)
    sentiment = analysis.sentiment

    # Prepare and return the response
    return {
        "text": text,
        "polarity": sentiment.polarity,
        "subjectivity": sentiment.subjectivity,
        "assessment": "positive" if sentiment.polarity > 0 else "negative" if sentiment.polarity < 0 else "neutral"
    }