dat <- read.table(header=TRUE, text='
      cond xval yval
   control 11.5 10.8
   control  9.3 12.9
   control  8.0  9.9
   control 11.5 10.1
   control  8.6  8.3
   control  9.9  9.5
   control  8.8  8.7
   control 11.7 10.1
   control  9.7  9.3
   control  9.8 12.0
 treatment 10.4 10.6
 treatment 12.1  8.6
 treatment 11.2 11.0
 treatment 10.0  8.8
 treatment 12.9  9.5
 treatment  9.1 10.0
 treatment 13.4  9.6
 treatment 11.6  9.8
 treatment 11.5  9.8
 treatment 12.0 10.6
')

library(ggplot2)
install.packages("dplyr",repos = "http://cran.us.r-project.org")
library(dplyr)
lines <- dat %>%
  group_by(cond) %>%
  summarise(
    x = mean(xval),
    ymin = min(yval),
    ymax = max(yval)
  )

png(file="sampleSave.png",
    width=500,height=400)
# Add colored lines for the mean xval of each group
sp + geom_hline(aes(yintercept=10)) +
     geom_linerange(aes(x=x, y=NULL, ymin=ymin, ymax=ymax), data=lines)

dev.off()


