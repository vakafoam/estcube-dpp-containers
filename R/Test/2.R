set.seed(183)
# Normally distributed numbers
x <- rnorm(80, mean=50, sd=5)

# Uniformly distributed numbers
z <- runif(80)

png(file="sampleSave.png",
    width=500,height=400)
qqnorm(z)
qqline(z)

dev.off()