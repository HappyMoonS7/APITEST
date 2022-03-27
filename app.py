from flask import Flask,jsonify 
import sqlite3
app = Flask(__name__)


@app.route("/")
def page1(): 
    return "HEllo"

@app.route("/page2")
def page2(): 
    return "Welcome to Page 2"

@app.route("/<fname>/<lname>") #GET 
def accept_data(fname,lname): 
    data = {'firstname':fname,'lastname':lname}
    #==== Database ==========
    with sqlite3.connect("test.db") as con: 
        curr = con.cursor()
        sql_cmd = """
            INSERT INTO People(fname,lname) VALUES(?,?);
        """

        curr.execute(sql_cmd,(fname,lname,)) #TypeError : Multiple Parameter
        con.commit()


    real_data = jsonify(data)
    return real_data



@app.route("/send_data/<ID>")
def get_data(ID):
    #==== Database ==========
    with sqlite3.connect("test.db") as con: 
        curr = con.cursor()
        sql_cmd = """
            SELECT * FROM People WHERE ID==?;
        """


        data = [i for i in curr.execute(sql_cmd,(ID,))][0]
        print(data)

        send_data = {'id':data[0],'fname':data[1],'lname':data[2]}
        return jsonify(send_data)   


if __name__ == '__main__':
    app.run(port=8000,debug=True)