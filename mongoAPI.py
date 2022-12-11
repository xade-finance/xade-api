from http.server import BaseHTTPRequestHandler, HTTPServer
from json import loads
from pymongo import MongoClient
from os import getenv
from dotenv import load_dotenv
load_dotenv()

connection = f"mongodb://mongoadmin:{getenv('mongoPass')}@localhost:27017"
print(connection)

client = MongoClient(connection)
#client = MongoClient("mongodb://localhost:27017/")
database = client["xade"]
users = database["users"]
wallets = database["wallets"]
phones = database["phones"]

class mongoAPI(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
    def do_GET(self):
        self.send_response(301)
        self.send_header('Location','https://app.xade.finance')
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) 
        post_data = self.rfile.read(content_length) 
        data = post_data.decode('utf-8')
        #if data.startswith("IP: "):
        #    i = open("./ips.log",'r')
        #    ip = open("./ips.log",'a')
        #    data = data.replace("IP: ","")
        #    if data not in i.readlines():
        #       ips.insert_one({"IP Address":data})
        #        ip.write(data+"\n")
        #    ip.close()
        #    i.close()
        if data.startswith("address:"):
            # w = open(".\\wallets.log",'r')
            # addr = open(".\\wallets.log",'a')
            z = data.split("||")
            adr = z[0].replace("address:","")
            i = z[1].replace("id:","")
            addrChk = wallets.find_one({"Wallet Address":adr})
            if addrChk == None:
                x = wallets.insert_one({"Wallet Address":adr,"ID":i})
            #     addr.write(adr+" ")
            # w.close()
            # addr.close()

        elif data.startswith('{"phone":'):
            # abcd = open(".\\phones.log",'r')
            # ph = open(".\\phones.log",'a')
            p = loads(data)
            phn = p["phone"]
            i = p["id"]
            #a = i+'\n'
            phnChk = phones.find_one({"Phone Number":phn})
            if phnCheck == None:
                x = phones.insert_one({"Phone Number":phn,"ID":i})
            #     ph.write(phn+" ")
            # abcd.close()
            # ph.close()

    
        else:
            
            j = data.replace("'", "\"")
            d = loads(j)

            email = d["email"]
            name = d["name"]
            pfp = d["profileImage"]
            verify = d["verifier"]
            i = d["verifierId"]
            login = d["typeOfLogin"]
            i = d["id"]
            if login == "jwt":
                login = "email"

            # info2 = f"{email}\n"
            # info3 = f"Email: {email} Login Type: {login}\n"
            # fa = open('.\\emails.log','a')
            # fr = open('.\\emails.log','r').read().split("\n")
            # fa2 = open('./logins.log','a')
            # fr2 = open('./logins.log','r').readlines()

            emailChk = users.find_one({"Email":email})
            if emailChk == None:
    
    
                info = {
                    "Email":email,
                    "Username":name,
                    "Login Type":login,
                    "ID":i
                }
    
                x = users.insert_one(info)

            # elif info3 not in fr2:
            #         fa2.write(info3)
            #         fa2.close()
    
            #         info = {
            #             "Email":email,
            #             "Username":name,
            #             "Profile Picture URL":pfp,
            #             "Login Type":login,
            #             "IP Address":ip,
            #             "Primary Login":'No',
            #             "ID":i
            #         }
    
            #         x = users.insert_one(info)
            else:
                info = "duplicate lol"

        #print(info)
        self._set_response()    
        self.wfile.write("{}".format(self.path).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=mongoAPI, port=8000):
    # logging.basicConfig(level=logging.INFO)
    server_address = ('127.0.0.1', 8000)
    httpd = server_class(server_address, handler_class)
    print(f"Listening on 127.0.0.1:{port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    run()
