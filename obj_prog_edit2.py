



















#Program Information:
prog_info = f'''
Objection Options:
One leg     Price    60 min     Repair Work      Do it myself
BBB         Wood Windows        Not interested   Another Company
Contractor  Not Ready           Did not Request  Install time
Just shopping     Too Many Calls    Can't Afford
'''
print(prog_info)
#Define lists first:
one_leg_list = ['leg', 'one leg', 'One leg', '1 leg', 'one-leg', 'One-Leg', 'One-leg']
price_list = ['price', 'Price']
sixty_minutes_list = ['sixty', 'Sixty', '60', '60 min' '60 minutes', '60 Minutes', 'sixty minutes', 'Sixty minutes', 'Sixty Minutes', '60 mins']
repair_list = ['repair', 'repair work', 'Repair']
do_it_myself_list = ['myself', 'Myself', 'do it', 'Do it', 'self', 'Self']
BBB_list = ['BBB', 'bbb', 'bb', 'BB', 'b', 'B']
not_interested_list = ['ni', 'NI', 'not interested', 'Not interested', 'Not Interested']
wood_windows_list = ['wood', 'Wood', 'Wood Windows', 'Wood windows', 'wood windows', 'wood window', 'wood windows']
no_request_list = ['request', 'Request']
another_company_list = ['another', 'competitor', 'Another', 'Competitor', 'company', 'Company', 'another company', 'Another Company', 'Another company']
contractor_list = ['Contractor', 'contractor']
not_ready_list = ['not ready', 'Not Ready', 'NR', 'nr', 'Not ready']
install_time_list = ['Install', 'install', 'Time', 'time']
just_shopping_list = ['shopping', 'Shopping', 'just', 'Just']
too_many_calls_list = ['calls', 'Calls', 'Call', 'call', 'many', 'Many']
cant_afford_list = ['afford', 'Afford']
over_phone_list = ['phone', 'over-the-phone', 'over', 'Phone', 'Over']

objection_search = input('What objection do you need?')

#Define main objection program
def objection_program(objection_search):
    if objection_search in one_leg_list:
        one_legs = f"""
        1. In our experience, there are two parts to the decision-making process. 
           First, there is the aesthetics portion; how the windows look, what options may be important, and choosing the different styles.
           Then, there is the obvious consideration of cost. We’ve found that, while one homeowner may be comfortable making the decision on options, 
           the other may be more concerned with the price.
           Having both homeowners present ultimately reduces the need for multiple visits. 
           Does this make sense?
        
        2. We're a little different than most companies. We carry about 15 different brands and styles, 
           30 different color options, and a variety of different grid patterns. 
           This is why we would prefer both of you to be there to select which options would work best for both of you. 
           Can we work this out without inconveniencing you?
        
        3. We build our windows to your exact specifications, measurements, and feature selections. 
           To best serve you, we prefer to meet with all the owners of the property,
           so you can see the samples and ask any questions that you both could have. 
           Not only will it save you time, but it will greatly increase the chance of getting results that you are both satisfied with. 
        
        NOT FOR: PPL/Canvas:
        4. Let me assure you this is not a requirement, we are grateful for the opportunity to meet with you.
           When we meet with one homeowner we often find that the other homeowner did want to have at least a little input or had some questions. 
           We'll work with you to resolve any issues that come up, but it does delay the proccess. Are there times that work best for both of you? 
        """
        print(one_legs)
    elif objection_search in price_list:
        price_objs = f"""
        1. The price depends on so many factors, such as the type of window, size, quantity, and composition of the existing windows frames. 
           However, if I can gather a few pieces of information, I'd be able to get you a no obligation quote in the next few days.
        
        2. Due to the uniquness of each installation, the only person who can provide you with an exact price is our Design Consultant. 
           I would be unable to give you an estimated price over the phone, but we can get you an exact price in the next couple days
           when our Design Consultant arrives.
        
        3. We can get you some pricing! I'll have one of our Design Consultants come to your home, take a look at your windows, 
           see what you need and lay out what options we have available. That way we can give you an exact price that covers all the expenses 
           of the project with no surprises. 
        """
        print(price_objs)
    elif objection_search in sixty_minutes_list:
        six_min = f"""
        1. When our Design Consultant arrives, they will spend about 20 minutes taking measurements, 
           20 minutes going over your options and styles, and then about 20 minutes to write up an estimate 
           and answer any questions you may have. We are never there longer than we need to be.
        """
        print(six_min)
    elif objection_search in repair_list:
        repair_print = f'''
        1. We are definitely able to help with the project, but we only provide full (product) replacement. 
           If you would like, we can send a Design Consultant out to your home to provide you with a free estimate on the (product),
           as repair jobs will probably only last for a short time.  
        '''
        print(repair_print)
    elif objection_search in do_it_myself_list:
        myself_print = f'''
        1. That is great you are so handy and can do this project yourself. Keep in mind that your project requires a lot of effort 
           and having another company do the work for you will lessen the hardship on yourself. We also install extremely quickly with 
           little impact to you.Also, we offer warranties and a world class Service Team.
        '''
        print(myself_print)
    elif objection_search in BBB_list:
        bbb_print = f'''
        1. While we're not rated by the Better Business Bureau, we are still affiliated with them. We recommend that our customers take 
           a look at Guild Quality, which takes surveys from each customer and posts the good and bad. We also have thousands of Google reviews 
           throughout our different markets. 
           
        2. Due to impacts from the pandemic, supply chain challenges and our rapid growth, Window Nation experienced an 
           unexpected increase in customer complaints. To focus on improvements to the customer experience and resolve open complaints, 
           Window Nation proactively suspended our participation in the BBB accreditation program. This only impacts the accreditation rating. 
           The BBB remains a valuable tool for customers and Window Nation.
        '''
        print(bbb_print)
    elif objection_search in not_interested_list:
        ni_print = f'''
        1. I understand. I wasn’t expecting to catch you the day you are ready to upgrade your home. However, if you were to have 
           one of our Design Consultants come out to give you that free estimate, the price we give you would be good for one year. 
           That way, you’ll be able toplan and budget accordingly.
           
        2. No problem, I understand. A lot of our customers have felt the same way. What we have found was that, even though they 
           weren’t ready to start their project that day, they at least had peace of mind after obtaining pricing to use that as a 
           budgeting tool for the future.
        '''
        print(ni_print)
    elif objection_search in not_ready_list:
        nin_print = f'''
        1. I understand. I wasn’t expecting to catch you the day you are ready to upgrade your home. However, if you were to have 
           one of our Design Consultants come out to give you that free estimate, the price we give you would be good for one year. 
           That way, you’ll be able toplan and budget accordingly.
           
        2. No problem, I understand. A lot of our customers have felt the same way. What we have found was that, even though they 
           weren’t ready to start their project that day, they at least had peace of mind after obtaining pricing to use that as a 
           budgeting tool for the future.
        '''
        print(nin_print)
    elif objection_search in wood_windows_list:
        wood_print = f'''
        1. We offer a variety of Energy Star efficient vinyl windows compared to alternative options. Our design consultant would be 
           happy to go over the many benefits of vinyl windows with you. Are you comfortable getting a quote on vinyl windows?                                                                                                                                                                                              
        '''
        print(wood_print)
    elif objection_search in no_request_list:
        request_print = f'''
        1. That's interesting. We only make calls to people who have put their information online to receive estimates on pricing for 
           (product). Is it possible you made an online request, because we would be able to get you a free quote including 
           (current promotion) in the next couple days?
        '''
        print(request_print)
    elif objection_search in another_company_list:
        company_print = f'''
        1. Congratulations on moving forward with your project, Did you receive at least 3 quotes? I ask because it is recommended to 
           get at least 3. Let me help you out by offering you a comparable quote. If you find that you like our windows or our price, 
           or both, you can still utilize a recission period to cancel your current contract.
           
        2. AWARDS => GUILDMASTER Award for Service Excellence/ ANGIE’S LIST Super Service Award / WINDOW & DOOR Dealer of the Year.
        '''
        print(company_print)
    elif objection_search in contractor_list:
        contractor_print = f'''
        1. That’s great. My only concern is that a lot of our customers have experienced an issue where they had a 
           contractor install their (product) and, for one reason or another, something happened that required a 
           repair. Then, when they tried contacting the contractor, they were unable to get the help they needed. 
           If you were to get a free estimate from Window Nation, know that we would be your start-to-finish 
           (product) replacement company, including any follow up service.  
        '''
        print(contractor_print)
    elif objection_search in install_time_list: 
        intstall_print = f'''
        1. It all depends on the type, style and size of the windows, so the best person to give you an estimated 
           time on the windows would be our design consultant.
        
        IF THEY KEEP ASKING:
        2. Our typical turnaound time is roughly 8-12 weeks, but again this varies based on the options you choose 
           and when we provide your quote, the design consultant will be able to give an accurate time frame.
        '''
        print(intstall_print)
    elif objection_search in just_shopping_list:
        shopping_print = f'''
        1. Great, so if I’m hearing you correctly, it sounds like you are in the budgetary phase of the process, is that 
           correct?  
           (IF YES) 
           Perfect! So, what we can do is have one of our Design Consultants come out to go over all of your options and 
           give you an exact price based on your choices. This way, you’ll be able to use the quote we give to help you 
           budget accordingly, as our quotes are good for one year.  
        
        2. I understand. I wasn’t expecting to catch you the day you are ready to upgrade your home. However, if you were 
           to have one of our Design Consultants come out to give you that free estimate, the price we give you would be 
           good for one year. That way, you’ll be able to budget accordingly.
        '''
        print(shopping_print)
    elif objection_search in too_many_calls_list:
        call_print = f'''
        1. I do apologize for that. When reaching out to customers, our goal is to make sure we are able to reach you before 
        our promotion of ______ ends. Would we be able to find a good time for us to provide you with that free price quote?
        '''
        print(call_print)
    elif objection_search in cant_afford_list:
        afford_print = f'''
        1. I understand that you may not be able to afford it right now. A lot of customers have felt the same way. What some 
           customers have found was that, by having us out to provide them with the free no obligation price quote, they realized 
           that the project has plenty of affordable options for them to choose from.
        '''
        print(afford_print)
    elif objection_search in over_phone_list:
        over_phone_print = f'''
        1. The best way to receive pricing is having one of our design consultants come to your home. We're a little different 
           than most companies; we carry about 15 different brands and styles, and 30 different color options, and a variety of 
           different grid patterns. Setting up an in-home estimate will help you capture the full design process.
        
        COVID:
        2. Our design consultants are very thoughtful and will wear PPE (incuding booties) through the demo. We check temperatures 
           and ensure the health and safety of both you and our design consultants.
        '''
        print(over_phone_print)
    else:
        print('Invalid Input')

#Calling the Main Function
objection_program(objection_search)
help_var = str(input('Did that help? y or n  (lowercase)'))

#Seeing if it worked:
help_check = ['n']
if help_var in help_check:
    objection_search = input('What objection do you need?')
    objection_program(objection_search)
else:
    print('Glad to help!')
