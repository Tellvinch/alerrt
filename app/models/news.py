class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,id,name,Author,title,description,publishedAt):
        self.id =id
        self.name = name
        self.Author = Author
        self.title= title
        self.description= description
        self.publishedAt=publishedAt
        