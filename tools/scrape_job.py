import requests
from bs4 import BeautifulSoup


def scrape_job_url(url: str) -> dict:
    if not url:
        return {
            "success": False,
            "text": "",
            "error": "No URL provided.",
        }

    try:
        response = requests.get(
            url,
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=15,
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "html.parser",
        )

        for tag in soup(
            ["script", "style", "nav", "footer", "header"]
        ):
            tag.decompose()

        text = soup.get_text(separator="\n")

        lines = [
            line.strip()
            for line in text.splitlines()
            if line.strip()
        ]

        cleaned_text = "\n".join(lines)

        if len(cleaned_text) < 500:
            return {
                "success": False,
                "text": "",
                "error": "Not enough job text was found.",
            }

        return {
            "success": True,
            "text": cleaned_text[:12000],
            "error": "",
        }

    except Exception as error:
        return {
            "success": False,
            "text": "",
            "error": str(error),
        }