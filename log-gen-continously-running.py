import logging
import random
import time

# Configure logging
logging.basicConfig(
    filename='d:/minikube_apps/Grafana_Prometheus_Loki_Opentelemetry_Alloy_Tempo_Course/grafana-udemy-main/docker/shared/logs/kubernetes_pod_logs.log',
    level=logging.DEBUG,
    format='%(asctime)s.%(msecs)03d level=%(levelname)s app=myapp component=%(component)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Define log levels and components
log_levels = ['INFO', 'WARNING', 'ERROR']
components = ['database', 'backend']

# Define log messages
log_messages = {
    'INFO': 'Information: Application running normally',
    'WARNING': 'Warning: Resource usage high',
    'ERROR': 'Critical error: Database connection lost'
}

# Generate logs continuously
try:
    while True:
        level = random.choice(log_levels)
        component = random.choice(components)
        message = log_messages[level]
        logging.log(getattr(logging, level), message, extra={'component': component})
        time.sleep(0.1)  # Sleep for a short time to simulate real-time logging
except KeyboardInterrupt:
    print("Log generation stopped. Logs written to 'kubernetes_pod_logs.log'.")