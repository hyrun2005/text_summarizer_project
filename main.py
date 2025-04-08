import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_dir, "src")
if src_path not in sys.path:
    sys.path.append(src_path)

from text_summarizer.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from text_summarizer.pipeline.stage02_data_validation import DataValidationPipeline
from text_summarizer.pipeline.stage03_data_transforamtion import DataTransformationPipeline
from text_summarizer.pipeline.stage04_model_training import ModelTrainingPipeline
from text_summarizer.pipeline.stage05_model_evaluation import ModelEvaluationPipeline
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


STAGE_NAME = 'Data Transformation stage'

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
    data_validation = DataTransformationPipeline()
    data_validation.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} <<<<<<<<<\n\nx=========")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'Model Training Stage'

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
    data_validation = ModelTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} <<<<<<<<<\n\nx=========")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Model Evaluation Stage'

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
    data_validation = ModelEvaluationPipeline()
    data_validation.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} <<<<<<<<<\n\nx=========")
except Exception as e:
    logger.exception(e)
    raise e