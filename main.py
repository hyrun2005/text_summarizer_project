from text_summarizer.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from text_summarizer.pipeline.stage02_data_validation import DataValidationPipeline
from text_summarizer.loggin import logger

STAGE_NAME = 'Data Ingestion stage'

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} <<<<<<<<<\n\nx=========")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Data Validation stage'

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
    data_validation = DataValidationPipeline()
    data_validation.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} <<<<<<<<<\n\nx=========")
except Exception as e:
    logger.exception(e)
    raise e