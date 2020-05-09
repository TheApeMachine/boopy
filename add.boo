// Instantiate two variables.
a = 12
b = 20

// Loop from 12 to 20 (8 loops).
a to b {
	// Print to stdout.
	a
}

// Loop from 12 to 20 (8 loops)
// with an interation index (0 to 7).
a to b as i {
	// Add together and print to stdout.
	a + i
}
