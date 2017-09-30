def _test_started(name):
  ret = {
    'name': name,
    'changes': {},
    'result': False,
    'comment': '',
    'pchanges': {},
  }
  ret['result'] = None
  inspect_service = __salt__['docker_service.inspect_service'](name)
  if inspect_service:
    ret['comment'] = 'The service "{0}" will be updated'.format(name)
  else:
    ret['comment'] = 'A new service "{0}" will be created'.format(name)
  return ret

def started(name, **kwargs):
  ret = {
    'name': name,
    'changes': {},
    'result': False,
    'comment': '',
    'pchanges': {},
  }
  if __opts__['test']:
    return _test_started(name)
  ret['result'] = __salt__['docker_service.create_service'](name, **kwargs)
  return ret;