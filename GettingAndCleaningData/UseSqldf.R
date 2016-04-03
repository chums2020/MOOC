###Use sqldf() to perform SQL query in R
#Download and Load Data

options(sqldf.driver = "SQLite") 
options(gsubfn.engine = "R") 
library(sqldf)
url <-"https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2Fss06pid.csv"
download.file(url, destfile = "CommunitySurvey.csv")
acs <- read.table("CommunitySurvey.csv", sep = ",", header = TRUE)


#Use sqldf() and unique() to generate two identical vectors
query <- as.matrix(sqldf("select distinct AGEP from acs"))
unique <- as.matrix(unique(acs$AGEP))

#The two vectors, query and unique, should be identical. But the command identical returns FALSE.
identical(query, unique)

#Find out why the two vectors are different
all.equal(query, unique)
which(unique != query, arr.ind=TRUE)
attributes(query)
attributes(unique)
attributes(query)$dimnames <- NULL

#The two vectors differ in attributes. After changing the attribute values, identical() returns TRUE.
identical(query, unique)

