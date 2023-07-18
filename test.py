from cnnClassifier.pipeline.stage_04_evaluation import EvaluationPipeline
from cnnClassifier.logging import logger


STAGE_NAME = "Evaluation"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_evaluation = EvaluationPipeline()
   model_evaluation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e