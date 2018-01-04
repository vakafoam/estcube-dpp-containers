library(RPostgreSQL)

# Initialize DB connection
drv <- dbDriver("PostgreSQL")
con <- dbConnect(drv, dbname = "estcube",
                 host = "localhost", port = 5432,
                 user = "postgres", password = 'xxx')
