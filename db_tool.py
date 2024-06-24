from peewee import *
import datetime


# db = MySQLDatabase('lsat_exam', user='root', password='root', host='localhost', port=3306)
db = MySQLDatabase('fastadmin', user='root', password='root', host='localhost', port=3306)

# 定义 Question 模型
class Question(Model):
    ques_id = AutoField(primary_key=True)
    ques_title = TextField()
    ques_section = IntegerField()
    ques_ans = CharField()
    ques_type = CharField()
    ques_create_time = DateTimeField(default=datetime.datetime.now)
    passage = TextField()
    print_num = CharField(unique=True)
    class Meta:
        database = db
        # table_name = 'exam_questions'
        table_name = 'fa_question'



# 定义 Option 模型
class Option(Model):
    id = AutoField(primary_key=True)
    ques_id = ForeignKeyField(Question, backref='options')
    opa = TextField(null=True)
    opb = TextField(null=True)
    opc = TextField(null=True)
    opd = TextField(null=True)
    ope = TextField(null=True)
    opf = TextField(null=True)

    class Meta:
        database = db
        # table_name = 'exam_options'
        table_name = 'fa_options'