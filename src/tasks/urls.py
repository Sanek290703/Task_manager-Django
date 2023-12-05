from django.urls import path
from .views import home, tasks, description, task_del, add_category, add_task, category_del, done_tasks, not_done, del_done

urlpatterns = [
    path('category/<int:c_id>', tasks, name='tasks'),
    path('category/task/<int:task_id>/del', task_del, name='task_del'),
    path('category/task/<int:task_id>', description, name='desc'),
    path('add_category', add_category, name='add_c'),
    path('category/<str:category>/add_task', add_task, name='add_task'),
    path('category/<int:c_id>/del', category_del, name='category_del'),
    path('done_tasks/<int:task_id>/not_done', not_done, name='not_done'),
    path('done_tasks/del_done', del_done, name='del_done'),
    path('done_tasks', done_tasks, name='done_tasks'),
    path('', home, name='home'),
]