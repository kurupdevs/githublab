"""Githublab."""
import os,logging
logging.basicConfig(level=logging.INFO,format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger=logging.getLogger(__name__)
def main():
 logger.info("Starting githublab...")
 token=os.getenv("BOT_TOKEN","")
 if not token:logger.error("BOT_TOKEN not set!");return
 logger.info("Githublab running!")
if __name__=="__main__":main()
