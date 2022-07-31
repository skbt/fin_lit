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