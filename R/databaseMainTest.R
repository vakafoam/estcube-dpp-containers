install.packages("DBI", repos="http://cran.r-project.org", lib = 'C:/Users/vaka/Documents/R/win-library/3.3')
install.packages('RPostgreSQL', repos="http://cran.r-project.org", lib = 'C:/Users/vaka/Documents/R/win-library/3.3')

library(RPostgreSQL)

# Initialize DB connection
drv <- dbDriver("PostgreSQL")
con <- dbConnect(drv, dbname = "DPP",
                 host = "localhost", port = 5432,
                 user = "postgres", password = 'retipu')

dbExistsTable(con, "weather")

# query the data from postgreSQL 
downloaded <- dbGetQuery(con, "SELECT * from weather")
# downloaded

# examine the DB
dbListTables(con)

# d <- as.data.frame(downloaded)
# 
# dbColumnInfo(d)
# 
# dbGetStatement(downloaded)
# dbHasCompleted(downloaded)
# dbGetRowCount(downloaded)

# # Plotting the data, saving to file
# install.packages("ggplot2")
# require(ggplot2)
# jpeg('G:/PythonCodes/data-processing-platform/Broker-R/R/rplot.jpg')
# ggplot(downloaded, aes(x = temp, y = humid, fill = humid)) + 
#   geom_boxplot() + theme_bw()
# dev.off()
# 
# # Secong approach
# ggplot(downloaded, aes(x = temp, y = humid, fill = humid)) + 
#   geom_boxplot() + theme_bw()+
#   ggsave('G:/PythonCodes/data-processing-platform/Broker-R/R/fig1.png',width=6, height=4,dpi=300)


# THE END
# disconnect from database
dbDisconnect(con)
# unload database driver
dbUnloadDriver(drv)
