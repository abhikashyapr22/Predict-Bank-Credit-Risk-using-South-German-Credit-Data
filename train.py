
from src.pipeline.training_pipeline import start_training_pipeline


file_path="/config/workspace/SouthGermanCreditRisk.csv"
print(__name__)
if __name__=="__main__":
    try:
        start_training_pipeline()
    except Exception as e:
        raise SGCException