#Making a data structure
book_details <-data.frame(
  book_id = c(1001:1002),
  book_title = c("Let us C","Python prohramming"),
  booK_author = c("Jim Robert","R.Gupta")
)
#Printing the data sturcture
print("Printing the data using Print")
print(book_details)
print("Printing the stucture of data using str")
str(book_details)
#printing a selected column of the data
print("Printing the ID column of the data")
print(book_details$book_id)
