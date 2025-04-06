from text_summarizer.components.data_ingestion import DataIngestion
from text_summarizer.config.configuration import ConfigurationManager
from text_summarizer.loggin import logger

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            
            logger.info("[OK] Config loaded successfully")
            
            data_ingestion = DataIngestion(config=data_ingestion_config)
            logger.info("[OK] DataIngestion class initialized")
            
            data_ingestion.download_file()
            logger.info("[OK] Download complete")
            
            data_ingestion.extract_zip_file()
            logger.info("[OK] Extraction complete")

        except Exception as e:
            raise e
