# ##############################################################################
#            *** MRL SERVICE - NEOPIXEL  ***
# ##############################################################################

  #TODO ADD PIXEL MATRIX
  
  #Animations;
  #"Color Wipe"
  #"Larson Scanner"
  #"Theater Chase"
  #"Theater Chase Rainbow"
  #"Rainbow"
  #"Rainbow Cycle"
  #"Flash Random"
  #"Ironman" > bug ?

  #speed: 1-65535   1=full speed, 2=2x slower than 1, 10=10x slower than 1
  #starting a animation :
##  neopixel.setAnimation("Animation Name", red, green, blue, speed)
##  optional : i01.setNeopixelAnimation("Animation Name", red, green, blue, speed, duration) > animation timeout, if neopixel exist

# ##############################################################################
#               PERSONNAL PARAMETERS
# ##############################################################################  
  
#read current service part config based on file name
ThisServicePart=RuningFolder+'config/service_'+os.path.basename(inspect.stack()[0][1]).replace('.py','')

CheckFileExist(ThisServicePart)
ThisServicePartConfig = ConfigParser.ConfigParser()
ThisServicePartConfig.read(ThisServicePart+'.config')
i01.isNeopixelActivated()=0



try:
    flash_when_speak = ThisServicePartConfig.getboolean('BASIC_REACTIONS', 'flash_when_speak')
except:
  flash_when_speak=0
  ThisServicePartConfig.set('BASIC_REACTIONS', 'flash_when_speak', 0)
  with open(ThisServicePart+'.config', 'wb') as f:
    ThisServicePartConfig.write(f)
  pass


try:
  i01.isNeopixelActivated()=ThisServicePartConfig.getboolean('MAIN', 'i01.isNeopixelActivated()') 
  masterArduinoPort=ThisServicePartConfig.get('MAIN', 'NeopixelMasterPort')
  pin=ThisServicePartConfig.getint('NEOPIXEL', 'pin') 
  numberOfPixel=ThisServicePartConfig.getint('NEOPIXEL', 'numberOfPixel')

  #neopixel can have basic pre programmed reactions:
  #TODO choose witch animation

  #light green while robot booting
  boot_green=ThisServicePartConfig.getboolean('BASIC_REACTIONS', 'boot_green')
  #blue while download something
  downloadSomething_blue=ThisServicePartConfig.getboolean('BASIC_REACTIONS', 'downloadSomething_blue')

  error_red=ThisServicePartConfig.getboolean('BASIC_REACTIONS', 'error_red')
except:
  errorSpokenFunc('ConfigParserProblem','Neopixel.config')
  pass
  
#for noworky
log.info("NEOPIXEL.config")
log.info("NeopixelMaster : "+str(ThisServicePartConfig.get('MAIN', 'NeopixelMaster')))
log.info("masterArduinoPort : "+str(masterArduinoPort))
log.info("i01.isNeopixelActivated() : "+str(i01.isNeopixelActivated()))
log.info("pin : "+str(pin))
log.info("numberOfPixel : "+str(numberOfPixel))
  
# ##############################################################################
#                 SERVICE START
# ##############################################################################

if i01.isNeopixelActivated()==1:
  neopixelArduino = Runtime.createAndStart("neopixelArduino","Arduino")
  
  #check if connection is serial or usb
  if masterArduinoPort[:3].lower()=="com" or masterArduinoPort[:4].lower()=="/dev":
    neopixelArduinoIsConnected=CheckArduinos(neopixelArduino,masterArduinoPort)
  else:
    try:
      masterArduino=eval(ThisServicePartConfig.get('MAIN', 'NeopixelMaster'))
      neopixelArduinoIsConnected=CheckArduinos(neopixelArduino,masterArduinoPort,masterArduino)
    except:
      errorSpokenFunc('BAdrduinoChoosen','Neo pixel')
      i01.isNeopixelActivated()=0
      neopixelArduinoIsConnected=0
      pass  
  
  
  sleep(0.1)

  neopixel = Runtime.createAndStart("neopixel","NeoPixel")
  if neopixelArduinoIsConnected==True:
    #Starting NeoPixel Service
    neopixel.attach(neopixelArduino, pin, numberOfPixel)
    i01.neopixel=neopixel
    i01.neopixelArduino=neopixelArduino
    i01.speakBlocking(i01.languagePack.get("startingNeoPixel"))
  else:
    i01.isNeopixelActivated()=0
    
if boot_green and i01.isNeopixelActivated():    
  i01.setNeopixelAnimation("Theater Chase", 0, 255, 50, 1)