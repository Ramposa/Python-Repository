import random

class Particle:
  def __init__(self):
    self.x_ = 0
    self.y_ = 0
    self.xVel_ = 0
    self.yVel_ = 0
    self.framesLeft_ = 0

  def init(self, x, y, xVel, yVel, lifetime):
    self.x_ = x
    self.y_ = y
    self.xVel_ = xVel
    self.yVel_ = yVel
    self.framesLeft_ = lifetime;

  def animate(self):
    # should never happen now
    if not self.inUse():
      return

    self.framesLeft_ -= 1
    self.x_ += self.xVel_;
    self.y_ += self.yVel_;

  def inUse(self):
    if self.framesLeft_ > 0:
      return True
    else:
      return False

class ParticlePool:
  POOL_SIZE = 100
  _unused = list()
  _used = list()

  def __init__(self):
    pass

  def create(self,x, y, xVel, yVel, lifetime):
    # if we have unused particles use one of them
    if len(self._unused)>0:
      # grab an unused particle and remove it from the unused list
      newParticle = self._unused.pop()
      # set the particles values
      newParticle.init(x, y, xVel, yVel, lifetime)
      # add the particle to the used list
      self._used.append(newParticle)
    elif len(self._used)< self.POOL_SIZE:
      # no available unused particles but pool not full, so add new particle to used 
      newParticle = Particle()
      newParticle.init(x, y, xVel, yVel, lifetime)
      self._used.append(newParticle)
    else:
      # pool full, can't create new
      return None
    

  
  def animate(self):
    for particle in self._used:    
      particle.animate()
      # check if particle is still inUse
      if not particle.inUse():
        # add particle to _unused to be used again
        self._unused.append(particle)
        # remove from used list
        self._used.remove(particle)


def newParticle(aPool):
  x = random.randint(20,25)
  y = 0
  xVel = random.randint(-5,5)
  yVel = random.randint(0,5)
  life = random.randint(15,20)
  aPool.create(x,y,xVel,yVel,life) 

myPool = ParticlePool()
for i in range(50):
  newParticle(myPool)



timer = 100

while timer>0:
  timer -= 1
  myPool.animate()
  poolCount = len(myPool._used)
  if poolCount<20:
    for i in range(50-poolCount):
      newParticle(myPool)
  print("pool count",poolCount)
