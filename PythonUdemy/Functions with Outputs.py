def format_name(f_name, l_name):
    print(f_name.title())
    print(l_name.title())

#format_name("chris", "gunn")

def format_name_output(f_name, l_name):
    formatted_first_name = f_name.title()
    formatted_last_name = l_name.title()
    return f"{formatted_first_name} {formatted_last_name}"

print(format_name_output("chris", "gunn"))