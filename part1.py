#Name: Chris Demundo
#Umich ID: cdemundo

#I did not receive access to the Twitter API in time.  I used a friends account to write the code, but I do not want to include his access info on GitHub. 
#I was able to complete the assignment and this code should work if you enter values to complete the authentication.


import tweepy
import nltk
from nltk.corpus import stopwords
import sys
import csv

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


# write your code here
# usage should be python3 part1.py <username> <num_tweets>
def main():
    try:
    	username = sys.argv[1]
    	num_tweets = sys.argv[2]
    except:
    	print("Usage is: python3 part1.py <username> <num_tweets>")

    #I believe include_rts is default false for Tweepy, but just to make sure I exclude retweets
    tweets = api.user_timeline(screen_name = username, count=num_tweets, include_rts = False)

    #also record number of favorite counts and retweets
    favorite_count = 0
    retweet_count = 0

    for tweet in tweets:
    	retweet_count = retweet_count + tweet.retweet_count
    	favorite_count = favorite_count + tweet.favorite_count

    #now let's handle looking at the word usage for the tweets
    tweet_words = []

    #nltk.download('stopwords')  <- uncomment this if stopwords isn't downloaded!

    #check for string.isalpha to exclude non-real words and URLS and also exclude stopwords
    for tweet in tweets:
    	words_in_string = tweet.text.split(" ")
    	for word in words_in_string:
    		if word not in stopwords.words('english') and word.isalpha() and word != 'RT':
    			tweet_words.append(word)

    #get part of speech for all words in tweets
    #nltk.download('averaged_perceptron_tagger') <- uncomment if needed
    part_of_speech = nltk.pos_tag(tweet_words)

    nouns = {}
    verbs = {}
    adjs = {}

    for word in part_of_speech:
    	if word[1] == "NN":
    		if word[0] in nouns:
    			nouns[word[0]] += 1
    		else:
    			nouns[word[0]] = 1
    	elif word[1] == "VB":
    		if word[0] in verbs:
    			verbs[word[0]] += 1
    		else:
    			verbs[word[0]] = 1
    	elif word[1] == "JJ":
    		if word[0] in adjs:
    			adjs[word[0]] +=1
    		else:
    			adjs[word[0]] = 1

    #use stable sorting to sort by multiple criteria - primarily by number and secondarily by alphabetical order
    nouns_sorted = sorted(nouns.items(), key=lambda x:x[0])
    nouns_sorted.sort(key = lambda x:x[1], reverse=True)

    verbs_sorted = sorted(verbs.items(), key=lambda x:x[0])
    verbs_sorted.sort(key = lambda x:x[1], reverse=True)

    adjs_sorted = sorted(adjs.items(), key=lambda x:x[0])
    adjs_sorted.sort(key = lambda x:x[1], reverse=True)

    #create the final output
    print("USER: {u}".format(u=username))
    print("TWEETS ANALYZED: {n}".format(n=num_tweets))
    print("VERBS: {v1}({v1n}) {v2}({v2n}) {v3}({v3n}) {v4}({v4n}) {v5}({v5n})".format(
    	v1=verbs_sorted[0][0], v1n=verbs_sorted[0][1],
    	v2=verbs_sorted[1][0], v2n=verbs_sorted[1][1],
    	v3=verbs_sorted[2][0], v3n=verbs_sorted[2][1],
    	v4=verbs_sorted[3][0], v4n=verbs_sorted[3][1],
    	v5=verbs_sorted[4][0], v5n=verbs_sorted[4][1])
    )

    print("NOUNS: {v1}({v1n}) {v2}({v2n}) {v3}({v3n}) {v4}({v4n}) {v5}({v5n})".format(
    	v1=nouns_sorted[0][0], v1n=nouns_sorted[0][1],
    	v2=nouns_sorted[1][0], v2n=nouns_sorted[1][1],
    	v3=nouns_sorted[2][0], v3n=nouns_sorted[2][1],
    	v4=nouns_sorted[3][0], v4n=nouns_sorted[3][1],
    	v5=nouns_sorted[4][0], v5n=nouns_sorted[4][1])
    )

    print("ADJECTIVES: {v1}({v1n}) {v2}({v2n}) {v3}({v3n}) {v4}({v4n}) {v5}({v5n})".format(
    	v1=adjs_sorted[0][0], v1n=adjs_sorted[0][1],
    	v2=adjs_sorted[1][0], v2n=adjs_sorted[1][1],
    	v3=adjs_sorted[2][0], v3n=adjs_sorted[2][1],
    	v4=adjs_sorted[3][0], v4n=adjs_sorted[3][1],
    	v5=adjs_sorted[4][0], v5n=adjs_sorted[4][1])
    )

    print("ORIGINAL TWEETS: {t}".format(t=len(tweets)))
    print("TIMES FAVORITED (ORIGINAL TWEETS ONLY): {f}".format(f=favorite_count))
    print("TIMES RETWEETED (ORIGINAL TWEETS ONLY): {r}".format(r=retweet_count))
    			
    #save nouns_sorted to CSV for part 4
    with open('noun_data.csv','w', newline="") as out:
	    csv_out=csv.writer(out)
	    csv_out.writerow(['Noun','Number'])
	    for row in nouns_sorted[0:5]:
	        csv_out.writerow(row)
       

if __name__ == "__main__":
    main()

