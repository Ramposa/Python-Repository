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

  def __init__(self):
    self.particles_ = []
    for i in range(self.POOL_SIZE):
      self.particle.append(Particle())

  def create(self,x, y, xVel, yVel, lifetime):
    for particle in self.particles_:    
      if not particle.inUse():
        particle.init(x, y, xVel, yVel, lifetime)

  def animate(self):
    for particle in self.particles_:    
      particle.animate();
