import os,logging
logging.basicConfig(level=logging.INFO)
logger=logging.getLogger(__name__)
def main():
 logger.info("githublab start")
 t=os.getenv("BOT_TOKEN","")
 if not t:logger.error("No token");return
 logger.info("Running!")
if __name__=="__main__":main()
