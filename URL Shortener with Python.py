import pyshortener 

def shorten_url(url):
    try:
        s = pyshorteners.Shortener()
        shortened_url = s.tinyurl.short(url)
        return shortened_url
    except pyshorteners.exceptions.BadURLException:
        return "Invalid URL. Please enter a valid URL."
    except pyshorteners.exceptions.ShorteningErrorException:
        return "Unable to shorten the URL. Please try again later."

def main():
    print("Welcome to the URL Shortener!")

    while True:
        long_url = input("Enter the URL you want to shorten (or 'quit' to exit): ")

        if long_url.lower() == 'quit':
            break

        shortened_url = shorten_url(long_url)

        print(f"Shortened URL: {shortened_url}\n")

    print("Thank you for using the URL Shortener!")

if __name__ == "__main__":
    main()

    