from controller import Robot
robot = Robot()

timeStep = int(robot.getBasicTimeStep())

MaxSpeed = 5.0
distanceSensorCalibrationConstant = 360

leftMotor = robot.getMotor('left wheel motor')
rightMotor = robot.getMotor('right wheel motor')
ps0 = robot.getDistanceSensor('ps0')
ps1 = robot.getDistanceSensor('ps1')
ps6 = robot.getDistanceSensor('ps6')
ps7 = robot.getDistanceSensor('ps7')

ps0.enable(timeStep)
ps1.enable(timeStep)
ps6.enable(timeStep)
ps7.enable(timeStep)
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))
initialVelocity = 0.7 * MaxSpeed
leftMotor.setVelocity(initialVelocity)
rightMotor.setVelocity(initialVelocity)

while robot.step(timeStep) != -1:
    m= ps0.getValue()
    left_obstacle = m > 85 or m > 85 
    right_obstacle = m > 85 or m > 85 
    if (left_obstacle):
        leftMotor.setVelocity(initialVelocity-(0.4*initialVelocity))
        rightMotor.setVelocity(initialVelocity+(0.4*initialVelocity))
    elif (right_obstacle):
        leftMotor.setVelocity(initialVelocity+(0.4*initialVelocity))
        rightMotor.setVelocity(initialVelocity-(0.4*initialVelocity))
