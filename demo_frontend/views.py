from django.shortcuts import render
from django.http import HttpResponse
from .models import Keywords

# Create your views here.

def home(request):
    return render(request, 'demo_frontend/index.html')

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

        # increment times classified
        update_record.times_classified += 1

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

        keyword = None
    return render(request, 'demo_frontend/index.html')