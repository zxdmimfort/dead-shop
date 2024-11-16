from config.settings import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path("users/", include("apps.users.urls", namespace="users")),
    path("products/", include("apps.products.urls", namespace="products")),
    path("categories/", include("apps.categories.urls", namespace="categories")),
    path("cart/", include("apps.cart.urls", namespace="cart")),
    path("order/", include("apps.order.urls", namespace="order")),
    path("", RedirectView.as_view(pattern_name="products:index")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
