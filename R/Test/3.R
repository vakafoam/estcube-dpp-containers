library('ggplot2')

pretest2  <- round( rnorm( n=5000, mean=80, sd=5) )
posttest2 <- round( pretest2 + rnorm( n=5000, mean=3, sd=3) )
pretest2 [pretest2  > 100] <- 100
posttest2[posttest2 > 100] <- 100
temp <- data.frame(pretest2,posttest2)

pretest2

png(file="sampleSave.png",
    width=565,height=400)


ggplot(temp, aes( x=pretest2, y=posttest2) ) +
  geom_point( size=1 ) + geom_density2d()


dev.off()
