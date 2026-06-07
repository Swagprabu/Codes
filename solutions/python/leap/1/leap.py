def leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
leap_year(2015)  
leap_year(1970)  
leap_year(1996)  
leap_year(1960)  
leap_year(2100)  
leap_year(1900)  
leap_year(2000)  
leap_year(2400)  
leap_year(1800)  





