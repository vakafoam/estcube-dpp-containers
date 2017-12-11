library(RPostgreSQL)

# Initialize DB connection
drv <- dbDriver("PostgreSQL")
con <- dbConnect(drv, dbname = "DPP",
                 host = "localhost", port = 5432,
                 user = "postgres", password = 'retipu')