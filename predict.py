from cog import BasePredictor, Input, Path
from PIL import Image
from rembg import remove
import tempfile


class Predictor(BasePredictor):
    def predict(self, input_image_path: Path = Input(description="Input file", default=None)) -> Path:

        if not input_image_path:
            raise ValueError("No input image selected")

        print("Input image path:", input_image_path)

        input_image = Image.open(input_image_path)

        print("Processing input image...")

        output_image = remove(input_image)

        print("Image processing complete.")

        output_path = Path(tempfile.mkdtemp()) / "output.png"
        output_image.save(output_path)

        print("Output image saved at:", output_path)

        return Path(output_path)
