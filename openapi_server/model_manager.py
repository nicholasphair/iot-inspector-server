from collections import defaultdict

from pathlib import Path


class ModelManager():
    DEFAULT_PATH = Path.home() / 'inspector_model.pt'

    def save_model(self, model):
        with open(self._path, 'wb') as f:
            f.write(model)

    def model_available(self):
        return self._path.exists() and self._path.stat().st_size

    @property
    def path(self):
        return self._path

    def __init__(self, path=DEFAULT_PATH):
        self._path = Path(path).resolve()
