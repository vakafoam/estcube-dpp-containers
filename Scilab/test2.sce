t=0:0.01:10;
subplot(211),plot2d(t,sin(t))
subplot(212),plot2d(t,sin(3*t))
xsave("G:\PythonCodes\data-processing-platform\Broker-Scilab\Scilab\foo.png", gcf())
clf()
//xload("G:\PythonCodes\data-processing-platform\Broker-Scilab\Scilab\foo.png")
exit
//a=gca();
//curve=a.children.children; //handle on the curve
//save("G:\PythonCodes\data-processing-platform\Broker-Scilab\Scilab\foo.png\foo.png", "curve")
//delete(curve)
//exit
