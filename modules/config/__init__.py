
import yaml
from pathlib import Path


def load_config(config_path: Path) -> dict:
    with open(config_path) as cfg:
        return yaml.safe_load(cfg)


params = load_config('config.yml')
