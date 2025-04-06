import os
from box.exceptions import BoxValueError
from box import ConfigBox
import yaml
from text_summarizer.loggin import logger
from beartype import beartype as ensure_annotations
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a yaml file and returns a ConfigBox object.
    Args:
        path_to_yaml (str): Path like input.
    Raises:
        ValueError: If the yaml file does not exist or is empty.
        e: empty file
    Returns:
        ConfigBox: A ConfigBox type.    
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {yaml_file} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
        create list ai directories
        Args:
            path_to_directories (list): list of path of directories
            ignore_log (bool, optional): ignore if muitiple dirs is to be created. Defaults to False
    """

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")


@ensure_annotations
def get_size(path: Path) -> str:
    """
        get size in KB
        Args:
            path (Path): path of the file
        Returs:
            str: size in KB
    """

    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} Kb"