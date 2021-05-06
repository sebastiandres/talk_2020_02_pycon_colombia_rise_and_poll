def dict2html(markdown_dict):
    my_html = ""
    fmt = '''<input type={0} name="survey" value="option_{1}"> {2} </br>\n'''
    # Add the question
    my_html += markdown_dict["question"] + " </br>\n"
    # Add the answer options
    for i, option in enumerate(markdown_dict["options"]):
        my_html += fmt.format(markdown_dict["type"], i, option)
    return my_html

if __name__=="__main__":
    print(dict2html({"question":"A question", "type":"radio", "options":["Uno","Dos","Tres"]}))
    print(dict2html({"question":"Another question", "type":"checkbox", "options":["Uno","Dos","Tres"]}))   