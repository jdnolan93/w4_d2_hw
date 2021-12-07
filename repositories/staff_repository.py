from db.run_sql import run_sql

from models.staff import Staff

import repositories.staff_repository as staff_repository

def save(staff):
    sql = "INSERT INTO staff (name, start_date, department, rating) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [staff.name, staff.start_date, staff.department, staff.rating]
    results = run_sql(sql, values)
    id = results[0]['id']
    staff.id = id
    return staff

def select_all():
    staff = []

    sql = "SELECT * FROM staff"
    results = run_sql(sql)

    for row in results:
        staffs = Staff(row['name'], row['start_date'], row['department'], row['rating'], row['id'])
        staff.append(staffs)
        return staffs

def delete_all():
    sql = "DELETE FROM staff"
    run_sql(sql) 

def delete(id):
    sql = "DELETE  FROM staff WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(staff):
    sql = "UPDATE staff SET (name, start_date, department, rating) = (%s, %s, %s, %s) WHERE id = %s"
    values = [staff.name, staff.start_date, staff.department, staff.rating, staff.id]
    run_sql(sql, values)