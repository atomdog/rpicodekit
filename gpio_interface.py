#gpio_interface.py
import RPi.GPIO as GPIO

class geep():
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.configured_inputs = []
        self.configured_outputs = []
        self.current_input_readings = []
    def config_outputs(self, pin_list):
        for x in range(0, len(pin_list)):
            GPIO.setup(pin_list[x],GPIO.OUT)
            self.configured_outputs.append(pin_list[x])
    def config_inputs(self, pin_list):
        for x in range(0, len(pin_list)):
            GPIO.setup(pinlist[x],GPIO.IN)
            self.configured_inputs.append(pin_list[x])
    def batch_read_input(self):
        self.current_input_readings = []
        for x in range(0, len(self.configured_inputs)):
            self.current_input_readings.append(GPIO.input(self.config_inputs[x]))
    def highlow_batch_send_output(self, outputlist):
        if(len(outputlist!=len(self.configured_outputs))):
            return(False)
        else:
            for x in range(0, len(outputlist)):
                if(outputlist[x]==1):
                    GPIO.output(self.configured_outputs[x],GPIO.HIGH)
                else:
                    GPIO.output(self.configured_outputs[x],GPIO.LOW)
    def clean(self):
        GPIO.cleanup()
