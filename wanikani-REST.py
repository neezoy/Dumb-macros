# A timer till your next lesson/review
import requests
import time
import os


def main():
    url = 'https://www.wanikani.com/api/user/##ID-KEYY###/study-queue'
    path = "C:/Users/pc/Desktop/Python/WaniKani/Zombified_Alligator.mp3"
    webpath = "https://www.wanikani.com/dashboard"
    current_time = time.time()

    response = requests.get(url)
    jsonOBJ = response.json()

    reviewsavalibe = int(jsonOBJ['requested_information']['reviews_available'])
    lessonsavalible = int(
        jsonOBJ['requested_information']['lessons_available'])
    nextreview_time = int(jsonOBJ['requested_information']
                     ['next_review_date'])

    time_left = ((nextreview_time-current_time)/60)

    print("time to next review: {} minutes".format(round(time_left)))

    if (nextreview_time-current_time) > 0:
        time.sleep(round(nextreview_time-current_time))
    print('Review ready!')
    print('reviews avalible: {}'.format(reviewsavalibe))
    os.startfile(path)
    os.startfile(webpath)
    time.sleep(1200)
    

if __name__ == '__main__':
    main()
