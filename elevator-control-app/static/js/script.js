let currentFloor = 1;  // Start at the first floor
let doorsOpen = false; // Keep track of whether doors are open

function moveElevator(direction) {
    let cart = document.getElementById('cart');
    
    // Check if doors are closed before moving the elevator
    if (doorsOpen) {
        alert("Please close the doors before moving the elevator!");
        return;
    }

    if (direction === 'up' && currentFloor === 1) {
        currentFloor = 2;
        cart.style.bottom = '50%';  // Move to the second floor
    } else if (direction === 'down' && currentFloor === 2) {
        currentFloor = 1;
        cart.style.bottom = '0';  // Move to the first floor
    } else {
        alert("Already at the " + (currentFloor === 1 ? "first" : "second") + " floor.");
    }

    // Send move event to the backend
    fetch('/move', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ event: direction === 'up' ? '2' : '4' })  // Example events for up/down
    })
    .then(response => response.json())
    .then(data => console.log(data));
}

function controlDoor(action) {
    let firstFloorDoors = document.getElementById('first-floor-doors');
    let secondFloorDoors = document.getElementById('second-floor-doors');

    // Only allow opening/closing doors when the elevator is stationary on a floor
    if (action === 'open') {
        if (doorsOpen) {
            alert("Doors are already open!");
            return;
        }
        doorsOpen = true;
        if (currentFloor === 1) {
            firstFloorDoors.style.width = '0%';  // Open first-floor doors
        } else if (currentFloor === 2) {
            secondFloorDoors.style.width = '0%';  // Open second-floor doors
        }
    } else if (action === 'close') {
        if (!doorsOpen) {
            alert("Doors are already closed!");
            return;
        }
        doorsOpen = false;
        if (currentFloor === 1) {
            firstFloorDoors.style.width = '100%';  // Close first-floor doors
        } else if (currentFloor === 2) {
            secondFloorDoors.style.width = '100%';  // Close second-floor doors
        }
    }

    // Send door event to the backend
    fetch('/door', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ event: action === 'open' ? '1' : '5' })  // Example events for open/close
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
    });
}

