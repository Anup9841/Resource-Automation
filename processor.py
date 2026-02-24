import os
from openai import OpenAI
from config import OPENAI_API_KEY, SEARCH_TOPIC

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_digest(scraped_data):
    """Synthesizes scraped data into a structured digest using AI."""
    
    # Format the scraped data for the prompt
    content = ""
    for source, reports in scraped_data.items():
        content += f"\nSource: {source.upper()}\n"
        for report in reports:
            content += f"- Title: {report['title']}\n  Summary: {report['summary']}\n"

    prompt = f"""
    You are a professional market research analyst. Based on the following raw data gathered from Mintel, WARC, and FIMA regarding the topic '{SEARCH_TOPIC}', write a comprehensive daily digest.
    
    Raw Data:
    {content}
    
    The digest must include:
    1. 5 key industry trends
    2. Market insights
    3. Consumer behavior highlights
    4. "Big Theme of the Week"
    
    Format the output in clean Markdown.
    """

    response = client.chat.completions.create(
        model="gpt-4o",  # Or another preferred model
        messages=[
            {"role": "system", "content": "You are a professional market analyst."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    # Example usage with mock data
    mock_data = {
        "mintel": [{"title": "Future of Retail", "summary": "Growth in AR/VR shopping."}],
        "warc": [{"title": "Ad Spend Trends", "summary": "Digital ad spend is rising."}],
        "fima": [{"title": "Banking Tech", "summary": "AI in fraud detection."}]
    }
    print(generate_digest(mock_data))
