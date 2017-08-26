/// PART 8 - LOOP EXERCISES
// Before we continue on with your project, let's practice some loops!
// You'll have just two problems, but you'll need to use each loop type we
// learned about to solve them!


///////////////////
//// PROBLEM 1 ///
/////////////////

// Use a For Loop to print (console.log()) out the word "hello" 5 times.
//
// Do this with a While Loop and a For Loop

// While Loop

var i = 0;

while (i < 5) {
	console.log('hello');
	i++
}

// For Loop

for (var i = 0; i < 5; i++) {
	console.log('hello')
}

// PROBLEM 2 ///

// While Loop

while (i <= 25) {
	if (i % 2) {
		console.log(i)
	}
	i++
}

// For Loop

for (var i = 1; i <= 25; i+=2) {
	console.log(i)
}