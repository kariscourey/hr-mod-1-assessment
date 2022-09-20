def format_name(name):
    try:
        return name["first"] + " " + name["middle"][0] + ". " + name["last"]
    except:
        return name["first"] +  " " + name["last"]



name = {"first": "Jocelyn", "middle": "Maria", "last": "Payne"}
print(format_name(name))  # --> "Jocelyn M. Payne"

name = {"first": "Jocelyn", "middle": "", "last": "Payne"}
print(format_name(name))  # --> "Jocelyn Payne"

name = {"first": "Jocelyn", "last": "Payne"}
print(format_name(name))  # --> "Jocelyn Payne"
