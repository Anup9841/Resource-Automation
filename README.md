# Daily Research Digest Automation

This project automates the process of gathering market research from university resources (Mintel, WARC, FIMA), synthesizing key insights using an AI layer, and delivering a daily digest via email.

## Project Structure

- `playwright_scraper/`: Contains the Playwright script for web scraping.
- `ai_processor/`: Contains the AI layer for synthesizing research findings.
- `email_sender/`: Contains the script for sending the daily digest via email.
- `scheduler/`: Contains the GitHub Actions workflow for daily scheduling.
- `config.py`: Configuration file for sensitive information and settings.
- `main.py`: Orchestrates the scraping, AI processing, and email sending.
- `README.md`: Project overview and setup instructions.

## Setup and Configuration

To get this automation running, you'll need to configure your environment variables and set up the GitHub Actions workflow.

### 1. Environment Variables (config.py)

The `config.py` file uses environment variables to store sensitive information and configuration settings. You will need to set these either directly in your environment if running locally, or as GitHub Secrets if using GitHub Actions.

Here's a breakdown of the variables:

| Variable Name       | Description                                                                 | Example Value                                  |
| :------------------ | :-------------------------------------------------------------------------- | :--------------------------------------------- |
| `SSO_URL`           | Your university's Single Sign-On (SSO) login page URL.                      | `https://sso.university.edu/login`             |
| `USERNAME`          | Your university login username.                                             | `your_student_id`                              |
| `PASSWORD`          | Your university login password.                                             | `your_secure_password`                         |
| `SEARCH_TOPIC`      | The research topic you want to search for on Mintel, WARC, and FIMA.        | `"Sustainable Packaging Trends"`             |
| `OPENAI_API_KEY`    | Your OpenAI API key for the AI synthesis layer.                             | `sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`         |
| `SMTP_SERVER`       | The SMTP server address for sending emails (e.g., Gmail, Outlook).          | `smtp.gmail.com`                               |
| `SMTP_PORT`         | The SMTP server port (e.g., 587 for TLS, 465 for SSL).                      | `587`                                          |
| `SENDER_EMAIL`      | The email address from which the digest will be sent.                       | `your_email@example.com`                       |
| `SENDER_PASSWORD`   | The password or app-specific password for the sender email account.         | `your_email_app_password`                      |
| `RECIPIENT_EMAIL`   | The email address where the daily digest will be delivered.                 | `your_recipient_email@example.com`             |

**Important:** For `SENDER_PASSWORD` with Gmail, you will likely need to generate an [App Password](https://support.google.com/accounts/answer/185833?hl=en) rather than using your main account password, especially if you have 2-Factor Authentication enabled.

### 2. GitHub Actions Deployment

1.  **Create a new GitHub Repository:** Initialize a new private repository on GitHub.
2.  **Upload Project Files:** Upload all the files and folders from this project (`daily_research_digest/`) to the root of your new GitHub repository.
3.  **Configure GitHub Secrets:**
    *   In your GitHub repository, go to `Settings` > `Secrets and variables` > `Actions`.
    *   Click on `New repository secret` and add each of the environment variables listed in the table above (`SSO_URL`, `USERNAME`, `PASSWORD`, `SEARCH_TOPIC`, `OPENAI_API_KEY`, `SMTP_SERVER`, `SMTP_PORT`, `SENDER_EMAIL`, `SENDER_PASSWORD`, `RECIPIENT_EMAIL`) as individual secrets. Ensure the names match exactly.
4.  **Enable Workflow:** The `daily_workflow.yml` file in the `scheduler/` directory is configured to run daily at 8 AM UTC. You can also manually trigger it from the `Actions` tab in your GitHub repository.

### 3. Local Execution (Optional)

If you wish to run this automation locally for testing or development, follow these steps:

1.  **Clone the Repository:**
    ```bash
    git clone <your-repository-url>
    cd daily_research_digest
    ```
2.  **Install Dependencies:**
    ```bash
    pip install playwright openai
    playwright install --with-deps chromium
    ```
3.  **Set Environment Variables:** Before running, set the environment variables mentioned in `config.py` in your local terminal session. For example:
    ```bash
    export SSO_URL="https://sso.university.edu/login"
    export USERNAME="your_student_id"
    # ... and so on for all variables
    ```
4.  **Run the Script:**
    ```bash
    python main.py
    ```

## Customization

-   **Scraping Logic:** The scraping functions (`scrape_mintel`, `scrape_warc`, `scrape_fima`) in `playwright_scraper/scraper.py` contain placeholder selectors. You will need to inspect the actual HTML structure of your university's SSO page and the target research platforms to identify the correct CSS selectors for login fields, search bars, and report data. This is crucial for the scraper to work correctly.
-   **AI Prompt:** The prompt in `ai_processor/processor.py` can be adjusted to refine the AI's output format and content.
-   **Email Content:** The `email_sender/sender.py` can be modified to change the email's subject, body, or to include HTML formatting.
-   **Scheduling:** The `cron` schedule in `scheduler/daily_workflow.yml` can be adjusted to run at a different time or frequency.

---

**Author:** Manus AI
**Date:** February 24, 2026
