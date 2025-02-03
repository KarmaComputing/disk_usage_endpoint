# Disk Space API

A simple Flask-based API that reports system disk space usage. The server listens on a configurable port and provides disk usage details in JSON format.

## Features
- Reports total, used, and free disk space.
- Configurable listening port via command-line argument or environment variable `DISK_USAGE_ENDPOINT_PORT` (default 5000).
- Runs as a `systemd` service for automatic startup and management.

### Setup
1. Clone or download the script to your desired directory:
   ```sh
   git clone https://github.com/your-repo/disk-space-api.git
   cd disk-space-api
   ```

## Installation

```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```


## Run
```
python app.py
```

# Systemd unit example
`/etc/systemd/system/disk_usage_endpoint.service`
```
[Unit]
Description=Disk Usage Endpoint
After=network.target

[Service]
User=disk_usage_endpoint_user
Group=disk_usage_endpoint_user
WorkingDirectory=/opt/disk_usage_endpoint
Environment="DISK_USAGE_ENDPOINT_PORT=5005"
ExecStart=/opt/disk_usage_endpoint/venv/bin/python3 /opt/disk_usage_endpoint/app.py
Restart=always

[Install]
WantedBy=multi-user.target
```
