from email.mime import image
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Init for main app
def db_init(app):
    app.config.from_object('config')
    db.app = app
    db.init_app(app)
    
    # migrate = Migrate(app, db)
    return db

# Init for Test Suite
def setup_db(app, database_path):
    '''binds a flask application and a SQLAlchemy service'''
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

def db_drop_and_create_all():
    '''drops the database tables and starts fresh
    can be used to initialize a clean database
    '''
    db.drop_all()
    db.create_all()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    school = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.role_id'))
    major = db.Column(db.String)
    phone = db.Column(db.String)
    dp = db.Column(db.String)

    quiz_1 = db.relationship('Quiz1', backref='user', lazy=True)
    quiz_2 = db.relationship('Quiz2', backref='user', lazy=True)
    quiz_3 = db.relationship('Quiz3', backref='user', lazy=True)
    quiz_8 = db.relationship('Quiz8', backref='user', lazy=True)
    workbook_1 = db.relationship('WorkBook1', backref='user', lazy=True)
    workbook_2 = db.relationship('WorkBook2', backref='user', lazy=True)
    quiz_5 = db.relationship('Quiz5', backref='user', lazy=True)
    quiz_4 = db.relationship('Quiz4', backref='user', lazy=True)
    test_1 = db.relationship('Test1', backref='user', lazy=True)
    quiz_7 = db.relationship('Quiz7', backref='user', lazy=True)
    quiz_6 = db.relationship('Quiz6', backref='user', lazy=True)


    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'school': self.school,
            'email': self.major,
            'major': self.phone,
            'phone': self.phone,
            'dp': self.dp,
            'role_id': self.role_id
        }

class Roles(db.Model):
    __tablename__ = 'roles'
    role_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.role_id,
            'name': self.name,
        }

class Points(db.Model):
    __tablename__ = 'points'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String, db.ForeignKey('users.id'))
    points = db.Column(db.Integer)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'points': self.points,
        }

class Modules(db.Model):
    __tablename__ = 'modules'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    desc= db.Column(db.String)
    image = db.Column(db.String)
    redirect = db.Column(db.String)

    quizzes = db.relationship('ModuleQuiz', backref='quiz')

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.desc,
            'image': self.image,
            'redirect': self.redirect
        }

class ModuleScore(db.Model):
    __tablename__ = 'module_scores'
    id = db.Column(db.Integer, primary_key=True)
    module_id = db.Column(db.Integer, db.ForeignKey('modules.id'))
    module_comp_id = db.Column(db.Integer, db.ForeignKey('module_completion.id'))
    score = db.Column(db.Float)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'module_id': self.module_id,
            'module_comp_id': self.module_comp_id,
            'score': self.score,
        }

class SubModules(db.Model):
    __tablename__ = 'submodules'
    id = db.Column(db.Integer, primary_key=True)
    module_id = db.Column(db.Integer, db.ForeignKey('modules.id'))
    name = db.Column(db.String)
    desc = db.Column(db.String)
    type = db.Column(db.Enum('PPT','PDF', 'IMG', 'VID'), nullable=False, server_default="PPT")
    data = db.Column(db.TEXT)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'module_id': self.module_id,
            'name': self.name,
            'description': self.desc,
        }

class ModuleMedia(db.Model):
    __tablename__ = 'module_media'
    id = db.Column(db.Integer, primary_key=True)
    sub_module_id = db.Column(db.Integer, db.ForeignKey('submodules.id'))
    media_id = db.Column(db.Integer, db.ForeignKey('media.id'))

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'sub_module_id': self.sub_module_id,
            'media_id': self.media_id,
        }

class Media(db.Model):
    __tablename__ = 'media'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String)
    path = db.Column(db.String)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'type': self.type,
            'path': self.path,
        }

class SubModuleCompletion(db.Model):
    __tablename__ = 'submodule_completion'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String, db.ForeignKey('users.id'))
    submodule_id = db.Column(db.Integer, db.ForeignKey('submodules.id'))
    completion = db.Column(db.Float)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'submodule_id': self.submodule_id,
            'completion': self.completion,
        }

class ModuleCompletion(db.Model):
    __tablename__ = 'module_completion'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String, db.ForeignKey('users.id'))
    module_id = db.Column(db.Integer, db.ForeignKey('modules.id'))
    completion = db.Column(db.Float)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'module_id': self.module_id,
            'completion': self.completion,
        }

class CourseCompletion(db.Model):
    __tablename__ = 'course_completion'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String, db.ForeignKey('users.id'))
    count = db.Column(db.Integer)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'count': self.count,
        }

class ModuleQuiz(db.Model):
    __tablename__ = 'module_quiz'
    id = db.Column(db.Integer, primary_key=True)
    module_id = db.Column(db.Integer, db.ForeignKey('modules.id'))
    name = db.Column(db.String)
    file_name = db.Column(db.String)
    type = db.Column(db.Enum('quiz','workbook'), nullable=False, server_default="quiz")

    module = db.relationship('Modules', back_populates='quizzes')

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'module_id': self.module_id,
            'name': self.name,
            'file_name': self.file_name,
            'type': self.type,
        }

class Videos(db.Model):
    __tablename__ = 'videos'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    file_name = db.Column(db.String)
    cover = db.Column(db.String)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'file_name': self.file_name,
            'cover': self.cover,
        }

class Quiz1(db.Model):
    __tablename__ = 'quiz_1'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String, db.ForeignKey('users.id'))
    q1 = db.Column(db.String)
    q2 = db.Column(db.String)
    q3 = db.Column(db.String)
    q4 = db.Column(db.String)
    q5 = db.Column(db.String)
    q6 = db.Column(db.String)
    q7 = db.Column(db.String)
    q8 = db.Column(db.String)
    q9 = db.Column(db.String)
    q10 = db.Column(db.String)
    q11 = db.Column(db.String)
    q12 = db.Column(db.String)
    q13 = db.Column(db.String)
    q14 = db.Column(db.String)
    q15 = db.Column(db.String)
    q16 = db.Column(db.String)
    q17 = db.Column(db.String)
    q18 = db.Column(db.String)
    q19 = db.Column(db.String)
    q20 = db.Column(db.String)
    q21 = db.Column(db.String)
    q22 = db.Column(db.String)
    score = db.Column(db.Float)

    student = db.relationship('User', back_populates='quiz_1')

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'score': self.score,
        }

class Quiz2(db.Model):
    __tablename__ = 'quiz_2'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String, db.ForeignKey('users.id'))
    q1 = db.Column(db.String)
    q2 = db.Column(db.String)
    q3 = db.Column(db.String)
    q4 = db.Column(db.String)
    q5 = db.Column(db.String)
    q6 = db.Column(db.String)
    q7 = db.Column(db.String)
    q8 = db.Column(db.String)
    q9 = db.Column(db.String)
    q10 = db.Column(db.String)
    q11 = db.Column(db.String)
    q12 = db.Column(db.String)
    q13 = db.Column(db.String)
    q14 = db.Column(db.String)
    q15 = db.Column(db.String)
    q16 = db.Column(db.String)
    q17 = db.Column(db.String)
    q18 = db.Column(db.String)
    q19 = db.Column(db.String)
    q20 = db.Column(db.String)
    
    score = db.Column(db.Float)

    student = db.relationship('User', back_populates='quiz_2')

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'score': self.score,
        }

class WorkBook1(db.Model):
    __tablename__ = 'workbook_1'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String, db.ForeignKey('users.id'))
    
    q1 = db.Column(db.String, nullable = True)
    q2 = db.Column(db.String, nullable = True)
    q3 = db.Column(db.String, nullable = True)
    q4 = db.Column(db.String, nullable = True)
    q5 = db.Column(db.String, nullable = True)
    q6 = db.Column(db.String, nullable = True)
    q7 = db.Column(db.String, nullable = True)
    q8 = db.Column(db.String, nullable = True)
    q9 = db.Column(db.String, nullable = True)
    q10 = db.Column(db.String, nullable = True)
    q11 = db.Column(db.String, nullable = True)
    q12 = db.Column(db.String, nullable = True)
    q13 = db.Column(db.String, nullable = True)
    q14 = db.Column(db.String, nullable = True)
    
    q15a = db.Column(db.String, nullable = True)
    q15b = db.Column(db.String, nullable = True)
    q15c = db.Column(db.String, nullable = True)
    
    q16a = db.Column(db.String, nullable = True)
    q16b = db.Column(db.String, nullable = True)
    q16c = db.Column(db.String, nullable = True)
    
    q17a = db.Column(db.String, nullable = True)
    q17b = db.Column(db.String, nullable = True)
    q17c = db.Column(db.String, nullable = True)
    
    q18a = db.Column(db.String, nullable = True)
    q18b = db.Column(db.String, nullable = True)
    q18c = db.Column(db.String, nullable = True)
    
    q19a = db.Column(db.String, nullable = True)
    q19b = db.Column(db.String, nullable = True)
    q19c = db.Column(db.String, nullable = True)
    
    q20a = db.Column(db.String, nullable = True)
    q20b = db.Column(db.String, nullable = True)
    q20c = db.Column(db.String, nullable = True)
    
    q21 = db.Column(db.String, nullable = True)
    
    score = db.Column(db.Float, nullable = True)

    student = db.relationship('User', back_populates='workbook_1')

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'score': self.score,
        }

class WorkBook2(db.Model):
    __tablename__ = 'workbook_2'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String, db.ForeignKey('users.id'))
    
    q1a = db.Column(db.String, nullable = True)
    q1b = db.Column(db.String, nullable = True)
    
    q2a = db.Column(db.String, nullable = True)
    q2b = db.Column(db.String, nullable = True)
    
    q3a = db.Column(db.String, nullable = True)
    q3b = db.Column(db.String, nullable = True)
    
    q4a = db.Column(db.String, nullable = True)
    q4b = db.Column(db.String, nullable = True)
    
    q5a = db.Column(db.String, nullable = True)
    q5b = db.Column(db.String, nullable = True)
    
    q6a = db.Column(db.String, nullable = True)
    q6b = db.Column(db.String, nullable = True)
    
    q7a = db.Column(db.String, nullable = True)
    q7b = db.Column(db.String, nullable = True)
    
    q8a = db.Column(db.String, nullable = True)
    q8b = db.Column(db.String, nullable = True)
    
    q9a = db.Column(db.String, nullable = True)
    q9b = db.Column(db.String, nullable = True)
    
    q10a = db.Column(db.String, nullable = True)
    q10b = db.Column(db.String, nullable = True)
    
    q11 = db.Column(db.String, nullable = True)
    
    score = db.Column(db.Float, nullable = True)

    student = db.relationship('User', back_populates='workbook_2')

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'score': self.score,
        }


class Quiz6(db.Model):
    __tablename__ = 'quiz_6'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String, db.ForeignKey('users.id'))
    q1 = db.Column(db.String)
    q2 = db.Column(db.String)
    q3 = db.Column(db.String)
    q4 = db.Column(db.String)
    q5 = db.Column(db.String)
    q6 = db.Column(db.String)
    q7 = db.Column(db.String)
    q8 = db.Column(db.String)
    q9 = db.Column(db.String)
    q10 = db.Column(db.String)
    q11a = db.Column(db.String)
    q11b = db.Column(db.String)
    q12a = db.Column(db.String)
    q12b = db.Column(db.String)
    q12c = db.Column(db.String)
    q13a = db.Column(db.String)
    q13b = db.Column(db.String)
    q13c = db.Column(db.String)
    q14 = db.Column(db.String)
    q15 = db.Column(db.String)
    q16a = db.Column(db.String)
    q16b = db.Column(db.String)
    q16c = db.Column(db.String)
    q16d = db.Column(db.String)
    q16e = db.Column(db.String)
    q16f = db.Column(db.String)
    q17 = db.Column(db.String)
    q18 = db.Column(db.String)
    q19 = db.Column(db.String)
    
    score = db.Column(db.Float)

    student = db.relationship('User', back_populates='quiz_6')

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'score': self.score,
        }

class Quiz5(db.Model):
    __tablename__ = 'quiz_5'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String, db.ForeignKey('users.id'))
    q1a = db.Column(db.String)
    q1b = db.Column(db.String)
    q1c = db.Column(db.String)
    q2a = db.Column(db.String)
    q2b = db.Column(db.String)
    q2c = db.Column(db.String)
    q2d = db.Column(db.String)
    q2e = db.Column(db.String)
    q2f = db.Column(db.String)
    q3 = db.Column(db.String)
    q4 = db.Column(db.String)
    q5a = db.Column(db.String)
    q5b = db.Column(db.String)
    q5c = db.Column(db.String)
    
    score = db.Column(db.Float)

    student = db.relationship('User', back_populates='quiz_5')
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'score': self.score,
        }

class Quiz4(db.Model):
    __tablename__ = 'quiz_4'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String, db.ForeignKey('users.id'))
    q1a= db.Column(db.String)
    q1b= db.Column(db.String)
    q1c= db.Column(db.String)
    q1d= db.Column(db.String)
    q1e= db.Column(db.String)
    

    q2a1= db.Column(db.String)
    q2a2= db.Column(db.String)
    q2b1= db.Column(db.String)
    q2b2= db.Column(db.String)
    q2c1= db.Column(db.String)
    q2c2= db.Column(db.String)
    q2d1= db.Column(db.String)
    q2d2= db.Column(db.String)
    q2e1= db.Column(db.String)
    q2e2= db.Column(db.String)
    q2f1= db.Column(db.String)
    q2f2= db.Column(db.String)
    q2g1= db.Column(db.String)
    q2g2= db.Column(db.String)
    q2h1= db.Column(db.String)
    q2h2= db.Column(db.String)
    q2i1= db.Column(db.String)
    q2i2= db.Column(db.String)
    
    q3= db.Column(db.String)
    q4= db.Column(db.String)
    q5= db.Column(db.String)
    q6= db.Column(db.String)

    score = db.Column(db.Float)

    student = db.relationship('User', back_populates='quiz_4')
    
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'score': self.score,
        }

class Quiz3(db.Model):
    __tablename__ = 'quiz_3'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String, db.ForeignKey('users.id'))
    
    q1 = db.Column(db.Text, nullable = True)
    q2 = db.Column(db.Text, nullable = True)    
    q3 = db.Column(db.Text, nullable = True)
    q4 = db.Column(db.Text, nullable = True)    
    q5 = db.Column(db.Text, nullable = True)
    q6 = db.Column(db.Text, nullable = True)    
    q7 = db.Column(db.Text, nullable = True)
    q8 = db.Column(db.Text, nullable = True)    
    q9 = db.Column(db.Text, nullable = True)
    q10 = db.Column(db.Text, nullable = True)    
    q11 = db.Column(db.Text, nullable = True)
    q12 = db.Column(db.Text, nullable = True)    
    q13 = db.Column(db.Text, nullable = True)
    q14 = db.Column(db.Text, nullable = True)    
    q15 = db.Column(db.Text, nullable = True)
    q16 = db.Column(db.Text, nullable = True)    
    q17 = db.Column(db.Text, nullable = True)
    q18 = db.Column(db.Text, nullable = True)    
    q19 = db.Column(db.Text, nullable = True)
    q20 = db.Column(db.Text, nullable = True)
    q21 = db.Column(db.Text, nullable = True)
    q22 = db.Column(db.Text, nullable = True)    
    q23 = db.Column(db.Text, nullable = True)
    q24 = db.Column(db.Text, nullable = True)    
    q25 = db.Column(db.Text, nullable = True)
    q26 = db.Column(db.Text, nullable = True)    
    q27 = db.Column(db.Text, nullable = True)
    q28 = db.Column(db.Text, nullable = True)    
    q29 = db.Column(db.Text, nullable = True)
    q30 = db.Column(db.Text, nullable = True)    
    q31 = db.Column(db.Text, nullable = True)
    q32 = db.Column(db.Text, nullable = True)    
    q33 = db.Column(db.Text, nullable = True)
    q34 = db.Column(db.Text, nullable = True)    
    q35 = db.Column(db.Text, nullable = True)
    q36 = db.Column(db.Text, nullable = True)    
    q37 = db.Column(db.Text, nullable = True)    
    q38 = db.Column(db.Text, nullable = True)

    q39a = db.Column(db.Text, nullable = True)
    q39b = db.Column(db.Text, nullable = True)
    q39c = db.Column(db.Text, nullable = True)
    q39d = db.Column(db.Text, nullable = True)
    
    q40a = db.Column(db.Text, nullable = True)
    q40b = db.Column(db.Text, nullable = True)
    q40c = db.Column(db.Text, nullable = True)
    q40d = db.Column(db.Text, nullable = True)
    
    q41a = db.Column(db.Text, nullable = True)
    q41b = db.Column(db.Text, nullable = True)
    q41c = db.Column(db.Text, nullable = True)
    q41d = db.Column(db.Text, nullable = True)
    
    q42a = db.Column(db.Text, nullable = True)
    q42b = db.Column(db.Text, nullable = True)
    q42c = db.Column(db.Text, nullable = True)
    q42d = db.Column(db.Text, nullable = True)
    
    q43a = db.Column(db.Text, nullable = True)
    q43b = db.Column(db.Text, nullable = True)
    q43c = db.Column(db.Text, nullable = True)
    q43d = db.Column(db.Text, nullable = True)
    
    q44a = db.Column(db.Text, nullable = True)
    q44b = db.Column(db.Text, nullable = True)
    q44c = db.Column(db.Text, nullable = True)
    q44d = db.Column(db.Text, nullable = True)
    
    q45a = db.Column(db.Text, nullable = True)
    q45b = db.Column(db.Text, nullable = True)
    q45c = db.Column(db.Text, nullable = True)
    q45d = db.Column(db.Text, nullable = True)
    
    q46a = db.Column(db.Text, nullable = True)
    q46b = db.Column(db.Text, nullable = True)
    q46c = db.Column(db.Text, nullable = True)
    q46d = db.Column(db.Text, nullable = True)    
    
    q47a = db.Column(db.Text, nullable = True)
    q47b = db.Column(db.Text, nullable = True)
    q47c = db.Column(db.Text, nullable = True)
    q47d = db.Column(db.Text, nullable = True)
    
    q48a = db.Column(db.Text, nullable = True)
    q48b = db.Column(db.Text, nullable = True)
    q48c = db.Column(db.Text, nullable = True)
    q48d = db.Column(db.Text, nullable = True)
    
    q49a = db.Column(db.Text, nullable = True)
    q49b = db.Column(db.Text, nullable = True)
    q49c = db.Column(db.Text, nullable = True)
    q49d = db.Column(db.Text, nullable = True)
    
    q50a = db.Column(db.Text, nullable = True)
    q50b = db.Column(db.Text, nullable = True)
    q50c = db.Column(db.Text, nullable = True)
    q50d = db.Column(db.Text, nullable = True)
    
    q51a = db.Column(db.Text, nullable = True)
    q51b = db.Column(db.Text, nullable = True)
    q51c = db.Column(db.Text, nullable = True)
    q51d = db.Column(db.Text, nullable = True)
    
    q52a = db.Column(db.Text, nullable = True)
    q52b = db.Column(db.Text, nullable = True)
    q52c = db.Column(db.Text, nullable = True)
    q52d = db.Column(db.Text, nullable = True)
    
    q53a = db.Column(db.Text, nullable = True)
    q53b = db.Column(db.Text, nullable = True)
    q53c = db.Column(db.Text, nullable = True)
    q53d = db.Column(db.Text, nullable = True)
    
    q54 = db.Column(db.Text, nullable = True)
    q55 = db.Column(db.Text, nullable = True)
    
    q56a = db.Column(db.Text, nullable = True)
    q56b = db.Column(db.Text, nullable = True)
    q56c = db.Column(db.Text, nullable = True)
    
    q57 = db.Column(db.Text, nullable = True)
    
    q58a = db.Column(db.Text, nullable = True)
    q58b = db.Column(db.Text, nullable = True)
    
    q59a = db.Column(db.Text, nullable = True)
    q59b = db.Column(db.Text, nullable = True)
    
    q60a = db.Column(db.Text, nullable = True)
    q60b = db.Column(db.Text, nullable = True)
    q60c = db.Column(db.Text, nullable = True)
    
    score = db.Column(db.Float, nullable = True)

    student = db.relationship('User', back_populates='quiz_3')
    
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'score': self.score,
        }

class Quiz8(db.Model):
    __tablename__ = 'quiz_8'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String, db.ForeignKey('users.id'))
    q1 = db.Column(db.String)
    q2 = db.Column(db.String)
    q3 = db.Column(db.String)
    q4 = db.Column(db.Text, nullable = True)    
    q5 = db.Column(db.Text, nullable = True)
    q6 = db.Column(db.Text, nullable = True)    
    q7 = db.Column(db.Text, nullable = True)
    
    q8n1a = db.Column(db.Text, nullable = True)
    q8n1d = db.Column(db.Text, nullable = True)
    q8p1a = db.Column(db.Text, nullable = True)
    q8p1d = db.Column(db.Text, nullable = True)
    
    q8n2a = db.Column(db.Text, nullable = True)
    q8n2d = db.Column(db.Text, nullable = True)
    q8p2a = db.Column(db.Text, nullable = True)
    q8p2d = db.Column(db.Text, nullable = True)
    
    q8n3a = db.Column(db.Text, nullable = True)
    q8n3d = db.Column(db.Text, nullable = True)
    q8p3a = db.Column(db.Text, nullable = True)
    q8p3d = db.Column(db.Text, nullable = True)
    
    q9 = db.Column(db.Text, nullable = True)
    q10 = db.Column(db.Text, nullable = True)
    q11 = db.Column(db.Text, nullable = True)
    
    score = db.Column(db.Float)

    student = db.relationship('User', back_populates='quiz_8')

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'score': self.score,
        }


class Test1(db.Model):
    __tablename__ = 'test_1'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String, db.ForeignKey('users.id'))
    q1 = db.Column(db.String)
    q2 = db.Column(db.String)
    q3 = db.Column(db.String)
    q4 = db.Column(db.String)
    q5 = db.Column(db.String)
    q6 = db.Column(db.String)
    q7 = db.Column(db.String)
    q8 = db.Column(db.String)
    q9 = db.Column(db.String)
    q10 = db.Column(db.String)
    q11 = db.Column(db.String)
    q12 = db.Column(db.String)
    q13 = db.Column(db.String)
    q14 = db.Column(db.String)
    q15 = db.Column(db.String)
    q16 = db.Column(db.String)
    q17 = db.Column(db.String)
    q18 = db.Column(db.String)
    q19 = db.Column(db.String)
    q20 = db.Column(db.String)
    q21 = db.Column(db.String)
    q22 = db.Column(db.String)
    q23 = db.Column(db.String)
    q24 = db.Column(db.String)
    q25 = db.Column(db.String)
    q26 = db.Column(db.String)
    q27 = db.Column(db.String)
    q28 = db.Column(db.String)
    q29 = db.Column(db.String)
    q30 = db.Column(db.String)
    q31 = db.Column(db.String)
    q32 = db.Column(db.String)
    q33 = db.Column(db.String)
    q34 = db.Column(db.String)
    q35 = db.Column(db.String)
    q36 = db.Column(db.String)
    q37 = db.Column(db.String)
    q38 = db.Column(db.String)
    q39 = db.Column(db.String)
    q40 = db.Column(db.String)
    q41 = db.Column(db.String)
    q42 = db.Column(db.String)
    q43 = db.Column(db.String)
    q44 = db.Column(db.String)
    q45 = db.Column(db.String)
    q46 = db.Column(db.String)
    q47 = db.Column(db.String)
    q48 = db.Column(db.String)

    score = db.Column(db.Float)

    student = db.relationship('User', back_populates='test_1')

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'score': self.score,
        }

class Quiz7(db.Model):
    __tablename__ = 'quiz_7'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String, db.ForeignKey('users.id'))
    q1 = db.Column(db.String, server_default="off")
    q2 = db.Column(db.String, server_default="off")
    q3 = db.Column(db.String, server_default="off")
    q4 = db.Column(db.String, server_default="off")
    q5 = db.Column(db.String, server_default="off")
    q6 = db.Column(db.String, server_default="off")
    q7 = db.Column(db.String, server_default="off")
    q8 = db.Column(db.String, server_default="off")
    q9 = db.Column(db.String, server_default="off")
    q10 = db.Column(db.String, server_default="off")
    q11 = db.Column(db.String, server_default="off")
    q12 = db.Column(db.String, server_default="off")
    q13 = db.Column(db.String, server_default="off")
    q14 = db.Column(db.String, server_default="off")
    q15 = db.Column(db.String, server_default="off")
    q16 = db.Column(db.String, server_default="off")
    q17 = db.Column(db.String, server_default="off")
    q18 = db.Column(db.String, server_default="off")
    q19 = db.Column(db.String, server_default="off")
    q20 = db.Column(db.String, server_default="off")
    q21 = db.Column(db.String, server_default="off")
    q22 = db.Column(db.String, server_default="off")
    q23 = db.Column(db.String, server_default="off")
    q24 = db.Column(db.String, server_default="off")
    q25 = db.Column(db.String, server_default="off")
    q26 = db.Column(db.String, server_default="off")
    q27 = db.Column(db.String, server_default="off")
    q28 = db.Column(db.String, server_default="off")

    score = db.Column(db.Float)

    student = db.relationship('User', back_populates='quiz_7')

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'score': self.score,
        }
