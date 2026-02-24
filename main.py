import asyncio
from playwright_scraper.scraper import main as run_scraper
from ai_processor.processor import generate_digest
from email_sender.sender import send_email

async def main():
    print("Starting daily research automation...")
    
    # 1. Scrape data
    try:
        scraped_data = await run_scraper()
    except Exception as e:
        print(f"Error during scraping: {e}")
        return

    # 2. Process with AI
    try:
        digest = generate_digest(scraped_data)
    except Exception as e:
        print(f"Error during AI processing: {e}")
        return

    # 3. Send email
    try:
        send_email(digest)
    except Exception as e:
        print(f"Error during email delivery: {e}")
        return

    print("Automation completed successfully.")

if __name__ == "__main__":
    asyncio.run(main())
