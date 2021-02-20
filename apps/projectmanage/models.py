from django.db import models

# Create your models here.
class Projectdata(models.Model):
    time = models.CharField(db_column="Time", primary_key=True, max_length=100,null=False) # 时间，不允许为空，主键
    projectName = models.CharField(db_column="ProjectName", max_length=100, null=False)  # 项目名称
    days = models.IntegerField(db_column="Days", null=False)  # 天数
    man = models.IntegerField(db_column="Man", null=False)  # 人数
    manDay = models.IntegerField(db_column="ManDay", null=False)  # 人日，
    bugNumber = models.IntegerField(db_column="BugNumber", null=False)  # bug数
    bugRate = models.FloatField(db_column="BugRate", null=False)  # bug率
    content = models.CharField(db_column="Content", max_length=100, null=False)  # 备注

    # 在默认情况下，生成的表名：App_class, 如果要自定义 ，需要使用Class Meta来自定义
    class Meta:
        managed = True
        db_table = "project_data"

    # __str__方法
    def __str__(self):
        return "时间:%s\t项目名称:%s\t天数:%s" %(self.time,self.projectName,self.days)