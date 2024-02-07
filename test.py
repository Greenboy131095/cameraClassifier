import pytest
from model import Model
from camera import Camera
from app import App
import numpy as np
# Test Model class

 # Assuming the model predicts binary classes
# def test_model_predict():
#     model = Model()
#     frame = (True, np.zeros((565, 10, 3), dtype=np.uint8))  # Mock frame as a numpy array representing an image
#     prediction = model.predict(frame)
#     assert prediction in [0, 1]  # Assuming the model predicts binary classes
# Test Camera class
def test_camera_init():
    camera = Camera()
    assert camera.width > 0
    assert camera.height > 0

# Test App class
def test_app_init():
    app = App()
    assert app.window is not None
    assert app.window_title == "Camera Classifier"
    assert app.counters == [1, 1]
    assert app.auto_predict == False

# You can write more tests for other methods in the App class as needed

if __name__ == "__main__":
    pytest.main(['-v'])