# Serial Interface Controller
import serial
import time
import logging
from src.config import SERIAL_PORT, BAUD_RATE

logging.basicConfig(level=logging.INFO)

class SerialHardwareController:
    def __init__(self):
        try:
            self.connection = serial.Serial(port=SERIAL_PORT, baudrate=BAUD_RATE, timeout=1)
            time.sleep(2)  # Allow Arduino connection to reset safely
            logging.info(f"Connected to Arduino hardware successfully on {SERIAL_PORT}")
        except Exception as e:
            logging.error(f"Failed to establish connection on serial port {SERIAL_PORT}: {e}")
            self.connection = None

    def dispatch_command(self, action_code: int, parameter: int):
        """Formats and transmits structured control bytes to the Arduino."""
        if not self.connection:
            logging.warning("Command dropped: No hardware device connected.")
            return False
            
        # Structure payload package: [Start Byte, Action, Value, End Byte]
        payload = bytes([0xAA, action_code, parameter, 0xBB])
        try:
            self.connection.write(payload)
            logging.info(f"Command transmitted to microcontroller: {payload.hex().upper()}")
            return True
        except Exception as e:
            logging.error(f"Transmission failure: {e}")
            return False

    def close(self):
        if self.connection:
            self.connection.close()
          
