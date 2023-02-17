# functions for moving joints and servos on the arm to make it move in certain ways
# Those functions are used to pick up the cones/cubes and place them where they need to be

from wpilib import Servo
from rev import CANSparkMax

from utils import math_functions

# maybe we need to use PID in arm control to get accurate positions and hold it there

class Arm:
   def __init__(self, _arm_elevator_motor : CANSparkMax, _arm_base_motor : CANSparkMax, _arm_end_servo_1 : Servo, _arm_end_servo_2 : Servo):
      self.arm_elevator_motor = _arm_elevator_motor
      self.arm_base_motor = _arm_base_motor

      self.arm_end_servo_1 = _arm_end_servo_1
      self.arm_end_servo_2 = _arm_end_servo_2

      self.arm_top_limit_switch = None
      self.arm_bottom_limit_switch = None

      self.HOME = 0
      self.GROUND = 1
      self.CUBE_ONE = 2
      self.CONE_ONE = 3
      self.CUBE_TWO = 4
      self.CONE_TWO = 5
      self.position = self.HOME

   def set_servo_1_angle(self, angle):
      clamped_angle = math_functions.clamp(angle, 0, 360)
      self.arm_end_servo_1.setAngle(clamped_angle)

   def set_servo_2_angle(self, angle):
      clamped_angle = math_functions.clamped(angle, 0, 360)
      self.arm_end_servo_2.setAngle(clamped_angle)

   def set_elevator_speed(self, speed):
      clamped_speed = math_functions.clamp(speed, 1, -1)
      self.arm_elevator_motor.set(clamped_speed)

   def set_base_speed(self, speed):
      clamped_speed = math_functions.clamp(speed, -1, 1)
      self.arm_base_motor.set(clamped_speed)


   def get_elevator_motor_encoder(self):
      return self.arm_elevator_motor.getAbsoluteEncoder()
   

   def get_base_motor_encoder(self):
      return self.arm_base_motor.getAbsoluteEncoder()


   def position_home(self):
      self.set_servo_1_angle(0)
      self.set_servo_2_angle(0)
      # figure out later where the motors need to spin to put the robot back to the "home" position
      self.position = self.HOME

   def position_ground(self):
      self.position = self.GROUND

   def position_cube_one(self):
      self.position = self.CUBE_ONE

   def position_cube_two(self):
      self.position = self.CUBE_TWO

   def position_cone_one(self):
      self.position = self.CONE_ONE

   def position_cone_two(self):
      self.position = self.CONE_TWO
   
   def calibration(self):
      # move motor down until the bottom limit switch is clicked
      # set the ground position to zero
      # move up one revolution at a time until the top limit switch is clicked
      # justify values to get a percent-based system by dividing the total number of revolutions by itself and multiply by 100
      pass