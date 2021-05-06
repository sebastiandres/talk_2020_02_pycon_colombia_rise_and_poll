def parse(my_string):
    checkbox_options = []
    radio_options = []
    question = ""
    for line in my_string.split("\n"):
        clean_line = line.strip()
        # Skip line if not even 2 chars
        if len(clean_line)<2:
            continue
        # Process line if at least 2 chars
        if clean_line[0].lower()=="x":
            checkbox_options.append(clean_line[1:].strip())
        elif clean_line[0].lower()=="o":
            radio_options.append(clean_line[1:].strip())
        else:
            question += clean_line
    # Check if data to be returned
    if len(checkbox_options)+len(radio_options)==0:
        print("No options were found")
        return {} 
    if len(checkbox_options)>0 and len(radio_options)>0:        
        print("Mixed checkbox and radio form types")
        return {}
    # Add the 
    my_dict = {}
    if len(checkbox_options)>0 and len(radio_options)==0:        
        my_dict["options"] = checkbox_options
        my_dict["type"] = "checkbox" 
    if len(checkbox_options)==0 and len(radio_options)>0:        
        my_dict["options"] = radio_options
        my_dict["type"] = "radio" 
    # Add the question
    my_dict["question"] = question
    return my_dict


if __name__=="__main__":
    test_1 = """
            Mi pregunta:
            x A
            X B
            x C
            """
    print(parse(test_1))

    test_2 = """
            Mi otra pregunta:
            o A
            o B
            O C
            """
    print(parse(test_2))

    test_3 = """
            Mi otra pregunta:
            """
    print(parse(test_3))

    test_4 = """
            Mi otra pregunta:
            o A
            o B
            X C
            """
    print(parse(test_4))
