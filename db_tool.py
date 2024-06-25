from peewee import *
import datetime


db = MySQLDatabase('lsat_exam', user='root', password='root', host='localhost', port=3306)
# db = MySQLDatabase('fastadmin', user='root', password='root', host='localhost', port=3306)

# 定义 Question 模型
class Question(Model):
    ques_id = AutoField(primary_key=True)
    ques_title = TextField()
    ques_section = IntegerField()
    ques_ans = CharField()
    ques_type = CharField()
    ques_create_time = DateTimeField(default=datetime.datetime.now)
    passage = TextField()
    printNum = CharField(unique=True)
    # print_num = CharField(unique=True)
    class Meta:
        database = db
        table_name = 'exam_questions'
        # table_name = 'fa_question'



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
        table_name = 'exam_options'
        # table_name = 'fa_options'
class Paper(Model):
    paper_id = IntegerField(primary_key=True)
    paper_name = CharField(max_length=255)
    paper_order = IntegerField(default=5)
    paper_status = IntegerField(default=5)
    paper_longtime = IntegerField(default=20)
    paper_createtime = IntegerField(default=10)
    paper_note = TextField(null=True)
    paper_group = CharField(max_length=255)
    paper_type = IntegerField(default=20)
    test_mode = IntegerField(default=10)
    paper_section = CharField(max_length=255)
    exam_type = IntegerField(default=20)
    class Meta:
        database = db
        # table_name = 'exam_options'
        table_name = 'exam_paper'
class Detail(Model):
    id = IntegerField(primary_key=True)
    paper_id = IntegerField()
    ques_id = IntegerField()
    pass_id = IntegerField()
    type = CharField(max_length=255)
    create_time = IntegerField()
    paper_modu = IntegerField()
    ques_order = IntegerField()
    paper_group_id = IntegerField()
    status = IntegerField()
    class Meta:
        database = db
        # table_name = 'exam_options'
        table_name = 'exam_paper_detail'