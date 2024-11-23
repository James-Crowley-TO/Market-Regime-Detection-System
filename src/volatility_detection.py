import yaml
import os

# Load thresholds from the YAML file
def load_thresholds(config_file='../configs/volatility_config.yaml'):
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    return config['volatility_thresholds']

# Regime determination function
def get_regime(vxn_value, config_file='../configs/volatility_config.yaml'):
    thresholds = load_thresholds(config_file)
    if vxn_value <= thresholds['low']:
        return 'Low Volatility'
    elif vxn_value <= thresholds['normal']:
        return 'Normal Volatility'
    elif vxn_value <= thresholds['high']:
        return 'High Volatility'
    else:
        return 'Extreme Volatility'