my_wp_service_started:
  docker_service.started:
    - name: sickrage
    - task_template:
        container_spec:
          image: sickrage/sickrage
          env:
            TEST=true
          mounts:
            - /etc/localtime:/etc/localtime:ro
            - /config:/plex/_config
            - /downloads:/plex/dl-sickrage
            - /tv:/plex/sickrage
        placement:
          - 'engine.labels.plex_storage: true'
    - endpoint_spec:
      ports:
        8081: 8081
