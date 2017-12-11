    #install.packages("DBI")
#install.packages('RPostgreSQL')
#install.packages("ggplot2")

library(RPostgreSQL)

# Initialize DB connection
drv <- dbDriver("PostgreSQL")
con <- dbConnect(drv, dbname = "DPP",
                 host = "localhost", port = 5432,
                 user = "postgres", password = 'retipu')

dbExistsTable(con, "weather")

# Create data
#dbGetQuery(con, "TRUNCATE weather") # clears the table
V1 <- c(1:100)
V2 <- replicate (100,rnorm(1, mean=11, sd=20))
V3 <- replicate (100,rnorm(1, mean=67, sd=30))
M <- cbind(V1,V2,V3)
D <- as.data.frame(M)

# Write data to DB
dbWriteTable(con, "weather", 
             value = D, 
             append = TRUE, row.names = FALSE)

# query the data from postgreSQL 
downloaded <- dbGetQuery(con, "SELECT * from weather")

# Plotting BoxPlot & Saving the result
library(ggplot2) 
#jpeg('G:/PythonCodes/data-processing-platform/Broker-R/R/rplot.jpg')
png(file="G:/PythonCodes/data-processing-platform/Broker-R/R/image.png",
    width=400,height=350)
qplot(temp, humid, data=downloaded, geom=c("boxplot", "jitter"),
      fill=humid, main="Temperature vs Humidity",
      xlab="Temperature", ylab="Humidity") 
dev.off()


# THE END
# disconnect from database
dbDisconnect(con)
# unload database driver
dbUnloadDriver(drv)
