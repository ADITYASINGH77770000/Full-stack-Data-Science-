import numpy as np
import logging

## logging setting 
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',

)

logger=logging.getLogger("AnomalyDetection")

def load_data():
    logger.info("Loading data")
    data=np.array([10, 12, 11, 13, 100])
    return data

def detect_anomalies(data):
    logger.info("start anomaly detection")
    
    if len(data) == 0:
        logger.error("Dataset is empty")
        return []
    
    mean=np.mean(data)
    std=np.std(data)
    
    logger.info(f"Mean={mean}, Std={std}")
    
    anomalies=[]
    
    for value in data:
        if abs(value-mean)>2*std:
            logger.warning(f"Anomaly Detected:{value}")
            anomalies.append(value)
    return anomalies

data = load_data()
anomalies = detect_anomalies(data)

logger.info(f"Final anomalies: {anomalies}")
