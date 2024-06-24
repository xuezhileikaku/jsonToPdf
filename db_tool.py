from peewee import *
import datetime


# db = MySQLDatabase('lsat_exam', user='root', password='root', host='localhost', port=3306)
db = MySQLDatabase('fastadmin', user='root', password='root', host='localhost', port=3306)

class Question(Model):
    ques_id = AutoField(primary_key=True)
    ques_title = TextField()
    ques_section = IntegerField()
    ques_ans = CharField()
    ques_type = CharField()
    ques_create_time = DateTimeField(default=datetime.datetime.now)
    passage = TextField()
    printNum = CharField()  # 假设这是一个打印编号字段

    class Meta:
        database = db
        # table_name = 'exam_questions'
        table_name = 'fa_question'



class Option(Model):
    id = AutoField(primary_key=True)
    ques_id = ForeignKeyField(Question, backref='option_set')
    opa = TextField()
    opb = TextField()
    opc = TextField()
    opd = TextField()
    ope = TextField()
    opf = TextField()

    class Meta:
        database = db
        # table_name = 'exam_options'
        table_name = 'fa_options'