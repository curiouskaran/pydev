#this is implementatiion of media.py - entertainment_center.py

import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
						"A story of a boy who's toys came to life",
						"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
						"https://youtu.be/KYz2wyBy3kc")

avatar = media.Movie("Avatar",
					"A US mariene is send to an alien world",
					"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
					"https://youtu.be/5PSNL1qE6VY")


beautiful_mind = media.Movie("A Beautiful Mind",
							"A life of a mathematician who get schizophrenia",
							"https://upload.wikimedia.org/wikipedia/en/b/b8/A_Beautiful_Mind_Poster.jpg",
							"https://youtu.be/WFJgUm7iOKw")

school_of_rock = media.Movie("School Of Rock",
							"A unsucessful rock band mussiacian turned into a teacher",
							"https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
							"https://youtu.be/3PsUJFEBC74")

midnight_in_paris = media.Movie("Midnight in Paris",
								"The movie explores themes of nostalgia and modernism.",
								"https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
								"https://youtu.be/dtiklALGz20")

fault_in_our_stars = media.Movie("The Fault in our stars",
								"This movie is about a disabled girl and her love",
								"https://upload.wikimedia.org/wikipedia/en/4/41/The_Fault_in_Our_Stars_%28Official_Film_Poster%29.png",
								"https://youtu.be/9ItBvH5J6ss")

movies = [toy_story, avatar, beautiful_mind,school_of_rock, midnight_in_paris, fault_in_our_stars]
fresh_tomatoes.open_movies_page(movies)