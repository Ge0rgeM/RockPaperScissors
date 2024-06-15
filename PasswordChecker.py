def is_only_english(str):
    for i in str:
        if (i >= '0' and i <= '9') or i == '_':
            continue
        if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
            continue
        else:
            return False
    return True

def has_one_capital(str):
    for i in str:
        if i > 'A' and i < 'Z':
            return True;
    return False;

def is_valid_length(str):
    valid_length = 8
    if len(str) < valid_length:
        return False
    else:
        return True

def has_special_character(str):
    for i in str:
        if (i >= '0' and i <= '9') or i == '_':
            return True
    return False

def is_password_okay(obj):
    is_valid = True
    for restrictions in obj:
        print(f'{restrictions} ---> {obj[restrictions]}')
        if obj[restrictions] == False:
            is_valid = False
    return is_valid

def valid_new_user_password(str):
    password_policy = {
        'is_only_english': is_only_english(str),
        'has_one_capital': has_one_capital(str),
        'is_valid_length': is_valid_length(str),
        #At least 1 number or character '0-9', '_'  
        'has_special_character': has_special_character(str)
    }
    return password_policy

    #To Do, Make Password Policy Obj where you tick whichever 
    #rule is fullfilled and then return boolean and obj itself
    #incase answer is False (not fullfilled all of them) so 
    # in the popup we can write whichever is not yet fullfilled.
    #To Do Make GUI of Login/Register Popups
