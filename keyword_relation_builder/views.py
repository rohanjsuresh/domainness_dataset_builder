from django.shortcuts import render
from demo_frontend.models import User_Extended
from .models import Keywords_in_Circulation
from .models import Keyword_Pairs
from django.shortcuts import redirect
from django.db import connection
from django.contrib.auth.models import User 
import random

relation_suggestion = ["", "", "", "", "", "", "", "", ""]
redirected_once = False

# Create your views here.
def home(request):
    global relation_suggestion
    keyword = select_keywords()

    if request.user.is_authenticated:
        # print("Logged in")
        username = request.user
        times_classified = get_number_classified_by_user(username)
        return render(request, 'keyword_relation_builder/index.html', {'title': keyword, 'times_classified':times_classified, 'keyword1':relation_suggestion[0], 'keyword2':relation_suggestion[1], 'keyword3':relation_suggestion[2], 'keyword4':relation_suggestion[3], 'keyword5':relation_suggestion[4], 'keyword6':relation_suggestion[5], 'keyword7':relation_suggestion[6], 'keyword8':relation_suggestion[7]})
    else:
        global redirected_once
        if redirected_once:
            redirected_once = False
            return render(request, 'keyword_relation_builder/index.html', {'title': keyword, 'times_classified':0, 'keyword1':relation_suggestion[0], 'keyword2':relation_suggestion[1], 'keyword3':relation_suggestion[2], 'keyword4':relation_suggestion[3], 'keyword5':relation_suggestion[4], 'keyword6':relation_suggestion[5], 'keyword7':relation_suggestion[6], 'keyword8':relation_suggestion[7]})
        else:
            # print("First login")
            redirected_once = True
            return redirect('home')

def select_keywords():
    # get random keyword we want to find relations to
    keyword_selection = Keywords_in_Circulation.objects.order_by('?').first().keyword

    # keep track of keywords we're using
    keywords_in_use = set()
    keywords_in_use.add(keyword_selection)

    # get suggestions
    global relation_suggestion
    relation_suggestion = ["", "", "", "", "", "", "", "", ""]

    num_suggestions = 0
    num_iterations  = 0

    # we want to loop till we get 8 unique suggestions but if this is 
    # not possible then just break
    while num_suggestions != 8 and num_iterations < 1000:

        trial_suggestion = Keywords_in_Circulation.objects.order_by('?').first().keyword
        if trial_suggestion not in keywords_in_use:
            relation_suggestion[num_suggestions] = trial_suggestion
            keywords_in_use.add(trial_suggestion)
            num_suggestions += 1
        
        num_iterations += 1

    return keyword_selection

def add_entry(request):
    # print("Submitted")

    # increment number of articles classified by user
    username = request.POST.get("username")

    update_user= User_Extended.objects.get(username = username)
    # increment times classified
    update_user.times_classified += 1
    update_user.save()

    # ids gettings retrieved from input
    input_ids = ["k1", "k2", "k3", "k4", "k5", "k6", "k7", "k8"]

    # programatically retreive values into array
    values = {}
    for i in range(len(input_ids)):
        val = request.POST.get(input_ids[i])
        if val is not None:
            values[input_ids[i]] = 1
        else:
            values[input_ids[i]] = 0



    # # print(values)
    
    # get keyword we presented
    keyword = request.POST.get("keyword_input").lower()

    # increment times keyword was classified
    update_record = Keywords_in_Circulation.objects.get(keyword = keyword)
    update_record.times_classified += 1
    update_record.save()

    # get keywords we passed as suggestions
    global relation_suggestion

    # iterate through list of keyword suggestions and if selected increment count/add to databasae
    for i in range(len(input_ids)):
        if values[input_ids[i]] > 0:
            
            # concatenate strings to create unique keyword pair (alphabetically order words)
            keyword_concat = ""
            if keyword < relation_suggestion[i]:
                keyword_concat = keyword + "&&" + relation_suggestion[i]
            else:
                keyword_concat = relation_suggestion[i] + "&&" + keyword

            # check to see if keywords is in table
            num_results = len(Keyword_Pairs.objects.filter(keyword_pair = keyword_concat))

            # if no results insert new element into table
            if num_results == 0:
                new_pair = Keyword_Pairs(keyword_pair = keyword_concat, times_classified=1)
                new_pair.save()
            # otherwise increment count
            else:
                update_record = Keyword_Pairs.objects.get(keyword_pair = keyword_concat)
                update_record.times_classified += 1

    update_titles_in_circulation()
    return home(request)

# if user skips increment total skips for that title
def skip_entry(request):
    # get keyword we presented
    keyword = request.POST.get("keyword_input2").lower()

    # increment times keyword was skipped
    update_record = Keywords_in_Circulation.objects.get(keyword = keyword)
    update_record.times_skipped += 1
    update_record.save()

    update_titles_in_circulation()
    return home(request)


def get_number_classified_by_user(username):
    user = User_Extended.objects.get(username = username)
    return user.times_classified


def update_titles_in_circulation():
    with connection.cursor() as cursor:
        cursor.execute('INSERT INTO keyword_relation_builder_keywords_classified(keyword, times_classified, times_skipped) SELECT keyword, times_classified, times_skipped FROM keyword_relation_builder_keywords_in_circulation WHERE times_classified >= 2;')
        cursor.execute('DELETE FROM keyword_relation_builder_keywords_in_circulation WHERE times_classified >= 2;')
        cursor.execute('INSERT INTO keyword_relation_builder_keywords_skipped(keyword, times_classified, times_skipped) SELECT keyword, times_classified, times_skipped FROM keyword_relation_builder_keywords_in_circulation WHERE times_skipped >= 5;')
        cursor.execute('DELETE FROM keyword_relation_builder_keywords_in_circulation WHERE times_skipped >= 5;')
