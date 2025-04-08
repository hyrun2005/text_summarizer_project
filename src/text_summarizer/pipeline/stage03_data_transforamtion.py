from text_summarizer.components.data_transformation import DataTransformation
from text_summarizer.config.configuration import ConfigurationManager
from text_summarizer.loggin import logger

class DataTransformationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()
