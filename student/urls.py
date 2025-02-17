
from django.urls import path

from student import views


urlpatterns=[

    path("register/",views.StudentRegisterView.as_view(),name="student-register"),
    path("signin/",views.SignInView.as_view(),name='sign-in'),

    path("index/",views.IndexView.as_view(),name='index'),

    path('courses/<int:pk>/',views.CourseDetailView.as_view(),name='course-detail'),

    path('courses/<int:pk>/add-to-cart/',views.AddToCartView.as_view(),name='add-to-cart'),

    path('carts/summary/',views.CartSummaryView.as_view(),name='cart-summary'),

    path('cart/<int:pk>/remove/',views.CartItemDeleteView.as_view(),name='cart-delete'),

    path('checkout/',views.CheckOutView.as_view(),name='check-out'),

    path('mycourses/',views.MyCourseView.as_view(),name='mycourses'),

    path('courses/<int:pk>/watch/',views.LessonDetailView.as_view(),name='lesson-detail'),

    path('payment/verify/',views.PaymentVerificationView.as_view(),name='payment-verify'),

    path('signout/',views.SignOutView.as_view(),name='sign-out'),

    

]