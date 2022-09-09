
# QUESTION 1

def hello_name(user_name):
  print("hello_"+user_name.upper()+"!")

hello_name('Katy') 
  


# QUESTION 2

def first_odds():
    for k in range(1,100,2):
        print(k)


 
 # QUESTION 3

def max_num_in_list(a_list):
    return(max(a_list))

my_list = [3,5,6,8,11,567]
answer = max_num_in_list(my_list)
print(answer)



# QUESTION 4

def is_leap_year(a_year):
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
 
year = int(input("Enter a year : "))
is_leap_year(year)
if is_leap_year(year):
    print(year,"is a leap year" )
else:
    print(year, "is NOT a leap year")



# QUESTION 5

def is_consecutive(a_list):

 

    s = 0

    for item in a_list:
        s = s + item

    maxx = max(a_list)
    minn = min(a_list)
    result = (maxx * (maxx + 1) - minn*(minn-1)) /2

    if result == s: 
        return True
    else:
      return False

a_list = [2,3,4,5,6]
print(is_consecutive(a_list))