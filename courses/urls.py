from django.contrib import admin
from django.urls import path,include
# from courses.views import CoursesCreateView, CoursesDeleteView, CoursesDetailView, CoursesView
from rest_framework.routers import DefaultRouter
from courses.views import CoursesViewSet

router = DefaultRouter()

router.register('courses', CoursesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
    # path('',CoursesView.as_view()),
    # path('<int:pk>/',CoursesDetailView.as_view()),
    # path('create/',CoursesCreateView.as_view()),
    # path('<int:pk>/delete/',CoursesDeleteView.as_view())

]
