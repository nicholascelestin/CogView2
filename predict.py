import os, time
from cog import BasePredictor, Path, Input, File
import uuid
import typing

class Predictor(BasePredictor):
    model_name = ""

    def setup(self):
        """Load the model into memory to make running multiple predictions efficient"""
        print(os.popen("nvidia-smi").read())

        print(f'Setup complete')

    def predict(self,
                prompt: str = Input(description="Image prompt"),
                batch_size: int = Input(description="Number of images to generate", default=1, ge=1,le=20),
                model_size: str = Input(description="Size of the model", default="MINI", choices=["MINI"])
                ) -> typing.List[Path]:
        print(os.popen("nvidia-smi").read())
        # model inference
        for i in range(batch_size):
            print(f'saving image {i}')
        print(f'took {time.time() - start_time}')
        return all_images