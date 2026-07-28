from client import LandingPageCopyClient

def main():
    client = LandingPageCopyClient()
    res = client.optimize_copy(headline='Our Product is Good')
    print(f"Result for suggested_headline: {res['suggested_headline']}")

if __name__ == "__main__":
    main()
