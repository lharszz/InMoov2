def relax():
  if isNeopixelActivated:
    i01.setNeopixelAnimation("Color Wipe", 0, 0, 20, 1)
    sleep(2)
    i01.setNeopixelAnimation("Ironman", 0, 0, 255, 1)
  i01.startedGesture()
  if (i01.isCameraOn()):
    i01.setHandVelocity("left", 43, 43, 43, 43, 43, 43)
    i01.setHandVelocity("right", 43, 43, 43, 43, 43, 43)
    i01.setArmVelocity("right", 31, 43, 23, 43)
    i01.setArmVelocity("left", 60, 23, 31, 31)
    #i01.setHeadVelocity(43, 43)
    i01.setTorsoVelocity(31, 16, -1)
    #i01.moveHead(79.00,100.00,122.17,64.06,0.00,90.00)
    i01.moveArm("left",5.00,84.00,25.00,12.00)
    i01.moveArm("right",5.00,82.00,25.00,12.00)
    i01.moveHand("left",92.00,33.00,37.00,71.00,66.00,25.00)
    i01.moveHand("right",81.00,66.00,82.00,60.00,23.00,160.00)
    i01.moveTorso(95.00,90.00,90.00)
  else:
    i01.setHandVelocity("left", 43, 43, 43, 43, 43, 43)
    i01.setHandVelocity("right", 43, 43, 43, 43, 43, 43)
    i01.setArmVelocity("right", 31, 43, 23, 43)
    i01.setArmVelocity("left", 60, 23, 31, 31)
    i01.setHeadVelocity(43, 43)
    i01.setTorsoVelocity(31, 16, -1)
    i01.moveHead(79.00,100.00,122.17,64.06,0.00,90.00)
    i01.moveArm("left",5.00,84.00,25.00,12.00)
    i01.moveArm("right",5.00,82.00,25.00,12.00)
    i01.moveHand("left",92.00,33.00,37.00,71.00,66.00,25.00)
    i01.moveHand("right",81.00,66.00,82.00,60.00,23.00,160.00)
    i01.moveTorso(95.00,90.00,90.00)
  i01.finishedGesture()
