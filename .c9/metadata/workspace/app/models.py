{"filter":false,"title":"models.py","tooltip":"/app/models.py","undoManager":{"mark":79,"position":79,"stack":[[{"start":{"row":0,"column":0},"end":{"row":39,"column":42},"action":"remove","lines":["from app import db","from werkzeug.security import generate_password_hash","","","class UserProfile(db.Model):","    # You can use this to change the table name. The default convention is to use","    # the class name. In this case a class name of UserProfile would create a","    # user_profile (singular) table, but if we specify __tablename__ we can change it","    # to `user_profiles` or some other name.","    __tablename__ = 'user_profiles'","","    id = db.Column(db.Integer, primary_key=True)","    first_name = db.Column(db.String(80))","    last_name = db.Column(db.String(80))","    username = db.Column(db.String(80), unique=True)","    password = db.Column(db.String(255))","","    def __init__(self, first_name, last_name, username, password):","        self.first_name = first_name","        self.last_name = last_name","        self.username = username","        self.password = generate_password_hash(password, method='pbkdf2:sha256')","","    def is_authenticated(self):","        return True","","    def is_active(self):","        return True","","    def is_anonymous(self):","        return False","","    def get_id(self):","        try:","            return unicode(self.id)  # python 2 support","        except NameError:","            return str(self.id)  # python 3 support","","    def __repr__(self):","        return '<User %r>' % self.username"],"id":11},{"start":{"row":0,"column":0},"end":{"row":43,"column":44},"action":"insert","lines":["from . import db","","","","class UserProfile(db.Model):","    __tablename__ = 'user_profiles'","","    id = db.Column(db.Integer, primary_key=True)","    first_name = db.Column(db.String(255))","    last_name = db.Column(db.String(255))","    email = db.Column(db.String(255))","    location = db.Column(db.String(80))","    description = db.Column(db.String(255))","    gender =db.Column(db.String(255))","    photo = db.Column(db.String(255))","    date = db.Column(db.String(255))","","    def __init__(self, first_name, last_name, email, location, description,gender,photo,date):","        self.first_name = first_name","        self.last_name = last_name","        self.email = email","        self.location = location","        self.description= description","        self.gender = gender","        self.photo = photo ","        self.date= date","","    def is_authenticated(self):","        return True","","    def is_active(self):","        return True","","    def is_anonymous(self):","        return False","","    def get_id(self):","        try:","            return unicode(self.id)  # python 2 support","        except NameError:","            return str(self.id)  # python 3 support","","    def __repr__(self):","        return '<User %r>' % (self.username)"]}],[{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["",""],"id":12}],[{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"remove","lines":["",""],"id":13}],[{"start":{"row":0,"column":5},"end":{"row":0,"column":6},"action":"remove","lines":["."],"id":14}],[{"start":{"row":0,"column":5},"end":{"row":0,"column":6},"action":"insert","lines":["a"],"id":15}],[{"start":{"row":0,"column":6},"end":{"row":0,"column":7},"action":"insert","lines":["p"],"id":16}],[{"start":{"row":0,"column":7},"end":{"row":0,"column":8},"action":"insert","lines":["p"],"id":17}],[{"start":{"row":0,"column":5},"end":{"row":0,"column":8},"action":"remove","lines":["app"],"id":18},{"start":{"row":0,"column":5},"end":{"row":0,"column":6},"action":"insert","lines":["."]}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":28},"action":"remove","lines":["class UserProfile(db.Model):"],"id":19},{"start":{"row":2,"column":0},"end":{"row":2,"column":28},"action":"insert","lines":["class UserProfile(db.Model):"]}],[{"start":{"row":3,"column":4},"end":{"row":3,"column":35},"action":"remove","lines":["__tablename__ = 'user_profiles'"],"id":20},{"start":{"row":3,"column":4},"end":{"row":3,"column":35},"action":"insert","lines":["__tablename__ = 'user_profiles'"]}],[{"start":{"row":5,"column":4},"end":{"row":5,"column":48},"action":"remove","lines":["id = db.Column(db.Integer, primary_key=True)"],"id":21},{"start":{"row":5,"column":4},"end":{"row":5,"column":48},"action":"insert","lines":["id = db.Column(db.Integer, primary_key=True)"]}],[{"start":{"row":6,"column":37},"end":{"row":6,"column":40},"action":"remove","lines":["255"],"id":22},{"start":{"row":6,"column":37},"end":{"row":6,"column":38},"action":"insert","lines":["8"]}],[{"start":{"row":6,"column":38},"end":{"row":6,"column":39},"action":"insert","lines":["0"],"id":23}],[{"start":{"row":7,"column":36},"end":{"row":7,"column":39},"action":"remove","lines":["255"],"id":24},{"start":{"row":7,"column":36},"end":{"row":7,"column":37},"action":"insert","lines":["8"]}],[{"start":{"row":7,"column":37},"end":{"row":7,"column":38},"action":"insert","lines":["0"],"id":25}],[{"start":{"row":9,"column":35},"end":{"row":9,"column":37},"action":"remove","lines":["80"],"id":26},{"start":{"row":9,"column":35},"end":{"row":9,"column":36},"action":"insert","lines":["2"]}],[{"start":{"row":9,"column":36},"end":{"row":9,"column":37},"action":"insert","lines":["5"],"id":27}],[{"start":{"row":9,"column":37},"end":{"row":9,"column":38},"action":"insert","lines":["5"],"id":28}],[{"start":{"row":15,"column":75},"end":{"row":15,"column":76},"action":"insert","lines":[" "],"id":29}],[{"start":{"row":15,"column":83},"end":{"row":15,"column":84},"action":"insert","lines":[" "],"id":30}],[{"start":{"row":15,"column":90},"end":{"row":15,"column":91},"action":"insert","lines":[" "],"id":31}],[{"start":{"row":41,"column":35},"end":{"row":41,"column":43},"action":"remove","lines":["username"],"id":32},{"start":{"row":41,"column":35},"end":{"row":41,"column":36},"action":"insert","lines":["e"]}],[{"start":{"row":41,"column":36},"end":{"row":41,"column":37},"action":"insert","lines":["m"],"id":33}],[{"start":{"row":41,"column":37},"end":{"row":41,"column":38},"action":"insert","lines":["a"],"id":34}],[{"start":{"row":41,"column":38},"end":{"row":41,"column":39},"action":"insert","lines":["i"],"id":35}],[{"start":{"row":41,"column":39},"end":{"row":41,"column":40},"action":"insert","lines":["l"],"id":36}],[{"start":{"row":23,"column":17},"end":{"row":23,"column":18},"action":"insert","lines":[" "],"id":37}],[{"start":{"row":13,"column":36},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":38},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":14,"column":4},"end":{"row":14,"column":5},"action":"insert","lines":["s"],"id":39}],[{"start":{"row":14,"column":5},"end":{"row":14,"column":6},"action":"insert","lines":["o"],"id":40}],[{"start":{"row":14,"column":6},"end":{"row":14,"column":7},"action":"insert","lines":["m"],"id":41}],[{"start":{"row":14,"column":7},"end":{"row":14,"column":8},"action":"insert","lines":["e"],"id":42}],[{"start":{"row":14,"column":8},"end":{"row":14,"column":9},"action":"insert","lines":["t"],"id":43}],[{"start":{"row":14,"column":9},"end":{"row":14,"column":10},"action":"insert","lines":["h"],"id":44}],[{"start":{"row":14,"column":10},"end":{"row":14,"column":11},"action":"insert","lines":["i"],"id":45}],[{"start":{"row":14,"column":11},"end":{"row":14,"column":12},"action":"insert","lines":["n"],"id":46}],[{"start":{"row":14,"column":12},"end":{"row":14,"column":13},"action":"insert","lines":["g"],"id":47}],[{"start":{"row":14,"column":13},"end":{"row":14,"column":14},"action":"insert","lines":[" "],"id":48}],[{"start":{"row":14,"column":14},"end":{"row":14,"column":15},"action":"insert","lines":["="],"id":49}],[{"start":{"row":14,"column":15},"end":{"row":14,"column":16},"action":"insert","lines":[" "],"id":50}],[{"start":{"row":14,"column":16},"end":{"row":14,"column":17},"action":"insert","lines":["d"],"id":51}],[{"start":{"row":14,"column":17},"end":{"row":14,"column":18},"action":"insert","lines":["b"],"id":52}],[{"start":{"row":14,"column":18},"end":{"row":14,"column":19},"action":"insert","lines":["."],"id":53}],[{"start":{"row":14,"column":19},"end":{"row":14,"column":20},"action":"insert","lines":["C"],"id":54}],[{"start":{"row":14,"column":20},"end":{"row":14,"column":21},"action":"insert","lines":["o"],"id":55}],[{"start":{"row":14,"column":21},"end":{"row":14,"column":22},"action":"insert","lines":["l"],"id":56}],[{"start":{"row":14,"column":22},"end":{"row":14,"column":23},"action":"insert","lines":["u"],"id":57}],[{"start":{"row":14,"column":23},"end":{"row":14,"column":24},"action":"insert","lines":["m"],"id":58}],[{"start":{"row":14,"column":24},"end":{"row":14,"column":25},"action":"insert","lines":["n"],"id":59}],[{"start":{"row":14,"column":25},"end":{"row":14,"column":27},"action":"insert","lines":["()"],"id":60}],[{"start":{"row":14,"column":26},"end":{"row":14,"column":27},"action":"insert","lines":["d"],"id":61}],[{"start":{"row":14,"column":27},"end":{"row":14,"column":28},"action":"insert","lines":["b"],"id":62}],[{"start":{"row":14,"column":28},"end":{"row":14,"column":29},"action":"insert","lines":["."],"id":63}],[{"start":{"row":14,"column":29},"end":{"row":14,"column":30},"action":"insert","lines":["S"],"id":64}],[{"start":{"row":14,"column":30},"end":{"row":14,"column":31},"action":"insert","lines":["t"],"id":65}],[{"start":{"row":14,"column":31},"end":{"row":14,"column":32},"action":"insert","lines":["r"],"id":66}],[{"start":{"row":14,"column":32},"end":{"row":14,"column":33},"action":"insert","lines":["i"],"id":67}],[{"start":{"row":14,"column":33},"end":{"row":14,"column":34},"action":"insert","lines":["n"],"id":68}],[{"start":{"row":14,"column":34},"end":{"row":14,"column":35},"action":"insert","lines":["g"],"id":69}],[{"start":{"row":14,"column":35},"end":{"row":14,"column":37},"action":"insert","lines":["()"],"id":70}],[{"start":{"row":14,"column":36},"end":{"row":14,"column":37},"action":"insert","lines":["2"],"id":71}],[{"start":{"row":14,"column":37},"end":{"row":14,"column":38},"action":"insert","lines":["5"],"id":72}],[{"start":{"row":14,"column":38},"end":{"row":14,"column":39},"action":"insert","lines":["5"],"id":73}],[{"start":{"row":2,"column":10},"end":{"row":2,"column":11},"action":"remove","lines":["P"],"id":74}],[{"start":{"row":2,"column":10},"end":{"row":2,"column":11},"action":"insert","lines":["p"],"id":75}],[{"start":{"row":2,"column":10},"end":{"row":2,"column":11},"action":"remove","lines":["p"],"id":76},{"start":{"row":2,"column":10},"end":{"row":2,"column":11},"action":"insert","lines":["P"]}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":41},"action":"remove","lines":["    something = db.Column(db.String(255))"],"id":77}],[{"start":{"row":13,"column":36},"end":{"row":14,"column":0},"action":"remove","lines":["",""],"id":78}],[{"start":{"row":12,"column":5},"end":{"row":12,"column":6},"action":"insert","lines":["#"],"id":79}],[{"start":{"row":22,"column":8},"end":{"row":22,"column":9},"action":"insert","lines":["#"],"id":80}],[{"start":{"row":12,"column":4},"end":{"row":12,"column":5},"action":"remove","lines":["p"],"id":81}],[{"start":{"row":12,"column":4},"end":{"row":12,"column":5},"action":"remove","lines":["#"],"id":82}],[{"start":{"row":12,"column":4},"end":{"row":12,"column":5},"action":"insert","lines":["p"],"id":83}],[{"start":{"row":12,"column":4},"end":{"row":12,"column":5},"action":"insert","lines":["#"],"id":84}],[{"start":{"row":15,"column":89},"end":{"row":15,"column":90},"action":"remove","lines":[","],"id":85},{"start":{"row":15,"column":88},"end":{"row":15,"column":89},"action":"remove","lines":["o"]},{"start":{"row":15,"column":87},"end":{"row":15,"column":88},"action":"remove","lines":["t"]},{"start":{"row":15,"column":86},"end":{"row":15,"column":87},"action":"remove","lines":["o"]},{"start":{"row":15,"column":85},"end":{"row":15,"column":86},"action":"remove","lines":["h"]},{"start":{"row":15,"column":84},"end":{"row":15,"column":85},"action":"remove","lines":["p"]}],[{"start":{"row":12,"column":4},"end":{"row":12,"column":5},"action":"remove","lines":["#"],"id":86}],[{"start":{"row":22,"column":8},"end":{"row":22,"column":9},"action":"remove","lines":["#"],"id":87}],[{"start":{"row":15,"column":84},"end":{"row":15,"column":85},"action":"insert","lines":["p"],"id":88},{"start":{"row":15,"column":85},"end":{"row":15,"column":86},"action":"insert","lines":["h"]},{"start":{"row":15,"column":86},"end":{"row":15,"column":87},"action":"insert","lines":["o"]},{"start":{"row":15,"column":87},"end":{"row":15,"column":88},"action":"insert","lines":["t"]}],[{"start":{"row":15,"column":88},"end":{"row":15,"column":89},"action":"insert","lines":["o"],"id":89},{"start":{"row":15,"column":89},"end":{"row":15,"column":90},"action":"insert","lines":[","]}],[{"start":{"row":15,"column":90},"end":{"row":15,"column":91},"action":"insert","lines":[" "],"id":90}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":15,"column":91},"end":{"row":15,"column":91},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1552860117047,"hash":"ae71b9d27dbeff791a15f269dce2bf451ec841da"}