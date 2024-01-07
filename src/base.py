from abc import ABC, abstractmethod
from typing import Optional, Dict, List, Any
import json

class VisualizerBase(ABC):
    def __init__(self, dataset_path:str) -> None:
        super().__init__()
        self.dataset_path = dataset_path
        self.cameras:Optional[Dict[str, Any]] = self.load_cameras()

    def load_cameras(self)->List[Dict[str,Any]]:
        """load dataset from self.dataset_path"""
        with open(self.dataset_path, 'r', encoding='utf-8') as f:
            cam_data = json.load(f)
        return cam_data['frames']
    
    @abstractmethod
    def visualize(self):
        """visualize data"""