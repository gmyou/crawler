from __future__ import print_function
from datetime import date, datetime, timedelta
import MySQLdb

cnx = MySQLdb.connect('localhost', 'user_id', 'user_pw', 'crawler')
cursor = cnx.cursor()
tomorrow = datetime.now().date() + timedelta(days=1)
add_employee = ("INSERT INTO site "
               "(site_name "
               "VALUES (%s)")
add_salary = ("INSERT INTO site_article "
              "(subject, link) "
              "VALUES (%(subject)s, %(link)s)")
data_employee = ('2cpu')
# Insert new employee
cursor.execute(add_employee, data_employee)
emp_no = cursor.lastrowid
# Insert salary information
# TODO
data_salary = {
  'subject': '',
  'link': '',
}
cursor.execute(add_salary, data_salary)
# Make sure data is committed to the database
cnx.commit()
cursor.close()
cnx.close()
