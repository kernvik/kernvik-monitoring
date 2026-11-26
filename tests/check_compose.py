"""Проверка нормализованной конфигурации Compose."""
import json
import subprocess


def main():
    config = json.loads(subprocess.check_output(
        ["docker", "compose", "-f", "deploy/compose.yaml", "config", "--format", "json"],
        text=True,
    ))
    assert set(config["services"]) == {"uptime-kuma"}
    service = config["services"]["uptime-kuma"]
    assert service["image"] == "louislam/uptime-kuma:2.5.12"
    assert service["restart"] == "unless-stopped"
    assert not service.get("privileged", False)
    assert not service.get("network_mode")
    ports = service["ports"]
    assert len(ports) == 1 and ports[0]["host_ip"] == "127.0.0.1"
    assert int(ports[0]["published"]) == int(ports[0]["target"]) == 3001
    volumes = service["volumes"]
    assert len(volumes) == 1 and volumes[0]["type"] == "volume"
    assert volumes[0]["source"] == "kuma-data" and volumes[0]["target"] == "/app/data"
    print("Конфигурация Compose проверена")


if __name__ == "__main__":
    main()
