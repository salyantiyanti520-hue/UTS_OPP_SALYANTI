import json

# DATA SOURCE FROM EXAM SHEET
employee_data = """{
  "employees": [
    {"emp_id": "EMP-001", "name": "Budi Pratama", "base_salary": 8500000.0, "is_permanent": true, "bonus_code": "PERF2026"},
    {"emp_id": "EMP-002", "name": "Siti Rahma", "base_salary": 6000000.0, "is_permanent": false, "bonus_code": null},
    {"emp_id": "EMP-003", "name": "Andi Wijaya", "base_salary": 12500000.0, "is_permanent": true, "bonus_code": null},
    {"emp_id": "EMP-004", "name": "Dewi Lestari", "base_salary": 7200000.0, "is_permanent": true, "bonus_code": "PERF2026"},
    {"emp_id": "EMP-005", "name": "Eko Prasetyo", "base_salary": 5500000.0, "is_permanent": false, "bonus_code": null},
    {"emp_id": "EMP-006", "name": "Fajar Nugroho", "base_salary": 9800000.0, "is_permanent": true, "bonus_code": "SENIOR10"},
    {"emp_id": "EMP-007", "name": "Gita Gutawa", "base_salary": 6800000.0, "is_permanent": false, "bonus_code": null},
    {"emp_id": "EMP-008", "name": "Hendra Kurniawan", "base_salary": 11000000.0, "is_permanent": true, "bonus_code": "PERF2026"},
    {"emp_id": "EMP-009", "name": "Indah Permata", "base_salary": 8000000.0, "is_permanent": true, "bonus_code": null},
    {"emp_id": "EMP-010", "name": "Joko Widodo", "base_salary": 5000000.0, "is_permanent": false, "bonus_code": null},
    {"emp_id": "EMP-011", "name": "Kiki Amalia", "base_salary": 7700000.0, "is_permanent": true, "bonus_code": "PERF2026"},
    {"emp_id": "EMP-012", "name": "Lukman Hakim", "base_salary": 13500000.0, "is_permanent": true, "bonus_code": "LEAD2026"},
    {"emp_id": "EMP-013", "name": "Maya Putri", "base_salary": 6200000.0, "is_permanent": false, "bonus_code": null},
    {"emp_id": "EMP-014", "name": "Nurdin Hasan", "base_salary": 8900000.0, "is_permanent": true, "bonus_code": null},
    {"emp_id": "EMP-015", "name": "Oki Setiana", "base_salary": 9500000.0, "is_permanent": true, "bonus_code": "PERF2026"},
    {"emp_id": "EMP-016", "name": "Panji Petualang", "base_salary": 5800000.0, "is_permanent": false, "bonus_code": null},
    {"emp_id": "EMP-017", "name": "Qory Sandioriva", "base_salary": 10500000.0, "is_permanent": true, "bonus_code": "SENIOR10"},
    {"emp_id": "EMP-018", "name": "Rian D'Masiv", "base_salary": 7000000.0, "is_permanent": true, "bonus_code": null},
    {"emp_id": "EMP-019", "name": "Rika Kohi", "base_salary": 14000000.0, "is_permanent": true, "bonus_code": "LEAD2026"},
    {"emp_id": "EMP-020", "name": "Tora Sudiro", "base_salary": 6400000.0, "is_permanent": false, "bonus_code": null},
    {"emp_id": "EMP-021", "name": "Uus Kartajaya", "base_salary": 8300000.0, "is_permanent": true, "bonus_code": "PERF2026"},
    {"emp_id": "EMP-022", "name": "Vina Panduwinata", "base_salary": 9100000.0, "is_permanent": true, "bonus_code": null},
    {"emp_id": "EMP-023", "name": "Wendra Pratama", "base_salary": 5300000.0, "is_permanent": false, "bonus_code": null},
    {"emp_id": "EMP-024", "name": "Xavier Marks", "base_salary": 11800000.0, "is_permanent": true, "bonus_code": "SENIOR10"},
    {"emp_id": "EMP-025", "name": "Yuni Shara", "base_salary": 7600000.0, "is_permanent": true, "bonus_code": null},
    {"emp_id": "EMP-026", "name": "Zainal Abidin", "base_salary": 8500000.0, "is_permanent": false, "bonus_code": null},
    {"emp_id": "EMP-027", "name": "Ahmad Dhani", "base_salary": 15000000.0, "is_permanent": true, "bonus_code": "LEAD2026"},
    {"emp_id": "EMP-028", "name": "Bella Saphira", "base_salary": 8200000.0, "is_permanent": true, "bonus_code": "PERF2026"},
    {"emp_id": "EMP-029", "name": "Cinta Laura", "base_salary": 10000000.0, "is_permanent": true, "bonus_code": null},
    {"emp_id": "EMP-030", "name": "Deddy Corbuzier", "base_salary": 6100000.0, "is_permanent": false, "bonus_code": null}
  ]
}"""

class Employee:
    def __init__(self, emp_id, name, base_salary, is_permanent):
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary
        self.is_permanent = is_permanent

    def calculate_total_salary(self):
        return self.base_salary

    def get_details(self):
        status = "Tetap" if self.is_permanent else "Kontrak"
        return f"ID: {self.emp_id} | Nama: {self.name:<18} | Status: {status:<7} | Total Gaji: Rp{self.calculate_total_salary():,.2f}"

class PerformanceEmployee(Employee):
    def calculate_total_salary(self):
        return self.base_salary + (self.base_salary * 0.15)

class SeniorEmployee(Employee):
    def calculate_total_salary(self):
        return self.base_salary + (self.base_salary * 0.10)

class LeadEmployee(Employee):
    def calculate_total_salary(self):
        return self.base_salary + (self.base_salary * 0.25)

raw_data = json.loads(employee_data)
processed_employees = []

for data in raw_data["employees"]:
    bonus_rule = data["bonus_code"]
    if bonus_rule == "PERF2026":
        obj = PerformanceEmployee(data["emp_id"], data["name"], data["base_salary"], data["is_permanent"])
    elif bonus_rule == "SENIOR10":
        obj = SeniorEmployee(data["emp_id"], data["name"], data["base_salary"], data["is_permanent"])
    elif bonus_rule == "LEAD2026":
        obj = LeadEmployee(data["emp_id"], data["name"], data["base_salary"], data["is_permanent"])
    else:
        obj = Employee(data["emp_id"], data["name"], data["base_salary"], data["is_permanent"])
    processed_employees.append(obj)

print("=" * 75)
print(f"{'LAPORAN PERHITUNGAN GAJI KARYAWAN':^75}")
print("=" * 75)
for emp in processed_employees:
    print(emp.get_details())
print("=" * 75)
