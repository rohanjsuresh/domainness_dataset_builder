from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'keyword_relation_builder/index.html', {'title': "test", 'times_classified':0, 'keyword1':"k1", 'keyword2':"k2", 'keyword3':"k3", 'keyword4':"k4", 'keyword5':"k5", 'keyword6':"k6", 'keyword7':"k7", 'keyword8':"k8"})

def add_entry(request):
    # print("Submitted")

    # increment number of articles classified by user
    username = request.POST.get("username")
    # # num_results = len(User_Extended.objects.filter(username = username))
    # #  # if no results insert new element into table
    # # if num_results == 0:
    # #     new_record = User_Extended(username = username, email = User.objects.get(username=username).email, times_classified=1)
    # #     new_record.save()
    # # # if records already exists, update it
    # # else:
    # update_user= User_Extended.objects.get(username = username)
    # # increment times classified
    # update_user.times_classified += 1
    # update_user.save()

    # ids gettings retrieved from input
    input_ids = ["k1", "k2", "k3" "k4", "k5", "k6", "k7", "k8"]

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
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(keyword)
    print(username)
    return render(request, 'keyword_relation_builder/index.html', {'title': "test", 'times_classified':0, 'keyword1':"k1", 'keyword2':"k2", 'keyword3':"k3", 'keyword4':"k4", 'keyword5':"k5", 'keyword6':"k6", 'keyword7':"k7", 'keyword8':"k8"})

    
    # check to see if keywords is in table
    num_results = len(Keywords.objects.filter(keyword = keyword))

    # if no results insert new element into table
    if num_results == 0:
        new_record = Keywords(keyword = keyword, times_classified = 1, computer_science = values["cs_input"], mathematics = values["math_input"], physics = values["physics_input"], electrical_engineering = values["ee_input"], quantitative_biology = values["qbio_input"], statistics = values["stat_input"], economics = values["econ_input"], other = values["other_input"])
        new_record.save()
        title = request.POST.get("title_input")
        # print("TITLE IS: " + title)
        update_record2 = Arxiv_Titles_In_Circulation.objects.get(title = title)
        update_record2.times_classified += 1
        update_record2.save()

    # if records already exists, update it
    else:
        # get record associated with keyword
        update_record = Keywords.objects.get(keyword = keyword)

        title = request.POST.get("title_input")
        # print("TITLE IS: " + title)
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

    title = get_title_by_user_subject(username)
    times_classified = get_number_classified_by_user(username)
    return render(request, 'demo_frontend/index.html', {'title': title, 'times_classified':times_classified})

# if user skips increment total skips for that title
def skip_entry(request):
    # print("Skipped")
    title = request.POST.get("title_input")
    # print(title)

    update_record = Arxiv_Titles_In_Circulation.objects.get(title = title)
    # increment times classified
    update_record.times_skipped += 1
    update_record.save()

    # update titles in circulation
    update_titles_in_circulation()

    username = request.POST.get("username2")
    new_title = get_title_by_user_subject(username)
    times_classified = get_number_classified_by_user(username)
    return render(request, 'demo_frontend/index.html', {'title': new_title, 'times_classified':times_classified})
