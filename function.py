def get_summ(one, two): #Функционал разделения по различным источникам делается через .split(), а не выражение delimeter
    message = str(one + "&" + two).upper()
    print(message.split("&"))

get_summ("Learn", "python")