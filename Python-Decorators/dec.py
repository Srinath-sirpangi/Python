
def log_message(decoFunc): #decoFunc is the function passed to decorator
    def foo(*args,**kwargs):
        output = decoFunc(*args,**kwargs) #get the return value (string) from passed function
        with open('string.txt','a') as f: #open a new file in append mode to write 
            f.write(output+"\n") #write every string in new line
        return output #return output
    return foo #return decorator function



@log_message
def a_function_that_returns_a_string():
    return "A string"

@log_message
def a_function_that_returns_a_string_with_newline(s):
    return "{}\n".format(s)

@log_message
def a_function_that_returns_another_string(string=""):
    return "Another string"

a_function_that_returns_a_string() 
a_function_that_returns_a_string_with_newline("hello")
a_function_that_returns_another_string()