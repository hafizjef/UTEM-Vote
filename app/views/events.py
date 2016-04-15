"""
SocketIO Events script
"""
from app import socketio

ccc = 0


@socketio.on('connect', namespace='/dd')
def test_connect():
    """Increment users count on connect"""
    global ccc
    ccc += 1
    socketio.emit('msg', {'data': 'Connected', 'count': ccc}, namespace='/dd')


@socketio.on('disconnect', namespace='/dd')
def test_disconnect():
    global ccc
    ccc -= 1
    socketio.emit('msg', {'data': 'Connected', 'count': ccc}, namespace='/dd')
