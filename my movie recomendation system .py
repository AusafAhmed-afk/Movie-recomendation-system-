import pandas as pd

movies = pd.read_csv("movies_dataset_500.csv")

def ask_preferences():
    print("Welcome to the Movie Recommendation System!\n")
    
    genre = input("Which genre do you want to watch? (Action, Comedy, Romance, Horror, Sci-Fi, Drama or leave blank): ").strip()
    mood = input("Do you want it Light, Funny, Emotional, Intense or leave blank: ").strip()
    era = input("Do you prefer Modern, Classic, or leave blank: ").strip()
    popularity = input("Do you want Popular movies, Hidden gems or leave blank: ").strip()
    length = input("Do you want Short, Long or leave blank: ").strip()

    preferences = {
        "genre": genre if genre else "doesn't matter",
        "mood": mood if mood else "doesn't matter",
        "era": era if era else "doesn't matter",
        "popularity": popularity if popularity else "doesn't matter",
        "length": length if length else "doesn't matter"
    }

    return preferences

def filter_movies(movies, preferences):
    filtered = movies.copy()
    
    for key, value in preferences.items():
        value = value.lower()
        if value != "doesn't matter":
            filtered = filtered[filtered[key].str.lower() == value]
    
    return filtered

def recommended_movies(filtered_movies):
    if filtered_movies.empty:
        print("\nSorry, no movies were found according to your preferences.")
    else:
        print("\nRecommended Movies:")
        for title in filtered_movies['title'].tolist()[:10]:
            print("- " + title)

def main():
    user_preferences = ask_preferences()
    filtered = filter_movies(movies, user_preferences)
    recommended_movies(filtered)

if __name__ == "__main__":
    main()
