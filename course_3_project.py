import requests_with_caching
import json


#1
def get_movies_from_tastedive(movie_name):
    '''
    Define a function, called get_movies_from_tastedive.
    It should take one input parameter, a string that is the name of a movie or music artist.
    The function should return the 5 TasteDive results that are associated with that string;
    be sure to only get movies, not other kinds of media.
    It will be a python dictionary with just one key, ‘Similar’.
    Try invoking your function with the input “Black Panther”.
    HINT: Be sure to include only q, type, and limit as parameters in order to extract data from the cache.
    If any other parameters are included, then the function will not be able to recognize the data
    that you’re attempting to pull from the cache. Remember, you will not need an api key in order
    to complete the project, because all data will be found in the cache.
    '''

    base_url = 'https://tastedive.com/api/similar'
    params_dict = {'q': movie_name, 'type': 'movies', 'limit': '5'}
    response = requests_with_caching.get(base_url, params=params_dict)
    print(response.url[:2])
    print(response.text[:100])
    
    # return response.json()
    return json.loads(response.text)

# some invocations that we use in the automated tests;
# uncomment these if you are getting errors and want better error messages
# get_movies_from_tastedive("Bridesmaids")
# get_movies_from_tastedive("Black Panther")



#2
def get_movies_from_tastedive(movie_name):

    base_url = 'https://tastedive.com/api/similar'
    params_dict = {'q': movie_name, 'type': 'movies', 'limit': '5'}
    response = requests_with_caching.get(base_url, params=params_dict)
    print(response.url[:2])
    print(response.text[:100])
    
    # return response.json()
    return json.loads(response.text)

def extract_movie_titles(response):
    '''
    Please copy the completed function from above into this active code window.
    Next, you will need to write a function that extracts just the list of movie titles
    from a dictionary returned by get_movies_from_tastedive. Call it extract_movie_titles.
    '''

    print(response)
    movie_names = [mov['Name'] for mov in response['Similar']['Results']]
    
    return movie_names

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# extract_movie_titles(get_movies_from_tastedive("Tony Bennett"))
# extract_movie_titles(get_movies_from_tastedive("Black Panther"))



#3
def get_movies_from_tastedive(movie_name):
    base_url = 'https://tastedive.com/api/similar'
    params_dict = {'q': movie_name, 'type': 'movies', 'limit': '5'}
    response = requests_with_caching.get(base_url, params=params_dict)
    print(response.url[:2])
    print(response.text[:100])
    
    # return response.json()
    return json.loads(response.text)

def extract_movie_titles(response):
    print(response)
    movie_names = [mov['Name'] for mov in response['Similar']['Results']]
    
    return movie_names

def get_related_titles(movie_titles_list):
    '''
    Please copy the completed functions from the two code windows above into this active code window.
    Next, you’ll write a function, called get_related_titles. It takes a list of movie titles as input.
    It gets five related movies for each from TasteDive, extracts the titles for all of them,
    and combines them all into a single list. Don’t include the same movie twice.
    '''

    movies = []
    for movie in movie_titles_list:
        response = get_movies_from_tastedive(movie)
        titles = extract_movie_titles(response)
        movies += [mov for mov in titles if mov not in movies]
        
    print(movies)
    return movies

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_related_titles(["Black Panther", "Captain Marvel"])
# get_related_titles([])



#4
def get_movie_data(movie_name):
    '''
    Your next task will be to fetch data from OMDB. The documentation for the API is at https://www.omdbapi.com/
    Define a function called get_movie_data. It takes in one parameter which is a string
    that should represent the title of a movie you want to search.
    The function should return a dictionary with information about that movie.
    Again, use requests_with_caching.get(). For the queries on movies that are already in the cache,
    you won’t need an api key. You will need to provide the following keys: t and r.
    As with the TasteDive cache, be sure to only include those two parameters
    in order to extract existing data from the cache.
    '''

    base_url = 'http://www.omdbapi.com/'
    params_dict = {'t': movie_name, 'r': 'json'}
    response = requests_with_caching.get(base_url, params=params_dict)
    print(response.url)
    print(response.text)
    
    # return response.json()
    return json.loads(response.text)

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movie_data("Venom")
# get_movie_data("Baby Mama")



#5
def get_movie_data(movie_name):
    '''
    Please copy the completed function from above into this active code window.
    Now write a function called get_movie_rating. It takes an OMDB dictionary result for one movie
    and extracts the Rotten Tomatoes rating as an integer. For example, if given the OMDB dictionary
    for “Black Panther”, it would return 97. If there is no Rotten Tomatoes rating, return 0.
    '''

    base_url = 'http://www.omdbapi.com/'
    params_dict = {'t': movie_name, 'r': 'json'}
    response = requests_with_caching.get(base_url, params=params_dict)
    print(response.url)
    print(response.text)
    
    # return response.json()
    return json.loads(response.text)

def get_movie_rating(movies_dict):
    for rating in movies_dict['Ratings']:
        if rating['Source'] == 'Rotten Tomatoes':
            return int(rating['Value'].replace('%', ''))
    
    return 0

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movie_rating(get_movie_data("Deadpool 2"))



#6
# Now, you’ll put it all together.
# Don’t forget to copy all of the functions that you have previously defined into this code window.

def get_movies_from_tastedive(movie_name):
    base_url = 'https://tastedive.com/api/similar'
    params_dict = {'q': movie_name, 'type': 'movies', 'limit': '5'}
    response = requests_with_caching.get(base_url, params=params_dict)
    
    return json.loads(response.text)

def extract_movie_titles(response):
    movie_names = [mov['Name'] for mov in response['Similar']['Results']]
    
    return movie_names

def get_related_titles(movie_titles_list):
    movies = []
    for movie in movie_titles_list:
        response = get_movies_from_tastedive(movie)
        titles = extract_movie_titles(response)
        movies += [mov for mov in titles if mov not in movies]
        
    return movies

def get_movie_data(movie_name):
    base_url = 'http://www.omdbapi.com/'
    params_dict = {'t': movie_name, 'r': 'json'}
    response = requests_with_caching.get(base_url, params=params_dict)
    
    return json.loads(response.text)

def get_movie_rating(movies_dict):
    for rating in movies_dict['Ratings']:
        if rating['Source'] == 'Rotten Tomatoes':
            return int(rating['Value'].replace('%', ''))
    
    return 0

def get_sorted_recommendations(movie_titles):
    '''
    Define a function get_sorted_recommendations. It takes a list of movie titles as an input.
    It returns a sorted list of related movie titles as output, up to five related movies
    for each input movie title. The movies should be sorted in descending order by their Rotten Tomatoes rating,
    as returned by the get_movie_rating function. Break ties in reverse alphabetic order,
    so that ‘Yahşi Batı’ comes before ‘Eyyvah Eyvah’.
    '''

    titles = get_related_titles(movie_titles)
    print(titles)
    ratings = sorted(titles, key = lambda title: (get_movie_rating(get_movie_data(title)), title), reverse=True)
    
    return ratings

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])






