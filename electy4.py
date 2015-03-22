
import tweepy

from flask import Flask
from flask import render_template
from datetime import datetime

auth = tweepy.OAuthHandler("X2nLW6De6Zc6PdSQeAYoFtzYW","CrO0hNqMwOL1oBy97Hioisqc2yROVmCasWrHxXUhkw3eCdpfTa")
auth.set_access_token("1725724472-oy2grBIetHm8AtTPjpKeu21gjk72zcheNubpgLc", "YINkhxK8TMlQpjuueJByoZvOeNpjJp61eCGsgnUISHe2A")

api = tweepy.API(auth)

def get_year():
	now = datetime.now()
	year = now.year
	return year

def get_month():
	now = datetime.now()
	month = now.month
	return month

def get_day():
	now = datetime.now()
	day = now.day - 7
	return day

app = Flask(__name__)


def get_labour_tweets(issue):
	tweets = api.search(q=['{0}'.format(issue.replace('_',' ')), 'since:{0}-{1}-{2}'.format(get_year(), get_month(), get_day()), 'from:UKLabour'], count=100)
	print 'Labour tweets:', tweets
	return len(tweets)

def get_conservative_tweets(issue):
	tweets = api.search(q=['{0}'.format(issue.replace('_',' ')), 'since:{0}-{1}-{2}'.format(get_year(), get_month(), get_day()), 'from:Conservatives'], count=100)
	print 'Conservative tweets:', tweets
	return len(tweets)

def get_libdem_tweets(issue):
	tweets = api.search(q=['{0}'.format(issue.replace('_',' ')), 'since:{0}-{1}-{2}'.format(get_year(), get_month(), get_day()), 'from:LibDems'], count=100)
	print 'LibDem tweets:', tweets
	return len(tweets)

def get_UKIP_tweets(issue):
	tweets = api.search(q=['{0}'.format(issue.replace('_',' ')), 'since:{0}-{1}-{2}'.format(get_year(), get_month(), get_day()), 'from:UKIP'], count=100)
	print 'UKIP tweets:', tweets
	return len(tweets)

def get_total_tweets(issue):
	total_tweets = get_labour_tweets(issue.replace('_',' ')) + get_conservative_tweets(issue) + get_libdem_tweets(issue) + get_UKIP_tweets(issue)
	print 'Total tweets:', total_tweets
	return total_tweets

def get_labour_proportion(issue):
	labour_proportion = float(get_labour_tweets(issue))/float(get_total_tweets(issue))*100
	print 'Labour proportion:',labour_proportion
	return labour_proportion

def get_conservative_proportion(issue):
	conservative_proportion = float(get_conservative_tweets(issue))/float(get_total_tweets(issue))*100
	print 'Conservative proportion:', conservative_proportion
	return conservative_proportion

def get_libdem_proportion(issue):
	libdem_proportion = float(get_libdem_tweets(issue))/float(get_total_tweets(issue))*100
	print 'Lib Dem proportion:', libdem_proportion
	return libdem_proportion

def get_UKIP_proportion(issue):
	UKIP_proportion = float(get_UKIP_tweets(issue))/float(get_total_tweets(issue))*100
	print 'UKIP proportion:', UKIP_proportion
	return UKIP_proportion

@app.route("/")
def get_homepage():
	return render_template('Electyupdate3.html')

@app.route("/<issue>")
def get_issue(issue):
	labour_proportion = get_labour_proportion(issue)
	conservative_proportion = get_conservative_proportion(issue)
	libdem_proportion = get_libdem_proportion(issue)
	UKIP_proportion = get_UKIP_proportion(issue)
	return render_template('Electyupdate3.html', issue=issue, labour_proportion=labour_proportion, conservative_proportion=conservative_proportion, libdem_proportion=libdem_proportion, UKIP_proportion=UKIP_proportion)


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000, debug=True)
