
from django.contrib import admin
from django.urls import path
#from student import views
from projectmanage import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('students/',views.get_students),  # 获取所有学生信息的接口
    # path('students/query/', views.query_students),  # 查询学生信息的接口
    # path('sno/check/', views.is_exists_sno),  # 校验学号是否存在
    # path('student/add/', views.add_student),  # 添加学生信息的接口
    # path('student/update/', views.update_student),  # 修改学生信息的接口
    # path('student/delete/', views.delete_student),  # 删除学生信息的接口
    # path('students/delete/', views.delete_students),  # 删除学生信息的接口
    # path('upload/', views.upload),  # 上传文件的接口
    # path('execl/import/',views.import_students_excel),#导入execl的文件
    # path('excel/export/', views.export_student_excel),  # 导出Excel文件
    path('projectmanage/', views.get_projectdata),  # 获取所有项目信息的接口
    path('projectmanage/query/', views.query_projectdata),  # 查询项目信息的接口
    path('projectname/check/', views.is_exists_projectname),  # 校验项目名称是否存在
    path('projectmanage/add/', views.add_projectdata),  # 添加项目信息的接口
    path('projectmanage/update/', views.update_projectdata),  # 修改项目信息的接口
    path('projectmanage/delete/', views.delete_projectdata),  # 删除项目信息的接口
    path('projectmanages/delete/', views.delete_projectdatas),  # 批量删除项目信息的接口
    path('execl/import/',views.import_projectdata_execl),#导入execl的文件
    path('execl/export/', views.export_projectdata_execl),  # 导出Excel文件
]
#添加这行--- 允许所有的media文件被访问
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)