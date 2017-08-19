def _test_started(name):
  ret = {
    'name': name,
    'changes': {},
    'result': False,
    'comment': '',
    'pchanges': {},
  }
  ret['result'] = None
  ret['comment'] = 'State docker_service.started will be executed with param "{0}"'.format(name)
  return ret
def started(name,
            **kwargs
            ):
  ret = {
    'name':name,
    'changes': {},
    'result': False,
    'comment': '',
    'pchanges': {},
  }
  if __opts__['test']:
    return _test_started(name)
  kwargs['image']= image
  ret_exec= __salt__['docker2.create_service'](**kwargs)
  ret['result'] = ret_exec
  return ret