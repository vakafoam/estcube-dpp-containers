d <- c(1,2,3)
v <- c(1,3,3)
#plot(v,d)
v+d
#if(!require(ggplot2)){install.packages("ggplot2")}

savePlot <- function (plot) {
  png(file="./sampleSave.png",
      width=500,height=400)
  plot
  dev.off()
}

#savePlot(qplot(v,d,color = 'blue'))
#print (qplot(v,d, color = 'blue'))

png(file="sampleSave.png",
    width=500,height=400)
#qplot(v,d,color = 'blue')
plot(v,d)
dev.off()
