install.packages("DBI")
install.packages('RPostgreSQL')

library(RPostgreSQL)

# Initialize DB connection
drv <- dbDriver("PostgreSQL")
con <- dbConnect(drv, dbname = "estcube",
                 host = "localhost", port = 5432,
                 user = "postgres", password = 'xxx')

dbExistsTable(con, "weather")

# Create data to write to DB
trial <- matrix(c(39,1,21), ncol=3)
colnames(trial) <- c('humid', 'id', 'temp')
dt <- as.table(trial)
dt

# Write data to DB
dbWriteTable(con, "weather",
             value = data.frame(humid=dt[1,1],id=dt[1,2],temp=dt[1,3]),
             append = TRUE, row.names = FALSE)

# query the data from postgreSQL
df_postgres <- dbGetQuery(con, "SELECT * from weather")
df_postgres

# Creating new data
# matrix of random values + hum
set.seed(42)
m=3
n=100
mymat <- replicate(m, rnorm(n))
dframe <- data.frame(mymat)
for (i in 1:m) {
  for (j in 1:n) {
    dframe[i,j]<-mydframe[i,j] + 10*sin(0.75*pi)
  }
}
# Write data to DB
dbWriteTable(con, "weather",
             value = dframe,
             append = TRUE, row.names = FALSE)

# query the data from postgreSQL
downloaded <- dbGetQuery(con, "SELECT * from weather")
downloaded

# examine the DB
dbListTables(con)

d <- as.table(downloaded)

dbColumnInfo(downloaded)

dbGetStatement(downloaded)
dbHasCompleted(downloaded)
dbGetRowCount(downloaded)

# Plotting the data, saving to file
install.packages("ggplot2")
require(ggplot2)
jpeg('G:/PythonCodes/data-processing-platform/Broker-R/R/rplot.jpg')
ggplot(downloaded, aes(x = temp, y = humid, fill = humid)) +
  geom_boxplot() + theme_bw()
dev.off()

# Secong approach
ggplot(downloaded, aes(x = temp, y = humid, fill = humid)) +
  geom_boxplot() + theme_bw()+
  ggsave('G:/PythonCodes/data-processing-platform/Broker-R/R/fig1.png',width=6, height=4,dpi=300)


###############################################
dbGetQuery(con, "TRUNCATE weather") # clears the table
V1 <- c(1:100)
V2 <- replicate (100,rnorm(1, mean=11, sd=20))
V3 <- replicate (100,rnorm(1, mean=67, sd=30))
M <- cbind(V1,V2,V3)
D <- as.data.frame(M)

# THE END
# disconnect from database
dbDisconnect(con)
# unload database driver
dbUnloadDriver(drv)
