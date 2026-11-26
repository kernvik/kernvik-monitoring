# Первый запуск

На отдельном лабораторном Linux-хосте с Docker Engine и Compose v2 из корня проекта:

```bash
docker --version
docker compose version
docker compose -f deploy/compose.yaml config
docker compose -f deploy/compose.yaml pull
docker compose -f deploy/compose.yaml up -d
docker compose -f deploy/compose.yaml ps
curl -I http://127.0.0.1:3001/
```

`config` проверяет конфигурацию, `pull` загружает фиксированную версию образа, `up -d` запускает контейнер в фоне, `ps` показывает состояние. При необходимости запускайте Docker через `sudo` согласно локальной политике доступа.

Откройте `http://127.0.0.1:3001` на хосте. Для удалённого доступа используйте SSH-туннель с доверенной машины: `ssh -N -L 3001:127.0.0.1:3001 user@server` (подставьте свои значения). Создайте уникальный пароль администратора. Не публикуйте порт 3001 в Интернет.

Журнал: `docker compose -f deploy/compose.yaml logs --tail 50`. Остановка без удаления данных: `docker compose -f deploy/compose.yaml down`. Не используйте `down -v` на рабочей установке: это удаляет том с данными. Храните том на локальной файловой системе с поддержкой POSIX-блокировок.

Источники: [установка Uptime Kuma](https://github.com/louislam/uptime-kuma/wiki/🔧-How-to-Install), [Docker Hub](https://hub.docker.com/r/louislam/uptime-kuma/tags), [релизы](https://github.com/louislam/uptime-kuma/releases).
