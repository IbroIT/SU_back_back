from django.db import models
from django.utils.translation import gettext_lazy as _


class Banner(models.Model):
    photo = models.ImageField(upload_to='banners/', verbose_name=_("Фото"))
    is_active = models.BooleanField(default=True, verbose_name=_("Активный"))
    order = models.PositiveIntegerField(default=0, verbose_name=_("Порядок"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата создания"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Дата обновления"))
    
    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = _("Баннер")
        verbose_name_plural = _("Баннеры")
    
    def __str__(self):
        return f"Banner {self.id} (Order: {self.order})"
