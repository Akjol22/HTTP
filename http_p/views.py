def about():
    with open ('http_p/templates/videohtml') as template:
        return template.read()
    
def video():
    with open ('http_p/templates/video.html') as template:
        return template.read()