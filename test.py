from gcp_integration_tools import CloudFunction as cf

cf = cf.Deployment({
  'name': 'first-deployment'
})
print(cf.name)