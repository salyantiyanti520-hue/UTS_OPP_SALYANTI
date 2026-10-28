import json

# DATA SOURCE FROM EXAM SHEET
sensor_data = """{
  "readings": [
    {"sensor_id": "SNS-A01", "location": "Boiler Room", "temperature": 88.5, "status": "DANGER", "operator_id": 101},
    {"sensor_id": "SNS-A02", "location": "Assembly Line", "temperature": 42.0, "status": "NORMAL", "operator_id": 102},
    {"sensor_id": "SNS-A03", "location": "Server Room", "temperature": 95.2, "status": "DANGER", "operator_id": 102},
    {"sensor_id": "SNS-A04", "location": "Chemical Lab", "temperature": 73.1, "status": "WARNING", "operator_id": 104},
    {"sensor_id": "SNS-A05", "location": "Turbine House", "temperature": 91.0, "status": "DANGER", "operator_id": 107},
    {"sensor_id": "SNS-A06", "location": "Warehouse", "temperature": 31.5, "status": "NORMAL", "operator_id": null},
    {"sensor_id": "SNS-A07", "location": "Turbine House", "temperature": 87.3, "status": "DANGER", "operator_id": 107},
    {"sensor_id": "SNS-A08", "location": "Assembly Line", "temperature": 45.8, "status": "NORMAL", "operator_id": 102},
    {"sensor_id": "SNS-A09", "location": "Server Room", "temperature": 89.9, "status": "DANGER", "operator_id": 109},
    {"sensor_id": "SNS-A10", "location": "Data Center", "temperature": 24.0, "status": "NORMAL", "operator_id": null},
    {"sensor_id": "SNS-A11", "location": "Boiler Room", "temperature": 96.4, "status": "DANGER", "operator_id": 101},
    {"sensor_id": "SNS-A12", "location": "Chemical Lab", "temperature": 68.0, "status": "WARNING", "operator_id": 104},
    {"sensor_id": "SNS-A13", "location": "Turbine House", "temperature": 92.1, "status": "DANGER", "operator_id": 107},
    {"sensor_id": "SNS-A14", "location": "Warehouse", "temperature": 29.8, "status": "NORMAL", "operator_id": 154},
    {"sensor_id": "SNS-A15", "location": "Server Room", "temperature": 86.0, "status": "DANGER", "operator_id": 109},
    {"sensor_id": "SNS-A16", "location": "Assembly Line", "temperature": 41.2, "status": "NORMAL", "operator_id": 102},
    {"sensor_id": "SNS-A17", "location": "Boiler Room", "temperature": 99.5, "status": "DANGER", "operator_id": 101},
    {"sensor_id": "SNS-A18", "location": "Data Center", "temperature": 22.5, "status": "NORMAL", "operator_id": null},
    {"sensor_id": "SNS-A19", "location": "Turbine House", "temperature": 88.0, "status": "DANGER", "operator_id": 107},
    {"sensor_id": "SNS-A20", "location": "Chemical Lab", "temperature": 75.4, "status": "WARNING", "operator_id": 104},
    {"sensor_id": "SNS-A21", "location": "Server Room", "temperature": 90.2, "status": "DANGER", "operator_id": 109},
    {"sensor_id": "SNS-A22", "location": "Assembly Line", "temperature": 39.9, "status": "NORMAL", "operator_id": 122},
    {"sensor_id": "SNS-A23", "location": "Boiler Room", "temperature": 93.7, "status": "DANGER", "operator_id": 101},
    {"sensor_id": "SNS-A24", "location": "Warehouse", "temperature": 30.0, "status": "NORMAL", "operator_id": null},
    {"sensor_id": "SNS-A25", "location": "Turbine House", "temperature": 87.8, "status": "DANGER", "operator_id": 107},
    {"sensor_id": "SNS-A26", "location": "Data Center", "temperature": 25.1, "status": "NORMAL", "operator_id": 126},
    {"sensor_id": "SNS-A27", "location": "Boiler Room", "temperature": 97.0, "status": "DANGER", "operator_id": 101},
    {"sensor_id": "SNS-A28", "location": "Chemical Lab", "temperature": 71.3, "status": "WARNING", "operator_id": 104},
    {"sensor_id": "SNS-A29", "location": "Server Room", "temperature": 85.5, "status": "DANGER", "operator_id": 109},
    {"sensor_id": "SNS-A30", "location": "Assembly Line", "temperature": 43.5, "status": "NORMAL", "operator_id": 102}
  ]
}"""

class SensorLog:
    def __init__(self, sensor_id, location, temperature, status, operator_id):
        self.sensor_id = sensor_id
        self.location = location
        self.temperature = temperature
        self.status = status
        self.operator_id = operator_id

    def is_critical(self):
        return False

    def get_log_details(self):
        op = self.operator_id if self.operator_id else "N/A"
        return f"[{self.sensor_id}] Lokasi: {self.location:<15} | Temp: {self.temperature}°C | Status: {self.status:<7} | Operator: {op}"

class DangerSensorLog(SensorLog):
    def is_critical(self):
        return self.status == "DANGER"

sensor_logs = json.loads(sensor_data)
critical_alerts = []

for log in sensor_logs["readings"]:
    if log["status"] == "DANGER":
        sensor_obj = DangerSensorLog(log["sensor_id"], log["location"], log["temperature"], log["status"], log["operator_id"])
        if sensor_obj.is_critical():
            critical_alerts.append(sensor_obj)

print("="*80)
print(f"{'PERINGATAN SENSOR KRITIKAL (STATUS: DANGER)':^80}")
print("="*80)
for alert in critical_alerts:
    print(alert.get_log_details())
print("="*80)
