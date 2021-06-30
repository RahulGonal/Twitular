import twint

search = input("What is the Topic you want to Search >>>> ")
city = input("City Name so that we can search near you >>>> ")
No = input("Number of Tweetes to Generate >>>> ")
Boi = twint.Config()
Boi.Search = search
Boi.Near = city
Boi.Limit = No
Boi.Popular_tweets = True
twint.run.Search(Boi)