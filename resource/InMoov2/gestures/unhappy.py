def unhappy():
  if isNeopixelActivated:
    i01.setNeopixelAnimation("Color Wipe", 20, 0, 0, 1)
    sleep(2)
  i01.startedGesture()
  i01.setHandVelocity("left", -1, -1, -1, -1, -1, -1)
  i01.setHandVelocity("right", -1, -1, -1, -1, -1, -1)
  i01.setArmVelocity("left", -1.0, -1.0, -1.0, -1.0)
  i01.setArmVelocity("right", -1.0, -1.0, -1.0, -1.0)
  i01.setHeadVelocity(-1, -1)
  i01.setTorsoVelocity(-1, -1, -1)
  i01.moveHead(85,40)
  i01.moveArm("left",79,42,23,41)
  i01.moveArm("right",71,40,14,39)
  i01.moveHand("left",180,180,180,180,180,47)
  i01.moveHand("right",99,130,152,154,145,180)
  i01.moveTorso(90,90,90)
  i01.finishedGesture()

