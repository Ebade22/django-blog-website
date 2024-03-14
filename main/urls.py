from django.urls import path 
from .views import home_page_view, about_page_view, contact_page_view, blog_detail_view, posts_by_category

urlpatterns =[
    # path('admin/', admin.site.urls),

    path('', home_page_view, name="home"),
    path('about/', about_page_view, name="about_page"),
    path('contact/', contact_page_view, name="contact_page"),
    path('post/<int:blog_id>/', blog_detail_view, name='post_detail'),
    path('category/<str:category_name>/',posts_by_category, name="category-post")
]