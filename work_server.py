from flask import Flask, json, jsonify, request
from redis import Redis


class WorkServer:
    def __init__(self):
        self.app = Flask(__name__)
        self.redis = Redis()


def create_server(server=WorkServer()):
    '''Create server, add endpoints, and return the server'''

    @server.app.route('/get_job', methods=['GET'])
    def get_job():
	# TODO: retrieve a job from the redis 'jobs_waiting'
        keys = server.redis.hkeys("jobs_waiting")
        if len(keys) == 0:
            return "There are no jobs available", 400 
        value = server.redis.hget("jobs_waiting", keys[0])
        server.redis.hdel("jobs_waiting", keys[0])
        return jsonify({keys[0].decode(): value.decode()}), 200

    @server.app.route('/put_results', methods=['PUT'])
    def put_results():
        data = json.loads(request.data)
        if ("job_id" not in data or "value" not in data):
            return '', 400            
        print("job_id: %s, value: %s" % (data["job_id"], data["value"]))
        return '', 200

    return server


if __name__ == '__main__':
    server = create_server()
    server.app.run(host='0.0.0.0', port=8080, debug=False)
