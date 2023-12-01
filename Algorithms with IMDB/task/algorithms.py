def read_and_store_movies(file_path):
    movies = []
    with open(file_path, encoding="UTF-8") as file:
        for line in file:
            parts = line.rsplit(',', 1)
            if len(parts) == 2:
                title, rating = parts
                title = title.strip().replace('"', '')
                try:
                    rating = float(rating.strip())
                    movies.append((title, rating))
                except ValueError:
                    # Handle invalid rating values
                    print(f"Invalid rating in line: {line.strip()}")
            else:
                print(f"Skipping invalid line: {line.strip()}")
    return movies

def search_movies_by_rating(movies, target_rating):
    for title, rating in movies:
        if rating == target_rating:
            print(f"{title} - {rating}")

def bubble_sort_movies(movies):
    n = len(movies)
    for i in range(n-1):
        swapped = False
        for j in range(0, n-i-1):
            if movies[j][1] > movies[j+1][1]:  # Compare ratings
                movies[j], movies[j+1] = movies[j+1], movies[j]  # Swap
                swapped = True
        if not swapped:  # Break if no swap occurred
            break
    return movies

def binary_search_movies(movies, target_rating):
    low, high = 0, len(movies) - 1
    while low <= high:
        middle = (low + high) // 2
        mid_rating = movies[middle][1]

        if mid_rating == target_rating:
            # Find all movies with rating 6.0 around the current index
            find_and_print_movies_with_same_rating(movies, middle, target_rating)
            break
        elif mid_rating < target_rating:
            low = middle + 1
        else:
            high = middle - 1

def find_and_print_movies_with_same_rating(movies, index, rating):
    # Check to the left of the found index
    left_index = index
    while left_index >= 0 and movies[left_index][1] == rating:
        print(f"{movies[left_index][0]} - {rating}")
        left_index -= 1

    # Check to the right of the found index
    right_index = index + 1
    while right_index < len(movies) and movies[right_index][1] == rating:
        print(f"{movies[right_index][0]} - {rating}")
        right_index += 1

def merge_sort_movies(movies):
    if len(movies) > 1:
        mid = len(movies) // 2
        left_half = movies[:mid]
        right_half = movies[mid:]

        merge_sort_movies(left_half)
        merge_sort_movies(right_half)

        i = j = k = 0

        # Merging the two halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i][1] < right_half[j][1]:
                movies[k] = left_half[i]
                i += 1
            else:
                movies[k] = right_half[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left_half):
            movies[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            movies[k] = right_half[j]
            j += 1
            k += 1

    return movies


movies = read_and_store_movies("/Users/ts/Downloads/movies.csv")
sorted_movies = merge_sort_movies(movies)  # Use merge sort instead of bubble sort
binary_search_movies(sorted_movies, 6.0)


