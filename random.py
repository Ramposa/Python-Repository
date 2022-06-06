import random
from datetime import datetime
randFloat = random.random()
print (randFloat)

randIntRange = random.randint(5,10)
print(randIntRange)

random.seed(1)
randFloat = random.random()
print (randFloat)

random.seed(1)
randFloat = random.random()
print (randFloat)


random.seed(1)
randFloat = random.random()
print (randFloat)


random.seed(1)
randFloat = random.random()
print (randFloat)

random.seed(datetime.now())
