// Define your independent values
x = [0 : 0.2 : 4*%pi];



driver('PNG');
xinit('plot.png');

// Define your functions and plot.
// The default color is black
plot2d3(x, sin(x))
// 5 at the end means red line
plot2d3(x, sin(2*x), 5)
// Superimpose a red envelope on the red lines
plot2d(x, sin(2*x), 5)

xend();
exit();
