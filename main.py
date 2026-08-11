"""Main entry point for githublab."""
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def main():
    """Start the application."""
    logger.info("Starting githublab...")
    token = os.getenv("BOT_TOKEN", "")
    if not token:
        logger.error("BOT_TOKEN not set!")
        return
    logger.info("githublab is running!")
    logger.info(f"Environment configured successfully")


if __name__ == "__main__":
    main()