from flask import Flask, render_template, request, jsonify
from ElevatorSimulation import IdleAtFirstFloor  # Adjust import based on your simulation file

app = Flask(__name__)

# Initialize elevator state
current_state = IdleAtFirstFloor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move', methods=['POST'])
def move_elevator():
    global current_state
    event = request.json.get('event')
    current_state = current_state.handle_event(event)
    
    # Here we can send the new state to the front-end (just a simple string for now)
    return jsonify({'state': str(current_state)})

@app.route('/door', methods=['POST'])
def control_door():
    global current_state
    event = request.json.get('event')
    current_state = current_state.handle_event(event)
    
    # Send the updated state to the front-end
    return jsonify({'state': str(current_state)})

if __name__ == '__main__':
    app.run(debug=True)

