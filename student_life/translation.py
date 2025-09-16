from modeltranslation.translator import register, TranslationOptions
from .models import PartnerOrganization, StudentAppeal

# Поскольку мы добавили мультиязычные поля напрямую в модели,
# нам больше не нужно использовать modeltranslation для автоматической генерации полей

# Оставляем пустые настройки для совместимости
@register(PartnerOrganization)
class PartnerOrganizationTranslationOptions(TranslationOptions):
    fields = ()


@register(StudentAppeal)
class StudentAppealTranslationOptions(TranslationOptions):
    fields = ()
