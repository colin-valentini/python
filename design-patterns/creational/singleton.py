class Singleton:
  __instance = None

  def __init__(self):
    if Singleton.__instance is None:
      Singleton.__instance = self
    else:
      raise Exception('Singleton is already instantiated. Use get_instance instead')
  
  @staticmethod
  def get_instance():
    if Singleton.__instance is None:
      Singleton()
    return Singleton.__instance

# Verify the singleton identity is constant across multiple invocations of get_instance
ids = [id(Singleton.get_instance()) for _ in range(10)]
assert len(set(ids)) == 1