

function z=f(x,y)
z=2*x^2+y^2;
endfunction
x=linspace(-1,1,100);
y=linspace(-2,2,200);
z=feval(x,y,f)';
z
fprintfMat('matrix.out',z )
exit
