t=0:0.01:10;
subplot(211),plot2d(t,sin(t))
subplot(212),plot2d(t,sin(3*t))
xsave("foo.png", gcf())
clf()
exit
//xload("G:\PythonCodes\data-processing-platform\Broker-Scilab\Scilab\foo.png")

//a=gca();
//curve=a.children.children; //handle on the curve
//save("G:\PythonCodes\data-processing-platform\Broker-Scilab\Scilab\foo.png\foo.png", "curve")
//delete(curve)

