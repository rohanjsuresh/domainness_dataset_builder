from django.shortcuts import render
from django.http import HttpResponse
from .models import Keywords
from .models import Keywords_Classified
from .models import Arxiv_Titles_In_Circulation
from .models import Arxiv_Titles_Classified
from django.db import connection

# Create your views here.

def home(request):
    title = Arxiv_Titles_In_Circulation.objects.order_by('?').first().title
    print(title)
    return render(request, 'demo_frontend/index.html', {'title': title})

def add_entry(request):
    print("Submitted")
    # ids gettings retrieved from input
    input_ids = ["cs_input", 
                 "math_input",
                 "physics_input",
                 "astro_input",
                 "ee_input",
                 "qbio_input",
                 "stat_input",
                 "econ_input",
                 "other_input"]

    # programatically retreive values into array
    values = {}
    for i in range(len(input_ids)):
        val = request.POST.get(input_ids[i])
        if val is not None:
            values[input_ids[i]] = 1
        else:
            values[input_ids[i]] = 0



    # print(values)
    
    # get keywords 
    keyword = request.POST.get("keyword_input").lower()
    print(keyword)
    
    # check to see if keywords is in table
    num_results = len(Keywords.objects.filter(keyword = keyword))

    # if no results insert new element into table
    if num_results == 0:
        new_record = Keywords(keyword = keyword, times_classified = 1, computer_science = values["cs_input"], mathematics = values["math_input"], physics = values["physics_input"], astronomy = values["astro_input"], electrical_engineering = values["ee_input"], quantitative_biology = values["qbio_input"], statistics = values["stat_input"], economics = values["econ_input"], other = values["other_input"])
        new_record.save()

    # if records already exists, update it
    else:
        # get record associated with keyword
        update_record = Keywords.objects.get(keyword = keyword)

        title = request.POST.get("title_input")
        print("TITLE IS: " + title)
        update_record2 = Arxiv_Titles_In_Circulation.objects.get(title = title)

        # increment times classified
        update_record.times_classified += 1
        update_record2.times_classified += 1

        # update subject counts
        if values["cs_input"] > 0:
            update_record.computer_science += values["cs_input"] 
        if values["math_input"] > 0:
            update_record.mathematics += values["math_input"] 
        if values["physics_input"] > 0:
            update_record.physics += values["physics_input"] 
        if values["astro_input"] > 0:
            update_record.astronomy += values["astro_input"] 
        if values["ee_input"] > 0:
            update_record.electrical_engineering += values["ee_input"] 
        if values["qbio_input"] > 0:
            update_record.quantitative_biology += values["qbio_input"] 
        if values["stat_input"] > 0:
            update_record.statistics += values["stat_input"] 
        if values["econ_input"] > 0:
            update_record.economics += values["econ_input"] 
        if values["other_input"] > 0:
            update_record.other += values["other_input"] 
            

        update_record.save()
        update_record2.save()

        keyword = None

        # update titles in circulation
        update_titles_in_circulation()

    title = Arxiv_Titles_In_Circulation.objects.order_by('?').first().title
    return render(request, 'demo_frontend/index.html', {'title': title})

# Updates tables so that only titles that have been classied
# less than 2 times are in circulation
# Runs this SQL query:
#   INSERT INTO demo_frontend_arxiv_titles_classified(title, times_classified)
#           SELECT title, times_classified
#           FROM demo_frontend_arxiv_titles_in_circulation
#           WHERE times_classified >= 2;
#   DELETE FROM demo_frontend_arxiv_titles_in_circulation
#           WHERE times_classified >= 2;
def update_titles_in_circulation():
    with connection.cursor() as cursor:
        cursor.execute('INSERT INTO demo_frontend_arxiv_titles_classified(title, times_classified) SELECT title, times_classified FROM demo_frontend_arxiv_titles_in_circulation WHERE times_classified >= 2;')
        cursor.execute('DELETE FROM demo_frontend_arxiv_titles_in_circulation WHERE times_classified >= 2;')