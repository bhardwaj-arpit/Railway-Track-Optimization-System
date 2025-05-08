from flask import Blueprint, jsonify
import openpyxl

user_bp = Blueprint('user_routes', __name__)

# Function to read user data from Excel
def get_user_data():
    wb = openpyxl.load_workbook('database.xlsx')
    sheet = wb.active
    users = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        users.append({'username': row[0], 'email': row[1], 'ticket_count': row[2]})
    return users

@user_bp.route('/', methods=['GET'])
def users():
    users = get_user_data()
    return jsonify(users)
