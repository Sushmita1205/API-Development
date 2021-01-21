from flask import Flask,request,jsonify
from flask_httpauth import HTTPBasicAuth

app=Flask(__name__)

auth=HTTPBasicAuth()

USER_DATA={
        "admin":"SuperSecretPwd"
        }


@auth.verify_password
def verify(username,password):
    if not(username and password):
        return False
    return USER_DATA.get(username) == password



        

books_list=[
    {
         "id":0,
         "author":"Jim Corbett",
         "language":"English",
         "title":"Story Of Sundarban",
    },
    {
         "id":1,
         "author":"Chinua Achebe",
         "language":"English",
         "title":"Things fall apart",
    },
    {
         "id":2,
         "author":"Hans Christian Anderson",
         "language":"Danish",
         "title":"Fairy Tales",
    },
    {   
         "id":3,
         "author":"Emily Bront",
         "language":"English",
         "title":"Wuthering heights",
    },        
    { 
         "id":4,
         "author":"Jorge Luis Borges",
         "language":"Spanish",
         "title":"Ficciones",
     },
     {
         "id":5,
         "author":"Sukumar Roy",
         "language":"Bengali",
         "title":"Sothpatra",
     },
     {
         "id":6,
         "author":"Arthur Conal Doyle",
         "language":"English",
         "title":"Sherlock Holmes",
     },
     {
         "id":7,
         "author":"Frances Hodgson Burnett",
         "language":"English",
         "title":"Secret Garden",
     },
     {
         "id":8,
         "author":"Dan Brown",
         "language":"English",
         "title":"Angels And Demons",
     },
]

@app.route('/books',methods=['GET','POST'])
def books():
    if request.method=='GET':
        if len(books_list)>0:
            return jsonify(books_list)
        else:
            'Nothing found',404

    if request.method=='POST':
         new_author= request.form['author']
         new_lang= request.form['language']
         new_title= request.form['title']
         iD=books_list[-1]['id']+1


         new_obj={
             'id':iD,
             'author':new_author,
             'language':new_lang,
             'title':new_title
         }
         books_list.append(new_obj)
         return jsonify(books_list),201



@app.route('/book/<int:id>',methods=['GET','PUT','DELETE'])
def single_book(id):
    if request.method=='GET':
        for i in books_list:
            if i['id']==id:
                return jsonify(i)
            pass
    
    if request.method=='PUT':
        for i in books_list:
            if i['id']==id:
                i['author']= request.form['author']
                i['language']= request.form['language']
                i['title']= request.form['title']
                
             
        return jsonify(books_list)


    if request.method=='DELETE':
        for index,i in enumerate (books_list):
            if i['id']==id:
                books_list.pop(index)
                
        return jsonify(books_list)



if __name__=='__main__':
    app.run()


 




