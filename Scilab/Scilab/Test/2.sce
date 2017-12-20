// Define your variable
t = linspace(0, 2*%pi, 100);
// Define your polar function
r = sqrt(abs(2 * cos(5*t)));

disp(r);

driver('PNG');
xinit('plot.png');


// Plot in polar coordinates
polarplot(t, r);
legend('r = Satellite passes');

xend();

exit();
