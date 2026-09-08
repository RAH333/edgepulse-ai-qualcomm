# Configuration
import os

# Hardware & Interface Settings
SERIAL_PORT = os.getenv("EDGEPULSE_SERIAL_PORT", "COM3")  # '/dev/ttyACM0' on Unix/Linux
BAUD_RATE = 115200

# Qualcomm Optimization Runtime Settings
MODEL_PATH = "models/edgepulse_vision_quantized.onnx"
CONFIDENCE_THRESHOLD = 0.65
ACCELERATOR_BACKEND = "NPU"  # Leveraging Snapdragon X Elite Hexagon NPU
