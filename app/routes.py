from flask import render_template
from flask import request
from app import app

from app.services import service_hibernate, service_wake

hosts = [
    {
        'host': '192.168.1.23',
        'name': 'PC 1',
        'user': 'theusr',
        'status': 'unknown',
        'keyfile' : 'pc1'
    },
    {
        'host': '192.168.1.33',
        'name': 'PI 4',
        'user': 'pi',
        'status': 'unknown',
    }
]

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home', hosts=hosts)

@app.route("/update_host", methods=["POST"])
def update_host():
    in_data = request.get_json()
    host_id = in_data['param']
    print(f'host_id: {host_id}')
    host_item = next((host for host in hosts if host['host'] == host_id), None)
    host_item['status'] = "updated status"
    # TODO: input_status ??
    # return f"updated: {host_id} with status host.status = {host_item['status']}"
    return render_template('index.html', title='Home', hosts=hosts)


@app.route("/hibernate/<host_ip>", methods=["POST"])
def hibernate(host_ip):
    print(f'host_id: {host_ip}')
    host_item = next((host for host in hosts if host['host'] == host_ip), None)
    service_hibernate(host_item)
    return f"sent hibernate to {host_ip}"

@app.route("/wake/<host_ip>", methods=["POST"])
def wake(host_ip):
    print(f'host_id: {host_ip}')
    host_item = next((host for host in hosts if host['host'] == host_ip), None)
    service_wake(host_item)
    return f"sent wakeup to {host_ip}"