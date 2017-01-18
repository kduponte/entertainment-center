import fresh_tomatoes
import media

inception = media.Movie("Inception",
                        "A thief, who steals corporate secrets through use of dream-sharing technology, is given the inverse task of planting an idea into the mind of a CEO.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=66TuSJo4dZM")

scarface = media.Movie("Scarface",
                        "In Miami in 1980, a determined Cuban immigrant takes over a drug cartel and succumbs to greed.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjAzOTM4MzEwNl5BMl5BanBnXkFtZTgwMzU1OTc1MDE@._V1_.jpg",
                        "https://www.youtube.com/watch?v=7pQQHnqBa2E")

juice = media.Movie("Juice",
                        "Four inner-city teenagers get caught up in the pursuit of power and happiness, which they refer to as 'the juice'.",
                        "https://images-na.ssl-images-amazon.com/images/I/51THDBz1OBL.jpg",
                        "https://www.youtube.com/watch?v=QsWto8p7t1E")

menace_II_society = media.Movie("Menace II Society",
                        "A young street hustler attempts to escape the rigors and temptations of the ghetto in a quest for a better life.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQyOTA5NzgzMl5BMl5BanBnXkFtZTgwMjgwNTcxMTE@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=CD2pjnGy8Fk")

city_of_god = media.Movie("City of God",
                        "Two boys growing up in a violent neighborhood of Rio de Janeiro take different paths: one becomes a photographer, the other a drug dealer.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA4ODQ3ODkzNV5BMl5BanBnXkFtZTYwOTc4NDI3._V1_.jpg",
                        "https://www.youtube.com/watch?v=ioUE_5wpg_E")

rockers = media.Movie("Rockers",
                        "Horsemouth sets himself up in business selling records but when gangsters steal his bike things start to turn nasty. As tensions build, Horsemouth and friends plot to end the gangsters reign of terror and restore justice to the people of Kingston"
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BOTIwNzcxNzk3OF5BMl5BanBnXkFtZTYwNjgwNjg4._V1_.jpg"
                        "https://www.youtube.com/watch?v=mx8g4yoVkGU")

movies = [inception, scarface, juice, menace_II_society, city_of_god, rockers]

fresh_tomatoes.open_movies_page(movies)
