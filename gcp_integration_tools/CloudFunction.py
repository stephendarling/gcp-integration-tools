import gcp_integration_tools.lib.utilities as utilities 

class Deployment(object):
  def __init__(self, config):
    self.name = config['name']