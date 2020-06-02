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
        

class Description:

    all_descriptions = []

    def __init__(self,id,name,Author,title,description,publishedAt):
        self.id =id
        self.name = name
        self.Author = Author
        self.title= title
        self.description= description
        self.publishedAt=publishedAt


    def save_description(self):
        Description.all_descriptions.append(self)


    @classmethod
    def clear_description(cls):
        Description.all_descriptions.clear()

    @classmethod
    def get_description(cls,id):

        response = []

        for description in cls.all_descriptions:
            if description.movie_id == id:
                response.append(description)

        return response