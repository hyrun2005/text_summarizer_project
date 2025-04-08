from text_summarizer.components.model_evaluation import ModelEvaluation
from text_summarizer.config.configuration import ConfigurationManager
from text_summarizer.loggin import logger

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_evaluation_conf = config.get_model_evaluation_config()
        model_evaluation_conf = ModelEvaluation(config=model_evaluation_conf)
        model_evaluation_conf.evaluate()
