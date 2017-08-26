var roster = []

function addNew(name) {
	roster.push(name)
}

function remove(argument) {
	roster.splice(roster.indexOf(argument), 1)
}

function display(arg) {
	console.log(arg)
}

keep = true

while (keep) {
	inside = true
	answer = prompt('Do you want to use the web app? (y/n)')
	if (answer == 'y') {
		// alert('ALLFINE')
		while (true) {
			answer = prompt('Do you want to add, remove, display or quit?')
			if (answer == 'add') {
				addNew(prompt('Whom to add to the list?'))
			}
			if (answer == 'remove') {
				remove(prompt('Whom to remove?'))
			}
			if (answer == 'display') {
				display(roster)
			}
			if (answer == 'quit') {
				alert('Ok, bye!')
				keep = false
				break
			}
		}
	} else if (answer == 'n') {
		alert('Ok, see you!')
		break
	}
}

// Use if and else if statements to execute the correct function for each command.
