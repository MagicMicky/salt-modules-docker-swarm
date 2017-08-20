sickrage_service_started:
  docker_service.started:
    - name: sickrage
    - task_template:
        container_spec:
          image: linuxserver/sickrage
          env:
            TZ: Europe/Paris
            PUID: 65534
            PGID: 65534
          mounts:
            - /mnt/plex/_config/sickrage:/config
            - /mnt/plex/dl-sickrage:/downloads
            - /mnt/plex/sickrage:/tv
        placement:
          constraints:
            - 'engine.labels.plex_storage==true'
    - endpoint_spec:
        ports:
          8081: 8081